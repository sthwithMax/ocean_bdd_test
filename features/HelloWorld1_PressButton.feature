Feature: Press button

Scenario: Press button
    Given I visit "http://localhost:9000/"
    When I press a button
    Then I should check the result