from behave import given, when, then
import csv

@given("I launch Google Maps")
def step_impl(context):
    context.page.goto("https://www.google.com/maps")
    context.page.wait_for_timeout(3000)

@when('I search for "{name}"')
def step_impl(context, name):
    search = context.page.locator('//input[@id="searchboxinput"]')
    search.fill(name)
    search.press("Enter")
    context.page.wait_for_timeout(3000)

@when('I choose {count:d} {name}')
def step_impl(context, count, name):
    scrollable_div = context.page.locator('//div[@role="feed"]')
    restaurants = []
    
    while len(restaurants) < count:
        items = context.page.locator('//a[@class="hfpxzc"]')
        total = items.count()

        for i in range(len(restaurants), total):
            if len(restaurants) >= count:
                break

            item = items.nth(i)
            item.scroll_into_view_if_needed()
            item.wait_for(state="visible", timeout=10000)
            item.click()
            context.page.wait_for_timeout(2000)

            try:
                name = context.page.locator('//h1[contains(@class,"DUwDvf")]').text_content(timeout=5000).strip()
            except:
                name = "N/A"

            try:
                rating = context.page.locator('//div[contains(@class,"F7nice ")]').first.text_content(timeout=5000).strip()
            except:
                rating = "N/A"

            try:
                address = context.page.locator('//div[contains(@class,"Io6YTe")]').first.text_content(timeout=5000).strip()
            except:
                address = "N/A"

            restaurant = [name, rating, address]
            if restaurant not in restaurants:
                restaurants.append(restaurant)
                print(len(restaurants), name, rating, address)

        scrollable_div.evaluate("el => el.scrollBy(0, 2000)")
        context.page.wait_for_timeout(5000)

    context.restaurants = restaurants

@then('I should save restaurant details into "{filename}"')
def step_impl(context, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Rating", "Address"])
        writer.writerows(context.restaurants)

    print(f"✅ Saved {len(context.restaurants)} restaurants to {filename}")
