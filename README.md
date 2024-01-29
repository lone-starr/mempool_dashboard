# Mempool Charts
This repository builds a basic dashboard using data saved from the [Mempool.space REST API](https://mempool.space/docs/api/rest). This data is persisted to a MongoDB instance by the [mempool_api repo](https://github.com/lone-starr/mempool_api) 
hosted on [Railway](https://railway.app) and invoked every 5 minutes by a CRON job in Railway.

## Setting Up
Clone the Repository:
```bash
git clone https://github.com/lone-starr/mempool_dashboard.git
```
```bash
cd mempool_dashboard
```

## Create a fresh Python virtual environment
```bash
python3 -m venv ./venv
```

## Select Python interpretor (Visual Studio Code)
Open VS Code from the mempool_dashboard directory:
```bash
code .
```
In VS Code press < Ctrl >< Shift >< p >, type Python and choose 'Python: Select Interpretor', choose the newly created venv for mempool_dashboard


## Install Dependencies
Open a new Terminal in VS Code and use the following command to install the required dependencies. Your Python venv should be indicated in your terminal shell.
```bash
pip install -r requirements.txt
```

## Environment Variables
Create a .env file with the necessary credentials and API keys for your MongoDB instance. You can create a free cluster to host your collection at https://cloud.mongodb.com/ or create a MongoDB instance on Railway.

## Run locally
Run the Streamlit App:
```bash
streamlit run Home.py
```
