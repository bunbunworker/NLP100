# -*- coding*utf-8 -*-
# Yukihiro Suzuki 2017/12/29
import gzip
import json
import re

frame = 'jawiki-country.json.gz'
result = []

with gzip.open(frame, 'rt') as data_file:
	for line in data_file:
		data_json = json.loads(line)
		if data_json['title'] == 'イギリス':
			result = (re.findall('\[\[Category:.*\]\]', data_json['text']))
			break

result = (re.sub("\[\[Category:","",row) for row in result)
print("\n".join(re.sub("\]\]","",row) for row in result))
