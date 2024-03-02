import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
import webbrowser


# API key
api_key = "dfc2104fcf1138d24fedb64aba8c5523"

# 获取经纬度
def get_lat_lon(city_name):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["lat"], data[0]["lon"]
        else:
            show_error(f"地点 '{city_name}' 不存在")
    else:
        show_error(f"获取经纬度失败，状态码：{response.status_code}")

# 获取天气数据
def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 401:
        show_error("请求未授权，请检查 API 密钥是否正确")
    elif response.status_code == 404:
        show_error("地点名称错误或 API 接口不可用")
    else:
        show_error(f"请求失败，状态码：{response.status_code}")

# 显示错误信息
def show_error(message):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle("错误 Error!")
    msg_box.setText(message)
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    msg_box.exec()

# 显示天气信息
def show_weather(city_name):
    lat, lon = get_lat_lon(city_name)
    if lat and lon:
        weather = get_weather(lat, lon)
        if weather:
            main_weather = weather["main"]
            temperature = main_weather["temp"]
            humidity = main_weather["humidity"]
            wind_speed = weather["wind"]["speed"]

            # 更新文本框内容
            text_city.setText(city_name)
            text_temperature.setText(f"{temperature:.1f}°C")
            text_humidity.setText(f"{humidity:.1f}%")
            text_wind_speed.setText(f"{wind_speed:.1f} m/s")
            text_wind_speed.setText(f"{wind_speed:.1f} m/s")
        else:
            show_error(f"获取 {city_name} 天气信息失败。")

def open_url():
    url = "https://github.com/CaslenZ/DaiMust/tree/main/DaiMust%20%E6%B0%94%E8%B1%A1%20Weainfo"
    webbrowser.open(url)

# 创建应用程序
app = QtWidgets.QApplication(sys.argv)

# 创建窗口
window = QtWidgets.QWidget()
window.setWindowTitle("DaiMust 气象 Weainfo")

window.setMaximumSize(QSize(640, 480))
window.setMinimumSize(QSize(640, 480))

# 创建输入框
text_city = QtWidgets.QLineEdit()

# 创建文本框
text_temperature = QtWidgets.QLineEdit()
text_temperature.setReadOnly(True)
text_humidity = QtWidgets.QLineEdit()
text_humidity.setReadOnly(True)
text_wind_speed = QtWidgets.QLineEdit()
text_wind_speed.setReadOnly(True)
Info_Sources = QtWidgets.QLineEdit()
Info_Sources.setReadOnly(True)

# 创建标签
label_city = QtWidgets.QLabel("地点 Location：")
label_temperature = QtWidgets.QLabel("温度 Temp：")
label_humidity = QtWidgets.QLabel("湿度 Humidity：")
label_wind_speed = QtWidgets.QLabel("风速 WindSpped：")

# 布局控件
layout = QtWidgets.QGridLayout()
layout.addWidget(label_city, 0, 0)
layout.addWidget(text_city, 0, 1)
layout.addWidget(label_temperature, 1, 0)
layout.addWidget(text_temperature, 1, 1)
layout.addWidget(label_humidity, 2, 0)
layout.addWidget(text_humidity, 2, 1)
layout.addWidget(label_wind_speed, 3, 0)
layout.addWidget(text_wind_speed, 3, 1)


# 创建按钮
button_query = QtWidgets.QPushButton("查询 CHECK ")
button_query.clicked.connect(lambda: show_weather(text_city.text()))

# 添加按钮到布局
layout.addWidget(button_query, 4, 0, 1, 2)

# 创建按钮
button_fb = QtWidgets.QPushButton("帮助与反馈 Help&Feedback")
button_fb.clicked.connect(lambda: open_url())
button_fb.setVisible(True)
button_fb.setFixedSize(QSize(600, 30))

# 添加按钮到布局
layout.addWidget(button_fb, 5, 0, 1, 2)

# 设置窗口布局
window.setLayout(layout)

# 显示窗口
window.show()

# 运行应用程序
sys.exit(app.exec())
