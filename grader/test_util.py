import json
import logging
from math import isclose
from pathlib import Path
from typing import List, Dict, Iterator, Any, NoReturn

from grader.test import Kwargs, ScoreRatioAndFeedback, Answer, CheckAnswer, Test, CreateTests

logger = logging.getLogger(__name__)


def check_exact_answer(input_kwargs: Kwargs, checker_kwargs: Kwargs, answer: Answer) -> ScoreRatioAndFeedback:
    correct_answer = checker_kwargs['correct_answer']

    if type(answer) != type(correct_answer):
        return 0.0, f'your answer has type {type(answer)}, but {type(correct_answer)} was expected'

    if answer == correct_answer if not isinstance(answer, float) else isclose(answer, correct_answer):
        return 1.0, 'correct answer'

    logger.info(f'wrong answer: correct = {correct_answer}, obtained = {answer}')
    return 0.0, 'wrong answer'


def simple_load_tests(path: Path, check_answer: CheckAnswer) -> List[Test]:
    with path.open('r') as in_:
        return [
            Test(
                input_kwargs=data['input_kwargs'],
                checker_kwargs=data['checker_kwargs'],
                check_answer=check_answer,
                timeout_s=data['timeout_s'],
                score=data['score'],
            ) for data in (json.loads(line) for line in in_)
        ]


def simple_load_part_id_to_create_tests(dir_path: Path, check_answer: CheckAnswer) -> Dict[str, CreateTests]:
    return {
        path.stem: lambda: simple_load_tests(path=path, check_answer=check_answer)
        for path in dir_path.rglob('*.json')
    }


def simple_save_test_datas(path: Path, test_datas: Iterator[Dict[str, Any]]) -> NoReturn:
    with path.open('w') as out:
        for data in test_datas:
            json.dump(fp=out, obj=data)
            out.write('\n')
