from playwright.sync_api import sync_playwright
text_alert=[]
def handle_dialog(dialog):
    message=dialog.message
    text_alert.append(message)
    dialog.accept()
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    #button is direct child
    #page.wait_for_selector('//div[@id="OKTab"]/button').click()
    
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(3000)
    #controlling the alert it will press ok instaed of cancel
    #page.on("dialog",lambda dialog:dialog.accept())
    #to cancel
    #page.on("dialog",lambda dialog:dialog.dismiss())
    #to print a message
    #page.on("dialog",lambda dialog:print(dialog.message))
    page.on("dialog",handle_dialog)
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    page.wait_for_timeout(3000)
    print(text_alert[0])