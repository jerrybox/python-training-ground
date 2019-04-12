import os
import re
import requests
import json
import copy
import logging
import threading

from downloader.data import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
headers = {
    "content-type": "text/css",
    "charset": "utf-8",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}
http_proxy = "http://127.0.0.1:1080"
https_proxy = "http://127.0.0.1:1080"
ftp_proxy = "http://127.0.0.1:1080"
proxyDict = {"http": http_proxy,  "https": https_proxy, "ftp": ftp_proxy}


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def format_key(string):
    """
    :param name_string:
    :return: 符合windows的路径字符串,符合字典key格式
    """
    return re.sub('\W', '_', string)


def get_video_url(web_url, referer):
    """
    :param web_url:  iframe获取到的视频网页地址
    :return: 提取出的720p的视频地址
    """
    headers.update({"referer":referer})
    try:
        response = requests.get(web_url, headers=headers)
        pattern = 'var config = (\{.*\})'
        data_dict = json.loads(re.findall(pattern, response.text)[0])
        videos_dict_list = data_dict['request']['files']['progressive']
        video_url = [videos_dict['url'] for videos_dict in videos_dict_list if videos_dict['quality'] == '720p'][0]
    except:
        return "error"
    return video_url


def get_dir_name(headline):
    """
    :param headline: 大标题
    :return: 创建对应的文件夹
    """
    dir_name = os.path.join(BASE_DIR, format_key(headline))
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_name


def download_video(url, file_path, referer):
    """
    :param url:  视频地址
    :param file_path:  视频要保存的位置
    :return: 保存至本地
    """
    logger.info("File {filename} Download start！".format(filename=file_path))
    headers.update({"referer": referer})
    response = requests.get(url, headers=headers, stream=True)
    print("File {filename} Download start！".format(filename=file_path))
    with open(file_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=512):
            file.write(chunk)
    logger.info("File {filename} Download complete！".format(filename=file_path))


if __name__ == "__main__":

    headline_url_dict = copy.deepcopy(headline_url_dict)
    headline_url_dict_copy = copy.deepcopy(headline_url_dict_copy)

    for headline, title_iframe_list in headline_url_dict_copy.items():
        dir_name = get_dir_name(headline)
        referer = headline_url_dict[headline]
        logger.info("----------------------")
        logger.info(headline)
        logger.info("----------------------")
        for title, iframe_url in title_iframe_list:
            video_url = get_video_url(iframe_url, referer)
            file_path = os.path.join(dir_name, format_key(title)) + ".mp4"
            thread = threading.Thread(target=download_video, args=(video_url, file_path, iframe_url))
            thread.start()
