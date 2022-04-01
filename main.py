from fastapi import FastAPI
from  scraper import Scraper

app = FastAPI()
data = Scraper()

@app.get('/api/home')
async def read_home():
	return data.getHome()

@app.get('/api/list/{url}')
async def read_chapter(url):
	return data.getChapterCount(url)

@app.get('/api/{u}/chapter/{c}')
async def read_item(u,c):
	
	return data.scrapedata(u,c)


# uvicorn main:app --reload
