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

@author_routes.route('/', methods=['GET'])
def get_author_list():
    try:
        author_fetch = Author.query.all()
        author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
        result = author_schema.dump(author_fetch)
        return response_with(resp.SUCCESS_200, value={"result": result})
    except Exception as e:
        logging.error(f"Server error: {e}")
        return response_with(resp.INVALID_INPUT_422)
    
@author_routes.route('<int:author_id>', methods=['GET'])
def get_authorby_id(author_id):
    try:
        fetched = Author.query.get_or_404(author_id)
        author_schema = AuthorSchema()
        result = author_schema.dump(fetched)
        return response_with(resp.SUCCESS_200, value={"result": result})
    except Exception as e:
        logging.error(f"server error: {e}")
        return response_with(resp.INVALID_INPUT_422) 