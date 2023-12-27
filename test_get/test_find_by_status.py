import pytest
import requests
import allure
from test_post.pet_body_validator import Pet

API_URL = "/pet/findByStatus"

@pytest.mark.get_method
@allure.title("Test GET method for Sold status")
@allure.description("This test sends a GET request to retrieve data for a sold pets.")
@allure.tag( "GetMethod")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_by_status_available(get_base_url):
    with allure.step("Send GET request to retrieve data for sold status"):
        data = requests.get(get_base_url + API_URL + "?status=sold")

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data Pet model"):
        pet = Pet(**data.json()[0])

    with allure.step("Validate the response name data from Pet model"):
        assert pet.name == "Charly Broun"

@pytest.mark.get_method
@allure.title("Test GET method for Lost status")
@allure.description("This test sends a GET request to retrieve data for lost pets.")
@allure.tag( "GetMethod")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_by_status_lost(get_base_url):
    with allure.step("Send GET request to retrieve data for lost status"):
        data = requests.get(get_base_url + API_URL + "?status=lost")

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 400

    with allure.step("Validate the response data Pet model"):
        pet = Pet(**data.json()[0])

    with allure.step("Validate the response name data from Pet model"):
        assert pet.name == "Charly Broun"