import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
        loader=FileSystemLoader(searchpath='./templates'),
        autoescape=select_autoescape(['html', 'txt'])
)
template = env.get_template(sys.argv[1])
result = template.render()
print(result)
if '-w' in sys.argv:
    with open('result.html', 'w') as f:
        f.write(result)

