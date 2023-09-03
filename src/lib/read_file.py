from pandas import read_excel as pd_read_excel
from lib.user_cli import UserCLI


def read_excel(cli: UserCLI):
    q = "Escribe la ubicacion del excel a leer"
    path_file = cli.get_path(q)

    base = pd_read_excel(path_file, sheet_name="DB", index_col=0, header=0)
    base_headers = list(base.columns.values)

    return {"data": base, "headers": base_headers}
