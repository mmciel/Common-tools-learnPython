"""
简单的python spider 获取知乎指定回答下所有图片
author：mmciel
time：2019年6月18日14:58:42
realize: requests json re

"""
import requests
import json
import re
import os
from time import sleep
from bs4 import BeautifulSoup

'''数据说明'''
# 问题ID
# img url list
# img_url_list = []
# 文件夹
parent_path = "./pic/"
'''请求相关数据说明'''
headers = {
    "content-type": "application/json",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}



def download_URL(img_url_list):
    """传入url列表，完成图片文件的下载"""
    id = str(problem_id)
    for url in img_url_list:
        md5 = re.compile(r"[a-fA-F0-9]{32,32}").search(url).group()
        iffx = re.compile(r".{4}$").search(url).group()
        filename = id+"-"+md5+iffx

        res = requests.get(url,headers)
        dirs = './'+id+"/"
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        with open(dirs+filename, 'wb') as f:
            f.write(res.content)
    pass

def get_img_url(problem_id):
    """获取所有下载链接到list"""
    # 合成正确的url
    limit = 5
    pagenum = 0
    url = "https://www.zhihu.com/api/v4/questions" \
          "/" + str(problem_id) + "/" \
                                  "answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&" \
                                  "limit=" + str(limit) + "&offset=" + str(
        pagenum) + "&platform=desktop&sort_by=default"


    #318446058
    img_url_list = []
    response = requests.get(url,headers=headers)
    # 获得原始数据
    original_data = json.loads(response.text)
    # print(url)
    flag = True
    #
    title = original_data['data'][0]['question']['title']
    print("启动爬取："+title)
    while flag:

        pagenum = pagenum+limit
        if pagenum%100 == 0 :
            print("请求页面超过100，正在跳转下载：")
            download_URL(img_url_list)
            img_url_list = []
        if original_data['paging']['is_end'] == 'true':
            print("【爬取完毕】")
            flag = False
        else:
            print("==========="+"页码"+str(pagenum)+"===========")
            update_url = original_data['paging']['next']
            # 解析content
            temp_list = []
            length = len(original_data['data'])
            for i in range(length):
                # 打印到控制台：
                author = original_data['data'][i]['author']['name']
                print("正在爬取作者：" + author)
                with open(title + "_log.txt", "a", encoding="utf-8") as f:
                    f.write(author)
                    f.write("\n")
                content_data = original_data['data'][i]['content']
                soup = BeautifulSoup(content_data, 'lxml')
                # print(soup.prettify())
                if soup.img != None:
                    for list in soup.find_all('img'):
                        attrs = list.attrs
                        if "src" in attrs:
                            image = attrs['src']
                            temp_list.append(image)
                            # print(image)
                    print(temp_list)
                    return
                # 写入日志
            img_url_list.extend(temp_list)
            with open(title+"_log.txt", "a", encoding="utf-8") as f:
                for i in temp_list:
                    f.write(i)
                    f.write("\n")
            # 更新original
            response = requests.get(update_url, headers=headers)
            original_data = json.loads(response.text)
            sleep(2)

    pass

if __name__ == "__main__":
    problem_id = input("please input problem id：")
    # 获取所有图片URL及相关信息
    get_img_url(problem_id)

