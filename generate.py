import csv
from jinja2 import Template
from secrets import *

with open('markers.template.html', 'r') as stream:
    template_text = stream.read()

with open('index.template.html', 'r') as stream:
    index_template = stream.read()

items = []
with open('data.csv', 'r') as stream:
	reader = csv.reader(stream, delimiter=';')
	for row in reader:
		cells = list(row)
		if cells[0] is None:
			break

		d = {
			'text': cells[0].replace("\"", "'"),
			'location': [
				cells[2],
				cells[3],
			],
			'info': cells[5].replace("\"", "'") + "<br/> More info at: <a href=\\\"{}\\\">{}</a>".format(cells[4],
																										   cells[4]),
		}

		if cells[6] is not None:
			d['icon'] = "icons/" + cells[6]
			del d['text']

		items.append(d)


template = Template(template_text)

text = template.render({
    'markers': items,
})

with open('index.html', 'w') as stream:
    stream.write(index_template.replace("MARKERDEFINITIONS", text).replace("MY_API_KEY", API_KEY_local))

with open('public/index.html', 'w') as stream:
    stream.write(index_template.replace("MARKERDEFINITIONS", text).replace("MY_API_KEY", API_KEY_prod))
