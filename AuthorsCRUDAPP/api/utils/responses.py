from flask import make_response, jsonify

def response_with(response, value=None, message=None, error=None, header=None,
                  pagination=None):
    result = {} # an empty dictionary

    if value is not None:
        result.update(value) # when value is passed merge to result

    if message is not None: 
        result['message'] = message  # message to result if it is passed
    elif response.get('message') is not None:
        result['message'] = response['message']

    if error is not None:
        result['errors'] = error # Include error details e.g when a user input is invalid

    if pagination is not None:
        result['pagination'] = pagination

    result['code'] = response.get('code', '') # Added an extra custom app-level code

    # Create and add custom HTTP header
    if header is None:
        header = {}
        header.update({
            'Access-Conrol-Allow-Origin': '*',
            'Server': 'Flask REST API'
        })

    return make_response(jsonify(result), response.get('http_code'), header)



# ---------------------------------------
# Predefined response templates
# ---------------------------------------

SUCCESS_200 = {
    "code": "SUCCESS",
    "message": "Request completed successfully.",
    "http_code": 200
}

SUCCESS_201 = {
    "code": "CREATED",
    "message": "Resource created successfully.",
    "http_code": 201
}

BAD_REQUEST_400 = {
    "code": "BAD_REQUEST",
    "message": "The request was invalid or cannot be otherwise served.",
    "http_code": 400
}

INVALID_INPUT_422 = {
    "code": "INVALID_INPUT",
    "message": "The input data is invalid.",
    "http_code": 422
}

SERVER_ERROR_500 = {
    "code": "INTERNAL_SERVER_ERROR",
    "message": "An unexpected error occurred on the server.",
    "http_code": 500
}

SERVER_ERROR_404 = {
    "code": "NOT_FOUND",
    "message": "The requested resource could not be found.",
    "http_code": 404
}
