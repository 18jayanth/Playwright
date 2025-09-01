from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    
    page.goto('https://demo.automationtesting.in/Selectable.html')
    
    #Mouse Actions
    #hover on a dropdown
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    #click an element
    page.wait_for_selector('//a[text()="SwitchTo"]').click()
    #double click an element
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
    #right click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button='right')
    #left click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button='left')
    #shift +click
    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers='Shift')
    
    #key board actions
    page.wait_for_selector('//a[text()="SwitchTo"]').press('A')
    #A-Z a-z 0-9 Special characters ctrl alt pgup pgdown alt enter
    page.wait_for_timeout(3000)