class RequestError:
    __slots__ = (
        "error",
        "error_description",
    )

    def __init__(self, error: str, error_description: str):
        self.error = error
        self.error_description = error_description

    def __str__(self):
        return f"{self.error}: {self.error_description}"
