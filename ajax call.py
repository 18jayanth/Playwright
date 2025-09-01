from playwright.sync_api import sync_playwright
def handle_rejex(response):
    if 'https://www.plus2net.com/php_tutorial/dd-ajax.php' in response.url:
        data=response.text()
        status=response.status
        print(f'Data:{data} Status:{status}')


with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php')
    
    select=page.wait_for_selector('//select[@id="s1"]')
    page.on('response',lambda response:handle_rejex(response))
    select.select_option(value="1")
   
    page.wait_for_timeout(3000)