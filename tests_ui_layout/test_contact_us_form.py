from playwright.sync_api import Playwright, sync_playwright, expect
from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    search_page = ContactUsPage(page)
    search_page.navigate()
    search_page.submit_form("qwert", "qweqwrwegfzv", "qwrqrqrqr")
    # page.pause()


with sync_playwright() as playwright:
    test_submit_form(playwright)
