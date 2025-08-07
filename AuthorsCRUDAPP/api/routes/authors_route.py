from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.authors import Author, AuthorSchema
from api.utils.database import db
import logging

author_routes = Blueprint('author_routes', __name__)

@author_routes.route('/', methods=['POST'])
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author_data = author_schema.load(data)
        new_author = author_data.create()
        result = author_schema.dump(new_author)
        return response_with(resp.SUCCESS_201, value={"author": result})
    
    except Exception as e:
        logging.error(f"Server error: {e}")
        return response_with(resp.INVALID_INPUT_422)
