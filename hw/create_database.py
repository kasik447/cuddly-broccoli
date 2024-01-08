from hw.models.database import create_db, Session
from hw.models.buyers import Buyers
from hw.models.sellers import Sellers
from faker import Faker


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):

    seller1 = Sellers(seller_name='Xiaomi')
    seller2 = Sellers(seller_name='Apple')
    session.add(seller1)
    session.add(seller2)

    faker = Faker('ru_RU')
    seller_list = [seller1, seller2]
    session.commit()

    for _ in range(10):
        full_name = faker.name().split()
        address = faker.address()
        seller = faker.random.choice(seller_list)
        student = Buyers(full_name, address, seller.id)
        session.add(student)

    session.commit()
    session.close()


