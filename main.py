import os
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
        loader=FileSystemLoader(searchpath='templates'),
        autoescape=select_autoescape(['html', 'txt'])
)
for template_file in os.listdir('templates'):
    template = env.get_template(template_file)
    result = template.render()
    with open('results/%s' % template.filename.split('/')[-1], 'w') as f:
        f.write(result)

