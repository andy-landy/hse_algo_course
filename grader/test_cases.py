from dataclasses import dataclass

from problems.lamps import gen_lamps_tests_1, gen_lamps_tests_2


@dataclass
class Test:
    input_kwargs: 'Dict[str, Any]'
    timeout_s: float
    check_result: 'Callable[[Dict[str, Any], Any], str]'
    score: float


part_id_to_gen_tests: 'Dict[str, Callable[[], List[Test]]]' = {
    'qwe123': gen_lamps_tests_1,
    'asd456': gen_lamps_tests_2,
    # add tests here
}
