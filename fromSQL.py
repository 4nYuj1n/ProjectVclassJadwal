import mysql.connector
import os
import sys
from datetime import datetime
def run():
    mydb=mysql.connector.connect(
        host="localhost",
        user="jossie",
        password="1234",
        database="tugas"
    )
 
    today_date=int(input("Masukkan tanggal hari ini: "))
    today_month=int(input("Masukkan bulan saat ini: "))
    mycursor=mydb.cursor()
    mycursor.execute("SELECT nama_matkul,nama_tugas,tanggal,bulan FROM vclass ORDER BY bulan asc,tanggal asc")
    result=mycursor.fetchall()


    
    open(os.path.join(sys.path[0],'D:\ProgrammingThing\ProjectVclassJadwal\ListAkhir.txt'), 'w').close()
    with open(os.path.join(sys.path[0],'D:\ProgrammingThing\ProjectVclassJadwal\ListAkhir.txt'),'r+') as list_akhir:
        #vclass
        list_akhir.writelines("Tugas dari Vclass: \n")
        tanggal_bef=0
        bulan_bef=0
        list_tugas=[]
        tugas_no_deadline=[]
        for i in result:
            if(i[3]>=today_month and i[2]>=today_date):
                if (bulan_bef!=i[3] or tanggal_bef!=i[2]) and bulan_bef!=0 and i[2]!=99:
                    list_akhir.writelines(str(tanggal_bef)+'/'+str(bulan_bef)+'\n')
                    for cnt,tugas in enumerate(list_tugas):
                        list_akhir.writelines(str(cnt+1)+'. '+tugas[0]+' : '+tugas[1]+'\n')
                    list_tugas=[]
                    list_tugas.append([])
                    list_tugas[len(list_tugas)-1].append(i[0])
                    list_tugas[len(list_tugas)-1].append(i[1])
                    bulan_bef=i[3]
                    tanggal_bef=i[2]
                elif i[2]==99:
                    tugas_no_deadline.append(i[0]+' : '+i[1]+'\n')
                      
                else:
                    list_tugas.append([])
                    list_tugas[len(list_tugas)-1].append(i[0])
                    list_tugas[len(list_tugas)-1].append(i[1])
                    bulan_bef=i[3]
                    tanggal_bef=i[2]
        if len(list_tugas)!=0:
            list_akhir.writelines(str(tanggal_bef)+'/'+str(bulan_bef)+'\n')
            for cnt,tugas in enumerate(list_tugas):
                list_akhir.writelines(str(cnt+1)+'. '+tugas[0]+' : '+tugas[1]+'\n')
        list_akhir.writelines("Tugas tanpa deadline\n")
        for cnt,i in enumerate(tugas_no_deadline):
            list_akhir.writelines(str(cnt+1)+'. '+i)
        #manual
        mycursor=mydb.cursor()
        mycursor.execute("SELECT nama_pelajaran,deskripsi FROM manual")
        result=mycursor.fetchall()
        list_akhir.writelines("\n")
        list_akhir.writelines("Tugas yang diberikan secara lisan: \n")
        list_tugas=[]
        for cnt,i in enumerate(result):
            list_akhir.writelines(str(cnt+1)+'.'+i[0]+'\n'+i[1]+'\n')
        list_akhir.writelines('\n')

if __name__=='__main__':
    run()        
                
