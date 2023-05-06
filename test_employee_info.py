import employee_info

def test_get_employees_by_age_range():
      new_name_list = []
      result = employee_info.get_employees_by_age_range(24,38)
      test_name_list = ['John', 'Jane','Chloe','Mike']
      for item in result:
          new_name_list.append(item['name'])
      assert(test_name_list == new_name_list)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert (result == 72200)

def test_get_employees_by_dept():
    employees = []
    result = employee_info.get_employees_by_dept('Sales')
    test_name_list = ['John', 'Peter']
    for item in result:
        employees.append(item['name'])
    assert(employees == test_name_list)