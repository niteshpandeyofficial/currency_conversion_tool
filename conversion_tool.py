from dotenv import load_dotenv
import requests
from langchain_core.tools import tool,InjectedToolArg
from typing import Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
load_dotenv()

@tool
def get_conversion_factor(base_currency:str, target_currency:str) -> float:
    """
    this function fetches the currency conversion factor between a given
    base currency and target currency.
    """
    url=f"https://v6.exchangerate-api.com/v6/4e607ff28defada84ff81693/pair/{base_currency}/{target_currency}"
    print(url)
    res=requests.get(url)
    print(res.json())
    return res

result=get_conversion_factor.invoke({"base_currency":"USD","target_currency":"INR"})
print(result)

@tool
def convert_currency(base_currency_value:int,conversion_rate:Annotated[float,InjectedToolArg]) -> float:
    """
    This function converts a given currency value into
    """
    return base_currency_value * conversion_rate

print(convert_currency.args)
result_new=convert_currency.invoke({"base_currency":98,"target_currency":10})
print(result_new)