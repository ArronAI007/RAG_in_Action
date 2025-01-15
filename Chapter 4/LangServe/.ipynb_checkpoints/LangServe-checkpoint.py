from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langchain_core.output_parsers import StrOutputParser


import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# 创建 FastAPI 应用实例
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# 创建提示模板
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 创建语言模型实例
model = ChatOpenAI()

# 创建输出解析器
parser = StrOutputParser()

# 创建链
chain = prompt_template | model | parser

# 添加路由
add_routes(
    app,
    chain,
    path="/translate",
)

# 启动服务
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)