#!/usr/bin/python3

# Author :   Turfa Auliarachman
# Date   :   October 20, 2016
# Inspired by Arrizal Amin's work

import urllib.request
import urllib.parse
import urllib.error
import json
import sys
import markdown2
import os
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

class HTTPRequest:
    def __init__(self, root):
        self.root = root

    def POST(self, address, data):
        data = urllib.parse.urlencode(data)
        data = data.encode('utf8')
        req = urllib.request.Request(self.root+address, data)

        return urllib.request.urlopen(req).read()

    def GET(self, address, data):
        data = urllib.parse.urlencode(data)
        req = urllib.request.Request(self.root+address+'?'+data)

        return urllib.request.urlopen(req).read()

class LanguageTool(HTTPRequest):
    def __init__(self, root = "https://languagetool.org/api/v2/"):
        super().__init__(root)

    def getLanguages(self):
        try:
            return json.loads(self.GET('languages','').decode('utf8'))
        except:
            return 'Error'

    def check(self, language, text):
        data = {'language' : language, 'text' : text};
        return json.loads(self.POST('check', data).decode('utf8'))


if __name__ == '__main__':
    print('https://languagetool.org/ API Consumer')
    print('Author : Turfa Auliarachman')
    print('Date : October 20, 2016')
    print('-'*50)
    print()

    LTool = LanguageTool()

    def usage():
        print("Usage : {} languages\n".format(str(sys.argv[0])))
        print("Usage : {} check <language> <filename>\n".format(str(sys.argv[0])))

    def languages():
        for element in LTool.getLanguages():
            print('Language : "{}", Code : "{}"'.format(element['name'], element['longCode']))

    def check():
        if (len(sys.argv)!=4):
            usage()
        else:
            text = ""

            try:
                text = open(sys.argv[3]).read()
            except:
                print("Error opening file")

            if (os.path.splitext(sys.argv[3])[1]=='.md'):
                text = strip_tags(markdown2.markdown(text))

            for err in LTool.check(sys.argv[2], text)['matches']:
                if (len(err['replacements'])>0):
                    print(err['message'])

                    print('Replacements :')
                    print(err['replacements'])

                    print('Context :')
                    print(err['context'])

                    print()
                    print()
                    print()


    if (len(sys.argv)==1):
        usage()
    elif (sys.argv[1]=='languages'):
        languages()
    elif (sys.argv[1]=='check'):
        check()
    else:
        usage()
