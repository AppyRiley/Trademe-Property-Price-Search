import chromedriver_autoinstaller
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    chromedriver_autoinstaller.install()

    opts = Options()
    opts.add_experimental_option("detach", False)
    return webdriver.Chrome(opts)


def house_in_pricerange(
    string: int,
    price_min: int,
    price_max: int,
) -> bool:
    driver.get(
        f"https://www.trademe.co.nz/a/property/residential/sale/search?price_min={price_min}&price_max={price_max}&search_string={string}"
    )
    try:
        driver.find_element(By.XPATH, '//div[@role="list"]')
        return True
    except NoSuchElementException:
        return False


def find_minimum_price(string: int, start_price=1_000_000) -> int:
    print(f"Searching for lowest price...")

    price_max = start_price
    step = 100_000

    while step > 1_000:
        while house_in_pricerange(string, price_min=0, price_max=price_max - step):
            price_max -= step
        step = int(step / 2)

    print(f"Property: {string}")
    print(f"Price:    {price_max}")

    return price_max


if __name__ == '__main__':
    driver = get_driver()

    find_minimum_price(4707820749)


