from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('I launch browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('I open applications')
def openUrl(context):
    context.driver.get("https://www.facebook.com//login/")


@when(u'Enter valid username and password')
def Credentials(context):
    print("Credentials----")


@when(u'click on login')
def clickLogin(context):
    print("clicklogin----")


@then('user must login to the dashboard')
def dashboard(context):
    print("Dashboard-----")


@when('navigate to search page')
def searchPage(context):
    print("Searchpage---")


@then(u'Search page should display')
def searchPageDisplay(context):
    print("SearchpageDisplay----")


@when(u'navigate to advanced search page')
def advanceSearchPage(context):
    print("advancedPage---")


@then(u'advanced Search page should display')
def advanceSearchPageDisplay(context):
    print("advanceSearchPageDisplay---")
