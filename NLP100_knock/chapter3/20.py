# -*- coding*utf-8 -*-
# Yukihiro Suzuki 2017/12/29
import gzip
import json

frame = 'jawiki-country.json.gz'
with gzip.open(frame, 'rt') as data_file:
	for line in data_file:
		data_json = json.loads(line)
		if data_json['title'] == 'イギリス':
			print(data_json['text'])
			break

