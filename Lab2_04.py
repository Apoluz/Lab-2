import xml.etree.ElementTree as ET

rпуть_к_файлу = r'C:\Users\marki\Desktop\Lab-2\currency.xml'

tree = ET.parse(rпуть_к_файлу)
root = tree.getroot()

словарь_name_charcode = {}

for valute in root.findall('Valute'):
    name = valute.find('Name').text
    char_code = valute.find('CharCode').text
    словарь_name_charcode[name] = char_code

print("Словарь 'Name - CharCode':")
for name, char_code in словарь_name_charcode.items():
    print(f"{name}: {char_code}")
