from langserve import RemoteRunnable

if __name__ == "__main__":
    chain = RemoteRunnable("http://localhost:8000/translate/")
    # 输出¡Hola, mundo!
    print(chain.invoke({"language": "Spanish", "text": "Hello, world!"}))






