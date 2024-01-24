import os
import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import json
from datetime import datetime

load_dotenv(".env")

MONGO_URI = os.environ.get('MONGO_URI')

st.title("Bitcoin Mempool Dashboard")

st.write("Mempool Transaction Count and Hash Rate over time")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client['mempool']
collection = db['blockheight']
fields_to_include = {"_id": 0, "count": 1, "ts": 1, "hashrate": 1}
result = collection.find({"height": {"$gt": 827042}}, fields_to_include)
# result = collection.find('', fields_to_include)
st.line_chart(result, x="ts", y=["count", "hashrate"])

st.write("Fastest and Minimum fees over time")

fields_to_include = {"_id": 0, "ts": 1, "minimumFee": 1, "fastestFee": 1}
result = collection.find({"ts": {"$gt": datetime.fromisoformat(
    '2024-01-24T18:20:21.764+00:00')}}, fields_to_include)
st.line_chart(result, x="ts", y=["minimumFee", "fastestFee"])

mongo_client.close()
