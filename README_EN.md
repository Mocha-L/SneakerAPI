# SneakerAPI

English | [中文版](./README.md)

SneakerAPI is a project that provides remote HTTP access to the Goat API, alias API, and StockX API. It supports all interfaces of these three platforms and serves as a global sneaker seller's tool, assisting in automating processes such as selling sneakers. The interfaces are actively maintained to ensure long-term availability.

For detailed information about the interfaces, please refer to the following documents.
- [StockX API documentation(Online testing interface)](http://stockxapi.spiderx.cc:61030/docs)
- [Goat/Alias API documentation(Online testing interface)](http://goatapi.spiderx.cc:61030/docs)

Python sample code can be found in the `python` directory.

## Supported Interfaces

SneakerAPI supports the following interfaces for Goat, alias, and StockX:

- Interfaces for non-login status:
  - Search for products
  - View historical sales records
  - Get product details
  - Retrieve product sizes/market prices

- Interfaces for login status:
  - Access user basic information
  - Retrieve seller information
  - Update access_token
  - Get on-sale products
  - View sold products
  - Access historical sold products
  - Retrieve order details
  - Enable/disable vacation mode
  - Remove products from sale
  - Create shipping label (StockX)
  - Modify product price (individual/batch)
  - List products for sale (individual/batch)

- Other interfaces:
  - Support additional interfaces as per your requirements

## How to Access

For access and inquiries, please reach out to:

E-Mail: mocha_lee@qq.com

Discord: Sting#3882

Discord Server: [SneakerAPI Group](https://discord.gg/zFwMS6GZYY)

Contact us to request a trial period (one week). If you have additional requirements or need further assistance, feel free to discuss them with us.

## Quotation

The fee is based on the total monthly call volume and is paid on a monthly basis.

| MonthlyCalls         | Cost（USD）                             | unit-price（USD/Req） |
| -------------------- | --------------------------------------- | --------------------- |
| <300,000             | $400                                    | 0.0013/req            |
| 300,000~2,000,000    | $800                                    | 0.0004/req            |
| 2,000,000~10,000,000 | $1600                                   | 0.00016/req           |
| >10,000,000          | Pending(Exclusive deployment resources) | <0.00016/req          |
