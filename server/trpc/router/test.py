import openai 
import os 
import dotenv
import csv 
import itertools
import pinecone

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

def csv_to_vectors(file_name):
    # Open the csv file
    with open(file_name, "r") as file:
        # Create a csv reader object
        reader = csv.reader(file)
        
        # Skip the header row
        next(reader)
        # Initialize the page_number and vector arrays
        page_number = []
        vector = []
        
        for row in reader:
        # Iterate through each row in the csv file
            # Append the page number to the page_number array
            # Append the content to the vector array

            page_number.append(int(row[0].split(" ")[1]))
            vector.append(row[1])    # Print the contents of both arrays
    
    return page_number, vector


# pinecone.list_indexes()

page_number, vector  = csv_to_vectors("book.pdf.pages.csv")


for i in range(len(page_number)):
    print("Page number: {}, Content: {}".format(page_number[i], vector[i]))

# Longterm, he couldn't do it.
# TODO: Upload vectors into pinecone (in batches using the youTuvbe video).
# https://www.youtube.com/watch?v=HjeW6ed2dmI


