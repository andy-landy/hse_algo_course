from traceback_with_variables import activate_by_import  # noqa

from grader.sample_test_cases import part_id_to_gen_tests  # put your checkers here
from grader.grader import main


if __name__ == '__main__':
    main(
        part_id_to_gen_tests=part_id_to_gen_tests,
        excuse_for_no_test='tests are not uploaded yet, please wait couple of days ;)',
    )
