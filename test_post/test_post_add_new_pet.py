import pytest
import requests
from pet_body_validator import Pet
import allure

API_URL = "/pet"



@pytest.mark.post_method
@allure.title("Test POST method for Add new pet")
@allure.description("This test sends a POST request to create a new pet.")
@allure.tag("PostMethod", "CreatePet")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("id, name", [
    (2, "Riki"),
    (10, "Molly")
]) # Знаю что нужно протестировать все поля но нету времени
def test_add_new(get_base_url, get_default_body, id, name):
    body = get_default_body
    body["id"] = id
    body["name"] = name

    with allure.step(f"Send POST request to create a new pet with data: {body}"):
        data = requests.post(get_base_url + API_URL, json=body)

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == 200

    with allure.step("Validate the response data against the Pet model"):
        assert Pet(**data.json())

    pet = Pet(**data.json())

    with allure.step("Check name"):
        assert pet.name == name

    with allure.step("Check id"):
        assert pet.id == id



@pytest.mark.post_method
@allure.title("Test POST method for Add new pet with empty body")
@allure.description("This test sends a POST request to create a new pet with empty body.")
@allure.tag("PostMethod", "CreatePet")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_pet_empty_body(get_base_url):

    with allure.step("Send POST request to create a new pet without data"):
        data = requests.post(get_base_url + API_URL)

    with allure.step("Verify the response status code is 415"):
        assert data.status_code == 415



@pytest.mark.post_method
@allure.title("Test POST method for Add new pet with empty dict")
@allure.description("This test sends a POST request to create a new pet with empty dict.")
@allure.tag("PostMethod", "CreatePet")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_pet_empty_dict(get_base_url):

    body = {}
    with allure.step("Send POST request to create a new pet without data"):
        data = requests.post(get_base_url + API_URL, json=body)

    with allure.step("Verify the response status code is 405"):
        assert data.status_code == 405





@pytest.mark.put_method
@allure.title("Test Pet Update via PUT Request")
@allure.description("This test sends a PUT request to update pet data.")
@allure.tag("Essentials", "PutMethod")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("id, name, status, code", [
    (2, "Riki", "sold", 200),
    (6, "Sunny", "lost", 200)
]) # Знаю что нужно протестировать все поля но нету времени

def test_change_exsiting_pet(get_base_url, get_default_body, id, name, status, code):
    body = get_default_body
    body["id"] = id
    body["name"] = name
    body["status"] = status

    with allure.step(f"Send PUT request to update pet "):
        data = requests.put(get_base_url + API_URL, json=body)

    with allure.step("Verify the response status code is 200"):
        assert data.status_code == code

    with allure.step("Validate the response data against the Pet model"):
        assert Pet(**data.json())

    pet = Pet(**data.json())

    with allure.step("Validate  Pet name"):
        assert pet.name == name

    with allure.step("Validate Pet id"):
        assert pet.id == id

    with allure.step("Validate Pet status"):
        assert pet.status == status



@pytest.mark.put_method
@allure.title("Test Pet Update via PUT Request unexciting object")
@allure.description("This test sends a PUT request to update pet data.")
@allure.tag("Essentials", "PutMethod")
@allure.severity(allure.severity_level.NORMAL)
def test_change_unexciting_obj(get_base_url, get_default_body):
    body = get_default_body
    body["id"] = -10
    body["name"] = "Kiki"
    with allure.step(f"Send PUT request to update pet "):
        data = requests.put(get_base_url + API_URL, json=body)

    with allure.step("Check status code"):
        assert data.status_code == 404


@pytest.mark.put_method
@allure.title("Test Pet Update via PUT Request invalid data")
@allure.description("This test sends a PUT request to update pet data.")
@allure.tag("Essentials", "PutMethod")
@allure.severity(allure.severity_level.NORMAL)
def test_change_invalid_id(get_base_url, get_default_body):
    body = get_default_body
    body["id"] = "ajisdjiasijd"
    with allure.step(f"Send PUT request to update pet "):
        data = requests.put(get_base_url + API_URL, json=body)

    with allure.step("Check status code"):
        assert data.status_code == 400

