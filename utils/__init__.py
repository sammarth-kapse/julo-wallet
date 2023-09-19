import secrets
import uuid
from datetime import datetime, timezone, timedelta

def get_formatted_time(timezone_offset_hours=-5):
    # Get the current UTC time
    current_time_utc = datetime.now(timezone.utc)

    # Calculate the offset for the desired timezone
    offset = timedelta(hours=timezone_offset_hours)

    # Calculate the time in the desired timezone
    current_time_timezone = current_time_utc + offset

    # Format the time as a string in ISO 8601 format
    formatted_time = current_time_timezone.strftime('%Y-%m-%dT%H:%M:%S%z')

    return formatted_time


def generate_token(length=42):
    token = secrets.token_hex(length // 2)
    return token


def generate_unique_id():
    unique_id = str(uuid.uuid4())
    return unique_id
