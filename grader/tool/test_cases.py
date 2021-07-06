from lib.test_cases import Test

from problems.lamps import gen_lamps_tests_1


part_id_to_gen_tests: 'Dict[str, Callable[[], List[Test]]]' = {
    'qwe123': gen_lamps_tests_1,
    # add tests here
}
