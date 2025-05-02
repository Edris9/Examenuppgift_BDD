Feature: Lägg till bok i mina böcker

  Scenario: jag kan lägga till en bok i den och ta bort den
    Given att jag öppnar läslistans webbsida 
    When jag klickar på knappen "Lägg till bok"
    And jag skriver "nbi_test" i titelrutan
    And jag skriver "Anderson" i författarrutan
    And jag klickar på knappen "Lägg till ny bok"
    And jag klickar på knappen "Katalog"
    And jag markerar "nbi_test" som favorit
    And jag klickar på knappen "Mina böcker"
    Then ska boken "nbi_test" visas i favoritlistan
    When jag klickar på knappen "Katalog"
    And jag avmarkerar "nbi_test" som favorit
    And jag klickar på knappen "Mina böcker"
    Then ska boken "nbi_test" inte visas i favoritlistan