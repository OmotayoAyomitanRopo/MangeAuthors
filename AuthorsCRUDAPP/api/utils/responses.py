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
    if headers is None:
        headers = {}
        headers.update({
            'Access-Conrol-Allow-origin': '*',
            'Server': 'Flask REST API'
        })

    return make_response(jsonify(result), response.get('http_code'), headers)

    