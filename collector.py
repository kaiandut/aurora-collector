import os
import psycopg2
import betfairlightweight

print("Aurora Booting...")

conn = psycopg2.connect(
    host=os.getenv("PGHOST"),
    port=os.getenv("PGPORT"),
    dbname=os.getenv("PGDATABASE"),
    user=os.getenv("PGUSER"),
    password=os.getenv("PGPASSWORD")
)

print("Postgres Connected")

trading = betfairlightweight.APIClient(
    username=os.getenv("BF_USERNAME"),
    password=os.getenv("BF_PASSWORD"),
    app_key=os.getenv("BF_APP_KEY"),
    certs="./certs/"
)

print("Betfair Client Ready")