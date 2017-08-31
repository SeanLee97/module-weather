# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pickle
import urllib.request as request
from lxml import etree

url = 'http://cj.weather.com.cn/support/detail.aspx?id=51837fba1b35fe0f8411b6df'
save_dir = 'citycode.pkl'

try:
	r = request.Request(url)
	response = request.urlopen(r)
	html = response.read()
	#print(html)
	selector = etree.HTML(html)
	data = selector.xpath('//div[@class="entry-content"]//p/text()')[0:]
	code_dict = {}
	# 注意到北京分隔符有中文逗号也有西文逗号故独立出来处理
	code_dict['北京'] = data[0].strip().split(',')[0]
	for item in data[1:]:
		arr = item.strip().split(',')
		code_dict[arr[1]] = arr[0]
	print(code_dict)
	with open(save_dir, 'wb') as f:
		pickle.dump(code_dict, f, True)
	with open('./dict.json', 'w') as f:
		json.dump(code_dict, f, ensure_ascii=False)
except Exception as e:
	print('faild> ', e)
