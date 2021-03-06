from logic import graph_creator, extended_names_unifier, results_filter, measuring_function_finder
from config import config


if __name__ == '__main__':
    measuring_function = measuring_function_finder.get_stats_measuring_function(config.MEASURE_BY)
    stats = measuring_function()
    stats = extended_names_unifier.unify_extended_names(stats)
    stats = results_filter.filter_results(stats)
    graph_creator.generate_stats_bar_graph(stats)
