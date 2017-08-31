# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import requests
from utils import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
#禁用安全警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Weather(object):
	def __init__(self, city, type='forecast'):
		self.type = type
		self.single_url = None
		self.multi_url = None
		code = get_code(city)
		if code != None:
			self.single_url = 'http://www.weather.com.cn/data/sk/{}.html'.format(code)
			self.multi_url = 'http://mobile.weather.com.cn/data/forecast/{}.html'.format(code)
	
	def process(self):
		if self.type == 'forecast':
			result = self.get_multi()
		else:
			result = self.get_single()
		return result
	
	def get_multi(self):
		result = {}
		if self.multi_url != None:
			r = requests.get(self.multi_url, verify=False)
			try:
				json = eval(str(r.content, 'utf-8'))
				result['type'] = 'forecast'
				result['city'] = json['c']['c3']
				result['results'] = []
				for i, item in enumerate(list(json['f']['f1'])):
					now = datetime.datetime.now()
					delta = datetime.timedelta(days=i)
					n_days = now + delta
					date = n_days.strftime('%Y-%m-%d')
					temp = [item['fc'], item['fd']]
					info = {
						'date': date,
						'temperature': {
							'low': min(temp),
							'high': max(temp)
						},
						'sunrise': item['fi'].split('|')[0],
						'sunset': item['fi'].split('|')[1]
					}
					result['results'].append(info)
			except Exception as e:
				print('error ', e)
		return result

	def get_single(self):
		result = {}
		if self.single_url != None:
			r = requests.get(self.single_url, verify=False)
			try:
				json = eval(str(r.content, 'utf-8'))
				result['type'] = 'realtime'
				result['city'] = json['weatherinfo']['city']
				result['temperature'] = json['weatherinfo']['temp']	
				result['wind'] = json['weatherinfo']['WD']
				result['rain'] = json['weatherinfo']['rain']
			except:
				return result
		return result

if __name__=='__main__':
	city = '深圳'
	print(city, '实时天气')
	print(Weather(city, 'realtime').process())
	
	print(city, '未来七天天气')
	print(Weather(city).process())
