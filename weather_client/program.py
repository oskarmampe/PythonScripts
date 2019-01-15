import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')

def main():
    header() 
    code = input('What zipcode do you want the weather for?')
    html = getHTML(code)
    report = get_weather(html)
    print('The temp in {} is {} {} and {}'.format(report.loc,  report.temp, report.scale, report.cond))

def getHTML(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    
    return response.text


def get_weather(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    cond = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    cond = cleanup_text(cond)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    #print(loc, cond, temp, scale)
    report = WeatherReport(cond=cond, temp=temp, scale=scale, loc=loc)
    return report

def cleanup_text(text : str):
    if not text:
        return text

    text = text.strip()
    return text

def header():
    print('WEATHER APP')

if __name__ == '__main__':
    main()
    
