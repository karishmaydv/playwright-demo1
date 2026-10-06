from playwright.sync_api import Page

def test_xanthus_screenshot(page: Page):
    page.goto("https://xanthus.in/")

    page.screenshot(path="screenshots/xanthus.png")
    full_page = True