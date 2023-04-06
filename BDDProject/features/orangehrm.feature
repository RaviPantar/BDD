Feature: OrangeHRM Logo
  Scenario: Logo present on orange HRM page
    Given launch the chrome browser
    When open orange hrm homepage
    Then verify that the logo present on page
    And close browser
