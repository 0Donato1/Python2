import requests

#1 Get
'''
response = requests.get("https://bank.gov.ua/")#"https://httpbin.org/get"
print(response.content)

print(f"Data type content - {type(response.content)}")
print(f"Data type text - {type(response.text)}")
'''


#2 Post
'''
response = requests.post("https://httpbin.org/post", data="Hello world", headers={'group':'S2816'})
print(response.text)
'''

#3 Parser HTML

from HTMLParser import HtmlParser

parser = HtmlParser("https://bank.gov.ua/")
parser.NbuParse(separator1='index-page', separator2='small')
print(parser.Result["usd"])




