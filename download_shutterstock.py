import requests
from bs4 import BeautifulSoup 

with open("src_urls.txt", "r", encoding="utf-8", errors="ignore") as urlfile:
    urls = urlfile.readlines()   


for idx, url in enumerate(urls): 
    response = requests.get(url,  headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"})
    if not response:
        print("Skipping " + url)
        print(response.status_code)
        continue
        
    html = response.content  
    soup = BeautifulSoup(html)
    a = soup.find_all('meta', {'data-react-helmet':'true'}) 
    for aa in a: 
        if aa['content'] is not None and aa['content'].endswith('.jpg'):
            furl = aa['content']
            print(furl)
            jpg = requests.get(furl, stream=True)
            if not jpg:
                print("cannot get " + furl)
                continue            
            fname = "%02d_" % idx
            fname = fname + furl[furl.rfind("/")+1:]
            with open(fname, 'wb') as f: 
                for chunk in jpg:
                    f.write(chunk)
                    
            
            