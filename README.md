# projectx-api

[![PyPI - Version](https://img.shields.io/pypi/v/projectx-api)](https://pypi.org/project/projectx-api/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/projectx-api)](https://pypistats.org/packages/projectx-api)

`projectx-api` is an async Python SDK for the [ProjectX Gateway API](https://gateway.docs.projectx.com/). It allows programmatic access to accounts, orders, positions, market data, and more.

---

## 📦 Installation

```
pip install projectx-api
```

## 🚀 Features

- ✅ Async HTTP client powered by httpx
- ✅ Supports [all endpoints described in the documentation](https://gateway.docs.projectx.com/docs/intro)
- ✅ Supports both API key and application-based authentication
- ✅ Automatic session revalidation (24h token auto-refresh)
- 🚧 WebSocket support (Realtime Updates) coming soon

## 🔧 Usage Example

```python
import asyncio
from projectx_api import ProjectXClient, Environment, LoginKeyCredentials, OrderSide, OrderType

async def main():
    client = ProjectXClient(Environment.TOPSTEP_X)
    await client.login(
        LoginKeyCredentials(userName="test", apiKey="test")
    )
    
    accounts = await client.search_for_account()
    print("Accounts:", accounts)
    accountId = accounts[0]["id"]
    
    orders = await client.search_for_open_orders(accountId=accountId)
    print("Open orders:", orders)
    
    positions = await client.search_for_positions(accountId=accountId)
    print("Positions:", positions)
    
    contracts = await client.search_for_contracts(searchText="NQ", live=True)
    print("Contracts:", contracts)
    contractId = contracts[0]["id"]
    
    result = await client.place_order(
        accountId=accountId,
        contractId=contractId,
        type=OrderType.LIMIT,
        side=OrderSide.BUY,
        size=1,
        limitPrice=2000,
    )
    print("Place Order", result)
    orderId = result["orderId"]
    
    result = await client.cancel_order(accountId=accountId, orderId=orderId)
    print("Cancel Order", result)
    
    await client.logout()

asyncio.run(main())
```

## 🌍 Supported Environments

[You can see the supported environments here](https://github.com/rundef/projectx-api/blob/main/projectx_api/enums.py)

## 📄 License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for details.
