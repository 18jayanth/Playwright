from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.automationtesting.in/Selectable.html')
    
    #storing multiple items using list
    elements=page.query_selector_all('b')
    print(len(elements))
    for i in elements:
        print(i.text_content())
    print('---------------------------------------')
    #storing all the links
    elements=page.query_selector_all('a')
    print(len(elements))
    for i in elements:
        print(i.text_content())
        #to print all the values of attribute 'href'
        print(i.get_attribute('href'))
    page.wait_for_timeout(3000)
        
    
    