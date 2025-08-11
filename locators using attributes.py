from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #CSS Selectors 3 types 1.ID(#) 2.CLASS(.) 3.ATTRIBUTE(TAG[ATTRIBUTE='VALUE'])
    #using attribute
    username=page.wait_for_selector("input[name='username']")
    username.type('Admin')
    password=page.wait_for_selector("input[type='password']")
    password.type('admin123')
   
    loginbutton=page.wait_for_selector("button[type='submit']")
    loginbutton.click()
    page.wait_for_timeout(5000)
    browser.close()