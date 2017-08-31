# module-weather
小模块： python获取 http://weather.com.cn/ 的天气数据

## 概述
搜索了一下天气接口，发现很多都是收费接口，或者免费调用但是有次数限制。
因为项目上刚好用到天气模块，但是又不需要很具体的天气信息，所以萌生了开发一个基于[中国天气](http://weather.com.cn/)数据的接口。
其实也不是很复杂，稍稍有点工作量的也就是在获取城市代码上。

## 环境要求
```
python3+ (我的版本是3.6所以2.7版本的可能需要稍稍改动一下一些不兼容的函数)
```

## 目录结构
```
|- weather
    |- citycode.pkl   # 爬取数据并生成的城市代码字典二进制文件
    |- crawer.py      # 爬取城市代码并生成字典导出到本地(citycode.pkl)
    |- dict.json      # 城市代码字典json文件（方便其它语言的调用）
    |- utils.py       # 工具包       
    |- weather.py     # 接口调用
```
## 运行效果
```
深圳实时天气
{'type': 'realtime', 'city': '深圳', 'temperature': '21', 'wind': '南风', 'rain': '0'}

深圳未来七天天气
{
  'type': 'forecast', 
   'city': '深圳', 
   'results': [
      {
        'date': '2017-08-31', 
        'temperature': {'low': '25', 'high': '32'}, 
        'sunrise': '06:18', 
        'sunset': '18:01'
      }, {
        'date': '2017-09-01', 
        'temperature': {'low': '25', 'high': '31'}, 
        'sunrise': '06:19', 
        'sunset': '18:00'
      }, {
        'date': '2017-09-02', 
        'temperature': {'low': '24', 'high': '27'}, 
        'sunrise': '06:19', 
        'sunset': '17:59'
      }, {
        'date': '2017-09-03', 
        'temperature': {'low': '21', 'high': '25'}, 
        'sunrise': '06:20', 
        'sunset': '17:58'
      }, {
        'date': '2017-09-04', 
        'temperature': {'low': '19', 'high': '23'}, 
        'sunrise': '06:20', 
        'sunset': '17:57'
      }, {
        'date': '2017-09-05', 
        'temperature': {'low': '20', 'high': '23'}, 
        'sunrise': '06:20', 
        'sunset': '17:56'
      }, {
        'date': '2017-09-06', 
        'temperature': {'low': '22', 'high': '25'}, 
        'sunrise': '06:21', 
        'sunset': '17:56'
      }
   ]
} 
```

## 问题反馈
欢迎和我交流！共同学习！

* 邮件(lxm_0828#163.com, 把#换成@)
* QQ: 929325776
* weibo: [@捏明](http://weibo.com/littlelxm)

## 关于作者

```
学生一枚，就读于山大（shanxi university）CS专业
对deep learning(深度学习), NLP(自然语言处理)，NLU(自然语言理解)，Big Data(大数据)有狂热的学习欲望
精通WEB开发
```
