Feature: Kontrollera startsidan 

 Scenario: Användaren ser startsidan
   Given att jag öppnar läslistans webbsida 
   Then ska jag se rubriken "Läslistan"
   And ska jag se bilden som är i header
   And ska jag se knappen "Katalog"
   And ska jag se knappen "Lägg till bok"
   And ska jag se knappen "Mina böcker"
   And ska jag se div-elementet med listan av böcker



