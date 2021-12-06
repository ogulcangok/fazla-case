from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

favs = db.Table("favs",
                db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                db.Column("item_id", db.Integer, db.ForeignKey("product.id")),
                db.Column("shop_id", db.Integer, db.ForeignKey("shop.id"))
                )

owns = db.Table("owns",
                db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
                db.Column("shop_id", db.Integer, db.ForeignKey("shop.id"), primary_key=True)
                )

sells = db.Table("sells",
                 db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
                 db.Column("shop_id", db.Integer, db.ForeignKey("shop.id"), primary_key=True)
                 )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    role = db.Column(db.String)
    created_at = db.Column(db.Integer, nullable=False,
                           default=int(datetime.datetime.timestamp(datetime.datetime.now())))
    updated_at = db.Column(db.Integer, nullable=False,
                           default=int(datetime.datetime.timestamp(datetime.datetime.now())))
    status = db.Column(db.Boolean, default=True)
    favourite_products = db.relationship("Product", secondary=favs, backref="favs")
    favourite_shops = db.relationship("Shop", secondary=favs, backref="favs")
    owns = db.relationship("Shop", secondary=owns, backref="owns")

    def __repr__(self):
        return self.fullname

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}




class Shop(db.Model):
    __searchable__ = ["name"]
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.Integer, nullable=False,
                           default=int(datetime.datetime.timestamp(datetime.datetime.now())))
    updated_at = db.Column(db.Integer, nullable=False,
                           default=int(datetime.datetime.timestamp(datetime.datetime.now())))
    status = db.Column(db.Boolean, default=True)
    sells = db.relationship("Product", secondary="sells", backref="sells")

    def __repr__(self):
        return self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Product(db.Model):
    __searchable__ = ["name"]
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    shop = db.Column(db.Integer, db.ForeignKey("shop.id"))
    created_at = db.Column(db.Integer, nullable=False,
                           default=int(datetime.datetime.timestamp(datetime.datetime.now())))
    updated_at = db.Column(db.Integer, nullable=False,
                           default=int(datetime.datetime.timestamp(datetime.datetime.now())))
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class SearchLogs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    endpoint_name = db.Column(db.String)
    user_query = db.Column(db.String)
    count = db.Column(db.Integer,default=1)
    created_at = db.Column(db.Integer, nullable=False,
                           default=int(datetime.datetime.timestamp(datetime.datetime.now())))
    updated_at = db.Column(db.Integer, nullable=False,
                           default=int(datetime.datetime.timestamp(datetime.datetime.now())))
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return self.name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}