import requests

name = '/Users/apple/Documents/phone_numbers'
text = 'سلام عزیزم'


def read_phone_numbers(filename):
    with open(filename) as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content


def send_sms(phone_num, text):
    api_key = '5631715168416635474C48594F4E3952653558304A4E55556263386545553161635A4F6C627245314B6C673D'
    url = f'https://api.kavenegar.com/v1/{api_key}/sms/send.json'
    mydata = {'receptor': phone_num, 'message': text}
    response = requests.post(url, data=mydata)
    return response.ok


phone_numbers = read_phone_numbers(name)
for number in phone_numbers:
    if not send_sms(number, text):
        print(number)
