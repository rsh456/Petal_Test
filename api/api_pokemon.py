from flask import Blueprint, request, jsonify,make_response
from data.data_connection import reader,writer,updater,delete,data_pagination,get_data_page,reader_id

api_pk = Blueprint('api_pk', __name__)

@api_pk.route("/pokemon", methods=["GET"])
def pokemon_read():
    id = request.args.get('id', type=int)
    if id is None:
        result = reader()
    else:
        result = reader_id(id)

    if result is not None:
        return jsonify(result), 200
    else:
        return "Bad request", 400

@api_pk.route("/pokemon", methods=["GET"])
def pokemon_read_id():
    id = request.args.get('id', type=int)
    result =reader(id)
    if result is not None:
        return jsonify(result), 200
    else:
        return "Bad request", 400


@api_pk.route("/pokemon_paginated", methods=["GET"])
def pokemon_all_paginated():
    page = request.args.get('page', type=int)
    per_page = request.args.get('per_page', 10, type=int)

    if page is None:
        result = data_pagination(per_page)
    else:
        result = get_data_page(per_page, page)

    if result is not None:
        return jsonify(result), 200
    else:
        return "Bad request", 400



@api_pk.route('/pokemon', methods=['POST'])
def add_pokemon():
    request_data = request.get_json()
    result = writer(request_data)

    if result is not None:
        return "Added", 200
    else:
        return "Bad request", 400

@api_pk.route('/pokemon', methods=['PUT'])
def update_pokemon():
    request_data = request.get_json()
    result = updater(request_data)
    if result is not None:
        return request_data, 200
    else:
        return "Bad request", 400

@api_pk.route('/pokemon', methods=['DELETE'])
def delete_pokemon():
    id = str(request.args.get('id', type=int))
    result = delete(id)
    if result is not None:
        return "Deleted", 200
    else:
        return "Bad request", 400