# -*- coding: UTF-8 -*-
from pymongo import *
import json,sys

def mongo_get(hosts):
    client = MongoClient(hosts, 27017)
    dbs = client.database_names()
    for db in dbs:
        mydb = client[db]
        cols = mydb.collection_names()
        for col in cols:

            book = mydb[col]
            print '---------------------------------------------------------------------'
            print 'DB:'+db+'----'+'Collections:'+col
            cont = str(book.find_one())
            print cont.decode('unicode_escape')
            print 'Number:'+str(book.find().count())
mongo_get(sys.argv[1])