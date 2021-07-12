import logging
from typing import Any

from grader.test_case import Kwargs, ScoreRatioAndFeedback, Answer, CheckAnswer


logger = logging.getLogger(__name__)


def create_check_exact(correct_answer: Answer) -> CheckAnswer:
    def check_answer(input_kwargs: Kwargs, kwargs: Kwargs, answer: Answer) -> ScoreRatioAndFeedback:
        if answer != correct_answer:
            logger.info(f'wrong answer: correct = {correct_answer}, obtained = {answer}')
            return 0.0, 'wrong answer'

        return 1.0, ''

    return check_answer


