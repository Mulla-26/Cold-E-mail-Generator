import chromadb

client=chromadb.Client()
collection = client.create_collection(name="my_db")

collection.add(
    documents=[
            "The topic is about Cottbus"
            "The topic is about Coimbatore"
    ],
    ids = ['id1', 'id2']

)

all_docs = collection.get()

print(all_docs)