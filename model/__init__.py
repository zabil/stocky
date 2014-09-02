__author__ = 'zabilcm'

from cqlengine import columns
from cqlengine.models import Model


class Stock(Model):
    name = columns.Text(primary_key=True)
    prices = columns.Map(columns.DateTime, columns.Float)
    events = columns.Map(columns.DateTime, columns.Text)

    def serialize(self):
        prices = [];
        for date, price in self.prices.iteritems():
            trend = {"date": date.isoformat(), "price": price}
            event = self.events.get(date)
            if event:
                trend["event"] = event
            prices.append(trend)

        return {
            'name': self.name,
            'prices': prices
        }
