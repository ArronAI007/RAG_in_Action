from flask import Flask, render_template, request


# 初始化 Flask 应用程序
app = Flask(__name__)


# 定义路由和处理函数
@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/about')
def about():
    return "This is the about page."


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 这里可以添加登录验证逻辑
        return f'Logged in as {username}'
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)