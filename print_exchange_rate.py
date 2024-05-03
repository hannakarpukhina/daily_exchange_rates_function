from helpers.format_validation_helper import FormatValidationHelper
from helpers.exchange_rate_helper import ExchangeRateHelper


if __name__ == "__main__":

    
    exchange_rates = ExchangeRateHelper()
    valid_param = FormatValidationHelper()

    while True:       
        try:
            input_date = input("Enter Exchange Rate Date: ")
            exchange_rate_date = valid_param.validate_date_format(input_date) 
            print(exchange_rates.get_exchange_rate(exchange_rate_date))
            break
        except:
            print("Date format is not corect, please provide correct date")
        

    
