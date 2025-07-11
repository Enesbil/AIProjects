import pymongo
from sentence_transformers import SentenceTransformer

client = pymongo.MongoClient("your cluster url")
db = client.sample_mflix
collection = db.movies


hf_token = "insert your huggingface token here. you could also swap it for openai but would need to modify the generate_embedding function"

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_embedding(text: str) -> list[float]:
    embedding = model.encode(text)
    return embedding.tolist()


"""
Run this once to modify the MongoDB collection to add encoded embeddings for the first 50 movies
for doc in collection.find({'plot':{"$exists": True}}).limit(50):
   doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
   collection.replace_one({'_id': doc['_id']}, doc)"""


query = "A soldier fighting in world war 2"

results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding_hf",
    "numCandidates": 50, #because we only encoded the first 50 movies
    "limit": 4,
    "index": "plot_semantic_search",
      }}
]);

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')