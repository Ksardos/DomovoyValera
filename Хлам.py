import lxml.html as html
import urllib
#from pandas import DataFrame

main_domain_stat = 'http://bash.im/'
quote = '441358'
page = html.parse('%squote/%s' % (main_domain_stat, quote))
e = page.getroot().\
        find_class('text').\
        pop()
t = e.getchildren().pop()
pr = e.text_content()

print (pr)


from grab import Grab
main_domain_stat = 'http://bash.im/'
quote = '441358'

g = Grab()
g.go ('%squote/%s' % (main_domain_stat, quote))
pr = g.xpath_text('//div[@class="text"]')
print (pr)


string = '''<html>
 <body>
  <div class="post">
   text <p> text </p> text <a> text </a>
   <span> text </span>
  <div class="post">
   another text <p> text </p>
 </body>
</html>'''


def get_quote():
    response = requests.get('http://bash.im/forweb/')
    response.encoding = 'CP1251'
    s = response.text
    s = s[s.find('0;">') + 4:s.find("<' + '/div><' + 'small>")] \
        .replace("<' + 'br>", "\n") \
        .replace("<' + 'br />", "\n") \
        .replace('&lt;', '<') \
        .replace('&gt;', '>') \
        .replace('&quot;', "'") \
        .replace('&nbsp;', ' ')
    return s


"""2016-09-30 17:32:09,612 (__init__.py:220 MainThread) ERROR - TeleBot: "A request to the Telegram API was unsuccessful. The server returned HTTP 400 Bad Request. Response body:
[b'{"ok":false,"error_code":400,"description":"Bad Request: Can\'t parse message text: Unsupported start tag \\"tami\\" at byte offset 63"}']""""
