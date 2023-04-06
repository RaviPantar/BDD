from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('launch the chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://www.facebook.com//login/")


@then('verify that the logo present on page')
def verifyLogo(context):
    logo = context.driver.find_element(By.XPATH, "//*[contains(text(),'Facebook')]").text
    assert logo in "Facebook"


@then('close browser')
def closebrowser(context):
    context.driver.close()
