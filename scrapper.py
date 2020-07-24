import requests
import pickle
from bs4 import BeautifulSoup
import json
import datetime
import os
nav = {
    "date": "",
    "nav": 1,
    "change": 1
}
navs = [""]


def scrapper():
    URL = "https://www.camsonline.com/InvestorServices/COL_ISNAVScheme.aspx?scheme=24G&amc=L&masURL="
    headers = {
        'Host': 'www.camsonline.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.camsonline.com/CAMS_Consent.aspx?ReturnUrl=%2fInvestorServices%2fCOL_ISNAVScheme.aspx%3fscheme%3d24G%26amc%3dL%26masURL%3d&scheme=24G&amc=L&masURL=',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cookie': 'cookiesession1=4057D2FA1L3HD4VUOVAN1TVWLM3MF08D; ASP.NET_SessionId=kxqx4k21n1ctr0xclax41bic; AuthenticationTicket=6821815F2F0DD764407DEC38393B3C6D1988DA047A17797D57F1F1C959CE7B7A65860D5E8207B03281DD09D4EC7E015074FB6A3D2EA7CAD9D092566AED895341872628E361E9D86AE37DCC4D9BE45B39C8E274151DF90584AFC82F11EA534F57A6E5136A6766CBB0EE294A6F161E58D2DA8A17BA81889DAD460654F7A776EB33B3FDC061E54E195BB82A847BE8A30EC9799BCC98979870990C7DE948CA74B48F',
        'Upgrade-Insecure-Requests': '1'
    }

    raw_data = requests.get(URL, headers=headers)
    formatted_data = BeautifulSoup(raw_data.content, 'html5lib')
    table_ = formatted_data.find('div', attrs={'id': 'divSchemeNav'}).tbody
    # print(table_)
    navs = []
    i = 0
    # print(navs)
    for row in table_.findAll('tr'):
        k = 0
        for col in row.findAll('td'):
            data_ = col.text
            if(data_[0] == '('):
                data_ = data_[1:len(data_)-2]
                data_ = -1 * float(data_)
            if(k != 0):
                data_ = float(data_)
            nav[("date" if k == 0 else ("nav" if k == 1 else (
                "change" if k == 2 else "prev")))] = data_
            k = k+1
        navs.append(nav.copy())
        i = i+1
        if i > 10:
            break
    print("scrapping done")
    del navs[0]
    # print(navs)
    with open("scrapped.pickle", "wb") as scrapped_data:
        pickle.dump(navs, scrapped_data)
        print(" scrapped data writting in pickle :: done")
    txt_writer()


def txt_writer():
    with open("scrapped.pickle", "rb") as scrapped_data:
        navs = pickle.load(scrapped_data)
    with open("scrapped.txt", "w") as scrapped_txt:
        for nav in navs:
            scrapped_txt.write(
                nav["date"]+" " + str(nav["nav"])+" "+str(nav["change"])+"\n")
    print("scrapped data writting in text :: done")
    history()


def history():
    with open("last_scrapped.txt", "w") as history:
        history.write(str(datetime.date.today()))


def starter():
    with open("last_scrapped.txt", "r") as history:
        if(history.read() == str(datetime.date.today())):
            print(" scrapping done today,  not scrapping again")
            return
    scrapper()


if __name__ == "__main__":
    print("in")
    # starter()
    scrapper()
    print("out")
