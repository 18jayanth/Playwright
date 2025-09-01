import re
from playwright.sync_api import expect



def test_google_search(page):
    page.wait_for_timeout(3000)
    page.goto('https://duckduckgo.com/')
    #this is for Accept All pop up
    try:
        page.get_by_role("button",name='Accept All').click(timeout=5000)
    except:
        print('No Popup To Accept')
    page.get_by_role('combobox',name='search').fill('Playwright')
    page.keyboard.press('Enter')
    expect(page).to_have_title(re.compile('Playwright.*DuckDuckGo', re.IGNORECASE))

    