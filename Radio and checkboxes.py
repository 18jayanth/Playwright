#radio button only one option checkbox more than one option
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    #radio button
    radio_button=page.query_selector('//input[@value="FeMale"]')
    #either click or check
    #radio_button.click()
    radio_button.check()
    if radio_button.is_checked():
        print('radio button is checked')
    
    #checkbox
    checkbox=page.query_selector('//input[@value="Cricket"]')
    #checkbox.click()
    checkbox.check()
    if checkbox.is_checked():
        print('checkbox is checked')
    page.wait_for_timeout(3000)