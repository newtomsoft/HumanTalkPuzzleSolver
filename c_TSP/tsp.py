import os
import random

import numpy as np
import matplotlib.pyplot as plt
import time
import tspManualHeuristic
import tspOrTools
import tspPulp
import tspScip
import tspZ3


def generate_random_tsp(n: int, seed: int = None) -> tuple[np.ndarray, np.ndarray]:
    if seed is not None:
        np.random.seed(seed)

    n1 = n // 10
    n2 = n // 15
    n3 = n // 20
    n0 = n - n1 - n2 - n3
    points0 = np.random.uniform(0, 1000, (n0, 2))
    points1 = np.random.uniform(0, 100, (n1, 2))
    points2 = np.random.uniform(900, 1000, (n2, 2))
    points3 = np.random.uniform(400, 600, (n3, 2))
    points = np.concatenate((points0, points1, points2, points3))

    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distances[i][j] = np.sqrt(((points[i] - points[j]) ** 2).sum())

    return points, distances


def plot_tsp_solution(points, tour, algo, solve_time, seed: int):
    if not tour:
        return

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.scatter(points[:, 0], points[:, 1], c='blue', s=50)

    for i, (x, y) in enumerate(points):
        ax.annotate(str(i), (x, y), xytext=(5, 5), textcoords='offset points')

    tour_points = np.array([points[i] for i in tour + [tour[0]]])
    ax.plot(tour_points[:, 0], tour_points[:, 1], 'r-')
    tour_length = sum(np.sqrt(np.sum((tour_points[i] - tour_points[i + 1]) ** 2)) for i in range(len(tour_points) - 1))

    ax.set_title(f"TSP {algo} - seed: {seed} - points: {len(points)}\n"
                 f"calcul: {solve_time:.2f}s - longueur: {tour_length:.2f}")

    ax.grid(True)
    plt.tight_layout()
    filename = f"{seed}_{len(points)}_{int(tour_length)}_{algo.lower()}.png"
    dir = 'benchmark_tsp'
    full_filename = os.path.join(dir, filename)
    plt.savefig(full_filename)
    plt.close()


def solve_and_draw_tsp(distances, points, nom_solveur, fonction_solveur, seed: int):
    start_time = time.time()
    tour = fonction_solveur(distances)
    solve_time = time.time() - start_time
    if not tour:
        return

    plot_tsp_solution(points, tour, nom_solveur.lower(), solve_time, seed)


if __name__ == "__main__":
    n_cities = 12
    seed = random.randint(0, 10_000)
    seed = 69
    print(f"seed: {seed}")
    points, distances = generate_random_tsp(n_cities, seed)
    solve_and_draw_tsp(distances, points, "OR-Tools", tspOrTools.solve_tsp_with_ortools, seed)
    # solve_and_draw_tsp(distances, points, "Manual Heuristic", tspManualHeuristic.solve_tsp_heuristic, seed)
    # solve_and_draw_tsp(distances, points, "PuLP", tspPulp.solve_tsp_with_pulp, seed)
    # solve_and_draw_tsp(distances, points, "SCIP", tspScip.solve_tsp_with_scip, seed)
    # solve_and_draw_tsp(distances, points, "Z3", tspZ3.solve_tsp_with_z3, seed)
