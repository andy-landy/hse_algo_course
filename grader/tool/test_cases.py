from lib.test_cases import Test

from problems.lamps import gen_lamps_tests_1


part_id_to_gen_tests: 'Dict[str, Callable[[], List[Test]]]' = {
    'YmGLo': gen_lamps_tests_0,
    'jEQnE': gen_lamps_tests_1,
    'K1r6z': gen_lamps_w_more_cells_tests,
    'YVTAJ': gen_soap_bag_tests,
    '2YSjT': gen_sabotage_tests,
    'paPkt': gen_several_bookings_tests,
    '62qj5': gen_simple_dijkstra_tests,
    'ACEki': gen_word_chains_tests,
    'Tgeji': gen_easy_zip_tests,
    'gLLso': gen_appr_tsp_tests,
    # add tests here
}
