Feature: Calculating bloodpressure

Scenario Outline: Calculating Blood Pressure
    Given I navigate to homepage
    And a valid name is used
    And systolic is  <Systolic>
    And diastolic is <Diastolic>
    When I click on Calculate Blood Pressure
    Then bloodpressure should be <Result>
    Examples:
        | Systolic  | Diastolic | Result |
        | 85        | 55        | Low  |
        | 95        | 75        | Ideal  |
        | 95        | 85        | Pre-High  |
        | 125       | 85        | Pre-High  |
        | 125       | 95        | High  |
        | 140       | 80        | High  |


