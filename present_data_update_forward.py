import urllib.request
import os
import time

path = "F:/intraQuarter"
def Check_Yahoo():
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    for e in stock_list[1:]:
        try:
            e = e.replace("F:/intraQuarter/_KeyStats\\","")
            link = "https://finance.yahoo.com/quote/"+e.upper()+"/key-statistics"
            resp = urllib.request.urlopen(link).read()

            save = "forward/"+str(e)+".html"
            print(str(e))
            store = open(save,"w")
            store.write(str(resp))
            store.close()

        except Exception as e:
            print(str(e))
            time.sleep(2)


Check_Yahoo()   
		
