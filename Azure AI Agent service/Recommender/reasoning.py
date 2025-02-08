from openai import AzureOpenAI
import pandas as pd
import os
from nixtla import NixtlaClient

from dotenv import load_dotenv
load_dotenv()

print(os.getenv("O1_ENDPOINT"))
print(os.getenv("AZURE_OPENAI_KEY"))

client = AzureOpenAI(
  azure_endpoint =os.getenv("O1_ENDPOINT"),
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-08-01-preview"
)

# Function to load historical data
def historical_data():
    # Replace with actual data loading logic
    return pd.read_csv('./data/consumption.csv')

# Function to forecast consumption
def forecast_consumption():
    # Replace with actual data loading logic
    nixtla_client = NixtlaClient(
        base_url=os.getenv("TIME_GEN_ENDPOINT"),
        api_key=os.getenv("TIME_GEN_KEY"),
    )
    consumption = pd.read_csv('./data/consumption.csv')
    forecasted_consumption = nixtla_client.forecast(df=consumption, h=12, freq='MS', time_col='month', target_col='consumption')               
    forecasted_consumption['month'] = forecasted_consumption['month'].astype(str)
    return forecasted_consumption

# Function to extract insights using AOAI advanced reasoning o1 model
def insights_extractor(query: str):
    historical_consumption_data = historical_data()
    forecasted_consumption_data = forecast_consumption()
    
    # Convert DataFrames to JSON without index
    historical_consumption_data = historical_consumption_data.reset_index(drop=True)
    forecasted_consumption_data = forecasted_consumption_data.reset_index(drop=True)
    
    content = (
      "Find insights in my electricity consumption patterns. Do not make recommendations\n"
      f"Historical Consumption Data: {historical_consumption_data}\n"
      f"Forecasted Consumption Data: {forecasted_consumption_data}"
  )
      
    response = client.chat.completions.create(
        model="o1-preview", # replace with the model deployment name of your o1 deployment.
        messages=[
            {"role": "user", "content": content},
        ],
        max_completion_tokens = 5000
    )
    return response.choices[0].message.content

    #print(response.choices[0].message.content)

