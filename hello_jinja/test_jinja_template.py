#-*-conding:UTF-8-*-
from jinja2 import Template

t = Template('''
    {% if name %}
        Hello, {{name}}
    {% else %}
        Hello, everybody
    {%endif%}
    ''')

print(t.render(name='Peter'))
print(t.render())