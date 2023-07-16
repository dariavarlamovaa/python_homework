from sqlalchemy import Column, ForeignKey, String, Integer
from .database import Base
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = 'Customers'
    c_id = Column(Integer, primary_key=True, nullable=False)
    c_name = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    s_id = Column(Integer, ForeignKey('Salesmen.s_id'))
    salesman = relationship('Salesman', backref='customers')

    def __init__(self, c_id, c_name, city, s_id):
        self.c_id = c_id
        self.c_name = c_name
        self.city = city
        self.s_id = s_id

    def __repr__(self):
        return f'Customer Id: {self.c_id}\n' \
               f'Customer Name: {self.c_name}\n'\
               f'City: {self.city}\n'\
               f'Salesman Id: {self.s_id}'