#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __created by junxi__

from bs4 import BeautifulSoup
import requests
import time

# 导入url
url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
# 已经登录的url地址
url_saves = 'https://cn.tripadvisor.com/Saves#56071414'
# 多页信息链接集合
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,1050,30)]
# 构造向服务器提交的参数 header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Cookie': 'TAUnique=%1%enc%3AQjrBcBVVBE6w8qII1kT24jVoo9TbEa3zshIdK3L5%2BR4xpOr4ewmmSQ%3D%3D; ServerPool=A; TASSK=enc%3AAMSrfShnSN%2Fe2fOtMoaJQU88QBfPZSLuDWqtfIBnm7VMBcq30PM1bkzHPv21QX14Z2SO0ONAiMMzxvHDnBiGNx%2F8%2B6%2Bj1emCZsCx9pA3twfXZ46H%2FJ%2BPpGlbTDMRpKT0GQ%3D%3D; __gads=ID=0fa9241fd45da8f7:T=1477907088:S=ALNI_Maeiz4T9jNZNqHFqQFADd7iYAs2KQ; TART=%1%enc%3AsPKiCNZE9uJ4kT3lVs4KKO5kmQTw7xLfnNjo6WuhmFH6Oiqf6g2nCzplojwtwdvMnJE08vJ9sLg%3D; SecureLogin2=3.4%3AAArnCfcUEVjqPsCSygTuz5m3QJ3xOiiJAt1U16v95W8krlrWZdehRwKyhhbkx7e6iOfA7Oxs1c4W9pE%2Fv%2BAzaJlm%2FL0bTS8sGZOeUVeW0dlBt09wPNKsjuMuEajsdouyZFuxusV5K9%2B%2BrqU4r2HSjZ3g3ATaDhykK76f9wAq4WiBcbs4oiFxNeS3Z4AR%2FPqQnOdQoFizJoXeQ53RhWsSKBU%3D; TAAuth3=3%3A259af513b83dc61c6c951389344738e5%3AAAe6N1bsS%2BBELqETX3awkdEY9fMtayfj9NHdN2Di54oH%2FC3IGRaAsBKxsPBW1v87IRVF5%2FkxP2agxDQI33P1bn5IeAaHlWz%2BMjFv9rPUQ5UxdlSR2SZPV9JVWtMW9bToXg7Uto4TZ950bxYZVbulsBGBbkpP244LV0rBKjZq7oa0aHw47xukOOrUZl%2FdZlOV5mMGsTrefGxYsWGMcRmx2RAJHdL5c7vBB7F4RXPMGpu2; CommercePopunder=SuppressAll*1477907185070; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_305l105127_305l143361_305*RS.1; TASession=%1%V2ID.92E2E6EEFA786616E4F93CF9D9EFAD8E*SQ.38*LR.http%3A%2F%2Fwww%5C.tripadvisor%5C.cn%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*PR.427%7C*LS.Attraction_Review*GR.8*TCPAR.62*TBR.57*EXEX.10*ABTR.59*PPRP.77*PHTB.27*FS.90*CPU.43*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.9DFE1AE9AB2666B6C628262DCB787AE3*LF.zhCN*FA.1*DF.0*FBH.2*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.143361; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CAWPUPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C3%2C-1%7Cbrandsess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCpmPopunder_1%2C1%2C1477993483%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C2%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C1%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1478511929%7CLaFourchette+MC+Banners%2C%2C-1%7CAWPUSess%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7C2016stickpers%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTakeOver%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAUD=LA-1477907080822-1*LG-201683-2.1.F.*LD-201684-.....; TAReturnTo=%1%%2FAttraction_Review-g60763-d143361-Reviews-Broadway-New_York_City_New_York.html; roybatty=TNI1625!AMCeupePpODOrdzUOwUyewV5gCJlq9EPimX73RgmQuz6BgreXLrPcbtRAr%2Fcuz7GGNTCRe5xiBlm7deJOfLcWM5DILPeoI2ag2EDb8tlPO%2FWp6stcNQUjXFIQwbYmM7lvd5QAuFg0McctS2v43Xo3w9nRcgNbHcXFf2bnu7n4AyM%2C1; NPID=; EVT=gac.BlackNavBar*gaa.clickSaves*gal.*gav.0*gani.false*gass.Saves*gasl.*gads.Saves*gadl.*gapu.WBcTNgokG4cAAFfKMSoAAAB6*gams.2'
}


def get_attractions(url,data=None):
    # 请求网页内容
    wb_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text,'lxml')   # 解析网页,text把html内容转换为文本
    titles = soup.select('div.property_title > a[target="_blank"]')
    images = soup.select('img[width="160"]')
    cates = soup.select('div.p13n_reasoning_v2')    # 分类

    if data == None:
        for title,image,cate in zip(titles,images,cates):
            data = {
                'title': title.get_text(),
                'image': image.get('src'),
                'cate': list(cate.stripped_strings),
            }
            print(data)


def get_favs(url,data=None):
    # 请求网页内容
    wb_data = requests.get(url_saves,headers=headers)
    # 解析网页内容
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('a.location-name')
    images = soup.select('div.photo > div.sizedThumb > img.photo_image')
    metas = soup.select('span.format_address')

    if data == None:
        for title, image, meta in zip(titles, images, metas):
            data = {
                'title': title.get_text(),
                'image': image.get('src'),
                'meta': list(meta.stripped_strings),
            }
            print(data)


# 连续循环爬取多个页面信息
for single_url in urls:
    get_attractions(single_url)
