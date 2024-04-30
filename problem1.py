def read_employees(file_path):
    employees = []
    with open(file_path, 'r', encoding='utf-8') as file:
        employees = file.readlines()
    return employees


def write_employees(file_path, employees):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(employees)


def main():

    employees = read_employees("C:\\Users\\User\\PycharmProjects\\buteel\\employees1.txt")





    retired_employees = []
    active_employees = []


    for employee in employees:
        if "тэтгэвэрт гарсан" in employee:
            retired_employees.append(employee)
        else:
            active_employees.append(employee)


    write_employees("C:\\Users\\User\\PycharmProjects\\buteel\\darkhan_database.txt", retired_employees)


    write_employees("C:\\Users\\User\\PycharmProjects\\buteel\\employees1.txt", active_employees)

    print("Тэтгэвэрт гарсан ажилчдыг шилжүүлж дууслаа. Үндсэн ажилчидаас мөн хаслаа")


if __name__ == "__main__":
    main()