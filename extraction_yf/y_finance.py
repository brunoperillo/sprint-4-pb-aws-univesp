
import pandas as pd
import yfinance as yf
from datetime import date
import warnings
warnings.simplefilter(action='ignore',category=FutureWarning)

def extraction_yahoo_finance():

    ticketb3 = pd.read_csv('marketstack-brazil-20.csv')

    ticketb3['yf_symbol'] = ticketb3['id'] + '.SA'
    
    dstart = date.today()
    dstart = dstart.strftime('%Y-%m-%d')
   
    df = pd.DataFrame([])
    for x in range(len(ticketb3)):
        shares = ticketb3.loc[x][0]
        company = ticketb3.loc[x][1]
        tickets_symbol = ticketb3.loc[x][2]
        data = yf.download(tickets_symbol,start=dstart)
        data['Symbol'] = shares
        data['Company'] = company
        #data['Id'] = data['Date'].astype(str)
        df = df.append(data)
    
    df = df.reset_index()
    #df = df[['Date','Open','Close','Symbol','Company']]
    df['Date'] = pd.to_datetime(df['Date'])
    df['Open'] = df['Open'].round(2)
    df['Close'] = df['Close'].round(2)
    df['Id'] = df['Date'].astype(str) + df['Symbol']
    df['Id'] = df['Id'].apply(lambda x: x.replace('-',''))
    df = df[['Id','Date','Open','Close','Symbol','Company']]
    return df


dataset = extraction_yahoo_finance()

dataset_origin = pd.read_csv('base_yf.csv')

dataset = dataset.append(dataset_origin)
dataset = dataset.drop_duplicates()

dataset.to_json('base_yf.json', orient = 'records')
dataset.to_json('base_yf.csv')
        

        