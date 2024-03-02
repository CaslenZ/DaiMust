# DaiMust 系列软件：DaiMust 气象 / Weainfo （[Click to English](#English)）
### 若对程序的合法性或相关权益存在质疑或反驳，请将合法证明和叙述发送到 caslen08@icloud.com，我们会积极跟进。  


## 使用教程
--运行程序。  
--在“地点 Location”一栏中输入您要查询的城市/县镇/州等的名称（目前查询可精确到区级，部分可精确到街道级，且全面支持中文和英文查询。区级及以上地名支持中、英、韩、俄、法、越等10+种语言查询）。  
--点击“查询 CHECK”按钮，等待3-5秒即可出数据。  


## 注意事项
--中国地名若过于精确（如村、乡）建议使用中文查询。国外地名若过于精确建议使用英文或当地语言查询。  
--气象数据来自openweathermap.org 。由各地气象机关上报，若发现气象数据错误，请与当地气象机关数据核对，若确实是程序错误，请到GitHub Issues反馈。  
-若程序出现点击”查询 CHECK“按钮后闪退，请您重启IDE和电脑再试。  
--报错目前仅支持中文，烦请自行翻译。  
--由于本程序不是用于商业用途，因此查询气象信息的API是个人限制性的，请您不要浪费每一次查询的次数。  

## 报错信息
-获取天气信息失败：请更换中文/英文/当地语言进行查询，若问题仍现，即为服务器问题，请稍后再试。  
-请求失败，状态码：请移步到下方“报错状态码”查看报错原因。  
-地点名称错误或 API 接口不可用：请更换中文/英文/当地语言进行查询，若问题仍现，即为服务器问题，请稍后再试。    
-请求未授权，请检查 API 密钥是否正确：请到GitHub Issues进行反馈。  
-获取经纬度失败，状态码：请移步到下方“报错状态码”查看报错原因。    
-地点不存在：请更换中文/英文/当地语言进行查询，若问题仍现，请到Wikipedia/百度百科查询地点官方名称，并使用官方名称查询。  

## 报错状态码
-401：请您不要修改PY文件。若已排除修改PY文件情况，请您到GitHub Issues反馈。  
-404：请您不要修改PY文件。若已排除修改PY文件情况，请更换中文/英文/当地语言进行查询，若问题仍现，请到Wikipedia/百度百科查询地点官方名称，并使用官方名称查询。  
-429：本程序当日可供查询次数已用尽，请您明天再查询。  
-500、502、503、504：请您把您的系统环境和Python版本环境发送到caslen08@icloud.com，我们会调查报错原因。  

## 版本更新
V 1.0 2024-03-02 在Github上发布。  

## DaiMust Series Software: DaiMust Weainfo 
<a id="English"></a>

### If you have any doubts or questions about the legality or related rights of the program, please send your legal proof and description to caslen08@icloud.com, and we will follow up promptly.

## Usage Guide

1. Run the program.
2. In the "Location" bar, enter the name of the city/county/state etc. you want to query (currently the query can be accurate to the district level, some can be accurate to the street level, and it fully supports Chinese and English queries. District and above place names support 10+ languages such as Chinese, English, Korean, Russian, French, and Vietnamese).
3. Click the "CHECK" button and wait for 3-5 seconds to get the data.

## Precautions

1. If Chinese place names are too precise (such as villages and towns), it is recommended to use Chinese query. If foreign place names are too precise, it is recommended to use English or the local language query.
2. The weather data comes from openweathermap.org. It is reported by local weather stations. If you find that the weather data is wrong, please check the data with the local weather station. If it is indeed a program error, please feedback to GitHub Issues.
3. If the program crashes after clicking the "CHECK" button, please restart your IDE and computer and try again.
4. Currently only Chinese is supported for error reporting, please translate it yourself.
5. Since this program is not for commercial use, the API for querying weather information is personally restrictive. Please do not waste every query.

## Error Information

- Get weather information failed: Please try to query in Chinese/English/local language, if the problem persists, it is a server problem, please try again later.
- Request failed, status code: Please move to the "Error Status Code" below to see the error reason.
- Location name error or API interface unavailable: Please try to query in Chinese/English/local language, if the problem persists, it is a server problem, please try again later.
- Request unauthorized, please check if the API key is correct: Please feedback to GitHub Issues.
- Get latitude and longitude failed, status code: Please move to the "Error Status Code" below to see the error reason.
- Location does not exist: Please try to query in Chinese/English/local language, if the problem persists, please search for the official name of the location on Wikipedia/Baidu Encyclopedia and use the official name to query.

## Error Status Code

- 401: Please do not modify the PY file. If you have ruled out the possibility of modifying the PY file, please feedback to GitHub Issues.
- 404: Please do not modify the PY file. If you have ruled out the possibility of modifying the PY file, please try to query in Chinese/English/local language. If the problem persists, please search for the official name of the location on Wikipedia/Baidu Encyclopedia and use the official name to query.
- 429: The number of queries available for this program today has been used up. Please query again tomorrow.
- 500, 502, 503, 504: Please send your system environment and Python version environment to caslen08@icloud.com, we will investigate the cause of the error.

## Version Update

V 1.0 2024-03-02 Released on Github.

