# github.com/NoTinyxd 
# not more features i may add proxy and other if i want to add
# i am not responsible for any illegal usage of this repoimport requests
from faker import Faker
fake = Faker()
import json

with open('config.json','r') as c:
    config = json.load(c)
    token = config['token']
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.6',
    'authorization': token,
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'priority': 'u=1, i',
    'referer': 'https://discord.com/channels/1499332587062034452/1499335291364704317',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'Asia/Karachi',
    'x-super-properties': 'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImhhc19jbGllbnRfbW9kcyI6ZmFsc2UsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0Ny4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTQ3LjAuMC4wIiwib3NfdmVyc2lvbiI6IiIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL2Rpc2NvcmQuY29tL2xvZ2luL29uZS10aW1lP3Rva2VuPU1UTTROVFl3TXpVNE9UQTJPVGN6T0RFek53LkgyZmhNRy5TbFY3YllHcFAwMTFtTUE1WmRndFN1SC12RlBVYTNnWERKbU9VSSIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6NTM2OTA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJjbGllbnRfbGF1bmNoX2lkIjoiZWFhODE4YTctMjVjMC00MDY2LTgzNTgtYjFmMzdlZTA5NWVkIiwibGF1bmNoX3NpZ25hdHVyZSI6IjkzMTI2NTZkLWU0NGQtNDQ2YS04ODcyLTgwM2EyZWM1ZTNmNCIsImNsaWVudF9oZWFydGJlYXRfc2Vzc2lvbl9pZCI6IjJlNWIzMjNhLWQ2MTctNGU1Ny05NjY3LWJkOTJkMTgxNDExMiIsImNsaWVudF9hcHBfc3RhdGUiOiJmb2N1c2VkIn0=',
}
i = input("Enter Amount? : ")

for _ in range(int(i)):
    name = (fake.color_name() + " " + fake.word().title())

    json_data = {
        'name': name,
        'icon': None,
        'channels': [],
        'system_channel_id': None,
        'guild_template_code': '2TffvPucqHkN',
    }
    response = requests.post('https://discord.com/api/v9/guilds', headers=headers, json=json_data)
    res_json=response.json()

    #print(response.text)
    #print(response.status_code)
    if response.status_code == 201:
        print(f"Created server with server id = ,{res_json['id']}")
    elif response.status_code == 429:
        print("Ratelimit Occured retry after",)
        #print(response.text)
    else:
        print("Something went Wrong")
