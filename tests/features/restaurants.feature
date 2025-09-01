Feature: Scrape restaurants from Google Maps

  Scenario Outline: User wants to scrape restaurants
    Given I launch Google Maps
    When I search for "<name>"
    And I choose <count> <name>
    Then I should save restaurant details into "<name>_<count>.csv"

    Examples:
     |name|                                       | count |
     |restaurants near me |                       | 50    |
     |hospitals near me|                          | 50    |
     |hotels near me|                             | 50    |
      
  