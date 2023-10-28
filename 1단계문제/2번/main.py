try:
    with open('mission_computer_main.log') as f:
        full_log_list = f.readlines()

    my_log_list = []
    full_log_list.pop(0) #타임스탬프 라인 제거

    for line in full_log_list:
        split_line = line.split(',')
        date = split_line[0]
        log = split_line[2].rstrip('\n')
        my_log_list.append((date, log))

    # print(my_log_list)
    my_log_dict = dict(my_log_list)


    json_str = '{'
    for time, log in my_log_dict.items():
        json_str += f'"{time}": "{log}",\n'
    json_str = json_str.rstrip(',\n') +'}'

    with open('mission_computer_main.json','w') as f:
        f.write(json_str)

except Exception as e:
    print("Catch exception")


