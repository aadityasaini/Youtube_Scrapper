from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import *

Description = f"""
Web Scraping BootCamp

"""

app = FastAPI(title="Web Sraping Bootcamp",description=Description)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

scrape_tool = Scrape()

@app.get("/Get_Data",tags=["Scraping_Endpoint"])
async def Get_Data(Query: str, Sort:Optional[bool]=False):
    return scrape_tool.data(Query,Sort)
    
