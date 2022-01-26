import requests
from bs4 import BeautifulSoup

link = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
response = requests.get(link)

#response.status_code
#response.text
#response.content

soup = BeautifulSoup(response.content,'html.parser')
#print(soup.prettify())

# Find all links on the page
all_links = soup.find_all("a")

# Find only the links in a specific table
target_table = soup.find("table", class_="wikitable")
country_links = target_table.find_all("a")

# only get the information in the title tags (the country names)
countries = []
for link in country_links:
    c = link.get("title")
    countries.append(c)

# remove continents and none
not_countries = [None,"Asia","Oceania","Europe","Antarctica"]
are_countries = [country for country in countries if country not in not_countries]

print(are_countries)
print(len(are_countries))

# Save results
textfile = open("countries.txt", "w")
for country in are_countries:
    textfile.write(str(country) + "\n")
textfile.close()