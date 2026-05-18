import os
import psycopg2
import betfairlightweight

print("Aurora Booting...")

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)

print("Postgres Connected")

trading = betfairlightweight.APIClient(
    username=os.getenv("BETFAIR_USERNAME"),
    password=os.getenv("BETFAIR_PASSWORD"),
    app_key=os.getenv("BETFAIR_APP_KEY"),
    certs="./certs/"
)

print("Betfair Client Ready")