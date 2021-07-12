from csv import reader
#csv데이터 리스트 변환
with open('sensor_data1.csv','r')as csv_pile:
    csv_reader=reader(csv_pile)

    list_of_rows = list(csv_reader)
    length=len(list_of_rows)
    aa=[]
    for i in range(1,length):
        k = list_of_rows[i][0]
        mon=k[5:7]
        if mon=='06':
            tem=list_of_rows[i][1]
            tem = float(tem)
            aa.append(tem)

    numjunetem=len(aa)
    print(sum(aa)/numjunetem)
