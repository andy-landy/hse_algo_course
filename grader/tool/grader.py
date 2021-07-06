from traceback_with_variables import activate_by_import

from lib.grader import main
from tool.test_cases import part_id_to_gen_tests


if __name__ == '__main__':
    main(part_id_to_gen_tests)

