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
result = collection.find({"ts": {"$gt": datetime.fromisoformat(
    '2024-01-24T18:20:21.764+00:00')}},   {
    "_id": 0,
    "time": {
        "$dateAdd": {
            "startDate": "$ts",
            "unit": "hour",
            "amount": -5
        }},
    "mempool size": {"$divide": ["$vsize", 1000]}, "tx count": "$count", "vsize": 1, "hashrate": 1
})
st.line_chart(result, x="time", y=["tx count", "mempool size", "hashrate"])

st.write("Fastest and Minimum fees over time")

result = collection.find({"ts": {"$gt": datetime.fromisoformat(
    '2024-01-24T18:20:21.764+00:00')}},   {
    "_id": 0,
    "time": {
        "$dateAdd": {
            "startDate": "$ts",
            "unit": "hour",
            "amount": -5
        }
    }, "min fee": "$minimumFee", "fast fee": "$fastestFee", "hour fee": "$hourFee"
})

st.line_chart(result, x="time", y=["min fee", "fast fee", "hour fee"])

st.write("Bitcoin conversion rate in major currencies")

result = collection.find({"ts": {"$gte": datetime.fromisoformat(
    '2024-02-05T22:29:27.182+00:00')}},   {
    "_id": 0,
    "time": {
        "$dateAdd": {
            "startDate": "$ts",
            "unit": "hour",
            "amount": -5
        }
    }, "USD": "$priceUSD", "EUR": "$priceEUR", "GBP": "$priceGBP", "CAD": "$priceCAD"
})

st.line_chart(result, x="time", y=["USD", "EUR", "GBP", "CAD"])

mongo_client.close()
