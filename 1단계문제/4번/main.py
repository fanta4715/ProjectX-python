

#입력은 cm라고 가정하자.
def sphere_area(this_diameter,  this_material='유리',this_thickness=1.0):
    #(diameter/2)**2 * 3.1415 * 2 * thickness가 면적임
    # 면적에 해당하는 유리, 알루미늄,탄소강의 가중치를 곱해준다.
    global material, diameter, thickness, area, weight
    diameter=this_diameter
    thickness = this_thickness
    material = this_material
    area = (this_diameter/2)**2 * 3.1415 * 2
    weight = area * float(thickness) * weightConvert(material) / 1000


def weightConvert(material):
    if material=='유리':
        return 2.4
    elif material=='알루미늄':
        return 2.7
    else:
        return 7.85


if __name__ == '__main__':
    while (True):
        my_vars_str = input("지름,재료,두께를 입력하세요. 종료를 원하시면 -1을 입력하세요")
        my_vars_list = my_vars_str.split(" ")
        if my_vars_list[0] == '-1':
            break

        if len(my_vars_list) == 1: sphere_area(float(my_vars_list[0]))
        elif len(my_vars_list) == 2: sphere_area(float(my_vars_list[0]), my_vars_list[1])
        else : sphere_area(float(my_vars_list[0]), my_vars_list[1], float(my_vars_list[2]))

        print(f'재질==>{material}, 지름==>{diameter}, 두께==>{thickness}, 면적==>{round(area,3)}, 무게==>{round(weight,3)}kg')





