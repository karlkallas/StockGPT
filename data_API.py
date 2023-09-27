from datetime import datetime
from typing import Dict
from typing import List

import yfinance as yf
import json

from yfinance import Ticker

# Basic caching mechanism to avoid querying same company many times
# ticker: Ticker
companies: Dict[str, Ticker] = {}
# ticker: datetime
company_cache_time: Dict[str, datetime] = {}


def get_info(ticker: str) -> str:  # e.g. TSLA
    company = _get_company(ticker)
    formatted_info = json.dumps(company.info, indent=4, sort_keys=True)
    return formatted_info


def get_historical_market_data(ticker: str, period: str) -> str:
    company = _get_company(ticker)
    hist = company.history(period=period)
    formatted_info = hist.to_csv()
    return formatted_info


def get_financials(ticker) -> List[Dict]:
    company = _get_company(ticker)
    income_stmt = company.income_stmt.to_csv()
    quarterly_income_stmt = company.quarterly_income_stmt.to_csv()
    balance_sheet = company.balance_sheet.to_csv()
    quarterly_balance_sheet = company.quarterly_balance_sheet.to_csv()
    cashflow = company.cashflow.to_csv()
    quarterly_cashflow = company.quarterly_cashflow.to_csv()
    return [
        # {"Income Statement": income_stmt},
        # {"Quarterly Balance Sheet": quarterly_balance_sheet},
        # {"Quarterly Income Statement": quarterly_income_stmt},
        # {"Balance Sheet": balance_sheet},
        {"Cashflow": cashflow},
        # {"Quarterly Cashflow": quarterly_cashflow},
    ]


def _get_company(ticker: str) -> Ticker:
    global companies, company_cache_time
    if companies.get(ticker) and (datetime.utcnow() - company_cache_time.get(ticker)).total_seconds() < (24 * 3600):
        return companies.get(ticker)
    company = yf.Ticker(ticker)
    companies[ticker] = company
    company_cache_time[ticker] = datetime.utcnow()
    return company
