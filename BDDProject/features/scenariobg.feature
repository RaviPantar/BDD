Feature: OrangeHRM Login

  Background:Common Steps
    Given I launch browser
    When I open applications
    And Enter valid username and password
    And click on login

  Scenario: Login to HRM application
    Then user must login to the dashboard

  Scenario: Search User
      When navigate to search page
      Then Search page should display

   Scenario: Advanced Search Page
      When navigate to advanced search page
      Then advanced Search page should display