import streamlit as st
import pandas as pd
import numpy as np


# 显示标题
st.title('Streamlit 示例应用')


# 显示文本
st.write("欢迎来到这个简单的 Streamlit 应用程序。")


# 创建一个滑块
number_of_points = st.slider('选择数据点的数量', 10, 100, 50)


# 生成随机数据
data = np.random.randn(number_of_points, 2)


# 创建一个数据表格
df = pd.DataFrame(data, columns=['x', 'y'])
st.write(df)


# 绘制散点图
st.subheader('数据散点图')
st.scatter_chart(df)


# 按钮操作
if st.button('点击我'):
    st.write('你点击了按钮！')


# 选择框
option = st.selectbox(
    '你最喜欢的颜色',
    ('蓝色', '红色', '绿色')
)
st.write('你最喜欢的颜色是', option)


# 文本输入
user_input = st.text_input('输入一些文本')
st.write('你输入的是：', user_input)

# 使用streamlit run Streamlit_Demo.py来运行该脚本