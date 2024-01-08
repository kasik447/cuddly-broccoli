from sqlalchemy import Column, Integer, String, ForeignKey

from lessons.modelsHW.database import Base


class Buyer(Base):
    __tablename__ = 'Buyers'

    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    address = Column(String)
    seller = Column(Integer, ForeignKey('sellers.id'))

    def __init__(self, full_name: list[str], address: str, seller: int):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.address = address
        self.seller = seller

    def __repr__(self):
        info: str = f'Покупатель [ФИО: {self.surname} {self.name} {self.patronymic}, ' \
            f'Адрес: {self.address}, ID продавца: {self.seller_id}]'
        return info





