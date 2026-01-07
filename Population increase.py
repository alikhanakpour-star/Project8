name_list = {'Isfahan': 2555, 'Shiraz': 2000, 'Tehran': 2500}
print(name_list)


city =input("enter your city:")
population =int(input("enter city population:"))

def city_population():

    name_list[city] = population

    return name_list


city_population()
print(name_list)