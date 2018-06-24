# -*- coding: utf-8 -*-
"""
Example module that says 'Hello World!'

This demonstrates how to produce a simple custom module.
"""

from forex_python.bitcoin   import BtcConverter
from forex_python.converter import CurrencyRates

class Py3status:

    def rates(self):
        usd = CurrencyRates().get_rate('USD', 'TRY')
        eur = CurrencyRates().get_rate('EUR', 'TRY')
        btc = BtcConverter().get_latest_price('USD')

        return {
            'full_text': '$: ' + str(usd) + ' €: ' + str(eur) + ' ₿: ' + str(btc),
            'cached_until': self.py3.CACHE_FOREVER
        }
