from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # 1. Launch browser
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    # 2. Create a page and go to RedBus
    page = context.new_page()
    page.goto("https://www.redbus.in")

    # 3. Get initial cookies
    print("\n--- Initial cookies ---")
    print(context.cookies())

    # 4. Clear all cookies (now browser is cookie-free)
    context.clear_cookies()
    print("\n--- After clearing cookies ---")
    print(context.cookies())

    # 5. Prepare your own cookie BEFORE visiting the site again
    future_expiry = int(time.time()) + 3600  # 1 hour from now
    my_cookie = [
        {
            "name": "Jayanth",
            "value": "12345",
            "domain": "www.redbus.in",
            "path": "/",
            "expires": future_expiry,  # Must be a future Unix timestamp
            "httpOnly": False,
            "secure": True,
            "sameSite": "Lax"
        }
    ]
    context.add_cookies(my_cookie)
    print("\n--- After adding custom cookie (before navigation) ---")
    print(context.cookies())

    # 6. Open a new page so navigation happens with your cookie already present
    page = context.new_page()
    page.goto("https://www.redbus.in")

    # 7. Check cookies after navigation
    print("\n--- After navigation (site may add its own cookies) ---")
    print(context.cookies())

    page.screenshot(path='test.png',full_page=True)
    browser.close()
