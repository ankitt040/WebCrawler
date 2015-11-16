import urllib.request
from bs4 import BeautifulSoup
import sys

def print_parse_tr( mytr ):
    i=0
    for td in mytr:
        if( str(td).strip() ==''):
            continue
        i+=1
        try:
            if(i==1):
                continue
            elif(i==2):
                print('Contest : ',end='')
            elif(i==3):
                print('start time : ',end='')
            elif(i==4):
                print('end time : ',end='')
            print( td.string)
        except:
            pass

print('* * * * Codechef Contests * * * * ' )

url='https://www.codechef.com/contests'

try:
    html = urllib.request.urlopen(url).readall()
except:
    print('\nConnection Not Available! Please try after sometime !' )
    sys.exit('Could not connect' )

soup = BeautifulSoup(html,"html.parser")

lsit_contests = soup.findAll( 'div',class_="table-questions",limit=2)
contest_type=0
for contest in lsit_contests:
    contest_type+=1
    if( contest_type == 1):
        print('=== ACTIVE CONTESTS ===')
    elif( contest_type == 2):
        print('=== FUTURE CONTESTS ===')
    soup_contest=BeautifulSoup(str(contest),"html.parser")
    my_trs = soup_contest.findAll('tr',attrs={'class': None})
    #print(my_trs)
    for mytr in my_trs:
        print_parse_tr(mytr)
        print()
            
print('\n','done')
input(':hit enter key to close:')

