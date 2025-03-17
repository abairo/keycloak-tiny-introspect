from keycloak_tiny_introspect.types import RequestError


def test_request_error():
    """Tests the initialization and attributes of RequestError"""
    request_error = RequestError("invalid_request", "Authentication failed.")
    assert request_error.error == "invalid_request"
    assert request_error.error_description == "Authentication failed."


def test_request_error_message():
    """Tests the message value (__str__)"""
    request_error = RequestError("invalid_request", "Authentication failed.")
    assert str(request_error) == "invalid_request: Authentication failed."
