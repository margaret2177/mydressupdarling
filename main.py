from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from  scraper import Scraper

app = FastAPI()
data = Scraper()

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    "",
    "https://floating-spire-08257.herokuapp.com",
    "http://localhost:3000"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
async def read_root():
	return 'Hello there!'

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
