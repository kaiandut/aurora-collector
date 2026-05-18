from fastapi import FastAPI
import os
import psycopg2
import betfairlightweight

app = FastAPI()

print("Aurora Booting...")

# PostgreSQL Connection
DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)

print("Postgres Connected")

# Betfair Client
trading = betfairlightweight.APIClient(
    username=os.getenv("BETFAIR_USERNAME"),
    password=os.getenv("BETFAIR_PASSWORD"),
    app_key=os.getenv("BETFAIR_APP_KEY"),
    certs="./certs/"
)

print("Betfair Client Ready")


# ROOT ENDPOINT
@app.get("/")
def root():
    return {
        "message": "Aurora Ω Online"
    }


# HEALTH ENDPOINT
@app.get("/health")
def health():
    return {
        "status": "ok"
    }