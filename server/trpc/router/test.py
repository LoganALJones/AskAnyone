import openai 
import os 
import dotenv
import csv 
import itertools
import pinecone
import numpy as np
import json 

# import environment variables
dotenv.load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.organization=os.environ["ORG_KEY"]

pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment="us-east1-gcp")
# Replace with your Pinecone API key

# Set the endpoint URL
url = "testing-f299968.svc.us-east1-gcp.pinecone.io"

MODEL = "text-embedding-ada-002"

batch_size = 1000
def chunks(iterable, batch_size):
    iterator = iter(iterable)
    for first in iterator:
        yield itertools.chain([first], itertools.islice(iterator, batch_size - 1))

page_number = []
vector = []


# def csv_embeddings_to_json(csvf_name, jsonFilePath):
#     data = {"vectors": []}
#     with open(csvf_name, 'r') as csvf:
#         csvReader = csv.DictReader(csvf)
#         for index, row in enumerate(csvReader):
#             data["vectors"].append({"id": "item_{}".format(index), "values": [float(value) for key, value in row.items() if key != "title"]})

#     with open(jsonFilePath, 'w') as jsonf:
#         jsonf.write(json.dumps(data, indent=4))


# jsonFilePath = 'data.json'
# csv_embeddings_to_json("book.pdf.embeddings.csv", jsonFilePath)


def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

vector_dim = 4096 # Dimension of each vector
vector_count = 10000

# Example generator that generates many (id, vector) pairs
example_data_generator = map(lambda i: (f'id-{i}', [random.random() for _ in range(vector_dim)]), range(vector_count))

# Upsert data with 100 vectors per upsert request
for ids_vectors_chunk in chunks(example_data_generator, batch_size=100):
    index.upsert(vectors=ids_vectors_chunk)  # Assuming `index` defined elsewhere# def csv_to_vectors(csvf_name):




#     # Open the csv csvf
#     with open(csvf_name, "r") as csvf:
#         # Create a csv reader object
#         reader = csv.reader(csvf)
        
#         # Skip the header row
#         next(reader)
#         # Initialize the page_number and vector arrays
#         page_number = []
#         vector = []
        
#         for row in reader:
#         # Iterate through each row in the csv csvf
#             # Append the page number to the page_number array
#             # Append the content to the vector array

#             page_number.append(int(row[0].split(" ")[1]))
#             vector.append(row[1])    # Print the contents of both arrays
    
#     return page_number, vector


# # pinecone.list_indexes()

# page_number, vector  = csv_to_vectors("book.pdf.pages.csv")

# # for i in range(len(page_number)):
# #     print("Page number: {}, Content: {}".format(page_number[i], vector[i]))

# # Longterm, he couldn't do it.
# # TODO: Upload vectors into pinecone (in batches using the youTuvbe video).
# # https://www.youtube.com/watch?v=HjeW6ed2dmI

# # Connect to pinecone Index 

# vector = np.zeros(1024)

# index = pinecone.Index('testing')

# index.upsert(vectors=zip(['a'], [5]))

