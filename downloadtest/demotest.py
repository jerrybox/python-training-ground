import os
import re
import requests
import json

from lxml import etree

from data import DATA


# 搬瓦工代理
headers = {
    "content-type": "text/css",
    "charset": "utf-8",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}
http_proxy = "http://127.0.0.1:1080"
https_proxy = "http://127.0.0.1:1080"
ftp_proxy = "http://127.0.0.1:1080"
proxyDict = {"http": http_proxy,  "https": https_proxy, "ftp": ftp_proxy}


def get_video_url(web_url):
    """
    :param web_url:  iframe获取到的视频网页地址
    :return: 提取出的720p的视频地址
    """
    print("Start Parse {web_url}".format(web_url=web_url))

    response = requests.get(web_url, headers=headers, proxies=proxyDict)
    pattern = 'var config = (\{.*\})'
    data_dict = json.loads(re.findall(pattern, response.text)[0])
    videos_dict_list = data_dict['request']['files']['progressive']
    video_url = videos_dict_list[1]['url'] if videos_dict_list[1]['quality'] == '720p' else videos_dict_list[0]['url']

    print("Complete Parse {web_url}".format(web_url=web_url))
    print("Video_url:{video_url}".format(video_url=video_url))
    return video_url


def replace_space(name_string):
    """
    :param name_string:
    :return: 符合windows的路径字符串
    """
    return name_string.replace(' ','_').replace('?','')


def get_dir_name(headline):
    """
    :param headline: 大标题
    :return: 创建对应的文件夹
    """
    dir_name = 'C:\\Users\\jerry\\Desktop\\myvideo\\' + replace_space(headline)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_name


def download_video(url, file_path):
    """
    :param url:  视频地址
    :param file_path:  视频要保存的位置
    :return: 保存至本地
    """
    response = requests.get(url, headers=headers, proxies=proxyDict, stream=True)

    print("File {filename} Download start！".format(filename=file_path))
    with open(file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
    print("File {filename} Download complete！".format(filename=file_path))


if __name__ == "__main__":
    headline_title_url = DATA
    print(len(DATA))
    for headline, title_url_list in headline_title_url[:1]:
        dir_name = get_dir_name(headline)
        for title, url in title_url_list:
            file_name = replace_space(title) + '.mp4'
            file_path = dir_name + '\\' + file_name
            video_url = get_video_url(url)
            download_video(video_url, file_path)


