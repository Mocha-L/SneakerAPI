# SneakerAPI

English | [中文版](./README.md)

SneakerAPI is a project that provides remote HTTP access to the Goat API, alias API, and StockX API. It supports all interfaces of these three platforms and serves as a global sneaker seller's tool, assisting in automating processes such as selling sneakers. The interfaces are actively maintained to ensure long-term availability.

For detailed information about the interfaces, please refer to the following documents.
- [StockX API documentation(Online testing interface)](http://api.spiderx.cc:61030/api/stockx/docs)
- [Goat/Alias API documentation(Online testing interface)](http://api.spiderx.cc:61030/api/alias/docs)

Python sample code can be found in the `python` directory.

## Supported Interfaces

SneakerAPI supports the following interfaces for Goat, alias, and StockX:

- Interfaces for non-login status:
  - Search products (including all filter conditions)
  - Search products by barcode
  - Product historical sales records (all sizes and specified sizes)
  - Product seller quotes (all sizes and specified sizes)
  - Product buyer bids (all sizes and specified sizes)
  - Product details
  - Product sizes/market prices
  - Product market data (including the highest price, lowest price, trading range, price fluctuations, sales volume, average price, etc., for the past 12 months)
  - Product official guidance price
  - Product historical prices

- Interfaces for login status:
  - Account login
  - User basic information
  - Seller information
  - Update access_token
  - Products for sale
  - Sold products
  - Historical sold products
  - Order details
  - Get shipping label PDF
  - Enable/disable vacation mode
  - Delist product
  - Create, delete, and get bulk shipping orders (StockX)
  - Request shipping extension
  - Cancel order
  - Download shipping label
  - Change product price (single/bulk)
  - List product (single/bulk)
  - Buyer bids

- Other interfaces:
  - Support additional interfaces as per your requirements

## How to Access

For access and inquiries, please reach out to:

E-Mail: mocha_lee@qq.com

Discord: sting_lee

Contact us to request a trial period (one week). If you have additional requirements or need further assistance, feel free to discuss them with us.

## Quotation

The fee is based on the total monthly call volume and is paid on a monthly basis.

| MonthlyCalls         | Cost（USD）                             | unit-price（USD/Req） |
| -------------------- | --------------------------------------- | --------------------- |
| <300,000             | $400                                    | 0.0013/req            |
| 300,000~2,000,000    | $800                                    | 0.0004/req            |
| 2,000,000~10,000,000 | $1600                                   | 0.00016/req           |
| >10,000,000          | Pending(Exclusive deployment resources) | <0.00016/req          |
