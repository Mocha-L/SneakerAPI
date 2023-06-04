
import requests

base_url = "http://stockxapi.spiderx.cc:61030"
# token 需要从作者处申请，测试可用本一周，在线测试可见http://stockxapi.spiderx.cc:61030/docs
# Token needs to be applied for from the author and can be tested this week. Online testing can be seen at http://stockxapi.spiderx.cc:61030/docs
# 联系作者 Email: mocha_lee@qq.com 微信：TTF_TTF
# Contact the author Email: mocha_lee@qq.com WeChat: TTF_TTF
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def ping():
    """
    @description: 测试接口是否可用 Test whether the interface is available
    @return:
    """
    url = f"{base_url}/ping"
    response = requests.get(url)
    return response.json()


def init_auth():
    """
    @description: 初始化auth，初始化一个设备ID，后面所有接口都要用到。该接口较慢。
    Initialize auth, initialize a device ID, and all subsequent interfaces will be used. This interface is slower.
    @return:
    """
    url = f"{base_url}/api/stockx/init_auth"
    params = {
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def search_product(auth, keyword, page):
    """
    @description: 搜索商品 Search for goods
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param keyword: 搜索关键词 Search keywords
    @param page: 页码 Page number
    @return:
    """
    url = f"{base_url}/api/stockx/search_product"
    params = {
        "token": TOKEN,
        "auth": auth,
        "keyword": keyword,
        "page": page
    }
    response = requests.get(url, params=params)
    return response.json()


def product_activity(auth, product_uuid):
    """
    @description: 商品活动信息(历史销售记录) Product activity information(historical sales records)
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param product_uuid: 商品ID Product ID
    @return:
    """
    url = f"{base_url}/api/stockx/product_activity"
    params = {
        "token": TOKEN,
        "auth": auth,
        "product_uuid": product_uuid
    }
    response = requests.get(url, params=params)
    return response.json()


def product_detail(auth, product_uuid):
    """
    @description: 商品详情 Product details
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param product_uuid: 商品ID Product ID
    @return:
    """
    url = f"{base_url}/api/stockx/product_detail"
    params = {
        "token": TOKEN,
        "auth": auth,
        "product_uuid": product_uuid
    }
    response = requests.get(url, params=params)
    return response.json()


def product_size_price(auth, product_id):
    """
    @description: 商品尺码价格 Product size price
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param product_id: 商品ID(精确到尺码的ID) Product ID(ID to size)
    @return:
    """
    url = f"{base_url}/api/stockx/product_size_price"
    params = {
        "token": TOKEN,
        "auth": auth,
        "product_id": product_id,
    }
    response = requests.get(url, params=params)
    return response.json()


def self_info(auth, access_token):
    """
    @description: 用户信息 User information
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @return:
    """
    url = f"{base_url}/api/stockx/self_info"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    return response.json()


def seller_info(auth, access_token):
    """
    @description: 卖家信息 Seller information
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @return:
    """
    url = f"{base_url}/api/stockx/seller_info"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    return response.json()


def update_access_token(auth, refresh_token, client_id, auth0_client):
    """
    @description: 更新access_token Update access_token
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param refresh_token: 用户登录后的refresh_token参数 refresh_token parameter after user login
    @param client_id:
    @param auth0_client:
    @return:
    """
    url = f"{base_url}/api/stockx/update_access_token"
    params = {
        "token": TOKEN,
        "auth": auth,
        "refresh_token": refresh_token,
        "client_id": client_id,
        "auth0_client": auth0_client,
    }
    response = requests.get(url, params=params)
    return response.json()


def get_selling_products(auth, access_token, cursor="", query=""):
    """
    @description: 获取正在出售中的商品 Get products on sale
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param cursor:
    @param query: 查询关键词，可为空 Query keywords, can be empty
    @return:
    """
    url = f"{base_url}/api/stockx/get_selling_products"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
        "cursor": cursor,
        "query": query,
    }
    response = requests.get(url, params=params)
    return response.json()


def get_sold_products(auth, access_token, cursor="", query=""):
    """
    @description: 获取已售出的商品 Get sold products
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param cursor:
    @param query: 查询关键词，可为空 Query keywords, can be empty
    @return:
    """
    url = f"{base_url}/api/stockx/get_sold_products"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
        "cursor": cursor,
        "query": query,
    }
    response = requests.get(url, params=params)
    return response.json()


def get_history_products(auth, access_token, cursor="", query=""):
    """
    @description: 获取历史已售商品 Get historical sold products
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param cursor:
    @param query: 查询关键词，可为空 Query keywords, can be empty
    @return:
    """
    url = f"{base_url}/api/stockx/get_history_products"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
        "cursor": cursor,
        "query": query,
    }
    response = requests.get(url, params=params)
    return response.json()


def get_order_detail(auth, access_token, chain_id):
    """
    @description: 获取订单详情 Get order details
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param chain_id: chain_id
    @return:
    """
    url = f"{base_url}/api/stockx/get_order_detail"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
        "chain_id": chain_id,
    }
    response = requests.get(url, params=params)
    return response.json()


def vacation_mode(auth, access_token, customer_id, switch_to):
    """
    @description: 设置假期模式 Set vacation mode
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param customer_id: customer_id
    @param switch_to: OFF:关闭假期模式 ON:开启假期模式 OFF: Turn off vacation mode ON: Turn on vacation mode
    @return:
    """
    url = f"{base_url}/api/stockx/vacation_mode"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
        "customer_id": customer_id,
        "switch_to": switch_to,
    }
    response = requests.get(url, params=params)
    return response.json()


def cancel_product(auth, access_token, chain_id):
    """
    @description: 下架商品 Cancel product
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param chain_id: chain_id
    @return:
    """
    url = f"{base_url}/api/stockx/cancel_product"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
        "chain_id": chain_id,
    }
    response = requests.get(url, params=params)
    return response.json()


# sold_product_list={"products": [{"chain_id": "", "sku": ""}]}
def create_shipment(auth, access_token, sold_product_list):
    """
    @description: 创建发货单 Create shipment
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param sold_product_list: 已售出的商品列表 Sold product list
    @return:
    """
    url = f"{base_url}/api/stockx/create_shipment"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
    }
    response = requests.post(url, params=params, json=sold_product_list)
    return response.json()


# chain_id_price_dict={
#     "chain_id": "",
#     "price": "",
#     "user_id": "",
#     "expires_second": 3600,
# }
def update_price_single(auth, access_token, chain_id_price_dict):
    """
    @description: 单个修改价格 Single price modification
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param chain_id_price_dict:
    @return:
    """
    url = f"{base_url}/api/stockx/create_shipment"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
    }
    response = requests.post(url, params=params, json=chain_id_price_dict)
    return response.json()


# chain_id_price_dict = {
#    "products": [{
#       "chain_id": "",
#       "price": "",
#       "user_id": "",
#       "expires_second": 3600,
#    }]
# }
def update_price_multi(auth, access_token, chain_id_price_dict):
    """
    @description: 批量修改价格 Batch modification of price
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param chain_id_price_dict:
    @return:
    """
    url = f"{base_url}/api/stockx/create_shipment"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
    }
    response = requests.post(url, params=params, json=chain_id_price_dict)
    return response.json()


# product_info = {
#    "product_uuid": "",
#    "price": "",
#    "expires_second": 3600,
# }
def listing_product_single(auth, access_token, product_info):
    """
    @description: 单个上架商品 Single listing product
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param product_info:
    @return:
    """
    url = f"{base_url}/api/stockx/listing_product_single"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
    }
    response = requests.post(url, params=params, json=product_info)
    return response.json()


# product_info = {
#    "products": [{
#       "product_uuid": "",
#       "price": "",
#       "expires_second": 3600,
#    }]
# }
def listing_product_multi(auth, access_token, product_info):
    """
    @description: 批量上架商品 Batch listing product
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param product_info_list:
    @return:
    """
    url = f"{base_url}/api/stockx/listing_product_multi"
    params = {
        "token": TOKEN,
        "auth": auth,
        "access_token": access_token,
    }
    response = requests.post(url, params=params, json=product_info)
    return response.json()


def get_product_size_info_by_sku(auth, sku):
    """
    @description: 获取商品尺码信息(内部缓存数据) Get product size information（internal cache data）
    @param auth: 初始化auth接口返回的auth参数 auth parameter returned by the init_auth interface
    @param access_token: 用户登录后的access_token参数 access_token parameter after user login
    @param sku: sku
    @return:
    """
    url = f"{base_url}/api/stockx/get_product_size_info_by_sku"
    params = {
        "token": TOKEN,
        "auth": auth,
        "sku": sku,
    }
    response = requests.get(url, params=params)
    return response.json()


if __name__ == '__main__':
    print(ping())
    print(init_auth())
