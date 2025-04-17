from peewee import Model, AutoField, PrimaryKeyField, CharField, SqliteDatabase, DecimalField, ForeignKeyField, FloatField

# db = SqliteDatabase('db2.db')
# class Category(Model):
#     id = PrimaryKeyField()
#     name = CharField(60)
#     class Meta:
#         database = db
#         db_table = 'categories'
# class Product(Model):
#     id = PrimaryKeyField()
#     name = CharField(60)
#     price = FloatField()
#     category_id = ForeignKeyField(Category)
#     class Meta:
#         database = db
#         db_table = 'products'

db = SqliteDatabase('db2.db')
class Category(Model):
    id = PrimaryKeyField()
    name = CharField(60)
    class Meta:
        database = db
        db_table = 'categories'
class Product(Model):
    id = PrimaryKeyField()
    name = CharField(60)
    price = FloatField()
    category_id = ForeignKeyField(Category)
    class Meta:
        database = db
        db_table = 'products'