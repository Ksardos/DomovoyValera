# -*- coding: utf-8 -*-
import requests
import config


def get_temp(domain, region):
    response = requests.get("%s?region=%s" % (domain, region))
    #response.encoding = 'CP1251'
    s = response.text
    # color = s[s.find('<temperature') + 37:s.find("</temperature>") - 5]
    wind_speed = s[s.find('<wind_speed>') + 12:s.find("</wind_speed>")]
    wind_direction = s[s.find('<wind_direction') + 23:s.find("</wind_direction>")] \
        .replace('>', '')
    s = s[s.find('<temperature class_name="t') + 24:s.find("</temperature>") + 14]
    s = s[s.find('color=') + 15:s.find("</temperature>")] \
        .replace("<' + 'br>", "\n") \
        .replace("<' + 'br />", "\n") \
        .replace('&lt;', '<') \
        .replace('&gt;', '>') \
        .replace('&quot;', "'") \
        .replace('&nbsp;', ' ')
    s = """Температура за бортом %s°C. Ветер %s, %s м/с.""" % (s, wind_direction, wind_speed)
    # s = ("%s?region=%s" % (domain, region))
    return s


temp = get_temp(config.ya_weather_url, 213)
print(temp)
