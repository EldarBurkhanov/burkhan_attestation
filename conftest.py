import pytest
import allure

BASE_URL = "https://petstore.swagger.io/v2"


"""Hook for add custom marks"""
def pytest_configure(config):
    config.addinivalue_line("markers", "delete_method: mark a test as a DELETE method test")
    config.addinivalue_line("markers", "get_method: mark a test as a GET method test")
    config.addinivalue_line("markers", "post_method: mark a test as a POST method test")
    config.addinivalue_line("markers", "put_method: mark a test as a PUT method test")
    config.addinivalue_line("markers", "patch_method: mark a test as a PATCH method test")


@pytest.fixture
def get_base_url():
    return BASE_URL


@pytest.fixture
def get_default_body():
    body = {"id": 1,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "Korjik",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
           }
    return body
