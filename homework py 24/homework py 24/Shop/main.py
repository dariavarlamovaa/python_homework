import os

from models.database import DATABASE_NAME, Session
import create_database as creator_db

from sqlalchemy import func
from models.salesmen import Salesman
from models.sales import Sale
from models.customers import Customer


class Menu:
    session = Session()

    @staticmethod
    def save_results_to_file(data):
        save_choice = input('Do you want to save your data to file? 1-yes, 2-no. Your answer: ')
        if save_choice == '1':
            output_file = 'output_file.txt'
            with open(output_file, 'w') as f:
                f.writelines(str(data))
                print(f'Data successfully saved to the file')
        else:
            pass

    @staticmethod
    def get_customers_name():
        customer_name = input('Enter customer`s name: ').capitalize().strip()
        customer = session.query(Customer).filter(Customer.c_name == customer_name).first()
        if customer:
            return customer_name
        return False

    @staticmethod
    def get_seller_name():
        seller_name = input('Enter seller`s name: ').capitalize().strip()
        seller = session.query(Salesman).filter(Salesman.s_name == seller_name).first()
        if seller:
            return seller_name
        return False

    @staticmethod
    def display_all_transactions():
        data = session.query(Sale)
        for order in data:
            print(order, end='\n--------------------\n')
        Menu.save_results_to_file(data.all())

    @staticmethod
    def display_the_transactions_of_a_specific_seller():
        seller_name = Menu.get_seller_name()
        if seller_name:
            data = session.query(Sale).join(Salesman).filter(Salesman.s_name == seller_name).all()
            for order in data:
                print(order, end='\n--------------------\n')
            Menu.save_results_to_file(data)
        else:
            print('No such seller in the Database')

    @staticmethod
    def display_the_maximum_transaction_amount():
        maximum = session.query(func.sum(Sale.amt)).group_by(Sale.s_id).order_by(func.sum(Sale.amt).desc())
        print(maximum.first()[0])
        Menu.save_results_to_file(maximum.first()[0])

    @staticmethod
    def display_the_minimum_transaction_amount():
        minimum = session.query(func.sum(Sale.amt)).group_by(Sale.s_id).order_by(func.sum(Sale.amt).asc())
        print(minimum.first()[0])
        Menu.save_results_to_file(minimum.first()[0])

    @staticmethod
    def display_the_maximum_transaction_amount_for_a_specific_seller():
        seller_name = Menu.get_seller_name()
        if seller_name:
            maximum = session.query(func.max(Sale.amt)).join(Salesman).filter(
                Salesman.s_name == seller_name)
            print(maximum.first()[0])
            Menu.save_results_to_file(maximum.first()[0])
        else:
            print('No such seller in the Database')

    @staticmethod
    def display_the_minimum_transaction_amount_for_a_specific_seller():
        seller_name = Menu.get_seller_name()
        if seller_name:
            minimum = session.query(func.min(Sale.amt)).join(Salesman).filter(
                Salesman.s_name == seller_name)
            Menu.save_results_to_file(minimum.first()[0])
        else:
            print('No such seller in the Database')

    @staticmethod
    def display_the_maximum_transaction_amount_for_a_specific_customer():
        customer_name = Menu.get_customers_name()
        if customer_name:
            maximum = session.query(func.max(Sale.amt)).join(Customer).filter(
                Customer.c_name == customer_name)
            print(maximum.first()[0])
            Menu.save_results_to_file(maximum.first()[0])
        else:
            print('No such customer in the Database')

    @staticmethod
    def display_the_minimum_transaction_amount_for_a_specific_customer():
        customer_name = Menu.get_customers_name()
        if customer_name:
            minimum = session.query(func.min(Sale.amt)).join(Customer).filter(
                Customer.c_name == customer_name)
            print(minimum.first()[0])
            Menu.save_results_to_file(minimum.first()[0])
        else:
            print('No such customer in the Database')

    @staticmethod
    def display_the_seller_with_maximum_amount_of_sales():
        seller_maximum = session.query(Salesman.s_name).join(Sale).group_by(Sale.s_id).order_by(
            func.sum(Sale.amt).desc())
        print(seller_maximum.first()[0])
        Menu.save_results_to_file(seller_maximum.first()[0])

    @staticmethod
    def display_the_seller_with_minimum_amount_of_sales():
        seller_minimum = session.query(Salesman.s_name).join(Sale).group_by(Sale.s_id).order_by(
            func.sum(Sale.amt).asc())
        print(seller_minimum.first()[0])
        Menu.save_results_to_file(seller_minimum.first()[0])

    @staticmethod
    def display_the_customer_with_maximum_amount_of_purchases():
        customer_maximum = session.query(Customer.c_name).join(Sale).group_by(Sale.c_id).order_by(
            func.sum(Sale.amt).desc())
        print(customer_maximum.first()[0])
        Menu.save_results_to_file(customer_maximum.first()[0])

    @staticmethod
    def display_the_average_purchase_amount_for_customer():
        customer_name = Menu.get_customers_name()
        if customer_name:
            customer_average = session.query(func.avg(Sale.amt)).join(Customer).filter(
                Customer.c_name == customer_name)
            print(customer_average.first()[0])
            Menu.save_results_to_file(customer_average.first()[0])
        else:
            print('No such customer in the Database')

    @staticmethod
    def display_the_average_purchase_amount_for_seller():
        seller_name = Menu.get_seller_name()
        if seller_name:
            seller_average = session.query(func.avg(Sale.amt)).join(Salesman).filter(
                Salesman.s_name == seller_name)
            print(seller_average.first()[0])
            Menu.save_results_to_file(seller_average.first()[0])
        else:
            print('No such seller in the Database')

    @staticmethod
    def insert_new_sale():
        seller_name = Menu.get_seller_name()
        customer_name = Menu.get_customers_name()
        if seller_name and customer_name:
            try:
                o_id = session.query(Sale.o_id).order_by(Sale.o_id.desc()).first()[0] + 1
                seller_id = session.query(Salesman.s_id).filter(Salesman.s_name == seller_name).first()[0]
                customer_id = session.query(Customer.s_id).filter(Customer.c_name == customer_name).first()[0]
                amount = float(input('Enter the amount of the sale: '))
                order_date = input('enter order date (yyyy-mm-dd 00:00:00): ')
                new_sale = Sale(o_id, seller_id, customer_id, amount, order_date)
                session.add(new_sale)
                session.commit()
                print('Sale successfully added to the Database')
            except ValueError:
                print('Amount and order date can not be empty')
        else:
            print('There is no such seller or customer in the Database')

    @staticmethod
    def update_sale():
        sale_id = int(input("Enter sale Id: "))
        sale = session.query(Sale).filter(Sale.o_id == sale_id).first()
        if sale:
            print(f'Current sale amount: {sale.amt}')
            try:
                new_amt = float(input(f'Enter new amount of {sale_id} sale Id: '))
                sale.amt = new_amt
                session.commit()
                print('Sale successfully updated')
            except ValueError:
                print('Amount can not be empty')
        else:
            print('There is no such sale in the Database')

    @staticmethod
    def delete_sale():
        sale_id = int(input("Enter sale Id: "))
        sale = session.query(Sale).filter(Sale.o_id == sale_id).first()
        if sale:
            session.delete(sale)
            session.commit()
            print('Sale successfully deleted')
        else:
            print('There is no such sale in the Database')

    @staticmethod
    def get_command():
        while True:
            print('1. Display all transactions\n'
                  '2. Display the transactions of a specific seller\n'
                  '3. Display the maximum transaction amount\n'
                  '4. Display the minimum transaction amount\n'
                  '5. Display the maximum transaction amount for a specific seller\n'
                  '6. Display the minimum transaction amount for a specific seller\n'
                  '7. Display the maximum transaction amount for a specific customer\n'
                  '8. Display the minimum transaction amount for a specific customer\n'
                  '9. Display the seller who has the maximum amount of sales for all transactions\n'
                  '10. Display the seller who has the minimum amount of sales for all transactions\n'
                  '11. Display the customer who has the maximum amount of purchases for all transactions\n'
                  '12. Display the average purchase amount for a specific customer\n'
                  '13. Display the average purchase amount for a specific seller\n'
                  '14. Inset new sale\n'
                  '15. Update the sale\n'
                  '16. Delete the sale\n'
                  '0. Exit the menu')
            command = input('Enter your choice: ').strip()
            print('-' * 10)
            if command == '1':
                Menu.display_all_transactions()
            elif command == '2':
                Menu.display_the_transactions_of_a_specific_seller()
            elif command == '3':
                Menu.display_the_maximum_transaction_amount()
            elif command == '4':
                Menu.display_the_minimum_transaction_amount()
            elif command == '5':
                Menu.display_the_maximum_transaction_amount_for_a_specific_seller()
            elif command == '6':
                Menu.display_the_minimum_transaction_amount_for_a_specific_seller()
            elif command == '7':
                Menu.display_the_maximum_transaction_amount_for_a_specific_customer()
            elif command == '8':
                Menu.display_the_minimum_transaction_amount_for_a_specific_customer()
            elif command == '9':
                Menu.display_the_seller_with_maximum_amount_of_sales()
            elif command == '10':
                Menu.display_the_seller_with_minimum_amount_of_sales()
            elif command == '11':
                Menu.display_the_customer_with_maximum_amount_of_purchases()
            elif command == '12':
                Menu.display_the_average_purchase_amount_for_customer()
            elif command == '13':
                Menu.display_the_average_purchase_amount_for_seller()
            elif command == '14':
                Menu.insert_new_sale()
            elif command == '15':
                Menu.update_sale()
            elif command == '16':
                Menu.delete_sale()
            elif command == '0':
                print('Bye-bye!')
                break
            else:
                print('Incorrect input. Try again.')


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        creator_db.create_database()
    session = Session()
    Menu().get_command()
