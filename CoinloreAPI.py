import requests


def inform_faezeh(price):
    # print(f'Good Price...Consider to buy Bitcoin at {price}')
    api_key = '5631715168416635474C48594F4E3952653558304A4E55556263386545553161635A4F6C627245314B6C673D'
    sms_url = f'https://api.kavenegar.com/v1/{api_key}/sms/send.json'
    sms_data = {'receptor': '09125067082', 'message': f'Hi Faezeh, Bitcoin is {price},nice buy chance!'}
    sms_response = requests.post(url=sms_url, data=sms_data)
    print(sms_response.json())


my_good_price = 30000

response = requests.get('https://api.coinlore.net/api/ticker/?id=90')
price = float(response.json()[0]['price_usd'])

if price < my_good_price:
    inform_faezeh(price)
