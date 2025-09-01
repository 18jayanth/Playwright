from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page=browser.new_page()
    yield page
    page.close()

def test_to_google(page):
    page.goto('https://www.google.com/')
    assert 'Google'==page.title()
    
def test_to_ms(page):
    page.goto('https://www.microsoft.com/en-in/')
    assert 'Microsoft – AI, Cloud, Productivity, Computing, Gaming & Apps'==page.title()
    