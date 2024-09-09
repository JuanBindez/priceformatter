class Formatter:
    def __init__(self, currency_name='Real'):
        """
        Initializes the currency formatter based on the currency name.

        :param currency_name: Name of the currency, such as 'Real', 'Dollar', 'Euro', etc.
        """
        self.currency_name = currency_name
        
        # Set formatting rules automatically based on the currency name
        if currency_name == 'Real':
            self.thousand_sep = '.'
            self.decimal_sep = ','
            self.name_position = 'after'
        elif currency_name == 'Dollar':
            self.thousand_sep = ','
            self.decimal_sep = '.'
            self.name_position = 'before'
        elif currency_name == 'Euro':
            self.thousand_sep = '.'
            self.decimal_sep = ','
            self.name_position = 'after'
        else:
            # Default formatting if the currency is not recognized
            self.thousand_sep = ','
            self.decimal_sep = '.'
            self.name_position = 'before'

    def format_currency(self, value):
        """
        Formats the value as a currency using automatic settings based on the currency name.

        :param value: Numeric value to be formatted.
        :return: String formatted as currency.
        """
        formatted_value = f"{value:,.2f}".replace(',', 'X').replace('.', self.thousand_sep).replace('X', self.decimal_sep)
        
        if self.name_position == 'before':
            return f"{self.currency_name} {formatted_value}"
        else:
            return f"{formatted_value} {self.currency_name}"
