from sqlalchemy import Column, Integer, ForeignKey, String, Float
from .database import Base
from sqlalchemy.orm import relationship


class Sale(Base):
    __tablename__ = 'Sales'
    o_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    s_id = Column(Integer, ForeignKey('Salesmen.s_id'))
    c_id = Column(Integer, ForeignKey('Customers.c_id'))
    amt = Column(Float, nullable=False)
    order_date = Column(String, nullable=False)
    salesman = relationship('Salesman', backref='sales')
    customer = relationship('Customer', backref='sales')

    def __init__(self, o_id, s_id, c_id, amt, order_date):
        self.o_id = o_id
        self.s_id = s_id
        self.c_id = c_id
        self.amt = amt
        self.order_date = order_date

    def __repr__(self):
        return f'Order Id: {self.o_id}\n' \
               f'Salesman Id: {self.s_id}\n'\
               f'Customer Id: {self.c_id}\n'\
               f'Amount: {self.amt}\n'\
               f'Order date: {self.order_date}'