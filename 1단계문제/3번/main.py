try:
    # list.csv 열기
    with open('Mars_Base_Inventory_List.csv','r') as f:
        full_list = f.readlines()

    full_list.pop(0)

    array=[]

    # ,단위로 split해서 list 형식으로 append
    for line in full_list:
        array.append(line.rstrip('\n').split(','))

    array.sort(reverse=True, key=lambda x:x[4])

    f = open('Mars_Base_Inventory_danger.csv','w')
    for line in array:
        if float(line[4]) >= 0.7:
            print(line)
            f.write(line[0]+" "+line[1]+" "+line[2]+" "+line[3]+'\n')

    #인화성 높은 순으로 출력
    #인화성 지수 0.7 목록 출력 & csv포멧으로 저장
except Exception as e:
    print("Exception catch",e)