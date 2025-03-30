class ToolError(Exception):
    """Raised when a tool encounters an error."""

    def __init__(self, message):
        self.message = message


class AikuroError(Exception):
    """Base exception for all Aikuro enterprise system errors"""


class TokenLimitExceeded(AikuroError):
    """Exception raised when the token limit is exceeded"""
