from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(no_viewport=True) #no_viewport=True used to open browser in full screen
    page.goto("https://www.saucedemo.com/")
    title = page.title()
    print(title)
    print(page.url)
    page.locator("input[name='user-name']").fill("standard_user")
    page.locator("input[name='password']").fill("secret_sauce")
    page.locator("input[name='login-button']").click()
    # page.goto("https://saucelabs.com/");
    # page.go_back();
    # page.go_forward();
  #   page.reload();
    back_button = page.locator("//div[contains(text(),'Sauce Labs Backpack')]");
    is_visible = back_button.is_visible()
    is_enabled = back_button.is_enabled()
    print("Is Visible: ", is_visible)
    browser.close()