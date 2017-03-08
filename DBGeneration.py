from pymongo import MongoClient
import random

client = MongoClient('localhost', 27017)
db = client['Insurance']
collection = db['Insurance']


def generate_company(size):
    if size >= 1000:
        security = random.randrange(5, 15)
        botnet = random.randrange(10, 25)
    else:
        security = random.randrange(0, 15)
        botnet = random.randrange(0, 30)
    attacks = size/100 + random.randrange(0, 10)
    company = dict()
    company.update({"size" : size, "security" : security, "botnet" : botnet, "attacks" : attacks})
    return company

def generate_market(small = 1000, medium = 500, large = 100, corporations = 10):
    companies = []
    for i in range(small):
        companies.append(generate_company(random.randrange(1, 100)))
    for i in range(medium):
        companies.append(generate_company(random.randrange(101, 1000)))
    for i in range(large):
        companies.append(generate_company(random.randrange(1001, 30000)))
    for i in range(corporations):
        companies.append(generate_company(random.randrange(30001, 100000)))
    for c in companies:
        collection.insert_one(c)