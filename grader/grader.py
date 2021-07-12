import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, Callable, List, NoReturn

from traceback_with_variables import format_exc
from timeout_decorator.timeout_decorator import timeout, TimeoutError

from grader.test_case import TestCase, Kwargs, CheckAnswer, Answer, Solve, ScoreRatioAndFeedback, GenTestCases

logger = logging.getLogger(__name__)


class FeedbackError(Exception):
    pass


def import_solve(dir_path: Path, name: str) -> Solve:
    py_files = list(dir_path.glob('*.py'))
    if len(py_files) == 0:
        raise FeedbackError(f'Please upload a .py file, e.g. called sample.py')
    if len(py_files) > 1:
        logger.error(f'instead of 1 file, this files found: {py_files}')
        raise FeedbackError(f'Please report an internal error "Several py files submitted"')

    temp_globals = {}
    exec(py_files[0].read_text(), temp_globals)
    if name not in temp_globals:
        logger.error(f'Solution must have "def {name}" but on the top level it has: {list(temp_globals)}')
        raise FeedbackError(f'Uploaded file has no function called {name}')

    return temp_globals[name]


def get_answer(case: TestCase, solve: Solve) -> Answer:
    old_stdout = sys.stdout
    sys.stdout = open('/dev/null', 'w')
    
    try:
        for trial in range(3):
            try:
                return timeout(case.timeout_s)(solve)(**case.input_kwargs)
            except TimeoutError:
                continue
            except Exception:
                logger.info(f'solve raised an exception: {format_exc()}')
                raise FeedbackError(f'Exception in solution')
        else:
            raise FeedbackError('Time limit of {test.timeout_s} sec exceeded.')

    finally:
        sys.stdout = old_stdout


def grade_one_case(case: TestCase, solve: Solve) -> ScoreRatioAndFeedback:
    try:
        answer = get_answer(case, solve)

        ratio, feedback = case.check_answer(
            input_kwargs=case.input_kwargs,  # noqa
            checker_kwargs=case.checker_kwargs,  # noqa
            answer=answer,  # noqa
        )  # noqa

    except FeedbackError as e:
        ratio, feedback = 0.0, str(e)

    return ratio, f'{feedback} on test: {case.input_kwargs}'


def grade(cases: List[TestCase]) -> ScoreRatioAndFeedback:
    try:
        solve = import_solve(Path("/shared/submission/"), 'solve')
        rfs = [grade_one_case(case, solve) for case in cases]

        verdict = 'Good job! All answers are correct!' if all(r < 1.0 for r, _ in rfs) else 'Some tests failed.'

        return (
            sum(r * c.score for (r, _), c in zip(rfs, cases)) / sum(c.score for c in cases),
            f'{verdict} Per-test feedbacks: {[f for _, f in rfs if f]}',
        )

    except FeedbackError as e:
        return 0.0, str(e)


def main(part_id_to_gen_tests: Dict[str, GenTestCases], excuse_for_no_test: str) -> NoReturn:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    gen_cases = part_id_to_gen_tests.get(os.getenv('partId'), None)  # part_id = sys.argv[2] in grader V1
    if gen_cases:
        score, feedback = grade(gen_cases())
    else:
        score, feedback = 0, excuse_for_no_test

    Path('/shared/feedback.json').write_text(json.dumps({'fractionalScore': score, 'feedback': feedback}))  # prn for V1
