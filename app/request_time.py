from datetime import datetime


def get_request_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    return current_time
