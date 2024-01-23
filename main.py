import os
import streamlit as st
from pymongo import MongoClient
from dotenv import load_dotenv
import json

load_dotenv(".env")

MONGO_URI = os.environ.get('MONGO_URI')

st.title("Bitcoin Mempool Dashboard")

st.write("Mempool size and hash rate over time")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client['mempool']
collection = db['blockheight']
fields_to_include = {"_id": 0, "count": 1, "vsize": 1, "ts": 1}
result = collection.find({"height": {"$gt": 827023}}, fields_to_include)
st.line_chart(result, x="ts", y=["count", "vsize"])

mongo_client.close()
