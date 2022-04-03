from database import insertUser, getUsers
from sqlite3 import Connection
from fpdf import FPDF
import pdfplumber


def importFromFile(path: str, conn: Connection):
    """Import data about user from PDF file to DB"""

    try:
        with pdfplumber.open(path) as pdf:
            text = pdf.pages[0].extract_text()
            text = text.split(' \n')
            user = []
            user.extend(text[2].split(' '))
            user.extend(text[4].split(', '))
            user.extend((text[5], text[6]))

            insertUser(user, conn)
            conn.commit()

            print('Success!')
    except FileNotFoundError as e:
        print(e)
        return


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
