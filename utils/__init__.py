import secrets
import uuid
import pytz
from datetime import datetime


def get_formatted_time(timezone_name='Asia/Kolkata'):
    current_time_timezone = datetime.now(pytz.timezone(timezone_name))
    formatted_time = current_time_timezone.strftime('%Y-%m-%dT%H:%M:%S%z')

    return formatted_time


def generate_token(length=42):
    token = secrets.token_hex(length // 2)
    return token


def generate_unique_id():
    unique_id = str(uuid.uuid4())
    return unique_id
