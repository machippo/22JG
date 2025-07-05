#대선 개표 현황 빨리 보기


import requests
def get_tupyo():
    resp = requests.get("https://news.kbs.co.kr/vote/20250603/KBS_SUNGER_DATA.json?d=20250603183720")
    num = resp.json()[0]['DONGSAMUSO_TUSU']
    return int(num)
    

last_tupyo = get_tupyo()
while True:
    tupyo = get_tupyo()
    if tupyo > last_tupyo:
        print(f'new, {tupyo} votes')
        last_tupyo = tupyo
    time.sleep(1)
