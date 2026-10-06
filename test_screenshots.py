from playwright.sync_api import Page


def test_google_screenshot(page: Page):
    page.goto("https://www.google.com")

    page.screenshot(path="screenshots/google.png")