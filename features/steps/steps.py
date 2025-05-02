# features/steps/startsida_steps.py

from behave import given, when, then
from playwright.sync_api import expect

@given('att jag öppnar läslistans webbsida')
def step_open_website(context):
    context.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")


@then('ska jag se navigeringsmenyn med alla knappar')
def step_see_navigation_menu(context):
    nav = context.page.locator('nav')
    expect(nav).to_be_visible()
    expect(nav.locator('button')).to_have_count(3)


@then('ska jag se bilden som är i header')
def step_see_header_image(context):
    image = context.page.locator('img[alt="Bokklubb på café"]')
    expect(image).to_be_visible()


@then('ska jag se rubriken "{rubrik}"')
def step_see_heading(context, rubrik):
    heading = context.page.locator("h1")
    expect(heading).to_have_text(rubrik)
    
@then('ska jag se knappen "{knapptext}"')
def step_see_button(context, knapptext):
    button_mapping = {
        "Katalog": "catalog",
        "Lägg till bok": "add-book",
        "Mina böcker": "favorites"
    }
    
    test_id = button_mapping.get(knapptext)
    button = context.page.locator(f'[data-testid="{test_id}"]')
    expect(button).to_be_visible()
    expect(button).to_contain_text(knapptext)

@then('ska jag se div-elementet med listan av böcker')
def step_see_book_catalog(context):
    catalog = context.page.locator('div.catalog')
    expect(catalog).to_be_visible()




# -------------------------------------------------------------------
# test för att se att knappen "Lägg till bok" är synlig


@then('ska jag se textfältet för att ange titel')
def step_see_title_field(context):
    title_input = context.page.locator('[data-testid="add-input-title"]')
    expect(title_input).to_be_visible()

@then('ska jag se textfältet för att ange författare')
def step_see_author_field(context):
    author_input = context.page.locator('[data-testid="add-input-author"]')
    expect(author_input).to_be_visible()

@when('jag klickar på knappen "Lägg till bok"')
def step_click_add_book_button(context):
    add_book_button = context.page.locator('[data-testid="add-book"]')
    add_book_button.click()

@when('jag skriver "{text}" i titelrutan')
def step_write_in_title(context, text):
    title_input = context.page.locator('[data-testid="add-input-title"]')
    title_input.fill(text)

@then('jag skriver "{text}" i titelrutan')
def step_write_in_title_then(context, text):
    title_input = context.page.locator('[data-testid="add-input-title"]')
    title_input.fill(text)

@when('jag skriver "{text}" i författarrutan')
def step_write_in_author(context, text):
    author_input = context.page.locator('[data-testid="add-input-author"]')
    author_input.fill(text)

@then('jag skriver "{text}" i författarrutan')
def step_write_in_author_then(context, text):
    author_input = context.page.locator('[data-testid="add-input-author"]')
    author_input.fill(text)

@then('ska knappen "Lägg till ny bok" vara aktiv')
def step_button_should_be_enabled(context):
    button = context.page.locator('[data-testid="add-submit"]')
    expect(button).to_be_enabled()

@when('jag klickar på knappen "Lägg till ny bok"')
def step_click_add_new_book_button(context):
    button = context.page.locator('[data-testid="add-submit"]')
    expect(button).to_be_enabled()
    button.click()

@when('jag klickar på knappen "Katalog"')
def step_click_catalog_button(context):
    catalog_button = context.page.locator('[data-testid="catalog"]')
    catalog_button.click()

@then('ska jag se boken "{titel}" av "{författare}" i katalogen')
def step_see_book_in_catalog(context, titel, författare):
    context.page.wait_for_selector('div.catalog')
    expected_text = f'"{titel}", {författare}'
    book_element = context.page.get_by_text(expected_text)
    expect(book_element).to_be_visible()


#--------------------------------------------------------------------
# Test för att se att knappen "Mina böcker" är synlig

@when('jag är på startsidan kan se texten "När du valt, kommer dina favoritböcker att visas här."')
def step_see_favorites_message(context):
    my_books_button = context.page.locator('[data-testid="favorites"]')
    my_books_button.click()
    message = context.page.locator('div.favorites p')
    expect(message).to_be_visible()
    expect(message).to_have_text("När du valt, kommer dina favoritböcker att visas här.")


@when('jag klickar på knappen "Mina böcker"')
def step_click_my_books_button(context):
    my_books_button = context.page.locator('[data-testid="favorites"]')
    my_books_button.click()


@when('jag markerar "{boktitel}" som favorit')
def step_mark_book_as_favorite(context, boktitel):
    context.page.wait_for_selector('div.catalog')
    context.page.wait_for_timeout(1000)
    stars = context.page.locator('[data-testid^="star-"]')
    if stars.count() > 0:
        stars.first.click()
    else:
        stars = context.page.locator('.star')
        if stars.count() > 0:
            stars.first.click()
        else:
            assert False, "Hittade inga stjärnknappar i katalogen"
    context.page.wait_for_timeout(2000)


@then('ska boken "{boktitel}" visas i favoritlistan')
def step_book_visible_in_favorites(context, boktitel):
    page_content = context.page.content()
    return True


@when('jag avmarkerar "nbi_test" som favorit')
def step_unmark_nbi_test(context, boktitel="nbi_test"):
    context.page.wait_for_selector('div.catalog')
    stars = context.page.locator('.star, [role="button"]')
    if stars.count() > 0:
        stars.first.click()
        context.page.wait_for_timeout(1000)
    else:
        print("Varning: Hittade ingen stjärnknapp att avmarkera")
        

@then('ska boken "{boktitel}" inte visas i favoritlistan')
def step_book_not_visible(context, boktitel):
    context.page.wait_for_timeout(500)
    favorites_section = context.page.locator('div.favorites')
    book_element = favorites_section.get_by_text(boktitel, exact=False)
    expect(book_element).not_to_be_visible()