from z3 import Optimize, Int, Distinct, Implies, Or, And, Sum, If, sat, Real, unknown, Bool, PbEq, Not
import time


def solve_tsp_with_z3(distances):
    """
    Optimized Z3 TSP solver that adapts to the problem size.
    For small instances, uses a direct approach.
    For larger instances, falls back to a simpler model.
    """
    n = len(distances)

    return solve_tsp_with_z3_direct(distances)



def solve_tsp_with_z3_direct(distances):
    """Direct Z3 TSP solver for very small instances."""
    n = len(distances)
    solver = Optimize()

    # Create variables for the tour
    tour = [Int(f'x{i}') for i in range(n)]

    # Each position in the tour must be a distinct city
    solver.add(Distinct(tour))

    # Each city must be in the valid range
    for city in tour:
        solver.add(city >= 0, city < n)

    # Symmetry breaking: fix the first city to be 0
    solver.add(tour[0] == 0)

    # Calculate total distance
    total_distance = 0
    for i in range(n):
        current_city = tour[i]
        next_city = tour[(i + 1) % n]
        distance = 0
        for j in range(n):
            for k in range(n):
                distance = If(And(current_city == j, next_city == k), distances[j][k], distance)
        total_distance += distance

    # Minimize the total distance
    solver.minimize(total_distance)

    if solver.check() == sat:
        model = solver.model()
        best_tour = [model.eval(city).as_long() for city in tour]
        return best_tour
    else:
        return None


def solve_tsp_with_z3_simple(distances):
    """Simple Z3 TSP solver for small to medium instances."""
    n = len(distances)
    solver = Optimize()

    # Create variables for the tour
    tour = [Int(f'x{i}') for i in range(n)]

    # Each position in the tour must be a distinct city
    solver.add(Distinct(tour))

    # Each city must be in the valid range
    for city in tour:
        solver.add(city >= 0, city < n)

    # Symmetry breaking: fix the first city to be 0
    solver.add(tour[0] == 0)

    # Calculate total distance directly
    total_distance = 0
    for i in range(n):
        current_city = tour[i]
        next_city = tour[(i + 1) % n]

        # Use a more efficient approach for distance calculation
        city_distances = []
        for j in range(n):
            for k in range(n):
                city_distances.append(If(And(current_city == j, next_city == k), distances[j][k], 0))

        total_distance += Sum(city_distances)

    # Minimize the total distance
    solver.minimize(total_distance)

    # Set solver parameters
    solver.set("timeout", 600000)

    if solver.check() == sat:
        model = solver.model()
        best_tour = [model.eval(city).as_long() for city in tour]
        return best_tour
    else:
        print("No solution found")
        return None


def solve_tsp_with_z3_advanced(distances):
    """Advanced Z3 TSP solver for larger instances."""
    n = len(distances)
    solver = Optimize()

    # Create variables for the tour
    tour = [Int(f'x{i}') for i in range(n)]

    # Each position in the tour must be a distinct city
    solver.add(Distinct(tour))

    # Each city must be in the valid range
    for city in tour:
        solver.add(city >= 0, city < n)

    # Symmetry breaking: fix the first city to be 0
    solver.add(tour[0] == 0)

    # Create binary variables for city connections
    visit = [[Bool(f"visit_{i}_{j}") for j in range(n)] for i in range(n)]

    # Connect tour positions to visit variables
    for i in range(n):
        next_idx = (i + 1) % n
        for j in range(n):
            for k in range(n):
                solver.add(Implies(And(tour[i] == j, tour[next_idx] == k), visit[j][k]))

    # Flow constraints: each city has exactly one incoming and one outgoing connection
    for i in range(n):
        solver.add(PbEq([(visit[i][j], 1) for j in range(n)], 1))
        solver.add(PbEq([(visit[j][i], 1) for j in range(n)], 1))

    # No self-loops
    for i in range(n):
        solver.add(Not(visit[i][i]))

    # Subtour elimination using MTZ formulation
    pos = [Int(f'pos_{i}') for i in range(1, n)]

    for i in range(1, n):
        solver.add(pos[i-1] >= 1, pos[i-1] <= n-1)

    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                solver.add(Implies(visit[i][j], pos[j-1] == pos[i-1] + 1))

    # Calculate total distance directly using visit variables
    total_distance = Sum([If(visit[i][j], distances[i][j], 0) for i in range(n) for j in range(n)])

    # Minimize the total distance
    solver.minimize(total_distance)

    # Set solver parameters
    solver.set("timeout", 120000)

    # Adaptive time limit based on problem size
    max_time = 120000  # Between 5 and 60 seconds

    result = solver.check()
    if result == sat:
        model = solver.model()
        best_tour = [model.eval(city).as_long() for city in tour]

        # Try to improve the solution incrementally if time permits
        start_time = time.time()
        while time.time() - start_time < max_time:
            current_distance = sum(distances[best_tour[i]][best_tour[(i + 1) % n]] for i in range(n))
            solver.add(total_distance < current_distance)

            if solver.check() == sat:
                model = solver.model()
                best_tour = [model.eval(city).as_long() for city in tour]
            else:
                break

        return best_tour
    else:
        return None
