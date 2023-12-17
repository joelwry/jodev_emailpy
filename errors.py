
class EmailPyAPIError(Exception): 
    """Exception raised for EmailPY API errors."""
    def __init__(self, status_code, message):
        super().__init__(f"EmailPY API error: {status_code} - {message}")
