from ortools.constraint_solver import pywrapcp, routing_enums_pb2


def solve_tsp_with_ortools(distance_matrix):
    n = len(distance_matrix)

    manager = pywrapcp.RoutingIndexManager(n, 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(distance_matrix[from_node][to_node] * 10000)

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        optimal_path = []
        index = routing.Start(0)
        while not routing.IsEnd(index):
            optimal_path.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))

        return optimal_path
    else:
        return None

