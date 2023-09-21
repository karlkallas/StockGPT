from opencopilot import OpenCopilot
from news_API import get_news
from data_API import get_info, get_historical_market_data, get_financials
from typing import List
from langchain.schema import Document
from opencopilot import OpenCopilot

copilot = OpenCopilot( 
    copilot_name="Stock Analyst Copilot",
    llm="gpt-4",
    prompt_file="prompt.txt"
    )

# Hardcoded to Tesla at the moment
# TODO: Parse company name from input message - use name & generate ticker for API calls

@copilot.data_loader
def load_news() -> List[Document]:
    news = get_news("Tesla")
    documents: List[Document] = []
    for n in news:        
        scraped_document = Document(page_content=n["content"], 
                                    metadata={"source": n["url"],
                                              "title": n["title"], 
                                              "description": n["description"],
                                              "image_url": n["urlToImage"],
                                              "time_published": n["publishedAt"]
                                              })
        documents.append(scraped_document)
    return documents

@copilot.data_loader
def load_info() -> List[Document]:
    info = get_info("TSLA")
    documents: List[Document] = []     
    scraped_document = Document(page_content=info, metadata={"source": "https://finance.yahoo.com/quote/TSLA"})
    documents.append(scraped_document)
    return documents

@copilot.data_loader
def load_historical_market_data() -> List[Document]:
    historical_market_data = get_historical_market_data("TSLA", "1mo") # ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    documents: List[Document] = []     
    scraped_document = Document(page_content=historical_market_data, 
                                metadata={"source": "https://finance.yahoo.com/quote/TSLA", 
                                          "title": "Historical Market Data for TSLA"})
    documents.append(scraped_document)
    return documents

@copilot.data_loader
def load_financial_data() -> List[Document]:
    financial_data = get_financials("TSLA")
    documents: List[Document] = []     
    for f in financial_data:
        for key, value in f.items():       
            scraped_document = Document(page_content=value, 
                                        metadata={"source": "https://finance.yahoo.com/quote/TSLA", "title": key})
            documents.append(scraped_document)
    return documents


copilot()