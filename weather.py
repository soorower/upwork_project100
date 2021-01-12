import requests
from bs4 import BeautifulSoup

weater = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
soup = BeautifulSoup(weater.content, 'html.parser')

seven_days = soup.find(id = 'seven-day-forecast-list')

# forecast_items = seven_days.find_all(class_ = 'forecast-tombstone')


# for i in range(1,9):
#     tonight = forecast_items[i]
#     period = tonight.find(class_="period-name").get_text()
#     short_desc = tonight.find(class_="short-desc").get_text()
#     temp = tonight.find(class_="temp").get_text()
#     img = tonight.find("img")
#     desc = img['title']
#     if None in (period,short_desc,temp,img,desc):
#             continue
#     print(desc)
#     print(period)
#     print(short_desc)
#     print(temp)

period_tags = seven_days.select(".forecast-tombstone .period-name")
periods = [pt.text for pt in period_tags]
short_descs = [sd.text for sd in seven_days.select(".forecast-tombstone .short-desc")]
temp = [t.text for t in seven_days.select(".forecast-tombstone .temp")]
print(periods)
print(short_descs)
print(temp)
#    python weather.py