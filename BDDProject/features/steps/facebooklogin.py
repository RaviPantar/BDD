from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('I launch Chrome browser')
def launchbrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('I open facebook Page')
def OpenUrl(context):
    context.driver.get("https://www.facebook.com//login/")


@when('Enter the username "{username}" and password "{password}"')
def enterCredentials(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username)
    context.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(password)


@when('Click on login button')
def clickLogin(context):
    context.driver.find_element(By.XPATH, "//button[@name='login']").click()


@then('User must login with valid credentials msg')
def message(context):
    msg = context.driver.find_element(By.XPATH, "//div[@class='_9ay7']//a").text
    assert msg in "Forgotten password?"
