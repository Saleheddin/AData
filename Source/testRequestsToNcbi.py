
# api_rootURL = 'https://api.ncbi.nlm.nih.gov/variation/v0/'


# url = api_rootURL + 'beta/refsnp/' + '248'
# url1 = requests.get(url)

# url2 = api_rootURL + 'beta/refsnp/' + '1234'
# url2 = requests.get(url)


# url3 = api_rootURL + 'beta/refsnp/' + '1238'
# url3 = requests.get(url)

# url4 = api_rootURL + 'beta/refsnp/' + '1298'
# url4 = requests.get(url)

# url4 = api_rootURL + 'beta/refsnp/' + '1237'
# url4 = requests.get(url)

import bz2
import json
from urllib.request import urlopen


path = "https://ftp.ncbi.nih.gov/snp/latest_release/JSON/refsnp-chrY.json.bz2"
import datetime
print("lauching the programm ")
now1 = datetime.datetime.now()
print(now1)
with urlopen(path) as stream:
    with bz2.BZ2File(stream) as file:
        for i, line in enumerate(file):
            max=i
            # print(i)
            if i == 25000: 
            
                print(line)
                break
            #tweets = json.loads(line)
            #lines.append(tweets)
    
now2 = datetime.datetime.now()
print(now2)
print("total time for this variant : " + str((now2-now1).seconds))
""" import bz2
import json
from urllib.request import urlopen
import linecache
import linecache

# read fifth line


path = "https://ftp.ncbi.nih.gov/snp/latest_release/JSON/refsnp-chrY.json.bz2"
import datetime
print("lauching the programm ")
now1 = datetime.datetime.now()
print(now1)
with urlopen(path) as stream:
    with bz2.BZ2File(stream) as file:
        myline = file.readline(1)
        line = linecache.getline(file, 5)
        print(line)
        print('line')
        print(line)
        for i, line in enumerate(file):
             if(i==200):
                print('---------------------------------------')
                print(line)
                break
        # if i == 10: break
        # if i==0:
        #     print(line)
        #tweets = json.loads(line)
        #lines.append(tweets)
    #print(max)
now2 = datetime.datetime.now()
print(now2) """