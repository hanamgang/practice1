from csv import reader
#csv데이터 리스트 변환
with open('sensor_data1.csv','r')as csv_pile:
    csv_reader=reader(csv_pile)

    list_of_rows = list(csv_reader)
    length=len(list_of_rows)
    t6=[]
    t7=[]
    h6=[]
    h7=[]
    for i in range(1,length):
        k = list_of_rows[i][0]
        mon=k[5:7]
        if mon=='06':
            tem6=list_of_rows[i][1]
            tem6 = float(tem6)
            t6.append(tem6)
        if mon=='07':
            tem7=list_of_rows[i][1]
            tem7 = float(tem7)
            t7.append(tem7)
        if mon == '06':
            hum6 = list_of_rows[i][2]
            hum6 = float(hum6)
            h6.append(hum6)
        if mon == '07':
            hum7 = list_of_rows[i][2]
            hum7 = float(hum7)
            h7.append(hum7)
    numjunetem=len(t6)
    result6t = (sum(t6) / numjunetem)
    numjulytem = len(t7)
    result7t = (sum(t7) / numjulytem)
    numjunehum = len(h6)
    result6h = (sum(h6) / numjunehum)
    numjulyhum = len(h7)
    result7h = (sum(h7) / numjulyhum)
    num = input('6월은 1,7월은 2를 입력하시오 : ')
    while(True):
        if num=='1':
            cho1=input('온도는 1,습도는 2를 입력하시오')
            if cho1=='1':
                print(round(result6t, 2))
            elif cho1=='2':
                print(round(result6h, 2))
            else:
                print('다시 입력하시오')
                continue
            break
        if num=='2':
            cho1=input('온도는 1,습도는 2를 입력하시오')
            if cho1=='1':
                print(round(result7t, 2))
            elif cho1=='2':
                print(round(result7h, 2))
            else:
                print('다시 입력하시오')
                continue
            break
        else:
            print('다시 입력하시오')
            num = input('6월은 1,7월은 2를 입력하시오')
            continue
        break