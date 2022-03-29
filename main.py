from fastapi import FastAPI
from  scraper import Scraper

app = FastAPI()
data = Scraper()

@app.get('/api/list')
async def read_chapter():
	return data.getChapterCount()

@app.get('/api/chapter/{c}')
async def read_item(c):
	return data.scrapedata(c)


# uvicorn main:app --reload
