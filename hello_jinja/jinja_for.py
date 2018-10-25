#-*-coding:UTF-8-*-
from jinja2 import Template

t = Template(
    '''
    <ul>
        {% for message in messages %}
            <li>{{message}}</li>
        {% endfor %}
    </ul>
    '''
    )

print(t.render(messages=['Apple', 'Orange', 'pear']))