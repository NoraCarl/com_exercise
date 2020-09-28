import requests
from bs4 import BeautifulSoup




if __name__ == "__main__":
    url = 'https://www.zhihu.com/hot'

    # 添加请求头
    headers={
        'host':'www.zhihu.com',
        'cookie':'_zap=56e96773-1d57-4ca0-b651-b81b61693a2c; d_c0="AIDayu0i6xGPTu3piR_YvmbDuuFJXgkfOUY=|1600617515"; _ga=GA1.2.568209324.1600617517; capsion_ticket="2|1:0|10:1600849231|14:capsion_ticket|44:Yzk4YmRiYzMxNTA0NDViODk2Nzc0ZGY5YjlmM2Q1MDg=|8f60c972df12b9c246e46c1907865308c5af4cec5fb243740b198122929186a2"; z_c0="2|1:0|10:1600849327|4:z_c0|92:Mi4xYWlqMUJBQUFBQUFBZ05ySzdTTHJFU2NBQUFDRUFsVk5ycEtTWHdEOWtOeXVnS1RxZVVpMVhXcWo1S1ZGMWFRbF9R|92dbad93c64e73766b13d623024bd6674f2ad6f76a81a51992bfe2d39c481c52"; q_c1=c377e27c1bc147be9c2acf6d8492ce78|1600916901000|1600916901000; _xsrf=28a0ecc2-77b3-4521-a60e-849bb4108975; _gid=GA1.2.653403254.1601308921; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1601308921,1601309313,1601310868,1601311640; SESSIONID=fjRrn8xbF7z8HVTEwSQaxNDQ8nEk1r5Sng7vV6tkr2L; JOID=VVsVBUnce9S2gNb2Y93Kwfpy9Rx1vhKAwOvqjQefSK2IzIWmJUNtpOiB0fNhJM_Qi8ful9f5yhK1OeEFAdA-g6Q=; osd=V1kRCkreedC5g9T0Z9LJw_h2-h93vBaPw-noiQicSq-Mw4akJ0dip-qD1fxiJs3UhMTsldP2yRC3Pe4GA9I6jKc=; tshl=; tst=h; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1601311876; _gat_gtag_UA_149949619_1=1; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1601311876|1601308921',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    html = requests.get(url, headers=headers, verify=False).content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find_all('a', target='_blank')
    for i in name:
        print(i)