from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    try:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto('https://demo.automationtesting.in/Selectable.html')
        
        #storing multiple items using list
        page.query_selector('a[@id="12345"]').click()
        elements=page.query_selector_all('b')
        print(len(elements))
        for i in elements:
            print(i.text_content())
        print('---------------------------------------')
        #storing all the links
        elements=page.query_selector_all('a')
        print(len(elements))
        for i in elements:
            #print(i.text_content())
            #to print all the values of attribute 'href'
            print(i.get_attribute('href'))
        page.wait_for_timeout(3000)
    except Exception as e:
        print(str(e))
    finally:
        print('Exectution Completed')
        
# output: 
# Page.query_selector: Unsupported token "@id" while parsing css selector "a[@id="12345"]". Did you mean to CSS.escape it?
# Exectution Completed