from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth as auth_routes

# Create DB tables (for dev; in prod, prefer Alembic)
Base.metadata.create_all(bind=engine)

#Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="NotifyIQ API")

app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to NotifyIQ API"}