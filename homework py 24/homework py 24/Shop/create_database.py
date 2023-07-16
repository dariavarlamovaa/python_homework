from models.database import Session, create_db

from models.sales import Sale
from models.salesmen import Salesman
from models.customers import Customer


def create_database(load_data=True):
    create_db()
    if load_data:
        _load_data(Session())


def _load_data(session):
    s_id = [1000, 1001, 1002, 1003, 1004, 1007]
    s_name = ['Rikki', 'Peel', 'Serres', 'Axelrod', 'Motika', 'Rifkin']
    commission = [0.89999997615814, 0.11999999731779, 0.12999999523163,
                  0.10000000149012, 0.10999999940395, 0.15000000596046]
    s_city = ['Rome', 'London', 'San Jose', 'New York', 'London', 'Barcelona']

    for i in range(len(s_id)):
        salesman = Salesman(s_id[i], s_name[i], commission[i], s_city[i])
        session.add(salesman)

    session.commit()

    o_id = [3001, 3002, 3003, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012]
    salesman_id = [1007, 1004, 1001, 1002, 1007, 1002, 1001, 1003, 1002, 1001, 1000]
    c_id = [2008, 2007, 2001, 2003, 2008, 2004, 2006, 2002, 2004, 2006, 2009]
    amt = [18.69, 767.19, 1900.1, 5160.45, 1098.16, 1713.23, 75.75, 4723, 1309.95, 9891.88, 421.3]
    order_date = ['1990-03-10 00:00:00', '1990-03-10 00:00:00', '1990-03-10 00:00:00', '1990-03-10 00:00:00',
                  '1990-03-10 00:00:00', '1990-04-10 00:00:00', '1990-04-10 00:00:00', '1990-05-10 00:00:00',
                  '1990-06-10 00:00:00', '1990-06-10 00:00:00', '1990-06-10 00:00:00']

    for i in range(len(o_id)):
        order = Sale(o_id[i], salesman_id[i], c_id[i], amt[i], order_date[i])
        session.add(order)

    session.commit()

    customer_id = [2001, 2002, 2003, 2004, 2006, 2007, 2008, 2009]
    c_name = ['Hoffman', 'Giovanni', 'Liu', 'Grass', 'Clemens', 'Pereira', 'Cisneros', 'Karl']
    c_city = ['London', 'Rome', 'San Jose', 'Berlin', 'London', 'Rome', 'San Jose', 'Rome']
    salesman_id2 = [1001, 1003, 1002, 1002, 1001, 1004, 1007, 1000]

    for i in range(len(customer_id)):
        customer = Customer(customer_id[i], c_name[i], c_city[i], salesman_id2[i])
        session.add(customer)

    session.commit()
    session.close()