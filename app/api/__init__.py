from flask import Blueprint, request, jsonify
from app.service import crud
from app.models import *


api_bp = Blueprint("api",__name__,url_prefix="/api")


@api_bp.route("/v1/<source>",methods = ["GET","POST","PUT","DELETE"])
def item_ops(source):
    sources = {
        "shop":Shop,
        "user":User,
        "product":Product
    }
    if request.method == "POST":
        data = request.get_json()
        item = crud.create_item(class_=sources[source],payload=data)
        return item

    elif request.method == "GET":
        data = request.args.get("id")
        item = crud.get_item(class_=sources[source],payload=data)
        return jsonify(item)
    elif request.method == "PUT":
        data = request.get_json()
        item = crud.update_item(class_=sources[source], payload=data)
        return item
    elif request.method == "DELETE":
        data = request.args.get("id")
        item=crud.delete_item(class_=sources[source],payload=data)
        return item


@api_bp.route("/v1/<source>/add-favourites",methods = ["POST"])
def add_to_favourites(source):
    sources = {
        "shop": Shop,
        "user": User,
        "product": Product
    }
    data = request.get_json()
    item = crud.add_favourite(class_=sources[source], payload=data)
    return item


@api_bp.route("/v1/<source>/search",methods = ["POST"])
def search_items(source):

    data = request.get_json()
    item = crud.search_item(class_=source, payload=data)
    return item