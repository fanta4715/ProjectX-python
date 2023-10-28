try:
    with open('mission_computer_main.log') as f:
        lines = f.readlines()

    line_list = []

    for line in lines:
        date = line.split(',')[0]
        line_list.append((date,line))

    line_list.sort(reverse=True, key=lambda x : x[0])


    with open('mission_computer_main_problem.log','w',encoding='UTF-8') as problem_file:
        for date,line in line_list:
            if 'Oxygen tank explosion' in line or 'Oxygen tank unstable' in line:
                problem_file.write(line)
            print(line, end='')

except Exception as e:
    print("exception catch", e)


