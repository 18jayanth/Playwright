from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #CSS Selectors 3 types 1.ID(#) 2.CLASS(.) 3.ATTRIBUTE(TAG[ATTRIBUTE='VALUE'])
    
    #using attribute //tagname[@attribute='value']
    # username_element=page.wait_for_selector('//input[@name="username"]')
    # username_element.type('Admin')
    # password_element=page.wait_for_selector('//input[@placeholder="Password"]')
    # password_element.type('admin123')
    # login_element=page.wait_for_selector('//button[@type="submit"]')
    # login_element.click()
    # page.wait_for_timeout(5000)
    # browser.close()
    
    #using text //tagname[text()=""]
    page.wait_for_selector('//p[text()="Forgot Your Password? "]').click()
    page.wait_for_timeout(5000)
    browser.close()
    
    #contains
    #attribute //tagname[contains(attribute,value)]
    #text      //tagname[contains(text(),value)]
    
    #starts-with //tagname[starts-with(@id,'value)]
    #ends-with   //tagname[ends-with(@id,'value')]
    
    #family
    #parent //tagname[@id='value']/parent::tagname
    #child //tagname[@id='value']/child::tagname
    #anchestor //tagname[@id='value']/anchestor::tagname
    #following-sibling //tagname[@id='value']/following-sibling::tagname
    