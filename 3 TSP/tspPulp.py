import pulp


def solve_tsp_with_pulp(distances):
    n = len(distances)

    # Create the model
    model = pulp.LpProblem("TSP", pulp.LpMinimize)

    # Create binary variables for edges
    x = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                x[i, j] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

    # Create variables for subtour elimination
    u = {}
    for i in range(1, n):
        u[i] = pulp.LpVariable(f"u_{i}", lowBound=1, upBound=n - 1, cat=pulp.LpInteger)

    # Objective: minimize total distance
    model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

    # Constraint: each city must be entered exactly once
    for j in range(n):
        model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

    # Constraint: each city must be exited exactly once
    for i in range(n):
        model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

    # Subtour elimination constraints (Miller-Tucker-Zemlin formulation)
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[j] >= u[i] + 1 - n * (1 - x[i, j])

    # Set time limit to 60 seconds
    model.solve(pulp.PULP_CBC_CMD(timeLimit=90, msg=False))

    # Check if a solution was found
    if model.status == pulp.LpStatusOptimal or model.status == pulp.LpStatusNotSolved:
        # Reconstruct the tour
        tour = [0]
        current = 0

        while len(tour) < n:
            for j in range(n):
                if j != current and pulp.value(x[current, j]) > 0.5:
                    tour.append(j)
                    current = j
                    break

        return tour
    else:
        return None
