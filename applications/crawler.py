import json
import requests
import datetime
# CWB-106E52B9-7BD5-4CA9-B9F6-A67A2660BA91

params = {
	'Authorization' : 'CWB-106E52B9-7BD5-4CA9-B9F6-A67A2660BA91'
}
# response = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-003", params = params)
# with open('original_data.txt','a+') as f:
# 	f.write(str(response.json()))
with open('./data.json','rb') as f:
	data = json.load(f)
with open('./meteorological.json','rb') as f:
	meteorological = json.load(f)

def all_key(dict_data, _dict = {}, all_data = []):

	def dfs(value):
		if isinstance(value, dict):
			all_key(value)
		if isinstance(value, list):
			for val in value:
				all_key(val)

	for key, val in dict_data.items():
		if key == 'locationName':
			_dict['location'] = val

		if key in ['lat', 'lon']:
			_dict[key] = float(val)

		if key in ['elementName', 'description','startTime', 'endTime']:
			if key == 'startTime':
				start_time = datetime.datetime.strptime(val,"%Y-%m-%d %H:%M:%S").hour
				if start_time == 6:
					_dict['time_unit'] = "AM"
				elif start_time == 18:
					_dict['time_unit'] = "PM"
				else:
					continue
			_dict[key] = val
		if key == 'value':
			try:
				_dict['value'] = int(dict_data['value'])
			except Exception:
				_dict['value'] = 404
			_dict['measures'] = dict_data['measures']
			if _dict.get('description','') == "天氣現象":
				_dict['value'] = meteorological.get(dict_data['value'], dict_data['value'])
			all_data.append(_dict.copy())
		dfs(val)
	return all_data


with open('result.txt','w+') as f:
	# all_key(response.json())
	f.write(json.dumps(all_key(data)))
