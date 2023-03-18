import sys
import requests
from bs4 import BeautifulSoup


# 爬取启明网的内容，保存标题，时间，链接3部分内容
# 读入url输出页面内容
def grab_information(url):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = 'utf-8'
        return r.text
    else:
        print("无法爬取网页信息")
        sys.exit(0)


# 读入网页源码，输出信息列表
# 将通知标题、时间、链接汇总成列表输出
def parse(html_page, records_per_page):
    if '<div id="wp_paging_w6">' not in html_page:
        return
    main_text = html_page.split("','c30':'0','c29':'1','c33':'1','c10':'50'}\">")[1]
    main_text = main_text.split(' <div id="wp_paging_w6"> ')[0]
    soup = BeautifulSoup(main_text, 'html.parser')
    list_info = []
    tag_li = soup.li
    for i in range(records_per_page):
        href = tag_li.a.get('href')
        if "/page.htm" in href:
            href = "https://xgc.nju.edu.cn" + href
        title = tag_li.a.string
        p_time = tag_li.find_all('span')[2].string
        list_info.append([title, href, p_time])
        tag_li = tag_li.find_next_sibling()
    return list_info


# 从网页提取总页面数、总记录数，每页记录数
# 读入网页，输出总页面数、总记录数,每页记录数
def parse_pcm(html):
    if '<ul class="wp_paging clearfix"> ' not in html:
        print("无列表数据")
        return
    pcm_text = html.split('<ul class="wp_paging clearfix"> ')[1]
    pcm_text = pcm_text.split('<li class="page_nav">')[0]
    pcm_soup = BeautifulSoup(pcm_text, 'html.parser')
    em_list = pcm_soup.find_all("em")
    records_per_page = min(int(em_list[0].string), int(em_list[1].string))
    print(records_per_page)
    return records_per_page


def parse_xuegong():
    # todo 爬取附件和正文
    url = 'https://xgc.nju.edu.cn/1537/list.htm'
    html = grab_information(url)
    records_per_page = parse_pcm(html)
    info_list = parse(html, records_per_page)
    return url, info_list


if __name__ == '__main__':
    parse_xuegong()

