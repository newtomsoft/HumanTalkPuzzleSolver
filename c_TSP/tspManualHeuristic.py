def calculate_distance(tour, distances):
    total = 0
    n = len(tour)
    for i in range(n):
        total += distances[tour[i]][tour[(i + 1) % n]]
    return total


def nearest_neighbor(distances, start_city=0):
    n = len(distances)
    tour = [start_city]
    unvisited = set(range(n))
    unvisited.remove(start_city)
    current = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    return tour


def two_opt_optimize(tour, distances, max_iterations=1500):
    best_tour = tour.copy()
    best_distance = calculate_distance(tour, distances)
    improved = True
    iteration = 0

    while improved and iteration < max_iterations:
        improved = False
        for i in range(len(tour)):
            for j in range(i + 2, len(tour) + (i > 0)):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = calculate_distance(new_tour, distances)

                if new_distance < best_distance:
                    best_tour = new_tour
                    best_distance = new_distance
                    improved = True
                    tour = best_tour.copy()
                    break
            if improved:
                break
        iteration += 1

    return best_tour


def solve_tsp_heuristic(distances):
    initial_tour = nearest_neighbor(distances)
    optimized_tour = two_opt_optimize(initial_tour, distances)
    return optimized_tour
