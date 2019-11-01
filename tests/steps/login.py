from behave import given, when, then
from pages.login import login
import time
from steps import common

@then('Login Form is Shown')
def stem_impl_login_verify(context):
    login.verify_login_form()

@when('I wait')
def step_impl_wait_for_page_to_load(context):
    time.sleep(1)

@when('I enter wrong credentials "{email}" "{password}" and submit')
def step_impl_enter_incorrect_creds(context, email, password):
    #import pdb; pdb.set_trace()
    print(email,password)
    login.action_enter_credentials(email, password)

@then('Error Message is {message} displayed')
def step_impl_incorrect_login_message(context, message):
    time.sleep(1)
    login.verify_incorrect_credentials_message(message)

@given('The Login Form is Loaded')
def stem_impl_login_verify(context):
    login.verify_login_form()