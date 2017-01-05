# -*- coding: utf-8 -*-
from lxml.html import fromstring
from grab import Grab
import re
import requests
import config  # импорт настроек


# ФУНКЦИИ

# Получение цитаты по ее номеру
def bash_get_quote_on_id(domain, quote_number):
    g = Grab()
    g.go('%squote/%s' % (domain, quote_number))
    quote_html = g.doc.select('.//div[@class="text"]').html()
    return quote_html


# Общее количество цитат
def bash_get_quote_count(domain):
    g = Grab()
    g.go("%squote/" % domain)
    quote_count = g.doc.select('.//div[@id="stats"]').select('.//b').number()
    return quote_count


# Рандомная цитата
def bash_get_quote_rnd_url(domain):
    g = Grab()
    g.go("%srandom/" % domain)
    quote_html = g.doc.select('.//div[@class="actions"]/a[@class="id"]').node().get("href")
    quote_html = re.sub(r'\D', '', quote_html)
    return quote_html


# Рандомная цитата
def bash_get_quote_rnd(domain):
    quote = bash_get_quote_rnd_url(domain)
    quote_url = ("%squote/%s" % (domain, quote))
    g = Grab()
    # qqq = ("%s%s" % (domain, quote))
    # print (qqq)
    g.go("%squote/%s" % (domain, quote))
    quote_html = g.doc.select('.//div[@class="text"]').html()
    quote_html = re.sub(r'\</?d[^>]*\>', '', quote_html)
    quote_html = re.sub(r'\<br>', '\n', quote_html)
    quote_html = """Цитата № <a href="%s">%s</a>:\n""" % (quote_url, quote) + "%s" % quote_html
    return quote_html


# Рандомная цитата вариант 2
def get_quote(domain):
    response = requests.get('%sforweb/' % domain)
    response.encoding = 'CP1251'
    s = response.text
    quote_id = s[s.find('">#') + 3:s.find("<\' + \'/a>")]
    s = s[s.find('0;">') + 4:s.find("<' + '/div><' + 'small>")] \
        .replace("<' + 'br>", "\n") \
        .replace("<' + 'br />", "\n") \
        .replace('&lt;', '<') \
        .replace('&gt;', '>') \
        .replace('&quot;', "'") \
        .replace('&nbsp;', ' ')
    s = """Цитата № <a href="%squote/%s">%s</a>:\n""" % (domain, quote_id, quote_id) + "%s" % s
    return s

# ------------
# quote = '441358'
# pr = bash_get_quote_on_id(config.bash_url, quote)
# count = bash_get_quote_count(config.bash_url)
# rnd = bash_get_quote_rnd(config.bash_url)
# url = bash_get_quote_rnd_url(config.bash_url)
# rnd = get_quote(config.bash_url)
# print(rnd)
