# DaiMust 系列软件：DaiMust 气象 / Weainfo  
### 若对程序的合法性或相关权益存在质疑或反驳，请将合法证明和叙述发送到 [caslenzh@gmail.com](mailto:caslenzh@gmail.com) ，我们会积极跟进。  


## 使用教程
--运行程序。  
--在“地点 Location”一栏中输入您要查询的城市/县镇/州等的名称（目前查询可精确到区级，部分可精确到街道级，且全面支持中文和英文查询。区级及以上地名支持中、英、韩、俄、法、越等10+种语言查询）。  
--点击“查询 CHECK”按钮，等待3-5秒即可出数据。  


## 注意事项
--中国地名若过于精确（如村、乡）建议使用中文查询。国外地名若过于精确建议使用英文或当地语言查询。  
--气象数据来自 [OpenWeatherMap](openweathermap.org) 。由各地气象机关上报，若发现气象数据错误，请与当地气象机关数据核对，若确实是程序错误，请到 [GitHub Issues](https://github.com/CaslenZ/DaiMust/issues) 反馈。  
-若程序出现点击”查询 CHECK“按钮后闪退，请您重启 IDE 和电脑再试。  
--报错目前仅支持中文，烦请自行翻译。  
--由于本程序不是用于商业用途，因此查询气象信息的API是个人限制性的，请您不要浪费每一次查询的次数。  

## 报错信息
-获取天气信息失败：请更换中文/英文/当地语言进行查询，若问题仍现，即为服务器问题，请稍后再试。  
-请求失败，状态码：请移步到下方“报错状态码”查看报错原因。  
-地点名称错误或 API 接口不可用：请更换中文/英文/当地语言进行查询，若问题仍现，即为服务器问题，请稍后再试。    
-请求未授权，请检查 API 密钥是否正确：请到 [GitHub Issues](https://github.com/CaslenZ/DaiMust/issues) 进行反馈。  
-获取经纬度失败，状态码：请移步到下方“报错状态码”查看报错原因。    
-地点不存在：请更换中文/英文/当地语言进行查询，若问题仍现，请到 [Wikipedia](www.wikipedia.com)/[百度百科](baike.baidu.com) 查询地点官方名称，并使用官方名称查询。  

## 报错状态码  
-400：请更换中文/英文/当地语言进行查询，若问题仍现，请到 [Wikipedia](www.wikipedia.com)/[百度百科](baike.baidu.com) 查询地点官方名称，并使用官方名称查询。  
-401：请您不要修改PY文件。若已排除修改PY文件情况，请您到 [GitHub Issues](https://github.com/CaslenZ/DaiMust/issues) 反馈。  
-404：请您不要修改PY文件。若已排除修改PY文件情况，请更换中文/英文/当地语言进行查询，若问题仍现，请到 [Wikipedia](www.wikipedia.com)/[百度百科](baike.baidu.com) 查询地点官方名称，并使用官方名称查询。  
-429：本程序当日可供查询次数已用尽，请您明天再查询。  
-500、502、503、504：请您把您的系统环境和 Python 版本环境、报错状态码发送到 [caslenzh@gmail.com](mailto:caslenzh@gmail.com) ，我们会调查报错原因。  

## 版本更新
V 1.0 2024-03-02 在 [Github](https://github.com/CaslenZ/DaiMust/tree/main/DaiMust%20%E6%B0%94%E8%B1%A1%20Weainfo) 上发布。  
