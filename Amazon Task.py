from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Go to Amazon home and search laptops
    page.goto('https://www.amazon.in')
    page.locator('//input[@id="twotabsearchtextbox"]').fill('laptops')
    page.locator('//input[@id="twotabsearchtextbox"]').press('Enter')
    page.wait_for_timeout(3000)

    # Step 2: Click "Add to Cart" for first 3 products
    add_to_cart_buttons = page.locator('//button[contains(text(),"Add to cart")]')
    count = min(add_to_cart_buttons.count(), 3)
    for i in range(count):
        add_to_cart_buttons.nth(i).click()
        page.wait_for_timeout(2000)  # wait for cart action

    # Step 3: Go to cart page
    page.goto("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    page.wait_for_timeout(3000)

    # Step 4: Get prices from cart
    prices=page.locator('//div[@class="sc-item-price-block"]//span[@aria-hidden="true"]').all_text_contents()
    print("Before Polishing Prices are",prices) #Before Polishing Prices are ['₹30,290.00', '₹39,990.00', '₹32,490.00']
    clean_prices = [float(p.replace("₹", "").replace(",", "").strip()) for p in prices]

    
    print("Prices:", clean_prices) #Prices: [30290.0, 39990.0, 32490.0]
    print("Total:", sum(clean_prices)) #Total: 102770.0
    
    total_price=page.locator('//div[@id="sc-buy-box"]//span[contains(@id,"sc-subtotal-amount-buybox")]/span').text_content()
    clean_total_price=float(total_price.replace("₹", "").replace(",", "").strip())
    print('Sub Total Price',clean_total_price) #Sub Total Price 102770.0
    if sum(clean_prices)==clean_total_price:
        print('True') #True
    else:
        print('False')
    
    browser.close()
