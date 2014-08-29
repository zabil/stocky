__author__ = 'zabilcm'

from model import Stock
import datetime


def run():
    from cqlengine import connection

    connection.setup(['127.0.0.1'], "cqlengine")

    from cqlengine import management

    management.drop_table(Stock)
    management.sync_table(Stock)

    Stock.create(name="WPRO", prices={
        datetime.date(2014, 12, 1): 200
        , datetime.date(2014, 12, 2): 220.45
        , datetime.date(2014, 12, 3): 250.67
        , datetime.date(2014, 12, 4): 246.86
        , datetime.date(2014, 12, 5): 201
        , datetime.date(2014, 12, 6): 233
        , datetime.date(2014, 12, 7): 245
        , datetime.date(2014, 12, 8): 300
        , datetime.date(2014, 12, 9): 307
        , datetime.date(2014, 12, 10): 180
        , datetime.date(2014, 12, 11): 405
        , datetime.date(2014, 12, 12): 400
        , datetime.date(2014, 12, 13): 670
        , datetime.date(2014, 12, 14): 260
        , datetime.date(2014, 12, 15): 250
        , datetime.date(2014, 12, 16): 251
        , datetime.date(2014, 12, 17): 254
        , datetime.date(2014, 12, 18): 267
        , datetime.date(2014, 12, 19): 270
    })

    Stock.create(name="INFY", prices={
        datetime.date(2014, 8, 1): 3200
        , datetime.date(2014, 8, 2): 3220.45
        , datetime.date(2014, 8, 3): 3250.67
        , datetime.date(2014, 8, 4): 3246.86
        , datetime.date(2014, 8, 5): 3201
        , datetime.date(2014, 8, 6): 3233
        , datetime.date(2014, 8, 7): 3245
        , datetime.date(2014, 8, 8): 3300
        , datetime.date(2014, 8, 9): 3307
        , datetime.date(2014, 8, 10): 3180
        , datetime.date(2014, 8, 11): 3405
        , datetime.date(2014, 8, 12): 3400
        , datetime.date(2014, 8, 13): 3670
        , datetime.date(2014, 8, 14): 3260
        , datetime.date(2014, 8, 15): 3250
        , datetime.date(2014, 8, 16): 3251
        , datetime.date(2014, 8, 17): 3254
        , datetime.date(2014, 8, 18): 3267
        , datetime.date(2014, 8, 19): 3270
    })
