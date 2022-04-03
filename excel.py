from sqlite3 import Connection
from database import insertUser, getUsers
import pandas as pd


def importFromFile(path: str, conn: Connection):
    """Import data about users from xls/xlsx file to DB"""

    try:
        dict = pd.read_excel(path, header=0)
    except FileNotFoundError as e:
        print(e)
        return

    for val in dict.values:
        insertUser(val, conn)

    conn.commit()
    print('Succes!')


def exportToFile(filename: str,  conn: Connection):
    """Export data about users from DB to xls/xlsx file"""

    res = getUsers(conn)

    res = pd.DataFrame(res)
    res.to_excel(
        filename,
        header=[
            'Фамилия',
            'Имя',
            'Отчество',
            'Регион',
            'Город',
            'Контактный телефон',
            'e-mail'
        ],
        index=False
    )
    print('Succes!')
