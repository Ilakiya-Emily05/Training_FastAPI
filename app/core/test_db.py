from app.core.database import engine

try:
    with engine.connect():
        print("PostgreSQL connection successful")
except Exception as e:
    print("Connection failed:", e)