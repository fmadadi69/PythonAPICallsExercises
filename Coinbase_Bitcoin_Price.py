from scrapingbee import ScrapingBeeClient
import urllib.parse

client = ScrapingBeeClient(api_key='CC2IFZVOQQS9WYSJM74MQCHHU8IYB7PF30SX2M8BE3ZDDHL7IR56LF89T73QNC7N7CZUF5KHOZ30DQLG')
encoded_url = urllib.parse.quote("https://api.coinbase.com/v2/prices/BTC-USD/buy \
  -H 'Authorization: Bearer abd90df5f27a7b170cd775abf89d632b350b7c1c9d53e08b340cd9832ce52c2c'")
print(encoded_url)
response = client.get(encoded_url, params={
    'country_code': 'us',
    'premium_proxy': 'True',
}
                      )

print('Response HTTP Status Code: ', response.status_code)
print('Response HTTP Response Body: ', response.content)