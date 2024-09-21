from playwright.sync_api import sync_playwright

from envs import URL


def __main():
    with sync_playwright() as p:
        _main(p)


def _main(p):
    browser = p.chromium.launch_persistent_context(
        user_data_dir=r"C:\Users\trojvn\AppData\Local\Google\Chrome\User Data",
        headless=False,
        channel="chrome",
        args=["--profile-directory=Profile 1"],
    )
    page = browser.new_page()
    page.goto(URL)
    page.wait_for_timeout(3000)
    _xpath = "//li[contains(@class,'dashboard-game')]/*[contains(@class,'dashboard-markets')]//button/span[contains(@text,'')]"
    elements_cf = page.query_selector_all(_xpath)
    _xpath = "//li[contains(@class,'dashboard-game')]/*[contains(@class,'dashboard-game-block')]//a"
    elements_url = page.query_selector_all(_xpath)
    for element in elements_url:
        href = element.get_attribute("href")
        cf1 = elements_cf.pop(0).inner_text()
        _ = elements_cf.pop(0)
        cf2 = elements_cf.pop(0).inner_text()
        print(href, cf1, cf2)
    browser.close()


def main():
    __main()


if __name__ == "__main__":
    main()
