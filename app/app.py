from flask import Flask, render_template
from form_request import form_request
import mongo

app = Flask(__name__)
HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<request_id>', methods=HTTP_METHODS)
def request_id(request_id):
    request_info = form_request(request_id)

    mongo.insert_into_db(request_info)
    return render_template('request_id.html', request_id=request_id), 200


@app.route('/<request_id>/requests', methods=['GET'])
def requests(request_id):
    result = mongo.get_requests_from_db(request_id)
    if result:
        return render_template('show_requests.html', request_id=request_id, data=result), 200

    else:
        return f'No requests for {request_id}'


if __name__ == '__main__':
    app.run(debug=True)
