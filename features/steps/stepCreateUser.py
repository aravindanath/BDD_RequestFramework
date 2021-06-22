from behave import *
import requests


# from behave import given, when, then, step
# import requests


@given('A user with valid access token')
def set_access_token_in_header(context):
    context.header = {"Authorization": "Bearer" + "<YOUR_ACCESS_TOKEN>"}


@step('the user wants to create a record with first name as "John X"')
def set_first_name(context):
    context.request_body = {"first_name": "John X"}

    @step('the user record has a last name of "Rocket"')
    def set_last_name(context):
        context.request_body['last_name'] = "Rocket"

    @step('the gender is "male"')
    def set_last_name(context):
        context.request_body['gender'] = "male"

    @step('date of birth is "1962-08-12"')
    def set_date_of_birth(context):
        context.request_body['dob'] = "1962-08-12"

    @step('an email of "johnrocketx@yopmail.com"')
    def set_email(context):
        context.request_body['email'] = 'johnrocketx@yopmail.com'

    @step('a phone number of "+637832233"')
    def set_phone_number(context):
        context.request_body['phone'] = '+637832233'

    @step('a website of "https://bit.ly/IqT6zt"')
    def set_website(context):
        context.request_body['website'] = "https://bit.ly/IqT6zt"

    @step('the address is "Platform 3/4 end of rainbow street"')
    def set_address(context):
        context.request_body['address'] = "Platform 3/4 end of rainbow street"

    @step('the user status is "active"')
    def set_user_status(context):
        context.request_body['status'] = "active"


@when('user submits the user data in "https://gorest.co.in/public-api/users"')
def execute_post_request_for_user_creation(context):
    response = requests.post('https://gorest.co.in/public-api/users', headers=context.header, json=context.request_body)
    context.response_body = response.json()
    context.status_code = response.status_code


@then('you should receive a "200" status code')
def check_status_code(context):
    assert context.status_code == 200


@step('first name "John X" should be in response body')
def check_first_name(context):
    assert context.response_body['result']['first_name'] == "John X"


@step('last name "Rocket" should be in response body')
def check_last_name(context):
    assert context.response_body['result']['last_name'] == "Rocket"


@step('gender "male" should be in response body')
def check_gender(context):
    assert context.response_body['result']['gender'] == "male"


@step('date of birth "1962-08-12" should be in response body')
def check_date_of_birth(context):
    assert context.response_body['result']['dob'] == "1962-08-12"


@step('email "johnrocketx@yopmail.com" should be in response body')
def check_email(context):
    assert context.response_body['result']['email'] == "johnrocketx@yopmail.com"


@step('phone number "+637832233" should be in response body')
def check_phone_number(context):
    assert context.response_body['result']['phone'] == "+637832233"


@step('website "https://bit.ly/IqT6zt" should be in response body')
def check_website(context):
    assert context.response_body['result']['website'] == "https://bit.ly/IqT6zt"


@step('address "Platform 3/4 end of rainbow street" should be in response body')
def check_address(context):
    assert context.response_body['result']['address'] == "Platform 3/4 end of rainbow street"


@step('user status "active" should be in response body')
def check_user_status(context):
    assert context.response_body['result']['status'] == "active"
