def handle_download(download):
    location='/text1.zip'
    download.save_as(location)
    
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://demo.imacros.net/Automate/Downloads')
    
    page.on('download',handle_download)
    page.wait_for_selector('//a[@href=''/Content/Download.zip]').click()
    page.wait_for_timeout(3000)
    