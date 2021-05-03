import mysql.connector
import os
import sys
def run():
    mydb=mysql.connector.connect(
        host="localhost",
        user="jossie",
        password="1234",
        database="tugas"
    )
    mycursor=mydb.cursor()
    hari={
        'Monday':'Senin',
        'Tuesday':'Selasa',
        'Wednesday':'Rabu',
        'Thursday':'Kamis',
        'Friday':'Jumat',
        'Saturday':'Sabtu',
        'Sunday':'Minggu',
        'Null':'Null'
    }
    sql="DELETE FROM vclass"
    mycursor.execute(sql)
    mydb.commit()
    #print("Data deleted")
    bulan=['January','February','March','April','May','June','July','August','September','October','November','December','Null']
    with open(os.path.join(sys.path[0],'D:\ProgrammingThing\ProjectVclassJadwal\ListTugas.txt'),'r') as list_tugas:
        temp=list_tugas.readlines()
        satu_matkul=[]
        for cnt,i in enumerate(temp):
            if(cnt%3==0):
                satu_matkul=[]
                satu_matkul.append(i[:len(i)-2:1])
            elif(cnt%3==1):
                satu_matkul.append(i[:len(i)-1:1])
            else:
                temp_list=i.split(' ')
                hari_matkul=temp_list[0]
                tanggal_matkul=temp_list[1]
                bulan_matkul=temp_list[2]
                hari_matkul=hari_matkul[:len(hari_matkul)-1:1]
                satu_matkul.append(hari[hari_matkul])
                satu_matkul.append(tanggal_matkul)
                satu_matkul.append(bulan.index(bulan_matkul)+1)
                #print(satu_matkul)
                sql="INSERT INTO vclass VALUES(%s,%s,%s,%s,%s)"
                val=(satu_matkul[0],satu_matkul[1],satu_matkul[2],satu_matkul[3],satu_matkul[4])
                mycursor.execute(sql,val)
                mydb.commit()
if __name__=="__main__":
    run()

                    