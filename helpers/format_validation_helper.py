from datetime import datetime

class FormatValidationHelper:
    def validate_date_format(self, exchange_rate_date):
        try:
            return datetime.strptime(exchange_rate_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date format is not corect, please provide correct date")
