# return all recent insider buys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# create web driver object
chrome_path = "C:\\Users\\Patrick\\Software\\chrome\\chromedriver_win32\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(chrome_path, options=chrome_options, keep_alive=False)

# read URL to web driver
driver.get("https://www.insidearbitrage.com/insider-sales/?desk=yes")

# get tickers

for i in range(2, 6):
    ticker_path = f"""/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[{i}]/td[2]/a"""
    ticker_id = driver.find_element_by_xpath(ticker_path)


    owner_path = f"""/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[{i}]/td[3]/a"""
    owner_id = driver.find_element_by_xpath(owner_path)

    relationship_path = f"""/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[{i}]/td[4]"""
    relationship = driver.find_element_by_xpath(relationship_path)

    date_path = f"""/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[{i}]/td[5]"""
    date = driver.find_element_by_xpath(date_path)

    cost_path = f"""/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[{i}]/td[6]"""
    cost = driver.find_element_by_xpath(cost_path)

    shares_path = f"""/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[{i}]/td[7]"""
    shares = driver.find_element_by_xpath(shares_path)

    value_path = f"""/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[{i}]/td[8]"""
    value = driver.find_element_by_xpath(value_path)

    total_held_path = f"""/html/body/div[1]/div[5]/div[1]/article/div[2]/div[1]/div[2]/table[2]/tbody/tr[{i}]/td[9]"""
    total_held = driver.find_element_by_xpath(total_held_path)

    print(ticker_id.text, owner_id.text, relationship.text, date.text, cost.text, shares.text, value.text, total_held.text)
