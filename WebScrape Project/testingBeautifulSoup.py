from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>HELLLOO<b>HOWWW<i>HYOUUUTML")
print(soup.prettify())
t=soup.find(string="HELLLOO")
t2=soup.find_all(char ="H")
print(soup.contents)
print(soup.p)
print(t2)
print(t)