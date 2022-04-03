import database as db
import excel
import pdf


def main():
    """Main function of porgramm"""

    conn = db.connect()

    if not conn:
        print('An error occurred while connecting to the DB')
        return

    answer = None
    while(True):
        if answer == 'q' or answer == 'Q':
            break

        print("\n1. Import from xls/xlsx to database\n"
              "2. Export from database to xls/xlsx\n"
              "3. Import from PDF to database\n"
              "4. Export from database to PDF\n")
        answer = input('Select operation or enter "q" to exit from program: ')
        if answer == '1':
            path = input('Enter path to xls/xlsx file: ')
            excel.importFromFile(path, conn)
        elif answer == '2':
            filename = input("Enter the filename you want to save the data: ")
            excel.exportToFile(filename, conn)
        elif answer == '3':
            path = input('Enter path to PDF file: ')
            pdf.importFromFile(path, conn)
        elif answer == '4':
            filename = input("Enter the filename you want to save the data: ")
            pdf.exportToFile(filename, conn)


if __name__ == '__main__':
    main()
