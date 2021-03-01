from pymongo import MongoClient
import os


def insert_into_db(value):
    """Inserts formed request into database."""
    client = MongoClient(os.environ.get('MONGOCLIENT'))
    db = client.request_trap
    requests = db.requests

    requests.insert_one(value)


def get_requests_from_db(request_id) -> list:
    """Finds all requests by given request id."""
    client = MongoClient(os.environ.get('MONGOCLIENT'))
    db = client.request_trap
    requests = db.requests
    query = {"request_id": request_id}
    display_results = []

    results = requests.find(query).sort('time', -1)  # sort by time desc
    for result in results:
        display_results.append(result)
    return display_results
