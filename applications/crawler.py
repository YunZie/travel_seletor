import json
import requests
import datetime

# with open('./data.json','rb') as f:
# 	data = json.load(f)
with open('./constant/meteorological.json','rb') as f:
	meteorological = json.load(f)

def all_key(dict_data, _dict = {}, all_data = []):

	def dfs(value):
		if isinstance(value, dict):
			all_key(value)
		if isinstance(value, list):
			for val in value:
				all_key(val)

	for key, val in dict_data.items():

		if key == 'locationsName':
			_dict['city'] = val

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

def get_weather_from_official(auth_token):
	# 'CWB-106E52B9-7BD5-4CA9-B9F6-A67A2660BA91'
	# https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-003
	params = {
		'Authorization' : auth_token
	}
	weather_urls = [
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-003',
		# # 鄉鎮天氣預報-宜蘭縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-007',
		# # 鄉鎮天氣預報-桃園市未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-011',
		# # 鄉鎮天氣預報-新竹縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-015',
		# # 鄉鎮天氣預報-苗栗縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-019',
		# # 鄉鎮天氣預報-彰化縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-023',
		# # 鄉鎮天氣預報-南投縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-027',
		# # 鄉鎮天氣預報-雲林縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-031',
		# # 鄉鎮天氣預報-嘉義縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-035',
		# # 鄉鎮天氣預報-屏東縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-039',
		# # 鄉鎮天氣預報-臺東縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-043',
		# # 鄉鎮天氣預報-花蓮縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-047',
		# # 鄉鎮天氣預報-澎湖縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-051',
		# # 鄉鎮天氣預報-基隆縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-055',
		# # 鄉鎮天氣預報-新竹市未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-059',
		# 鄉鎮天氣預報-嘉義市未來1週天氣預報
		'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-063',
		# 鄉鎮天氣預報-臺北市未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-067',
		# # 鄉鎮天氣預報-高雄市未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-071',
		# # 鄉鎮天氣預報-新北市未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-075',
		# # 鄉鎮天氣預報-臺中市未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-079',
		# # 鄉鎮天氣預報-臺南市未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-083',
		# # 鄉鎮天氣預報-連江縣未來1週天氣預報
		# 'https://opendata.cwb.gov.tw/api//v1/rest/datastore/F-D0047-087',
		# # 鄉鎮天氣預報-金門縣未來1週天氣預報
	]

	for _url in weather_urls:
		response = requests.get(_url, params = params)
		reponse_as_dict = response.json()
		yield all_key(reponse_as_dict)
# with open('original_data.txt','a+') as f:
# 	f.write(str(response.json()))

