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
    # back_button = page.locator("//div[contains(text(),'Sauce Labs Backpack')]");
    # is_visible = back_button.is_visible()
    # is_enabled = back_button.is_enabled()
    # print("Is Visible: ", is_visible)

    # Traversing
    # page.locator("//select/child::option[1]").click();
    # page.locator("select").select_option("az");
    # page.locator("//option[@value='za']/following-sibling::option[1]").click()

    # Keyboard actions
    # page.locator("//input[@name='user-name']").press("Enter")

    # Multiple elements
    # web_elements = page.locator("//a").all()
    # for element in web_elements:
    #     print(element.inner_text())

    # Select multiple elements
    # elements = page.locator("//div[@class='inventory_item_name']").all()
    # for element in elements:
    #     value = element.get_attribute("value")
    #    if value == "ABC" or value == "XYZ":
    #         element.click()
    # 
    # select option from dropdown
    # option = page.locator("//select").select_option("abc")     

    # Scroll up and down
    # page.mouse.wheel(0,500) #scroll down
    # page.mouse.wheel(0,-500) #scroll up

    # Screenshot
    # page.screenshot(path="screenshot.png", full_page=True)

    # Actions
    # page.locator("//div[@class='inventory_item_name']").hover() --> Hover on the element
    # page.locator("//div[@class='inventory_item_name']").dblclick() --> Double click on the element
    # page.locator("//div[@class='inventory_item_name']").drag_to() --> Drag and drop the element
    # page.locator("//div[@class='inventory_item_name']").click(button="right") --> Right click on the element

    # Alerts
    # page.on("dialog", lambda dialog: dialog.accept()) --> Accept the alert
    # page.on("dialog", lambda dialog: dialog.dismiss()) --> Dismiss the alert
    # page.on("dialog", lambda dialog: dialog.accept("text")) --> Type text in the alert
    # page.on("dialog", lambda dialog: dialog.message()) --> Get the message from the alert
    
    browser.close()