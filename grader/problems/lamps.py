from random import randint as ri, seed

from lib.test_cases import Test


def check_result(lamps: 'List[float]', cells: 'List[float]', max_cord_len: float, result: bool) -> str:
    if not isinstance(result, bool):
        return f'function must result bool, not {type(result)}'

    true_result = (max(abs(l - c) for l, c in zip(sorted(lamps), sorted(cells))) <= max_cord_len)

    if result != true_result:
        return f'wrong answer: {result}, correct answer: {true_result}'
    
    return ''


def gen_lamps_tests_1():
    seed('32143')

    return [Test(
        input_kwargs={
            'lamps': [ri(-ml, ml) for _ in range(n)],
            'cells': [ri(-cl, cl) for _ in range(n)],
            'max_cord_len': mcl,
        },
        timeout_s=1.0,
        check_result=check_result,
        score=1.0,
    ) for n, ml, cl, mcl in [
        (3, 10, 10, 10),
        (3, 10, 10, 10),
        (3, 10, 10, 10),
        (3, 10, 10, 1),
        (3, 10, 10, 1),
        (3, 10, 10, 1),
        (1, 10, 10, 1), 
        (20, 10, 10, 3),
        (10, 100, 10, 95),
        (10, 100, 10, 95),
        (10, 100, 10, 95),
        (10000, 100000, 100000, 1),
        (10000, 100000, 100000, 1),
        (10000, 100000, 100000, 10),
        (10000, 100000, 100000, 10),
        (10000, 100000, 100000, 100),
        (10000, 100000, 100000, 100),
        (10000, 100000, 100000, 1000),
        (10000, 100000, 100000, 1000),
        (10000, 100000, 100000, 10000),
        (10000, 100000, 100000, 10000),
        (10000, 100000, 100000, 50000),
    ]]
