import requests
import json


def main():    
    file_name = input('Type name of file to save json response: ')
    url = "https://api.twitter.com/1.1/friends/list.json"
    user = input('Type twitter username: ')
    print_text = input('Print result to console Yes/No(yes/no)? ')
    querystring = {"cursor":"-1","screen_name":f"{user}","skip_status":"false","include_user_entities":"true", "count":789}

    payload = ""
    headers = {
        'Authorization': "Bearer AAAAAAAAAAAAAAAAAAAAAH%2F69QAAAAAAWVGuIRk6Yp2I1qlFF5Sj%2BtcRbXY%3DHkggXxRwJPiDchl3Hnw2spNAnQDgBrUIeFLBGWsS4CW0vbFYJV",
        'cache-control': "no-cache",
        'Postman-Token': "41f7add3-b49f-43be-bd0d-a9a695dd9032"
        }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    json.dump(json.loads(response.text), open(file_name,'w'))
    if print_text.lower()[0] == 'y':
        print(response.text)

if __name__ == '__main__':
    main()