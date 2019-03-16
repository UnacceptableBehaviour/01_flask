TEMPLATE_STR = """
{% for l in result.items() %}
<div class="link">
    <a href="{{ l.url }}"> {{l.title}}</a>
    <img src="{{ l.img }}" width="100" height="100">
</div>
{% endfor %}
"""

from jinja2 import Template

template = Template(TEMPLATE_STR)

class democlass(object):
    def getTitle(self): return "Hello world"
    def getLink(self): return "google.co.uk"
    def getImg(self): return "myimage.png"

class democlass2(object):
    def getTitle(self): return "Foo bar"
    def getLink(self): return "stackoverflow.com"
    def getImg(self): return "a_photo.jpeg"

l = democlass()
m = democlass2()

dict1 = {}
dict1['l'] =  { 'title': l.getTitle(), 'url': l.getLink(), 'img': l.getImg() }
dict1['m'] =  { 'title': m.getTitle(), 'url': m.getLink(), 'img': m.getImg() }

#print( render_template(TEMPLATE_STR, result=dict1) )

#print( template.render(result=dict1) )

print( template.__class__.__name__ )

dict_a = { 'Aa': 00 , 'Bb': 11 , 'Cc': 33, 'Dd': 44 , 'Ee': 55 }

for mytuple in dict_a.items():
    print(f"class:{mytuple.__class__.__name__} - {mytuple}")

for key, value in dict_a.items():
    print(f"k:{key} - v:{value}")

print( template.render( result = dict_a ) )

# - - - - - - 
#
# from
# https://stackoverflow.com/questions/29547200/how-to-get-a-python-dict-into-an-html-template-using-flask-jinja2?rq=1
#
# - - - - - - 