from contextlib import asynccontextmanager

from fastapi import FastAPI
from dotenv import load_dotenv
from api.routes.google_form  import router as form_router
from bot.bot import init_telegram_bot, stop_telegram_bot

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_telegram_bot()
    yield
    await stop_telegram_bot()
    
app = FastAPI(lifespan=lifespan)

app.include_router(form_router, prefix="/webhooks")


@app.get("/")
def root():
    return {"status": "ok"}