from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://www.amazon.in/ref=cs_503_link/')
    page.locator('//input[@id="twotabsearchtextbox"]').fill('laptops')
    page.locator('//input[@id="twotabsearchtextbox"]').press('Enter')
    page.wait_for_timeout(3000)
    for i in range(3):
        page.locator(f'//button[@id="a-autoid-{i+1}-announce"]').click()
    
    
    
    page.wait_for_timeout(5000)