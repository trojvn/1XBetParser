from playwright.sync_api import sync_playwright

from envs import URL


def _main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)
        browser.close()


def main():
    pass


if __name__ == "__main__":
    main()
