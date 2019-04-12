"""
https://venturewell.org/i-corps/llpvideos/
    headline(http://headline)  章节目录名
        title(http://headline)  视频标题（iframe地址页）
            (http://headline)  高清视频地址
"""
import os
import re
import requests
import json
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

headers = {
    "content-type": "text/css",
    "charset": "utf-8",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}
http_proxy = "http://127.0.0.1:1080"
https_proxy = "http://127.0.0.1:1080"
ftp_proxy = "http://127.0.0.1:1080"
proxyDict = {"http": http_proxy,  "https": https_proxy, "ftp": ftp_proxy}


def format_key(string):
    """
    :param name_string:
    :return: 符合windows的路径字符串,符合字典key格式
    """
    return string.replace(' ', '_').replace('?', '')


def tuple_to_dict(name_url, flag=False):
    """
    :param flag: k,v转换
    :param name_url: (name, url)
    :return:
    """
    dict_data = {}
    if flag:
        for k, v in name_url:
            dict_data[format_key(k)] = v
    else:
        for k, v in name_url:
            dict_data[format_key(v)] = k
    return dict_data


def get_headline_url(origin_url):
    """
    :param url: 课程目录页
    :return: [(title, title_url)]章节页面的地址，url地址最后一个字段就是章节名称
    """
    response = requests.get(origin_url, headers=headers)
    pattern = '<a href="(https://venturewell.org/i-corps/llpvideos/.*?/)" target="_blank" rel="noopener">(.*?)</a>'
    headline_url_list = re.findall(pattern, response.text)
    return headline_url_list


def get_title_url(headline_url):
    """
    :param headline_url:  章节目录的url
    :return: 返回video_title, iframe_url
    """
    response = requests.get(headline_url, headers=headers)
    pattern = '<h2>(.*?)</h2>\n<p><iframe src="(.*?)" width='
    title_url_list = re.findall(pattern, response.text)
    return title_url_list


def get_video_url(web_url, referer):
    """
    :param web_url:  iframe获取到的视频网页地址
    :return: 提取出的720p的视频地址
    """
    logger.info("Start Parse {web_url}".format(web_url=web_url))
    headers.update({"referer":referer})
    try:
        response = requests.get(web_url, headers=headers, proxies=proxyDict)
        pattern = 'var config = (\{.*\})'
        data_dict = json.loads(re.findall(pattern, response.text)[0])
        videos_dict_list = data_dict['request']['files']['progressive']
        video_url = videos_dict_list[1]['url'] if videos_dict_list[1]['quality'] == '720p' else videos_dict_list[0]['url']
    except:
        return "error"
    logger.info("Complete Parse {web_url}".format(web_url=web_url))
    logger.info("Video_url:{video_url}".format(video_url=video_url))
    return video_url


def get_dir_name(headline):
    """
    :param headline: 大标题
    :return: 创建对应的文件夹
    """
    dir_name = 'C:\\Users\\jerry\\Desktop\\myvideo\\' + format_key(headline)
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
    logger.info("File {filename} Download complete！".format(filename=file_path))


if __name__ == "__main__":
    URL = "https://venturewell.org/i-corps/llpvideos/"

    headline_title_url_dict = {}
    # 原始页面获取{"headline":"url"}
    headline_url = get_headline_url(URL)
    headline_url_dict = tuple_to_dict(headline_url, flag=True)

    # 章节页获取{"video_title":"iframe_url"}



    # 视频播放页获取url


