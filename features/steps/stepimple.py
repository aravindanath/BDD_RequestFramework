from behave import *
import requests


@given('the student app is running')
def step_imp(context):
    print("Student app is up and running")


@when('we excute the student list api method')
def step_impl(context):
    context.url = requests.get("http://localhost:8080/student/list")
    print(context.url.text)


@then('student list is displayed')
def step_impl(context):
    print(context.url.text)
