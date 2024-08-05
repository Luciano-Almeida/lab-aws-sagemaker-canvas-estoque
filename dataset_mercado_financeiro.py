import yfinance as yf
from datetime import datetime, timedelta

def get_stock_data(ticker):
    try:
        # Define the date range for the past year
        end_date = datetime.now()
        start_date = end_date - timedelta(days=800)
        
        # Download data for the given ticker with daily interval
        stock = yf.Ticker(ticker)
        stock_data = stock.history(start=start_date, end=end_date, interval="1d")
        
        # Check if data is empty, which might indicate the ticker is delisted
        if stock_data.empty:
            print(f"Nenhum dado encontrado para a ação {ticker}. Ela pode ter sido removida da listagem.")
            return None
        
        # Reset the index to get the default integer index
        stock_data.reset_index(inplace=True)
        
        # Add an ID column
        stock_data['ID'] = stock_data.index + 1
        
        # Display the first few rows of the data
        print(stock_data.head())
        
        return stock_data
    except Exception as e:
        print(f"Erro ao obter dados para a ação {ticker}: {e}")
        return None

if __name__ == "__main__":
    ticker = input("Digite o símbolo da ação (ticker): ")
    data = get_stock_data(ticker)
    if data is not None:
        # Save data to a CSV file
        data.to_csv(f"{ticker}_data.csv", index=False)
        print(f"Os dados foram salvos em {ticker}_data.csv")
