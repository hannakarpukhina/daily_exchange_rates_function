import requests
from datetime import date
import helpers.constant as c


class ExchangeRateHelper:

    def get_exchange_rate(self, exchange_rate_date):

        if exchange_rate_date == date.today():
            response = requests.get(c.LATEST_API_LINK)
            data = response.json().get("data")
        else:
            response = requests.get(
                f"{c.HISTORICAL_API_LINK}&date_from={exchange_rate_date}&date_to={exchange_rate_date}"
            )
            data = response.json().get("data").get(str(exchange_rate_date))

        result = {"date": str(exchange_rate_date), "data": data}
        return result
