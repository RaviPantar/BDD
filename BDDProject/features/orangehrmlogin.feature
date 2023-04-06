Feature: Facebook Login
  Scenario: Login to facebook with valid credentials
    Given I launch Chrome browser
    When I open facebook Page
    And Enter the username "ravimpantar@gmail.com" and password "ffdkf12"
    And Click on login button
    Then User must login with success message

  Scenario Outline: Login to facebook credentials
    Given I launch Chrome browser
    When I open facebook Page
    And Enter the username "<username>" and password "<password>"
    And Click on login button
    Then User must login with success message

    Examples:
    | username | password |
    | ravimp@gmail.com | ad234r |
    | ravimp1@gmail.com | ad234r |
    | ravimp2@gmail.com | ad234r |
    | ravimp3@gmail.com | ad234r |
