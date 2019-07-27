import requests
from bs4 import BeautifulSoup

data = requests.get('https://ocw.mit.edu/courses/most-visited-courses/')

soup = BeautifulSoup(data.text, 'html.parser')

course_table = soup.find('table', { 'class': 'courseList'})

# find the heading of the relevant section using the find method from
# BeautifulSoup, ignore everything else
tbody = course_table.find('tbody')

# for loop to capture the information from each course in turn
# within the heading of the section identified as relevant, extract the text
# related to each course, and strip out anything unnecessary
for tr in tbody.find_all('tr'):
  course_num = tr.find_all('td')[0].text.strip()
  course_title = tr.find_all('td')[1].text.strip()
  course_level = tr.find_all('td')[2].text.strip()

  print(course_num, course_title, course_level)

