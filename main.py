import requests

url = 'https://api.777bar.com/api/v1/platform/asset_order/withdraw_info/del'

# Get user input for User ID, Token, and Withdraw Info ID
user_id = input("Enter User ID:")
token = input("Enter Token: ")
withdraw_info_id = input("Enter Withdraw Info ID: ")

headers = {
    'sec-ch-ua':
    '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'authorization': f'{user_id};{token}',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://777bar.com/',
    'U-DeviceType': 'pc',
    'sec-ch-ua-platform': '"macOS"'
}

data = {
    "withdraw_info_id": int(withdraw_info_id),
    "withdraw_type": "electronic_wallet",
    "token": token,
    "user_id": user_id
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
