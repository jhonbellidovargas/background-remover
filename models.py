# models.py
from pydantic import BaseModel

class ImageResponse(BaseModel):
    message: str
    image_data: bytes

# Clase para controlar el número de consultas por día
class UsageControl:
    def __init__(self, max_requests: int):
        self.max_requests = max_requests
        self.requests_today = 0

    def increment_requests(self):
        if self.requests_today < self.max_requests:
            self.requests_today += 1
            return True
        return False

    def reset_daily_usage(self):
        self.requests_today = 0

usage_control = UsageControl(max_requests=200)
