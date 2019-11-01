Feature: Login
  Scenario: Login Page
    Given I load the website
    When I wait
    Then Login Form is Shown

  Scenario: I Enter Incorrect Login Details
    Given The Login Form is Loaded
    When I enter wrong credentials "abc@abc.com" "SomePass" and submit
    Then Error Message is "You have entered an incorrect email ID or password." displayed