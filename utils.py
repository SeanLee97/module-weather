# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

def get_code(city):
	citydict = {}
	with open('./citycode.pkl', 'rb') as f:
		citydict = pickle.load(f)
	if city in citydict:
		return citydict[city]
	return None

