import peewee
from models import *


def add_category(name):
    row = Category(
        name=name.lower().strip(),
    )
    row.save()


def add_product(name, price, category_name):
    cat_exist = True
    try:
        category = Category.select().where(Category.name == category_name.strip()).get()
    except DoesNotExist as de:
        cat_exist = False

    if cat_exist:
        row = Product(
            name=name.lower().strip(),
            price=price,
            category=category
        )
        row.save()


if __name__ == '__main__':
    add_category('Books')
    add_category('Electronic Appliances')

    add_product('C++ Premier', 24.5, 'books')
    add_product('Juicer', 224.25, 'Electronic Appliances')
