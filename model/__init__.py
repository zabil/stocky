__author__ = 'zabilcm'

from cqlengine import columns
from cqlengine.models import Model


class Stock(Model):
    name = columns.Text(primary_key=True)
    prices = columns.Map(columns.DateTime, columns.Float)

    def serialize(self):
        return {
            'name': self.name,
            'prices': [dict({"date": date.isoformat(), "price": price}) for date, price in self.prices.iteritems()]
        }
