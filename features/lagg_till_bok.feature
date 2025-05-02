Feature: Lägg till bok

  Scenario: Lägga till en bok och se den i katalogen
    Given att jag öppnar läslistans webbsida
    When jag klickar på knappen "Lägg till bok"
    Then ska jag se textfältet för att ange titel
    And ska jag se textfältet för att ange författare
    When jag skriver "nbi_test" i titelrutan
    And jag skriver "Anderson" i författarrutan
    Then ska knappen "Lägg till ny bok" vara aktiv
    When jag klickar på knappen "Lägg till ny bok"
    And jag klickar på knappen "Katalog"
    Then ska jag se boken "nbi_test" av "Anderson" i katalogen
  
    