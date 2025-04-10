from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage


def about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    print('Hey!')


with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)
