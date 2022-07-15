from models import (csv_reader, brand_csv_reader, engine)
import models
import view_product
import add_product
import analyze_database
import backup_database


def menu():
    selection = input('''------Store Inventory Manager------\n
            \rPlease Select from the Menu Below
            \r\tEnter V to view a single product
            \r\tEnter N to add a product
            \r\tEnter A to Analyze the Database
            \r\tEnter B to backup the database
            \r\tEnter Q to Exit the Program
            \rEnter Command: ''')

    if selection.lower() == "v":
        view_product.view_summary()

    elif selection.lower() == "n":
        add_product.add_product()

    elif selection.lower() == "a":
        analyze_database.analyze_database()

    elif selection.lower() == "b":
        backup_database.backup_csv()

    elif selection.lower() == 'q':
        print('Thank you for using this program!')
        exit()
    else:
        input('''\nA Valid Command Was Not Entered
                \rPress Enter To Try Again.''')
        menu()


if __name__ == '__main__':
    models.Base.metadata.create_all(engine)
    brand_csv_reader()
    csv_reader()
    menu()
