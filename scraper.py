import requests
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27018/')


def scrape_ticker_page(ticker, page):
    cookies = {
        'fullscreengg': '1',
        'fullscreengg2': '1',
        'qgqp_b_id': '54560b99b050bd4b9ad7f8972fcd02c9',
        'st_si': '92207428003672',
        'st_pvi': '39982775811958',
        'st_sp': '2025-03-20%2020%3A27%3A11',
        'st_inirUrl': 'https%3A%2F%2Fguba.eastmoney.com%2F',
        'st_sn': '2',
        'st_psi': '20250320202718671-117001356556-0010488901',
        'st_asi': 'delete',
    }
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://guba.eastmoney.com/?jumph5=1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    
    response = requests.get(f'https://guba.eastmoney.com/list,{ticker},{page}.html', cookies=cookies, headers=headers)
    print(response.text)
