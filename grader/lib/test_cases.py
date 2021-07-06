from dataclasses import dataclass


@dataclass
class Test:
    input_kwargs: 'Dict[str, Any]'
    timeout_s: float
    check_result: 'Callable[[Dict[str, Any], Any], str]'
    score: float
