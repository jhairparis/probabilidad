from lib.user_cli import UserCLI


def percentage_view(val, cli: UserCLI):
    if cli.answers["percentage"] == True:
        return "{:.0%}".format(val)
    else:
        return val
