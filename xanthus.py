from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://xanthus.in/")
    print("Page title:", page.title())
    page.wait_for_timeout(5000)  # keep browser open for 5 seconds to view
    browser.close()
    