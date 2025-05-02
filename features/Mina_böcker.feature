Feature: Lägg till bok i mina böcker

  Scenario Outline: jag kan lägga till en bok i den och ta bort den
    Given att jag öppnar läslistans webbsida 
    When jag klickar på knappen "Lägg till bok"
    And jag skriver "<titel>" i titelrutan
    And jag skriver "<författare>" i författarrutan
    And jag klickar på knappen "Lägg till ny bok"
    And jag klickar på knappen "Katalog"
    And jag markerar "<titel>" som favorit
    And jag klickar på knappen "Mina böcker"
    Then ska boken "<titel>" visas i favoritlistan
    When jag klickar på knappen "Katalog"
    And jag avmarkerar "<titel>" som favorit
    And jag klickar på knappen "Mina böcker"
    Then ska boken "<titel>" inte visas i favoritlistan

    Examples:
      | titel      | författare |
      | nbi_test   | Anderson   |
   