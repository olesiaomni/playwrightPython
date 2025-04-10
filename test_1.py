import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("handle-button").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("symon.storozhenko@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("test123")
    page.get_by_role("textbox", name="Password").press("Enter")

    expect(page.get_by_role("button", name="Log in with Email")).to_be_hidden()

    product = page.get_by_text('$85').first.locator(('xpath=../../../../..')).text_content()
    print(product)
    assert product != 'Socks'

    all_links = page.get_by_role('link').all()
    for link in all_links:
        print(link.text_content())
    print('Hey!')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
