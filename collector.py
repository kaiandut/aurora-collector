import os
import tempfile

from fastapi import FastAPI
import betfairlightweight

app = FastAPI()

# =========================
# WRITE CERT FILES
# =========================

crt_data = os.getenv("BETFAIR_CERT_CRT")
key_data = os.getenv("BETFAIR_CERT_KEY")

crt_path = "/tmp/client-2048.crt"
key_path = "/tmp/client-2048.key"

with open(crt_path, "w") as f:
    f.write(crt_data)

with open(key_path, "w") as f:
    f.write(key_data)

# =========================
# BETFAIR CLIENT
# =========================

trading = betfairlightweight.APIClient(
    username=os.getenv("BETFAIR_USERNAME"),
    password=os.getenv("BETFAIR_PASSWORD"),
    app_key=os.getenv("BETFAIR_APP_KEY"),
    certs="/tmp"
)

# =========================
# ROOT
# =========================

@app.get("/")
def home():
    return {"status": "Aurora API Online"}

# =========================
# HEALTH
# =========================

@app.get("/health")
def health():
    return {"status": "healthy"}

# =========================
# LOGIN TEST
# =========================

@app.get("/login")
def login():

    try:

        trading.login()

        return {
            "success": True,
            "session_token": trading.session_token
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }