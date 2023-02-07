import openai 
import os 
import dotenv
import csv 
import itertools
import pinecone

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.organization=os.environ["ORG_KEY"]

dotenv.load_dotenv()
pinecone.init(api_key=os.environ["OPENAI_API_KEY"], endpoint="testing-f299968.svc.us-east1-gcp.pinecone.io")
# Replace with your Pinecone API key
api_key = os.environ.get("OPENAI_API_KEY")

# Set the endpoint URL
url = "testing-f299968.svc.us-east1-gcp.pinecone.io"

# Set the headers for the request
headers = {
    "Authorization": "Bearer " + api_key,
    "Content-Type": "application/json",
}

batch_size = 1000

def chunks(iterable, batch_size):
    iterator = iter(iterable)
    for first in iterator:
        yield itertools.chain([first], itertools.islice(iterator, batch_size - 1))

MODEL = "text-embedding-ada-002"

res = openai.Embedding.create(
    input=[
        "Sample document text goes here",
        "there will be several phrases in each batch"
    ], engine=MODEL
)
print(res)