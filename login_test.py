"""
Playwright login script - email + OTP flow
Target: https://cfab-superadmin.xanthusdemo.in/jobs

NOTE: I could not fetch/render the actual page (it appears to be a JS-based
SPA), so the selectors below are placeholders based on common email+OTP
login patterns. You'll need to confirm/replace them with the real ones.

Fastest way to get exact selectors:
    playwright codegen https://cfab-superadmin.xanthusdemo.in/jobs
Click through the login manually - Codegen will print the real selectors
Playwright used, which you can paste in below.
"""

from playwright.sync_api import sync_playwright

LOGIN_URL = "https://cfab-superadmin.xanthusdemo.in/jobs"
EMAIL = "sagarr@xanthus.in"
OTP = "1234"


def login(page):
    page.goto(LOGIN_URL)

    # --- Step 1: Enter email and submit ---
    # Replace these selectors with the real ones from the page.
    page.fill("input[type='email']", EMAIL)
    page.click("button:has-text('Send OTP')")  # or 'Continue' / 'Next'

    # Wait for the OTP screen to appear
    page.wait_for_selector("input[type='text'], input[name*='otp' i]", timeout=10000)

    # --- Step 2: Enter OTP ---
    # Some sites use a single input for the whole OTP; others use one input
    # per digit. Handle both cases below - keep whichever matches the site.

    otp_inputs = page.locator("input[name*='otp' i], input[maxlength='1']")
    count = otp_inputs.count()

    if count > 1:
        # Multiple boxes - one digit per input
        for i, digit in enumerate(OTP):
            otp_inputs.nth(i).fill(digit)
    else:
        # Single OTP field
        page.fill("input[name*='otp' i]", OTP)

    # --- Step 3: Submit OTP ---
    page.click("button:has-text('Verify')")  # or 'Login' / 'Submit'

    # --- Step 4: Confirm login succeeded ---
    page.wait_for_url("**/jobs**", timeout=10000)
    print("Login successful, current URL:", page.url)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context()
        page = context.new_page()

        try:
            login(page)
            page.screenshot(path="after_login.png", full_page=True)
        except Exception as e:
            page.screenshot(path="login_error.png", full_page=True)
            print("Login failed:", e)
            raise
        finally:
            browser.close()


if __name__ == "__main__":
    main()