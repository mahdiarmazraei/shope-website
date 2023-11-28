from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By
import time
import psycopg2

# conn = psycopg2.connect("dbname=bingx user=postgres")
conn=psycopg2.connect(host ="localhost" ,database="bingx", user="postgres", password="postgres",port="5432")

cur = conn.cursor()
cur.execute("CREATE TABLE cral (id serial PRIMARY KEY, uid varchar , TradingPair varchar ,shortlong varchar , x varchar , OpenPrice varchar , ClosePrice varchar, CloseTime varchar, ROI varchar);")

driver = webdriver.Chrome()
conf_list = open("conf.txt", "r")
for line in conf_list:
    y = line.split()
    a = y[0]
    b = y[1]
    driver.get("https://bingx.com/en-us/CopyTrading/{}/?apiIdentity={}&rankStatisticDays=30&list_id=popular&from=1&accountEnum=BINGX_SWAP_FUTURES".format(a, b))
    element = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div[3]')

    element.click()
    time.sleep(5)
    flag = True
    for i in range(1):
        if flag == False:
            break
        try: 
            clide = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div/div')
            clide.click()
            time.sleep(5)
        except NoSuchElementException: 
            flag = False


    time.sleep(5)
    x = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[2]/div[2]/div/table/tbody').text
    f = open("info.txt", "w")
    f.write(x)
    f.close()
    file = open("info.txt", 'r')

    dict = {}
    list_info = []
    count,idinfo = 0 , 1
    for each in file:
        list_info.append(each.replace("\n",""))
        count += 1
        if count % 7 == 0:
            cur.execute("INSERT INTO bingx (uid, TradingPair, shortlong, x, OpenPrice, ClosePrice, CloseTime, ROI) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (a, list_info[0], list_info[1], list_info[2],list_info[3],list_info[4],list_info[5],list_info[6]))
            conn.commit()
            dict[idinfo] = list_info
            idinfo += 1
            list_info = []

cur.close()
conn.close()
    

