# Python program to scrape website

import requests
import csv
from lxml import html


def scrapper(price):
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
    r = requests.get(URL, headers=headers)

    page = html.fromstring(r.content)

    table = page.xpath(
        '//div[@id="divSchemeNav"]//table//td//text()')
    k = 0
    strt = ""
    ofile = open('scrapped.txt', 'w')
    ofile.write(
        "    Date               NavPoint       TotalValue       ChangeOfValue\n")
    for i in table:
        if(k % 4 == 0):
            strt = i
        elif(k % 4 == 1):
            t = i
            strt = strt + "       " + \
                str(round(float(t), 2)) + "        " + \
                str(round(price*float(t), 2))+"       "
        elif(k % 4 == 2):
            t = ""
            t1 = str(i)
            for j in t1:
                if(j != '(' and j != ')'):
                    t += j
                elif(j == '('):
                    t += '-'
            strt += str(round(price*float(t), 2))
        k = k + 1
        if(k % 4 == 0):
            ofile.write(strt)
            ofile.write("\n")
        if(k > 40):
            break

    ofile.close()
