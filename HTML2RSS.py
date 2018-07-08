# coding: utf8
import sys
from bs4 import BeautifulSoup
import requests
import datetime
from codecs import open
import re
import argparse

class SoupObj:
    def __init__(self, urlfile=None, tag=None, AttrName=None, ValueName=None):
        self.urlfile = urlfile
        self.tag = tag
        self.AttrName = AttrName
        self.ValueName = ValueName
        self.list = []


    def CollectData(self):
        self.urlfile = self.TestFile(str(self.urlfile))
        with self.urlfile as f:
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

        self.urlfile.close()

    def parse_args(self, argv=None):

        self.tag = args.tag
        self.urlfile = self.TestFile(args.file)
        self.AttrName = args.attribute
        self.ValueName = args.value

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
    
    def TestFile(self, files):
        try:
            print(files)
            if files is not None:
                ThisFile = open(files, 'r', encoding='utf-8')
                return ThisFile 
        except Exception as e:
            print("!!! --------Cannot Open the specified file -----!!!!")
            sys.exit()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(    description='''This script will send request to each http adress in a txt file and will parse the html response to a RSS file based on tag name (i.e :"div" or "article"), attribute (i.e : "name" or "id") and value (i.e : "news" or whatever) ''', epilog="""Output in source directory and name will be 'rss_ouput.xml""")
    requiredNamed = parser.add_argument_group('required arguments')
    requiredNamed.add_argument('-uf', '--urlfile', type=str, help = 'This is a simple text file that contains http url one by one . If you want to comment you url file, you can do this by adding a "#" at the begining of the line. The script will simply ignore this line.', required=True)
    requiredNamed.add_argument('-t', '--tag', type=str, help = 'target tag in DOM HTML', required=True)
    requiredNamed.add_argument('-att', '--AttrName', type=str, help ='target attribute of the above tag', required=True)
    requiredNamed.add_argument('-v', '--ValueName', type=str , help='attribute value of the tag', required=True)
    args = parser.parse_args()
    a = SoupObj()
    parser.parse_args(namespace=a)
    a.CollectData()
    a.CreateRSS()







# HtmlParser = SoupObj(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
# HtmlParser.CollectData()
# HtmlParser.CreateRSS()