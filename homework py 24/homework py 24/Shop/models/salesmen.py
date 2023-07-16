from sqlalchemy import Column, Integer, String, Float
from .database import Base
from sqlalchemy.orm import relationship


class Salesman(Base):
    __tablename__ = 'Salesmen'
    s_id = Column(Integer, primary_key=True, nullable=False)
    s_name = Column(String(100), nullable=False)
    commission = Column(Float, default=0)
    city = Column(String(100), nullable=False)

    def __init__(self, s_id, s_name, commission, city):
        self.s_id = s_id
        self.s_name = s_name
        self.commission = commission
        self.city = city

    def __repr__(self):
        return f'Salesman Id: {self.s_id}\n' \
               f'Salesman name: {self.s_name}\n' \
               f'Commission: {self.commission}\n' \
               f'City: {self.city}'
