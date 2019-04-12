from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest

def get_key(path):
    with open(path) as fp:
        return fp.read()


def get_url_request():
    app_alipay_sanbox_private_path = r'C:\Users\jerry\Desktop\app_private_key.pem'
    alipay_sanbox_public_path = r'C:\Users\jerry\Desktop\alipay_public_key.pem'


    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = "https://openapi.alipaydev.com/gateway.do"
    alipay_client_config.app_id = "20160923420591565"
    alipay_client_config.app_private_key = get_key(app_alipay_sanbox_private_path)
    alipay_client_config.alipay_public_key = get_key(alipay_sanbox_public_path)

    alipay_client_config.charset = 'utf-8'

    client = DefaultAlipayClient(alipay_client_config=alipay_client_config)


    model = AlipayTradePagePayModel()
    model.out_trade_no = "pay201805020000227"
    model.total_amount = 50
    model.subject = "test"
    model.body = "alipaytest"
    model.product_code = "FAST_INSTANT_TRADE_PAY"


    # settle_detail_info = SettleDetailInfo()
    # settle_detail_info.amount = 50
    # settle_detail_info.trans_in_type = "userId"
    # settle_detail_info.trans_in = "2088302300165605"
    #
    # settle_detail_infos = list()
    # settle_detail_infos.append(settle_detail_info)
    #
    # settle_info = SettleInfo()
    # settle_info.settle_detail_infos = settle_detail_infos
    #
    # model.settle_info = settle_info
    #
    #
    # sub_merchant = SubMerchant()
    # sub_merchant.merchant_id = "208830234153246"
    #
    # model.sub_merchant = sub_merchant

    request = AlipayTradePagePayRequest(biz_model=model)

    response = client.page_execute(request, http_method="GET")
    return response

if __name__ == "__main__":
    app_alipay_sanbox_private_path = r'C:\Users\jerry\Desktop\app_private_key.pem'
    alipay_sanbox_public_path = r'C:\Users\jerry\Desktop\alipay_public_key.pem'


    alipay_client_config = AlipayClientConfig()
    alipay_client_config.server_url = "https://openapi.alipaydev.com/gateway.do"
    alipay_client_config.app_id = "201609234200591565"
    alipay_client_config.app_private_key = get_key(app_alipay_sanbox_private_path)
    alipay_client_config.alipay_public_key = get_key(alipay_sanbox_public_path)

    alipay_client_config.charset = 'utf-8'

    client = DefaultAlipayClient(alipay_client_config=alipay_client_config)


    model = AlipayTradePagePayModel()
    model.out_trade_no = "pay20180452320000227"
    model.total_amount = 50
    model.subject = "test"
    model.body = "alipaytest"
    model.product_code = "FAST_INSTANT_TRADE_PAY"


    # settle_detail_info = SettleDetailInfo()
    # settle_detail_info.amount = 50
    # settle_detail_info.trans_in_type = "userId"
    # settle_detail_info.trans_in = "2088323400165605"
    #
    # settle_detail_infos = list()
    # settle_detail_infos.append(settle_detail_info)
    #
    # settle_info = SettleInfo()
    # settle_info.settle_detail_infos = settle_detail_infos
    #
    # model.settle_info = settle_info
    #
    #
    # sub_merchant = SubMerchant()
    # sub_merchant.merchant_id = "208823420153246"
    #
    # model.sub_merchant = sub_merchant


    request = AlipayTradePagePayRequest(biz_model=model)

    response = client.page_execute(request, http_method="GET")
    print("alipay.trade.page.pay response:" + response)
