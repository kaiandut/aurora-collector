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

crt_file = tempfile.NamedTemporaryFile(delete=False, suffix=".crt")
key_file = tempfile.NamedTemporaryFile(delete=False, suffix=".key")

crt_file.write(crt_data.encode())
key_file.write(key_data.encode())

crt_file.close()
key_file.close()

# =========================
# BETFAIR CLIENT
# =========================

trading = betfairlightweight.APIClient(
    username=os.getenv("BETFAIR_USERNAME"),
    password=os.getenv("BETFAIR_PASSWORD"),
    app_key=os.getenv("BETFAIR_APP_KEY"),
    certs=tempfile.gettempdir()
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
# BETFAIR LOGIN TEST
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