from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/')
    #CSS Selectors 3 types 1.ID(#) 2.CLASS(.) 3.ATTRIBUTE(TAG[ATTRIBUTE='VALUE'])
    #using id
    emailtextbox=page.wait_for_selector('#email')
    emailtextbox.type('type@gmail.com')
   
    loginbutton=page.wait_for_selector('#enterimg')
    loginbutton.click()
    page.wait_for_timeout(3000)
    browser.close()