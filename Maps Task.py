from playwright.sync_api import sync_playwright
import csv
prev_count=-1
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/maps")
    page.wait_for_timeout(3000)

    search = page.locator('//input[@id="searchboxinput"]')
    search.fill("restaurants near me")
    search.press("Enter")
    page.wait_for_timeout(3000)

    choice = int(input("Please Enter the choice of your Restaurants: "))
    scrollable_div = page.locator('//div[@role="feed"]')
    restaurants = []
    
    while len(restaurants) < choice:
        items = page.locator('//a[@class="hfpxzc"]')
        count = items.count()
        print('count is ',count)
        print('No of Resturants Stored',len(restaurants))

        for i in range(len(restaurants), count):
        #for i in range(count):
            if len(restaurants) >= choice:
                break 
            item = items.nth(i)
            item.scroll_into_view_if_needed()
            item.wait_for(state="visible", timeout=10000)
            item.click()
            page.wait_for_timeout(2000)

            # try:
            #     page.wait_for_selector('//h1[contains(@class,"DUwDvf")]')
            #     rest_name = page.locator('//h1[contains(@class,"DUwDvf")]').text_content()
            #     page.wait_for_selector('//div[contains(@class,"F7nice ")]')
            #     rating = page.locator('//div[contains(@class,"F7nice ")]').first.text_content()
            #     page.wait_for_selector('//div[contains(@class,"Io6YTe")]')
            #     address = page.locator('//div[contains(@class,"Io6YTe")]').first.text_content()
            
            # except Exception as e:
            #     print(e)
            try:
                rest_name = page.locator('//h1[contains(@class,"DUwDvf")]').text_content(timeout=5000).strip()
            except:
                rest_name = "N/A"

            try:
                rating = page.locator('//div[contains(@class,"F7nice ")]').first.text_content(timeout=5000).strip()
            except:
                rating = "N/A"

            try:
                address = page.locator('//div[contains(@class,"Io6YTe")]').first.text_content(timeout=5000).strip()
            except:
                address = "N/A"


            restaurant = [rest_name, rating, address]
            if restaurant not in restaurants:
                restaurants.append(restaurant)
                print(len(restaurants), rest_name, rating, address)
                
        print('count is ',count)
        print('No of Resturants Stored',len(restaurants))

        
        
    
        scrollable_div.evaluate("el => el.scrollBy(0, 2000)")
        page.wait_for_timeout(5000)
        
        # if count == prev_count:
        #     print("⚠️ No more restaurants available")
        #     break
        # prev_count = count
        

    
    with open("restaurants.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Rating", "Address"])
        writer.writerows(restaurants)

    print("✅ Saved to restaurants.csv")
    browser.close()
