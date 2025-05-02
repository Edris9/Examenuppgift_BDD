Feature: Lägg till bok i mina böcker


  Scenario: jag kan lägga till en bok i den och ta bort den
    Given att jag öppnar läslistans webbsida 
    When jag är på startsidan kan se texten "När du valt, kommer dina favoritböcker att visas här."
    When jag klickar på knappen "Katalog"
    And jag markerar boken "nbi_test" som favorit
    And jag klickar på knappen "Mina böcker"
    Then ska boken "nbi_test" visas i "Mina böcker"