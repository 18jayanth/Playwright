from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_selector('//button[contains(text(),"    click   ")]').click()
    page.wait_for_timeout(3000)
    #How to Find Total pages
    total_pages=context.pages
    print(len(total_pages))#2
    for i in total_pages:
        print(i)
    
    
    
    new_page=total_pages[1]
    print(page.title()) #it will print old page title
    #How to switch to new tab
    new_page.bring_to_front() #it will bring child page
    print(new_page.wait_for_timeout(5000))
    print(new_page.title()) #it will print child page title
    new_page.close()
    
    page.bring_to_front()
    page.wait_for_timeout(5000)
    
    browser.close()
    