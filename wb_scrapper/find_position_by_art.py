import asyncio

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import config

SCROLL_DELAY = config.SCROLL_DELAY
PAGE_LOAD_DELAY = config.PAGE_LOAD_DELAY


def prepare_url(query: str, page: int):
    return ('https://www.wildberries.ru/catalog/0/search.aspx'
            f'?page={page}&sort=popular&search={query}')


def get_webdriver():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless=new')
    # set option to don't load images
    chromeOptions.add_experimental_option('prefs',
                                          {'profile.managed_default_content_settings.images': 2})

    return webdriver.Chrome(chrome_options=chromeOptions)


async def get_good_position(query: str, art: str, start_page: int = 1) -> tuple[int]:

    with get_webdriver() as driver:
        driver.set_window_size(1680, 1000)

        page = start_page
        absolute_position = 0

        while True:
            # Prepairing url and do request.
            url = prepare_url(query, page)
            driver.get(url)

            # Waiting for page loading.
            # Indicators are 'pagination' and 'not-found-search' classes.
            while (not driver.find_elements(By.CLASS_NAME, 'pagination')
                   and len(driver.find_elements(By.CLASS_NAME, 'not-found-search')) == 0):
                await asyncio.sleep(PAGE_LOAD_DELAY)

            # Stop searching if nothing more found.
            if len(driver.find_elements(By.CLASS_NAME, 'not-found-search')) != 0:
                return (-1, -1, -1)

            # Scrolling while cards loading.
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                # Scrolling to the last product_card.
                driver.execute_script("arguments[0].scrollIntoView(true);",
                                      driver.find_elements(
                                          By.XPATH,
                                          "//div[@class='product-card-list']/article")[-1])

                await asyncio.sleep(SCROLL_DELAY)

                # Checking is height changed after scrolling.
                new_height = driver.execute_script(
                    "return document.body.scrollHeight")
                if new_height == last_height:
                    break

                last_height = new_height

            # Collecting all cards in main catalog.
            elements = driver.find_elements(
                By.XPATH, "//div[@class='product-card-list']/article")

            # Searching for target card position.
            for i, element in enumerate(elements):
                if element.get_dom_attribute('data-nm-id') == art:
                    return (page, i + 1, absolute_position + i + 1)

            absolute_position += len(elements)
            page += 1
