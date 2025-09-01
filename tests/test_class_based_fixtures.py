from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope='class')
def browser(request):
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        request.cls.browser=browser
        yield browser
        browser.close()
        
@pytest.fixture(scope="function")
def page(browser):
    page=browser.new_page()
    yield page
    
    
@pytest.mark.usefixtures("browser")
class Test_titleclass:
     def test_google(self,page):
         page.goto('https://www.google.com')
         assert page.title()=='Google'
    
     def test_microsoft(self,page):
         page.goto('https://www.microsoft.com')
         assert page.url=='https://www.microsoft.com/en-in/'
         
    
    
    