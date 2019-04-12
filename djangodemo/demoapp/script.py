import re
import requests


from demoapp.models import Region


def fetch_region_data():
    headers = {
        "content-type": "text/css",
        "charset": "utf-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    }

    url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/201901-06/201902061009.html'
    response = requests.get(url, headers=headers)

    pattern = re.compile('<td class=xl7016597>.*?([0-9\u4e00-\u9fa5]+).*?</td>')
    data_list = re.findall(pattern, response.text)

    data_num = len(data_list)

    for i in range(0, data_num, 2):
        print(data_list[i], ':', data_list[i + 1])
        if data_list[i][4:] == '00':
            if data_list[i][2:4] == '00':
                Region.objects.create(code=data_list[i], name=data_list[i + 1], grade="province")
            else:
                parent = Region.objects.get(code=data_list[i][:2] + '0000')
                Region.objects.create(code=data_list[i], name=data_list[i + 1], grade="city", parent=parent)
        else:
            try:
                parent = Region.objects.get(code=data_list[i][:4] + '00')
            except Region.DoesNotExist:
                parent = Region.objects.get(code=data_list[i][:2] + '0000')
            Region.objects.create(code=data_list[i], name=data_list[i + 1], grade="country", parent=parent)


if __name__ == "__main__":
    fetch_region_data()

