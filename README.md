# Azure_AI_Agent_Service_workshop

# Workshop: Building Agents with Azure AI Agent Service SDK
 
This workshop is designed to help you build intelligent agents using the Azure AI Agent Service SDK. You will explore the Azure AI Agent Service through both a playground experience and code-first approach. Below are the different notebooks you will work through, each providing a step-by-step guide to get you started. Please follow them in sequence.

Notebooks to Get Started:
 

1. data_reader.ipynb: This notebook leverages the code interpreter action to run Python code for data ingestion and analysis.
2. forecaster.ipynb: This notebook utilizes the Azure MaaS model TimeGEN to forecast future consumption.
3. retrieve.ipynb: This notebook employs Azure AI Agent Service's File Search knowledge source to query unstructured data.
4. recommender.ipynb: This notebook simulates a multi-agent conversation using function calling in the AI Agent Service. It uses user-defined functions (reasoning.py and ai_search.py) to generate final recommendations by combining retrieved knowledge and advanced reasoning results using AOAI o1.


Introduction
Imagine you are an organisation EcoPower, who is committed to delivering reliable and efficient energy utilities services". One of your mission is to empower consumers with insights into their energy usage, enabling them to save on costs and reduce their carbon footprint. You are tasked with developing a smart AI-driven agent that can help achieve this vision.

Step 1: Understanding Consumption Patterns
EcoPower starts by fetching consumer energy consumption data from its backend systems. You will run basic statistical analyses to uncover patterns and trends in the data. This will provide a foundation for understanding how customers use energy over time.

Step 2: Forecasting Future Usage
Next, EcoPower Solutions needs to predict future energy consumption to help customers plan better. You need to forecast energy usage for the next 12 months. This will allow customers to anticipate their energy needs and adjust their behavior accordingly.

Step 3: Providing Grounded Energy-Saving Information
EcoPower Solutions has a wealth of internal knowledge, including unstructured data such as documents, reports, and research papers. You then need to query this internal knowledge base to extract actionable energy-saving tips and information. This AI-powered search will provide customers with reliable and grounded advice.

Step 4: Delivering Personalized Recommendations
Finally, EcoPower Solutions aims to offer personalized recommendations to each customer. By combining advanced reasoning techniques with proprietary information, your AI agent will simulate multi-agent conversations. The agent will analyze the retrieved knowledge and consumption patterns to generate tailored advice. This will help customers make informed decisions to optimize their energy usage.


Conclusion
By the end of this workshop, you will have developed a powerful AI agent , capable of helping customers understand their energy consumption, forecast future usage, access valuable energy-saving information, and receive personalized recommendations. This AI-driven approach will not only enhance customer satisfaction but also contribute to a more sustainable future.

### Pre-requisties

## Install Project Dependencies
Use `pip` to install all the required dependencies for the project as specified in the `requirements.txt` file:

`pip install -r requirements.txt`

## Create Azure AI Foundry resource

**Copy the connection string from your AI Foundry.**

**Set Environment Variables**  
Ensure you set the required environment variables in `.env` file.

**Create TimeGEN MaaS endpoint**
Go to Azure Foundry --> Model Catalog --> TimeGen --> Deploy , copy endpoints and key
