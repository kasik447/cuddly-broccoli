from faker import Faker

from lessons.modelsHW.database import create_db, Session
from lessons.modelsHW.buyers import Buyer
from lessons.modelsHW.sellers import Seller


def create_database(load_fake_data: bool = True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session: Session):

    seller1 = Seller(seller_name='Xiaomi')
    seller2 = Seller(seller_name='Apple')
    seller3 = Seller(seller_name='Vivo')
    seller4 = Seller(seller_name='Nokia')
    session.add(seller1)
    session.add(seller2)
    session.add(seller3)
    session.add(seller4)

    faker = Faker('ru_RU')
    seller_list = [seller1, seller2, seller3, seller4]
    session.commit()

    for _ in range(30):
        full_name = faker.name().split(' ')
        address = faker.address()
        seller = faker.random.choice(seller_list)
        buyers = Buyer(full_name, address, seller.id)
        session.add(buyers)

    session.commit()
    session.close()
