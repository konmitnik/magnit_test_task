from database import getUsers
from sqlite3 import Connection
from fpdf import FPDF


def importFromFile(path: str, conn: Connection):
    """Import data about user from PDF file to DB"""
    pass


def exportToFile(filename, conn):
    """Export data about all users from DB to PDF"""

    users = getUsers(conn)

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', r'font\DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', size=10)

    for user in users:
        pdf.write(
            h=10,
            txt=' '.join([str(item) for item in user])+'\n'
        )

    pdf.output(filename)
    print('Success!')
