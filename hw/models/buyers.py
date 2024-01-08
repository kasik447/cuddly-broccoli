from lessons.models.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Buyers(Base):
    __tablename__ = 'buyers'

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    address = Column(Integer)
    seller = Column(Integer, ForeignKey('seller.id'))

    def __init__(self, full_name, address, seller):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.address = address
        self.seller = seller

    def __repr__(self):
        return f"Покупатель (ФИО: {self.surname} {self.name} {self.patronymic}), " \
                f"адресс: {self.address}, ID_продавца: {self.seller}"



