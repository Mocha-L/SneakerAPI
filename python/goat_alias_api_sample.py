
import requests

base_url = "http://goatapi.spiderx.cc:61030"
# token 需要从作者处申请，测试可用本一周，在线测试可见http://goatapi.spiderx.cc:61030/docs
# Token needs to be applied for from the author and can be tested this week. Online testing can be seen at http://goatapi.spiderx.cc:61030/docs
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


def query_by_sku(keyword, page):
    """
    @description: 根据sku查询商品信息 Query product information by sku
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/query_by_sku"
    params = {
        "keyword": keyword,
        "page": page,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def query_by_condition(condition, page):
    """
    @description: 根据条件查询商品信息 Query product information by condition
    @param {type} condition in ['condition', 'on_sell', 'coming_soon']
    @return:
    """
    url = f"{base_url}/api/alias/query_by_condition"
    params = {
        "condition": condition,
        "page": page,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def init_auth():
    """
    @description: 初始化auth，获取auth. Init auth, get auth
    @return:
    """
    url = f"{base_url}/api/alias/init_auth"
    params = {
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def login(auth, account, password):
    """
    @description: 登录Alias Login Alias
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/login"
    params = {
        "auth": auth,
        "account": account,
        "password": password,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def self_info(auth, access_token):
    """
    @description: 获取自己的信息 Get your own information
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/self_info"
    params = {
        "auth": auth,
        "access_token": access_token,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def seller_info(auth, access_token):
    """
    @description: 获取卖家信息 Get seller information
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/seller_info"
    params = {
        "auth": auth,
        "access_token": access_token,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def update_access_token(auth, refresh_token):
    """
    @description: 更新access_token Update access_token
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/update_access_token"
    params = {
        "auth": auth,
        "refresh_token": refresh_token,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def get_product_detail(auth, access_token, slug):
    """
    @description: 获取商品详情 Get product details
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/get_product_detail"
    params = {
        "auth": auth,
        "access_token": access_token,
        "slug": slug,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def get_recent_orders(auth, access_token, slug, size_us, consigned, region_id):
    """
    @description: 查询最近销量情况 Query recent sales
    @param {type} consigned in [True, False], region_id可从self_info中获得。consigned in [True, False], region_id can be obtained from self_info.
    @return:
    """
    url = f"{base_url}/api/alias/get_recent_orders"
    params = {
        "auth": auth,
        "access_token": access_token,
        "slug": slug,
        "size_us": size_us,
        "consigned": consigned,
        "region_id": region_id,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def lowest_price(auth, access_token, slug, region_id):
    """
    @description: 查某slug的本区域最低价信息 Check the lowest price information of a slug in this area
    @param {type} region_id可从self_info中获得。region_id can be obtained from self_info.
    @return:
    """
    url = f"{base_url}/api/alias/lowest_price"
    params = {
        "auth": auth,
        "access_token": access_token,
        "slug": slug,
        "region_id": region_id,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def get_selling_info(auth, access_token):
    """
    @description: 获取商品的在售信息 Get the selling information of the product
    @param {type}
    @return:在售情况。返回整体计数信息。Selling situation. Return overall count information.
    """
    url = f"{base_url}/api/alias/get_selling_info"
    params = {
        "auth": auth,
        "access_token": access_token,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def get_sold_info(auth, access_token):
    """
    @description: 获取商品的已售信息 Get the sold information of the product
    @param {type}
    @return: 已售情况。返回整体计数信息。Sold information. Return overall count information.
    """
    url = f"{base_url}/api/alias/get_sold_info"
    params = {
        "auth": auth,
        "access_token": access_token,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def get_selling_products(auth, access_token, page, query):
    """
    @description: 获取在售商品列表 Get the list of products on sale
    @param {type}
    @return: 在售商品列表。返回商品列表。On sale product list. Return the list of products.
    """
    url = f"{base_url}/api/alias/get_selling_products"
    params = {
        "auth": auth,
        "access_token": access_token,
        "page": page,
        "query": query,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def get_sold_products(auth, access_token, page):
    """
    @description: 获取已售商品列表 Get the list of sold products
    @param {type}
    @return: 已售商品列表。返回商品列表。Sold product list. Return the list of products.
    """
    url = f"{base_url}/api/alias/get_sold_products"
    params = {
        "auth": auth,
        "access_token": access_token,
        "page": page,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def get_history_products(auth, access_token, page):
    """
    @description: 获取历史已售商品 Get the list of historical sold products
    @param {type}
    @return: 历史商品列表。返回商品列表。Historical sold product list. Return the list of products.
    """
    url = f"{base_url}/api/alias/get_history_products"
    params = {
        "auth": auth,
        "access_token": access_token,
        "page": page,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def get_sold_products_detail(auth, access_token, order_number):
    """
    @description: 获取已售商品详情 Get the detail of sold products
    @param {type}
    @return: 已售商品详情。返回商品详情。Detail of sold products. Return the detail of products.
    """
    url = f"{base_url}/api/alias/get_sold_products_detail"
    params = {
        "auth": auth,
        "access_token": access_token,
        "order_number": order_number,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def enable_vacation_mode(auth, access_token):
    """
    @description: 开启假期模式 Enable vacation mode
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/enable_vacation_mode"
    params = {
        "auth": auth,
        "access_token": access_token,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


def cancel_product(auth, access_token, product_id):
    """
    @description: 下架商品 Cancel product
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/cancel_product"
    params = {
        "auth": auth,
        "access_token": access_token,
        "product_id": product_id,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()


# product_id_price_dict = {
#     "product_id": ""
#     "price_cents": 12300         -> $123
# }
def update_price_single(auth, access_token, product_id_price_dict):
    """
    @description: 单个商品改价 Single product price change
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/update_price_single"
    params = {
        "auth": auth,
        "access_token": access_token,
        "token": TOKEN
    }
    response = requests.post(url, params=params, json=product_id_price_dict)
    return response.json()


# product_info = {
#     "sku": "",
#     "product_slug": "",
#     "price_cents": 12300      -> $123
#     "size_us": 4.5
# }
def listing_product_single_step1(auth, access_token, product_info):
    """
    @description: 单个商品上架第一步 Single product listing step 1
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/listing_product_single_step1"
    params = {
        "auth": auth,
        "access_token": access_token,
        "token": TOKEN
    }
    response = requests.post(url, params=params, json=product_info)
    return response.json()


def listing_product_single_step2(auth, access_token, product_id):
    """
    @description: 单个商品上架第二步 Single product listing step 2
    @param {type} product_id: listing_product_single_step1返回的product_id
    @return:
    """
    url = f"{base_url}/api/alias/listing_product_single_step2"
    params = {
        "auth": auth,
        "access_token": access_token,
        "product_id": product_id,
        "token": TOKEN
    }
    response = requests.post(url, params=params)
    return response.json()


# product_id_price_list = {
#     "products" :[{
#         "sku": "",
#         "product_slug": "",
#         "price_cents": 12300      -> $123
#         "size_us": 4.5
#     }]
#}
def listing_product_multi(auth, access_token, product_id_price_list):
    """
    @description: 多个商品上架 Multi product listing
    @param {type}
    @return:
    """
    url = f"{base_url}/api/alias/listing_product_multi"
    params = {
        "auth": auth,
        "access_token": access_token,
        "token": TOKEN
    }
    response = requests.post(url, params=params, json=product_id_price_list)
    return response.json()


if __name__ == '__main__':
    print(ping())
    print(query_by_sku("FW2499", 0))
    print(query_by_condition("popular", 0))

