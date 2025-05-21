from z3 import Optimize, Int, Distinct, Implies, Or, And, Sum, If, sat, Real, unknown


def solve_tsp_with_z3(distances):
    n = len(distances)
    solver = Optimize()

    tour = [Int(f'x{i}') for i in range(n)]
    solver.add(Distinct(tour))

    for city in tour:
        solver.add(city >= 0, city < n)

    total_distance = 0
    for i in range(n):
        current_city = tour[i]
        next_city = tour[(i + 1) % n]
        distance = 0
        for j in range(n):
            for k in range(n):
                distance = If(And(current_city == j, next_city == k), distances[j][k], distance)
        total_distance += distance

    solver.minimize(total_distance)

    if solver.check() == sat:
        model = solver.model()
        best_tour = [model.eval(city).as_long() for city in tour]
        return best_tour
    else:
        return None
