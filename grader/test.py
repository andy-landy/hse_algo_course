from dataclasses import dataclass
from typing import Any, Dict, Callable, Tuple, List

Kwargs = Dict[str, Any]
Answer = Any
Solve = Callable[..., Answer]
ScoreRatioAndFeedback = Tuple[float, str]
# args names:           input_kwargs, checker_kwargs, answer
CheckAnswer = Callable[[Kwargs, Kwargs, Answer], ScoreRatioAndFeedback]


@dataclass
class Test:
    input_kwargs: Kwargs
    checker_kwargs: Kwargs
    timeout_s: float
    check_answer: CheckAnswer
    score: float


CreateTests = Callable[[], List[Test]]
