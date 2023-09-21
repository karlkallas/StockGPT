import yfinance as yf
import json

def get_info(ticker): # e.g. TSLA
    company = yf.Ticker(ticker)
    formatted_info = json.dumps(company.info, indent=4, sort_keys=True)
    return formatted_info


def get_historical_market_data(ticker, period): # e.g. TSLA
    company = yf.Ticker(ticker)
    hist = company.history(period=period)
    formatted_info = hist.to_csv()
    return formatted_info


def get_financials(ticker): # e.g. TSLA
    company = yf.Ticker(ticker)
    income_stmt = company.income_stmt.to_csv()
    quarterly_income_stmt = company.quarterly_income_stmt.to_csv()
    balance_sheet = company.balance_sheet.to_csv()
    quarterly_balance_sheet = company.quarterly_balance_sheet.to_csv()
    cashflow = company.cashflow.to_csv()
    quarterly_cashflow = company.quarterly_cashflow.to_csv()
    return [{"Income Statement" : income_stmt},
            {"Quarterly Balance Sheet" : quarterly_balance_sheet}, 
            {"Quarterly Income Statement" : quarterly_income_stmt}, 
            {"Balance Sheet" : balance_sheet}, 
            {"Cashflow" : cashflow}, 
            {"Quarterly Cashflow" : quarterly_cashflow}]