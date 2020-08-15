import requests
from time import sleep
from bs4 import BeautifulSoup

URL = 'https://atkinsonsbullion.com/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
# Initialising variables
silverGrams = 0
silverOz = 0
goldGrams = 0
goldOz = 0
# Variables for input to be stored
silverGramsTotal = 0
silverOzTotal = 0
goldGramsTotal = 0
goldOzTotal = 0


def get_price():  # Scalpe live web spot prices
    global silverGrams
    global silverOz
    global goldGrams
    global goldOz

    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Silver Grams
    silver_Grams = soup.find(
        'td', class_='js-lp-silver-grams').get_text().strip()[1:]
    silver_Grams = float(silver_Grams)
    silverGrams = silver_Grams
    # Silver Oz's
    silver_Oz = soup.find(
        'td', class_='js-lp-silver-toz').get_text().strip()[1:]
    silver_Oz = float(silver_Oz)
    silverOz = silver_Oz
    # Gold Ozs
    gold_Oz = soup.find('td', class_='js-lp-gold-toz').get_text().strip()[1:]
    gold_Oz = float(gold_Oz.replace(',', ''))
    goldOz = gold_Oz
    # Gold Oz's
    gold_Grams = soup.find(
        'td', class_='js-lp-gold-grams').get_text().strip()[1:]
    goldprice = float(gold_Grams)
    goldGrams = goldprice
    return silverGrams, silverOz, goldOz, goldGrams


def silver_grams():  # Function for investment total
    global silverGrams
    global silverGramsTotal
    silverGramsTotal = silverGrams * \
        float(input('\nEnter Silver weight in Grams...'))
    print('\n')
    print(f'Total Silver investment in Grams: £', silverGramsTotal)
    print('\n')
    return silverGramsTotal


def silver_oz():  # Function for investment total
    global silverOz
    global silverOzTotal
    silverOzTotal = silverOz * \
        float(input('\nEnter Silver weight in Ozs...'))
    print('\n')
    print(f'Total Silver investment in Oz: £', silverOzTotal)
    print('\n')
    return silverOzTotal


def gold_grams():  # Function for investment total
    global goldGrams
    global goldGramsTotal
    goldGramsTotal = goldGrams * \
        float(input('\nEnter Gold weight in Grams...'))
    print('\n')
    print(f'Total Gold investment in Grams: £', goldGramsTotal)
    print('\n')
    return goldGramsTotal


def gold_oz():  # Function for investment total
    global goldOz
    global goldOzTotal
    goldOzTotal = goldOz * \
        float(input('\nEnter Gold weight in Ozs...'))
    print('\n')
    print(f'Total Gold investment in Oz: £', goldOzTotal)
    print('\n')
    return goldOzTotal


def total_investment():  # Function for combining total portfolio
    total = silverGramsTotal + silverOzTotal + goldGramsTotal + goldOzTotal
    print(f'\nTotal Investment Value: £', total)


try:
    get_price()
except:
    print('Error receiving current stop prices.\n')
    print('Please reload program or conact support.\n')

while True == True:
    print('Metal Investment calculator.\n \n 1. Silver in Grams \n 2. Silver in Oz \n 3. Gold in Grams \n 4. Gold in Oz \n 5. Gold & Silver Investment \n 6. Exit')
    try:
        x = input('\nSelect Option\n')
        ans = int(x)
    except:
        print('Please select using a number.')
    if ans == 1:
        silver_grams()
    elif ans == 2:
        silver_oz()
    elif ans == 3:
        gold_grams()
    elif ans == 4:
        gold_oz()
    elif ans == 5:
        total_investment()
    elif ans == 6:
        print('Exiting...')
        sleep(1)
        exit()
