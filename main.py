from playwright.sync_api import sync_playwright

from envs import URL


def _main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)
        page.wait_for_timeout(3000)
        _xpath = "xpath=//li[contains(@class,'dashboard-game')]"
        elements = page.query_selector_all(_xpath)
        print(elements)
        browser.close()


def main():
    _main()


if __name__ == "__main__":
    main()
