from app.models import *


def create_item(class_, payload):
    if class_ == User:
        item = User(
            email=payload.get("email"),
            fullname=payload.get("fullname"),
            phone=payload.get("phone"),
            role=payload.get("role")
        )
    elif class_ == Shop:
        item = Shop(
            name=payload.get("name"),
            owner=payload.get("owner")
        )
    else:
        item = Product(
            name=payload.get("name"),
            shop=payload.get("shop")
        )
    db.session.add(item)
    db.session.commit()
    return item.as_dict()


def get_item(class_, payload):
    item = class_.query.filter_by(id=payload).first()
    favourite_products = [i.as_dict()["name"] for i in item.favourite_products]
    favourite_shops = [i.as_dict()["name"] for i in item.favourite_shops]

    item_dict = item.as_dict()
    item_dict["favourite_shops"] = favourite_shops
    item_dict["favourite_products"] = favourite_products
    return item_dict


def update_item(class_, payload):
    id_ = payload.pop("id")
    item = class_.query.filter_by(id=id_).update(payload)

    db.session.commit()
    item = class_.query.filter_by(id=id_).first()
    return item.as_dict()


def delete_item(class_, payload):
    class_.query.filter_by(id=payload).delete()

    db.session.commit()
    return "True"


def add_favourite(class_, payload):
    if class_ == "Product":
        user = User.query.filter_by(id=payload.get("user_id")).first()
        item = Product.query.filter_by(id=payload.get("product_id")).first()

        user.favourite_products.append(item)
    else:
        user = User.query.filter_by(id=payload.get("user_id")).first()
        item = Shop.query.filter_by(id=payload.get("shop_id")).first()

        user.favourite_shops.append(item)

    db.session.add(item)
    db.session.commit()
    return "True"


def search_item(class_, payload):
    sources = {
        "shop": Shop,
        "user": User,
        "product": Product
    }
    search_logs(class_, payload)
    items = sources[class_].query.filter(sources[class_].name.like("%" + payload["query"] + "%")).all()




    return {
        "data":[item.as_dict() for item in items]
    }


def search_logs(class_,payload):

    log = SearchLogs.query.filter_by(user_query=payload["query"]).first()
    if log:
        log.count += 1
    else:
        log = SearchLogs(endpoint_name=class_,user_query=payload["query"])
    db.session.add(log)
    db.session.commit()
    return log.as_dict()
