# coding: utf8
import sys
from bs4 import BeautifulSoup
import requests
import datetime
from codecs import open
import re


class SoupObj:
    def __init__(self, file, tag, AttrName, ValueName):
        self.source = self.TestFile(file)
        self.tag = tag
        self.AttrName = AttrName
        self.ValueName = ValueName
        self.list = []

    def CollectData(self):
        with self.source as f:
            lines = [line.rstrip('\n') for line in f if re.match('^#', line) is None]
            for url in lines:
                
                try:
                    
                    SendRequest = requests.get(url).text
                    print(f'----- \"for url\" : {url}-----------------')
                    soup = BeautifulSoup(SendRequest, 'lxml')
                    FoundAttibutes = soup.find_all(self.tag, {self.AttrName : str(self.ValueName)})
                    for row in FoundAttibutes:
                        self.list.append(row.text)
                except Exception as e:
                    print(f"!!!!!  cannot open the url {url}   !!!")

        self.source.close()

    def CreateRSS(self):
        date = datetime.datetime.now()
        dateStr = str(date)
        xmlData = open('rss_output.xml', 'w', encoding='utf-8')
        xmlData.write('<?xml version="1.0" encoding=\"UTF-8\"?>' + "\n")
        xmlData.write('<rss version=\"2.0\" xmlns:a10=\"http://www.w3.org/2005/Atom\">' + "\n")
        xmlData.write('    ' + '<channel>' + "\n")
        xmlData.write('        ' +'<title>News</title>' + "\n")
        xmlData.write('        ' +f'<lastBuildDate>{dateStr}</lastBuildDate>' + "\n")
        RowGen = (row for row in self.list if row != "")
        for row in RowGen :
            itemContent = row
            xmlData.write('        ' +'<item>' + "\n")
            xmlData.write(f'             <description>{itemContent}</description>' + "\n")
            xmlData.write('        ' +'</item>' + "\n")
        
        xmlData.write('</channel>' + "\n")
        xmlData.write('</rss>' + "\n")
        xmlData.close()
    
    def TestFile(self, file):
        try:
            ThisFile = open(file, 'r', encoding='utf-8')
            return ThisFile 
        except expression as identifier:
            print("!!! --------Cannot Open the specified file -----!!!!")
            sys.exit()






HtmlParser = SoupObj(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
HtmlParser.CollectData()
HtmlParser.CreateRSS()