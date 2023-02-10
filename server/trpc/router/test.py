import openai 
import os 
import dotenv
import csv 
import itertools
import pinecone
import numpy as np
import json 
import pandas as pd


# import environment variables
dotenv.load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.organization=os.environ["ORG_KEY"]

pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment="us-east1-gcp")
# Replace with your Pinecone API key

# Set the endpoint URL
url = "testing2-f299968.svc.us-east1-gcp.pinecone.io"

MODEL = "text-embedding-ada-002"
res = openai.Embedding.create(
    input = [

        "What's the meaning of life?"
    ], engine=MODEL 
)
res



batch_size = 1000
def chunks(iterable, batch_size):
    iterator = iter(iterable)
    for first in iterator:
        yield itertools.chain([first], itertools.islice(iterator, batch_size - 1))

page_number = []
vector = []

import csv

import pandas as pd

def join_csvs(file1, file2, joined_file):
    df1 = pd.read_csv(file1, float_precision='round_trip')
    df2 = pd.read_csv(file2, float_precision='round_trip')
    
    df1 = df1.rename(columns={'title': 'page'})
    df2 = df2.rename(columns={'title': 'page'})
    
    joined_df = pd.merge(df1, df2, on='page')
    joined_df.to_csv(joined_file, float_format="%.34f")

join_csvs('book.pdf.pages.csv', 'book.pdf.embeddings.csv', 'joined.csv')








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

index = pinecone.Index('testing2')

index.describe_index_stats

# TODO: Put this code into a function.
# def chunks(iterable, batch_size=100):
#     """A helper function to break an iterable into chunks of size batch_size."""
#     it = iter(iterable)
#     chunk = tuple(itertools.islice(it, batch_size))
#     while chunk:
#         yield chunk
#         chunk = tuple(itertools.islice(it, batch_size))

# # Load the JSON data
# with open('data.json') as f:
#     data = json.load(f)

# # Get the list of vectors from the JSON data
# vectors = [(vector['id'], vector['values']) for vector in data['vectors']]

# # Upsert data with 100 vectors per upsert request
# for ids_vectors_chunk in chunks(vectors, batch_size=100):
#     index.upsert(vectors=ids_vectors_chunk)  # Assuming `index` defined elsewhere








#TODO: Learn to query the vector database
#TODO: Implement two functinons (convert the csv into the vector json format ) (attempt to upload on pinecone to see the vector dimensions) AND chunk upload the vectors into the database)



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
# # https://www.youtube.com/watch?v=HjeW6ed2dmI

# # Connect to pinecone Index 

# vector = np.zeros(1024)

# index = pinecone.Index('testing2')

# index.upsert(vectors=zip(['a'], [5]))





