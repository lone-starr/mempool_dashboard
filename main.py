import os
import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import json

load_dotenv(".env")

MONGO_URI = os.environ.get('MONGO_URI')

st.title("Bitcoin Mempool Dashboard")

st.write("Mempool transaction count and hash rate over time")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client['mempool']
collection = db['blockheight']
fields_to_include = {"_id": 0, "count": 1, "ts": 1, "hashrate": 1}
result = collection.find({"height": {"$gt": 827042}}, fields_to_include)
# result = collection.find('', fields_to_include)
st.line_chart(result, x="ts", y=["count", "hashrate"])

st.write("Minimum fees over time")

fields_to_include = {"_id": 0, "ts": 1, "minimumFee": 1}
result = collection.find({"height": {"$gt": 827042}}, fields_to_include)
st.line_chart(result, x="ts", y="minimumFee")

mongo_client.close()
