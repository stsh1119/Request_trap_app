from request_time import get_request_time
from flask import request


def form_request(request_id):
    time = get_request_time()
    request_info = {}
    headers = dict(request.headers)
    request_info['headers'] = headers
    request_info['request_id'] = request_id
    request_info['time'] = time
    request_info['ip'] = request.remote_addr
    request_info['method'] = request.method
    request_info['scheme'] = request.scheme
    if request.cookies:  # check if there are cookies, if no - skip it
        request_info['cookies'] = request.cookies
    if request.args:  # check if there is a query string, if no - skip it
        request_info['query-string'] = request.args
    if request.json:
        request_info['data'] = request.json

    return request_info
