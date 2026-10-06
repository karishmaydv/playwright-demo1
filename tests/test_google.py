# add import statements here
#re is regular expression module in python regex used in
import re
from playwright.sync_api import expect

def test_google_search(page):
    page.wait_for_timeout(5000)
    page.goto("https://www.google.com")

    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No popup found")

    page.get_by_role("combobox", name="Search").fill("Playwright Python") 

    expect(page).to_have_title(re.compile(".*Playwright Python.*"))
         