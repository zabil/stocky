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
