from pyscipopt import Model, quicksum


def solve_tsp_with_scip(distances):
    n = len(distances)

    model = Model("TSP")

    x = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                x[i, j] = model.addVar(vtype="B", name=f"x_{i}_{j}")

    u = {}
    for i in range(1, n):
        u[i] = model.addVar(vtype="C", lb=1, ub=n - 1, name=f"u_{i}")

    model.setObjective(
        quicksum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j),
        "minimize"
    )

    for j in range(n):
        model.addCons(
            quicksum(x[i, j] for i in range(n) if i != j) == 1,
            name=f"enter_{j}"
        )

    for i in range(n):
        model.addCons(
            quicksum(x[i, j] for j in range(n) if i != j) == 1,
            name=f"leave_{i}"
        )

    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model.addCons(
                    u[j] >= u[i] + 1 - n * (1 - x[i, j]),
                    name=f"mtz_{i}_{j}"
                )

    model.setRealParam('limits/time', 300)
    model.setIntParam('display/verblevel', 0)
    model.optimize()
    status = model.getStatus()

    if status == "optimal" or status == "timelimit":
        tour = [0]
        current = 0

        while len(tour) < n:
            for j in range(n):
                if j != current and current != j and model.getVal(x[current, j]) > 0.5:
                    tour.append(j)
                    current = j
                    break

        return tour
    else:
        return None
