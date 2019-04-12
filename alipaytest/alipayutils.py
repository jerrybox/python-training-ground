from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest


def get_key(path):
    """
    :param path: key file path
    :return: key string
    """
    with open(path) as fp:
        return fp.read()


if __name__ == "__main__":
    app_alipay_sanbox_private_path = r'C:\Users\jerry\Desktop\app_private_key.pem'
    alipay_sanbox_public_path = r'C:\Users\jerry\Desktop\alipay_public_key.pem'
    slack_path = r'E:\Documents\DesktopDocuments\ChatSlack.txt'

