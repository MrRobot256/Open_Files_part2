import xml.etree.ElementTree as ET

def open_xml(file):
    pars = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file, pars)
    root = tree.getroot()

    return root

def create_list(file_open):
    xml_file = file_open.findall('channel/item')
    list_desc = []

    for item in xml_file:
        desc = item.find('description')
        list_desc.extend(desc.text.split())

    return list_desc

def get_ten_rated(descriptions_list):
    dict_word = {}
    rated_list = []

    for word in descriptions_list:
        if len(word) > 6:
            if word in dict_word:
                dict_word[word] += 1
            else:
                dict_word[word] = 1
        else:
            continue

    for key, value in dict_word.items():
        rated_list.append((value, key))
    rated_list.sort(reverse=True)

    for item in rated_list[:10]:
        print(f'{item[1]}: {item[0]}')

get_ten_rated(create_list(open_xml('newsafr.xml')))
