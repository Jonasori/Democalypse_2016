import requests
from bs4 import BeautifulSoup
from urllib2 import Request
import pickle
#from apscheduler.schedulers import BlockingScheduler
import sched


### Democalypse 2016 ###


url='http://fivethirtyeight.com/live-blog/2016-election-results-coverage/'
response = requests.get(url)
html = response.content
soup=BeautifulSoup(html, "lxml")
body = soup.find('body')

#def presidential_race():

# Polls
vote_share=body.findAll(attrs={'class':"site-main"})
prob=str(vote_share)
prob0=prob.split("</")[-80:-40]

print(prob0)

#pres_section=str(vote_share[0])

#print(pres_section)

"""
h_vote_share=str(vote_share[0])
t_vote_share=str(vote_share[1])
hillary=h_vote_share.split('">')[1].split("</")[0]
trump=t_vote_share.split('">')[1].split("</")[0]

# Likelihood
d_part0=body.findAll(attrs={'class':"candidate one dem"})
d_part1=str(d_part0)
h_percent=d_part1.split('</div')[1].split('data-party="D">')[1].split('<')[0]
r_part0=body.findAll(attrs={'class':"candidate three rep"})
r_part1=str(r_part0)
t_percent=r_part1.split('</div')[0].split('data-party="R">')[1].split('<')[0]

# Date
datebody=body.findAll(attrs={'data-tab':"presidency"})
strdate=str(datebody)
date=strdate.split('</span>')[3].split('"')[5]


# if it's easier to grab numbers later, maybe worth putting str() around each number.
content = ("\n" + date + "\n\n" +
        "Poll Results:" + "\n" + "Hillary: " + hillary + "\n" + "Trump: " + trump + "\n\n" +
        "Likelihood of Winning:" + "\n" + "Hillary: " +  h_percent + "%" + "\n" + "Trump: " + t_percent + "%" + "\n\n\n")



f = open('538_predictions.txt', 'a') # a for append
f.write( content )
f.close()

f2=open('538_predictions.txt', 'r')
print(f2.read())
f.close()
"""
