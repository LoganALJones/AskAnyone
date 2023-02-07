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


page_number = []
vector = []

batch_size = 1000

def chunks(iterable, batch_size):
    iterator = iter(iterable)
    for first in iterator:
        yield itertools.chain([first], itertools.islice(iterator, batch_size - 1))

MODEL = "text-embedding-ada-002"





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
        
        # Iterate through each row in the csv file
        for row in reader:
            # Append the page number to the page_number array
            page_number.append(int(row[0].split(" ")[1]))
            # Append the content to the vector array
            vector.append(row[1])





