from convert import terminal_convert
from lib.exam.main import exam
from user_cli import yesOrNo


def run_other(base):
    other = yesOrNo("Question of exam?")
    if other:
        exam(base["data"], base["headers"])

    run_convert = yesOrNo("Do you need convert?")
    if run_convert:
        terminal_convert()
