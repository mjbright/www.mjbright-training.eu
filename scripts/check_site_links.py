#!/usr/bin/env /Users/mjb/scripts/HASHBANG_PYTHON3_venv.sh tftui
#!/usr/bin/env python3

import sys
import requests
#from bs4 import BeautifulSoup

#url = "https://example.com/news"
url = "https://www.mjbright-training.eu"

check_pages = [ 
               '',
               'fr/',
               'about/',
               'fr/about/',
               ]

check_index_pages = [ 
               'docs/',
               'blog/',
               'cv/',
               'fr/docs/',
               'fr/blog/',
               'fr/cv/',
                     ]

## == Func: ===========================================================================

def die(msg):
    sys.stderr.write(f'die: {msg}\n')
    sys.exit(1)

def getURL(url):
    global num_urls, error_urls
    num_urls += 1

    response = None
    try:
        #response = requests.get(url, params={'s': thing})
        response = requests.get(url)
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print(f'GET {url} => [{response.status_code}] Timedout')
        error_urls.append(url)
        return None
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print(f'GET {url} => [{response.status_code}] Too many redirects')
        error_urls.append(url)
        return None
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print()
        if response:
            print(f'GET {url} => [{response.status_code}] Catastrophique error {e}')
        else:
            print(f'GET {url} => Catastrophique error {e}')
        error_urls.append(url)
        raise SystemExit(e)
        return None

    print(f'GET {url} => [{response.status_code} OK] {len(response.content)} bytes')
    return response

def check_index_page(site_url, index_url):
    global error_urls

    response = requests.get(index_url)

    #print(f'type={ type( str(response.content) ) }')
    for entry in str(response.content).split("href=")[1:]:
        url = entry[1:]

        if entry[0] == '"':
            url = url[ : url.find('"') ]
        elif entry[0] == "'":
            url = url[ : url.find("'") ]
        else:
            url = url[ : url.find(" ") ]

        # print(url)
        if url == '/':
            continue
        if 'favicon' in url:
            continue
        if url.endswith('.css'):
            continue
        if url.endswith('.xml'):
            continue
        if url.endswith('_print/'):
            continue
        if url.startswith('mailto:'):
            continue
        if url.startswith('http:'):
            continue
        if url.startswith('https:'):
            continue

        if url.startswith('/'):
            url = f'{site_url}/{url}'
        else:
            url = f'{index_url}/{url}'

        #response = getURL(f'{index_url}/{url}')
        response = getURL(url)

        if not response: error_urls.append(url)

## == Args: ===========================================================================

if len(sys.argv) > 1:
    if sys.argv[1] == "mjb":
        site_url = "https://www.mjbright-training.eu"
    elif sys.argv[1] == "-l":
        site_url = "http://localhost:1313"
    else:
        site_url = sys.argv[1]

## == Main: ===========================================================================

print()
print(f'Checking site {site_url}/{url}')
print()

error_urls = []
num_urls   = 0

for url in check_pages:
    url = f'{site_url}/{url}'
    response = getURL(url)
    if not response: error_urls.append(url)
    

for url in check_index_pages:
    url = f'{site_url}/{url}'
    #response = requests.get(url)
    response = getURL(url)
    #die("OK")
    check_index_page(site_url, url)

print()
print('SUMMARY')
print('=======')
if len(error_urls) == 0:
    print(f'All {num_urls} links OK')
else:
    print(f'{len(error_urls)} of {num_urls} produced errors:')
    for url in error_urls:
        print('  - ' + url)

#for headline in soup.find_all('h2'):
    #print(headline.text)
sys.exit()
#soup = BeautifulSoup(response.content, 'html.parser')


