from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lessons.modelsHW.database import Base


class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    seller_name = Column(String)
    buyer = relationship('Buyer')

    def __repr__(self):
        return f'Продавец [ID: {self.id}, продукт: {self.seller_name}]'


