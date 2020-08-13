class ResponseException(Exception):
    def __init__(self, status_code, message=""):
        self.message = message
        self.status_code = status_code

    def __str__(self):
        # return self.message + f"Response gave status code {self.status_code}"
        return self.message + "Response gave status code " + str(self.status_code) + ". Try updating your token!"
