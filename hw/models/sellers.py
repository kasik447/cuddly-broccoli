from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from hw.models.database import Base


class Sellers(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True)
    seller_name = Column(String(250), nullable=False)
    buyers = relationship('Buyers')

    def __repr__(self):
        return f"Продавец (ID: {self.id}, Продукция: {self.seller_name})"



