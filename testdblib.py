import pymongo
import datetime

def db_insert(employee, company, job, twitter, tags):
    employee = employee
    company = company
    twitter = twitter
    tags = []
    record = {"employee": employee,
              "company": company,
              "job": job,
              "twitter": twitter,
              "tags": tags,
              "date": datetime.datetime.utcnow()}


    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.testdb
    collection = db.testdb_collection
    collection.insert_one(record).inserted_id


def db_find_by_name(name):
    name = name

    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.testdb
    collection = db.testdb_collection
    record = collection.find_one({"name": name})
    return record


def db_find_by_company(company):
    company = company

    client = MongoClient('mongodb://localhost:27017/')
    db = client.testdb
    collection = db.testdb_collection
    record = collection.find_one({"company": company})
    return record


def db_find_by_twitter(twitter):
    twitter = twitter

    client = MongoClient('mongodb://localhost:27017/')
    db = client.testdb
    collection = db.testdb_collection
    record = collection.find_one({"twitter": twitter})
    return record
