from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(no_viewport=True) #no_viewport=True used to open browser in full screen
    page.goto("https://www.saucedemo.com/")
    title = page.title()
    print(title)
    print(page.url)
    browser.close()