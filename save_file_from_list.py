import urllib
import os

with open('url_list.txt') as fp:
    for line in fp:
    	filePath = line.rsplit('/', 2)
    	fileName = filePath[1] + "/" + filePath[2].replace('\n','')
    	os.makedirs(os.path.dirname(fileName))
    	urllib.urlretrieve(line, fileName)
		