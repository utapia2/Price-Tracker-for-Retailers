
import requests
from bs4 import BeautifulSoup
import smtplib
import time
from email.mime.text import MIMEText

def BestbuyPriceTracker():
    print('caling bestbuy tracker')
    #define the function 

def WalmartPriceTracker():
    print('caling walmart tracker')

    website = input('Enter Walmart item page you want to track: ')
    response = requests.get(website)

    if response.status_code == 200:
        print('Success! Website is accessible')
        time.sleep(2)

    wishprice = float(input('Enter the price you wish to notify you when the item is that price or lower: '))

    
    to = input('Enter your email address to receive an alert when the price drops: ')


    freq = int(input('How often would you like to check for this price? ex: Type 2 for every 2 hours: '))
    print('Okay program will check every', freq,' hours')


    while True:

        while True:
            if response.status_code == 200:
                print('Success! Website is accessible-- inside second while, in try except to catch price')
                time.sleep(2)
            soup = BeautifulSoup(response.content, "lxml")
            findprice = soup.find('span', {'class': "price-characteristic"})
            price = float(findprice["content"])
            if isinstance(price, float):
                print('success price is a float and was captured')
                break
            else:
                print('Trying again to capture price!...')
            

        
        if price <= wishprice:

            print('Your item is on sale!--- trying to send email')
            sent_from = 'codemail5678@gmail.com'
            password = 'qwzx5678'

            subject='Price Alert!'
            email_body = 'Congratulations! Go to the page:\n' + website + '''\n You're saving $''' + str(price - wishprice) + '!'
            mailtext='Subject:'+subject+'\n\n'+email_body
            

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(sent_from, password)
            server.sendmail(sent_from, to, mailtext)
            server.close()
            break

        else:
            print('Item is not on sale')
            print('Checking again!')
            #temporary exit(), remove when actually price tracking
            #exit()
            time.sleep(freq)
            


def main():

    print("in main function")

    selection = int(input("Enter 1 for Walmart \nEnter 2 for BestBuy \nEnter 3 for Target\n: "))

    if selection == 1:
        WalmartPriceTracker()

    elif selection == 2:
        BestbuyPriceTracker()
    else:
        exit()

if __name__ == '__main__':
    main()
