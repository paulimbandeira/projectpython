from pymongo import MongoClient

dbcliente = MongoClient('mongodb+srv://paulo_roberto:Paulo12344321@cluster0.qy4tjpr.mongodb.net/?retryWrites=true&w=majority')

db = dbcliente['cadastro']
coll = db['cliente']

doc = coll.find()
for x in doc:
    print(x)

'''
query = {'bairro': 'cidade de deus'}
doc = coll.find(query)
'''

