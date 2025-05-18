import enum
from typing import NamedTuple

class ConnectionURLS(NamedTuple):
    api_endpoint: str
    user_hub: str
    market_hub: str

class Environment(enum.Enum):
    ALPHA_TICKS = ConnectionURLS(
        api_endpoint="https://api.alphaticks.projectx.com",
        user_hub="https://rtc.alphaticks.projectx.com/hubs/user",
        market_hub="https://rtc.alphaticks.projectx.com/hubs/market"
    )
    BLUE_GUARDIAN = ConnectionURLS(
        api_endpoint="https://api.blueguardianfutures.projectx.com",
        user_hub="https://rtc.blueguardianfutures.projectx.com/hubs/user",
        market_hub="https://rtc.blueguardianfutures.projectx.com/hubs/market"
    )
    BLUSKY = ConnectionURLS(
        api_endpoint="https://api.blusky.projectx.com",
        user_hub="https://rtc.blusky.projectx.com/hubs/user",
        market_hub="https://rtc.blusky.projectx.com/hubs/market"
    )
    E8X = ConnectionURLS(
        api_endpoint="https://api.e8.projectx.com",
        user_hub="https://rtc.e8.projectx.com/hubs/user",
        market_hub="https://rtc.e8.projectx.com/hubs/market"
    )
    FUNDING_FUTURES = ConnectionURLS(
        api_endpoint="https://api.fundingfutures.projectx.com",
        user_hub="https://rtc.fundingfutures.projectx.com/hubs/user",
        market_hub="https://rtc.fundingfutures.projectx.com/hubs/market"
    )
    THE_FUTURES_DESK = ConnectionURLS(
        api_endpoint="https://api.thefuturesdesk.projectx.com",
        user_hub="https://rtc.thefuturesdesk.projectx.com/hubs/user",
        market_hub="https://rtc.thefuturesdesk.projectx.com/hubs/market"
    )
    FUTURES_ELITE = ConnectionURLS(
        api_endpoint="https://api.futureselite.projectx.com",
        user_hub="https://rtc.futureselite.projectx.com/hubs/user",
        market_hub="https://rtc.futureselite.projectx.com/hubs/market"
    )
    FXIFY_FUTURES = ConnectionURLS(
        api_endpoint="https://api.fxifyfutures.projectx.com",
        user_hub="https://rtc.fxifyfutures.projectx.com/hubs/user",
        market_hub="https://rtc.fxifyfutures.projectx.com/hubs/market"
    )
    GOAT_FUNDED = ConnectionURLS(
        api_endpoint="https://api.goatfundedfutures.projectx.com",
        user_hub="https://rtc.goatfundedfutures.projectx.com/hubs/user",
        market_hub="https://rtc.goatfundedfutures.projectx.com/hubs/market"
    )
    TICK_TICK_TRADER = ConnectionURLS(
        api_endpoint="https://api.tickticktrader.projectx.com",
        user_hub="https://rtc.tickticktrader.projectx.com/hubs/user",
        market_hub="https://rtc.tickticktrader.projectx.com/hubs/market"
    )
    TOP_ONE_FUTURES = ConnectionURLS(
        api_endpoint="https://api.toponefutures.projectx.com",
        user_hub="https://rtc.toponefutures.projectx.com/hubs/user",
        market_hub="https://rtc.toponefutures.projectx.com/hubs/market"
    )
    TOPSTEP_X = ConnectionURLS(
        api_endpoint="https://api.topstepx.projectx.com",
        user_hub="https://rtc.topstepx.projectx.com/hubs/user",
        market_hub="https://rtc.topstepx.projectx.com/hubs/market"
    )
    TX3_FUNDING = ConnectionURLS(
        api_endpoint="https://api.tx3funding.projectx.com",
        user_hub="https://rtc.tx3funding.projectx.com/hubs/user",
        market_hub="https://rtc.tx3funding.projectx.com/hubs/market"
    )


class OrderSide(enum.IntEnum):
    BUY = 0
    SELL = 1


class OrderType(enum.IntEnum):
    LIMIT = 1
    MARKET = 2
    STOP = 4
    TRAILING_STOP = 5
    JOIN_BID = 6
    JOIN_ASK = 7


class OrderStatus(enum.IntEnum):
    OPEN = 1
    FILLED = 2
    CANCELLED = 3
    EXPIRED = 4
    REJECTED = 5
    PENDING = 6


class PositionType(enum.IntEnum):
    LONG = 1
    SHORT = 2


class AggregationUnit(enum.IntEnum):
    SECOND = 1
    MINUTE = 2
    HOUR = 3
    DAY = 4
    WEEK = 5
    MONTH = 6
