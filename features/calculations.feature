Feature: Calculating bloodpressure

Scenario: Calculating low bloodpressure
    Given I navigate to homepage
    And a valid name is used
    And systolic is less than 90
    And diastolic is less than 60
    When I click on Calculate Blood Pressure
    Then bloodpressure should be Low
