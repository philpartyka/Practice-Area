import xml.etree.ElementTree as ET
import re

tree= ET.parse('movies.xml')
root= tree.getroot()
print(root)
print(root.tag)
print(root.attrib) #collection doesn't have a name=value pair like movies does (category="Action")

for child in root:
    print(child.tag, child.attrib)

#print([elem.tag for elem in root.iter()])

#print(ET.tostring(root, encoding='utf8').decode('utf8'))

for movie in root.iter('movie'):
    print(movie.attrib)

for description in root.iter('description'):
    print(description.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format/[@multiple = 'Yes']..."): #... at the end will return parent
    print(movie.attrib)

#b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
#print(b2tf)
#b2tf.attrib["title"] = "Back to the Future"
#print(b2tf.attrib)

#tree.write("movies.xml")
#above will overwrite the original xml file with the current tree object we have been working on

# for movie in root.findall("./genre/decade/movie"):
#     print(movie.attrib)

# #below is same as above
# for movie in root.iter('movie'):
#     print(movie.attrib)

# for form in root.findall("./genre/decade/movie/format"):
#     match = re.search(",", movies.xml)

print("break")
for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)
    
action=root.find("./genre[@category='Action']")
new_dec= ET.SubElement(action, 'decade')
new_dec.attrib["years"]= '2000s'
#print(ET.tostring(action, encoding='utf8').decode('utf8'))

xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s= root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
# dec1990s= root.find("./genre[@category='Action']/decade[@years='1990s']")
# dec1990s.remove(xmen)
#print(ET.tostring(action, encoding='utf8').decode('utf8'))

#tree.write("movies.xml")
thriller=root.find("./genre[@category='Thriller']")
new_dec= ET.SubElement(thriller, 'decade')
new_dec.attrib["years"]= '2000s'

psycho = root.find("./genre/decade/movie[@title='American Psycho']")
dec2000s= root.find("./genre[@category='Thriller']/decade[@years='2000s']")
dec2000s.append(psycho)
dec1980s= root.find("./genre[@category='Thriller']/decade[@years='1980s']")
dec1980s.remove(psycho)
print(ET.tostring(thriller, encoding='utf8').decode('utf8'))