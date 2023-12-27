import pytest
import requests
from test_post.pet_body_validator import Pet
import allure

API_URL = "/pet/"


@pytest.mark.delete_method
@allure.title("Test DELETE method")
@allure.description("This test sends a DELETE request to delete a Pet. Fails if any error happens.")
@allure.tag("DeleteMethod")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete(get_base_url):
    with allure.step("Send DELETE request to delete user with ID 2"):
        data = requests.delete(get_base_url + API_URL + "2")

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Send delete request another time"):
        data = requests.delete(get_base_url + API_URL + "2")

    with allure.step("Verify the response status code is 404"):
        assert data.status_code == 404

    with allure.step("Send delete request another time again"):
        data = requests.delete(get_base_url + API_URL + "asdasd")

    with allure.step("Verify the response status code is 404"):
        assert data.status_code == 404