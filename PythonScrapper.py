from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import sys

def run():
    options=Options()
    options.headless=True
    options.add_argument("--window-size=1920,1200")
    #reading input from txt
    with open(os.path.join(sys.path[0],'D:\ProgrammingThing\ProjectVclassJadwal\LoginInfo.txt'),'r') as login:
        read_data=login.readlines()
    username=read_data[0]
    password=read_data[1]

    #getting driver ready
    DRIVER_PATH='D:\ProgrammingThing\chromedriver\chromedriver.exe'
    driver = webdriver.Chrome(DRIVER_PATH)

    #login to vclass
    driver.get("https://v-class.gunadarma.ac.id/login/index.php")
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("username").send_keys(username)


    #getting all web link(doesnt need to be runned everytime, only check when web link changed)
    #with open(os.path.join(sys.path[0],'weblist.txt'),'w') as web:
        #for i in soup.findAll('div',{'class':'column c1'}):
            #web.write(i.a['href']+'\n')

    #getting web into list
    link_list=[]
    with open(os.path.join(sys.path[0],'D:\ProgrammingThing\ProjectVclassJadwal\weblist.txt'),'r') as link:
        temp=link.read()
        temp2=temp.splitlines()
    for i in temp2:
        link_list.append(i)

    #checking the web one by one and getting data
    open(os.path.join(sys.path[0],'D:\ProgrammingThing\ProjectVclassJadwal\ListTugas.txt'), 'w').close()
    hari=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    with open(os.path.join(sys.path[0],'D:\ProgrammingThing\ProjectVclassJadwal\ListTugas.txt'),'r+') as kertas:
        for i in link_list:
            temp_hasil=[]
            #kertas.writelines("=========================================================\n")
            #temp_hasil.append("=========================================================\n")
            driver.get(i)
            soup=BeautifulSoup(driver.page_source,'html.parser')
            #kertas.writelines(soup.h1.text+"\n")
            #mengambil nama pelajaran
            judul=soup.h1.text.split('|')
            #cnt=0
            cnt_all=0





            #kertas.writelines("Assignment:\n")
            #temp_hasil.append("Assignment:\n")
            #mencari assignment
            for j in soup.findAll(('li'),{'class':'activity assign modtype_assign'}):
                #kertas.writelines(j.find(('span'),{'class':'instancename'}).text+'\n')
                temp_hasil.append(j.find(('span'),{'class':'instancename'}).text+'\n')
                #cnt+=1
                cnt_all+=1
                driver.get(j.a['href'])
                soup=BeautifulSoup(driver.page_source,'html.parser')
                temp=soup.find(('td'),{'class':'cell c1 lastcol'}).text
                hasil=temp.split("\n")
                kumpul_akhir="Null, 99 Null 999, 99:99 PM"
                for teks in hasil:
                    for day in hari:
                        if day in teks:
                            kumpul_akhir=teks
                            break
                #kertas.writelines(kumpul_akhir+'\n')
                temp_hasil.append(kumpul_akhir+'\n')
            #if(cnt==0):
                #kertas.writelines("none\n")
                #temp_hasil.append("none\n")
        # kertas.writelines('\n')
        # temp_hasil.append('\n')
            #cnt=0




            #kertas.writelines("Quiz:\n")
         #temp_hasil.append("Quiz:\n")
            #mencari quiz
            for j in soup.findAll(('li'),{'class':'activity quiz modtype_quiz'}):
                #kertas.writelines(j.text+'\n')
                temp_hasil.append(j.text+'\n')
                #cnt+=1
                cnt_all+=1
                driver.get(j.a['href'])
                soup=BeautifulSoup(driver.page_source,'html.parser')
                temp=soup.find(('div'),{'class':'box py-3 quizinfo'}).text
                hasil=temp.split("\n")
                kumpul_akhir="Null, 99 Null 9999, 99:99 PM"
                for teks in hasil:
                    for day in hari:
                        if day in teks:
                            kumpul_akhir=teks
                            posisi_hari=kumpul_akhir.find(day)
                            kumpul_akhir=kumpul_akhir[posisi_hari:len(kumpul_akhir):1]
                            break
            # kertas.writelines(kumpul_akhir+'\n')
                temp_hasil.append(kumpul_akhir+'\n')
            #if(cnt==0):
            # kertas.writelines("none\n")
            #temp_hasil.append("none\n")






            if cnt_all>=1:
                for cnt,k in enumerate(temp_hasil):
                    if(cnt%2==0):
                        kertas.writelines(judul[2][1::1]+'\n')
                    kertas.writelines(k)
    driver.close()
if __name__=='__main__':
    run()
        
    