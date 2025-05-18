class ProjectXAPIError(Exception):
    def __init__(self, code: int, message: str):
        super().__init__(f"API error: [{code}] {message}")
        self.code = code
        self.message = message

class StatusCodeError(Exception):
    pass
