from pandas import DataFrame
from lib.other.convert import terminal_convert
from lib.other.exam import exam
from lib.user_cli import UserCLI


def run_other(base: DataFrame, cli: UserCLI):
    other = cli.yesOrNo("Question of exam?")
    if other:
        exam(base["data"], base["headers"])

    run_convert = cli.yesOrNo("Do you need convert?")
    if run_convert:
        terminal_convert()
