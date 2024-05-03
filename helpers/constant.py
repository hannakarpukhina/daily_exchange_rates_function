import helpers.config as c

BASE_API_LINK = "https://api.freecurrencyapi.com/v1"
LATEST_API_LINK = f"{BASE_API_LINK}/latest?apikey={c.API_KEY}"
HISTORICAL_API_LINK = f"{BASE_API_LINK}/historical?apikey={c.API_KEY}"
DEFAULT_DATE = "2024-04-26"
