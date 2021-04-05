import requests

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'YzVlYWUxYTMtNWNlMy00ZjFkLWE5ZDQtMjE4N2I1YWQ0MTQ2MmQ5NTFiZGItZDcx_PF84_ebdf3b62-c327-4af2-8733-10d8711bb8cd'

httpHeaders = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

queryParams = { 'sortBy': 'lastactivity', 'max': '2'}

response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

print(response.status_code)
print(response.text)
