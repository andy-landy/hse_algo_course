from dataclasses import dataclass
from typing import Any, Dict, Callable, Tuple, Protocol, List

Kwargs = Dict[str, Any]
Answer = Any
Solve = Callable[..., Answer]
ScoreRatioAndFeedback = Tuple[float, str]
# var names:            input_kwargs, checker_kwargs, answer
CheckAnswer = Callable[[Kwargs, Kwargs, Answer], ScoreRatioAndFeedback]


@dataclass
class TestCase:
    input_kwargs: Kwargs
    checker_kwargs: Kwargs
    timeout_s: float
    check_answer: CheckAnswer
    score: float


GenTestCases: Callable[[], List[TestCase]]
