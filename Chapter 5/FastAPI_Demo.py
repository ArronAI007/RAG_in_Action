from fastapi import FastAPI


# 初始化 FastAPI 应用程序
app = FastAPI()


# 定义一个根路由
@app.get("/")
def read_root():
    return {"Hello": "World"}


# 定义一个带参数的路由
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "你好"):
    return {"item_id": item_id, "q": q}


# 启动应用程序
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)