import json
import logging
import os
import shutil
import stat
import sys
from dataclasses import dataclass
from pathlib import Path

from timeout_decorator.timeout_decorator import timeout, TimeoutError


logger = logging.getLogger(__name__)
Kwargs = Dict


@dataclass
class Test:
    input_kwargs: 'Dict[str, Any]'
    timeout_s: float
    check_result: 'Callable[[Dict[str, Any], Any], str]'
    score: float


class FeedbackError(Exception):
    pass


def assert_answer(answer, input_kwargs, solve):
    expected = solve(**input_kwargs)

    if expected != solve:
        logger.info(f'wrong answer (user a. != correct a.): {answer} != {expected}')
        raise FeedbackError(f'wrong answer')


def import_solve(dir_path: Path, name: str) -> 'Callable':
    py_files = list(dir_path.glob('*.py'))
    if len(py_files) != 1:
        raise FeedbackError(f'Please upload a .py file, e.g. called sample.py')
    
    temp_globals = {}
    exec(py_files[0].read_text(), temp_globals)
    if name not in temp_globals:
        raise FeedbackError(f'Uploaded file has no function called {name}')

    return temp_globals[name]


def grade_one_test_and_get_error(test: Test, solve: 'Callable') -> str:
    short_error = grade_one_test_and_get_short_error(test, solve)

    return short_error and '{short_error} on test: {test.input_kwargs}'


def get_result_and_error(test: Test, solve: 'Callable') -> 'Tuple[Any, str]':
    old_stdout = sys.stdout
    sys.stdout = open('/dev/null', 'w')
    
    try:
        for trial in range(3):
            try:
                return timeout(test.timeout_s)(solve)(**test.input_kwargs), ''
            except TimeoutError:
                continue
        else:
            return None, f'Time limit of {test.timeout_s} sec exceeded'

    finally:
        sys.stdout = old_stdout


def grade_one_test_and_get_short_error(test: Test, solve: 'Callable') -> str:
    result, error = get_result_and_error(test, solve)

    return error or test.check_result(**test.input_kwargs, result=result)
    

def grade(part_id: str, part_id_to_gen_tests: 'Dict[str, Callable[[], List[Test]]]') -> 'Tuple[float, str]':
    try:
        solve = import_solve(Path("/shared/submission/"), 'solve')
    except FeedbackError as e:
        return 0.0, str(e)

    tests = part_id_to_gen_tests[part_id]()

    solved_score = 0.0
    total_score = sum(test.score for test in tests)
    for test in tests:
        error = grade_one_test_and_get_error(test, solve)
        if error:
            return solved_score / total_score, 'Some tests were failed, e.g.:\n' + error
        solved_score += test.score

    return 1.0, 'Great job! You passed all test cases'


def main(part_id_to_gen_tests: 'Dict[str, Callable[[], List[Test]]]') -> 'NoReturn':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    part_id = os.getenv('partId')
    # part_id, = sys.argv[2:3]  # grader V1
    
    score, feedback = grade(part_id, part_id_to_gen_tests)
    
    result_str = json.dumps({'fractionalScore': score, 'feedback': feedback})
    # print(result_str)  # grader V1
    Path('/shared/feedback.json').write_text(result_str)

