import random
from datetime import datetime, timedelta

def random_date(start, end):
    delta = (end - start).days
    rng = random.randrange(1, delta)
    return start + timedelta(days=rng)

def gen_datetime(start=datetime(2020,1,1,00,00,00), end=datetime.now()):
    time = start + (end - start) * random.random()
    return datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)



def position_filling():
    position_data = open("DB_lab_4\RAW_DATA\position_titles.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Position(Salary, Title) VALUES '
    for i in range(len(position_data) - 1):
        salary = random.randint(2500, 3500)
        if position_data[i] == 'Head of company':
            salary = 5000
        s += f'({salary}, {position_data[i]}), '
    salary = random.randint(2500, 3500)
    s += f'({salary}, {position_data[-1]});'
    stream = open("DB_lab_4\INSERTS\insert_postion.txt", 'w')
    stream.write(s)
    return len(position_data)

def employee_filling(position_number):
    first_names_data = open("DB_lab_4\RAW_DATA\employee_first_names.txt", 'r', encoding="utf-8").read().splitlines()
    last_names_data = open("DB_lab_4\RAW_DATA\employee_last_names.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Employee(Name, Surname, ID_Position) VALUES '
    s += '(Ozwell, Spencer, 1), '
    employee_number = random.randint(4000, 5000)
    test_subjects = []
    spec_ops = []
    for i in range(1, employee_number):
        first_name = first_names_data[random.randint(0, len(first_names_data) - 1)]
        last_name = last_names_data[random.randint(0, len(last_names_data) - 1)]
        pos = random.randint(2, position_number)
        s += f'({first_name}, {last_name}, {pos}), '
        if pos == position_number:
            test_subjects.append(i + 1)
        if pos in range(position_number - 6, position_number):
            spec_ops.append(i + 1)
    first_name = first_names_data[random.randint(0, len(first_names_data) - 1)]
    last_name = last_names_data[random.randint(0, len(last_names_data) - 1)]
    pos = random.randint(1, position_number - 8)
    s += f'({first_name}, {last_name}, {pos});'
    stream = open("DB_lab_4\INSERTS\insert_employee.txt", 'w')
    stream.write(s)
    return employee_number + 1, test_subjects, spec_ops

def documents_filling():
    documents_types_data = open("DB_lab_4\RAW_DATA\document_types.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Documents(Type, Date) VALUES '
    documents_number = random.randint(4000, 5000)
    for i in range(documents_number - 1):
        doc_type = documents_types_data[random.randint(0, len(documents_types_data) - 1)]
        date = random_date(datetime.date(2020, 1, 1), datetime.date(2022, 12, 19))
        if i % 2000 == 0:
            s += f'({doc_type}), '
        else:
            s += f'({doc_type}, {date}), '
    doc_type = documents_types_data[random.randint(0, len(documents_types_data) - 1)]
    s += f'({doc_type});'
    stream = open("DB_lab_4\INSERTS\insert_documents.txt", 'w')
    stream.write(s)
    return documents_number

def documents_participants_filling(employee_number, documents_number):
    s = 'INSERT INTO s311288.Document_participants(ID_Employee, ID_Document) VALUES '
    for i in range(1, documents_number):
        num_participants = random.randint(1, 5)
        for j in range(num_participants):
            id_employee = random.randint(1, employee_number)
            s += f'({id_employee, i}), '
    id_employee = random.randint(1, employee_number)
    s += f'({id_employee}, {documents_number});'
    stream = open("DB_lab_4\INSERTS\insert_documents_participants.txt", 'w')
    stream.write(s)
    return

def laboratory_filling():
    location_data = open("DB_lab_4\RAW_DATA\locations.txt", 'r', encoding="utf-8").read().splitlines()
    building_states_data = open("DB_lab_4\RAW_DATA\building_states.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Laboratory(Location, Building_state) VALUES '
    for i in range(len(location_data) - 1):
        building_state = building_states_data[random.randint(0, len(building_states_data) - 1)]
        s += f'({location_data[i]}, {building_state}), '
    building_state = building_states_data[random.randint(0, len(building_states_data) - 1)]
    s += f'({location_data[-1]}, {building_state});'
    stream = open("DB_lab_4\INSERTS\insert_laboratories.txt", 'w')
    stream.write(s)
    return len(location_data)

def employee_in_lab_filling(employee_number, laboratory_number):
    s = 'INSERT INTO s311288.Employee_in_lab(ID_Employee, ID_Laboratory) VALUES '
    for i in range(1, employee_number):
        num_labs = random.randint(1, laboratory_number)
        for j in range(num_labs):
            id_lab = random.randint(1, laboratory_number)
            s += f'({i, id_lab}), '
    id_lab = random.randint(1, laboratory_number)
    s += f'({employee_number, id_lab});'
    stream = open("DB_lab_4\INSERTS\insert_employee_in_lab.txt", 'w')
    stream.write(s)
    return

def expedition_filling():
    expedition_statuses_data = open("DB_lab_4\RAW_DATA\expedition_statuses.txt", 'r', encoding="utf-8").read().splitlines()
    expedition_positions_data = open("DB_lab_4\RAW_DATA\locations.txt", 'r', encoding="utf-8").read().splitlines()
    territories = open("DDB_lab_4\RAW_DATA\wild_territory.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Expedition(Termination_date, Commencement_date, Position, Status, Territory) VALUES '
    expedition_number = random.randint(20,30)
    for i in range(expedition_number - 1):
        status = expedition_statuses_data[random.randint(0, len(expedition_statuses_data) - 1)]
        com_date = random_date(datetime.date(2020, 1, 1), datetime.date(2022, 12, 19))
        term_date = None
        if status == 'Done':
            term_date = random_date(datetime.date(2020, 1, 1), datetime.date(2022, 12, 19))
            com_date = random_date(datetime.date(2020, 1, 1), term_date)
        pos =  expedition_positions_data[random.randomint(0, len(expedition_positions_data) - 1)]
        ter = territories[random.randomint(0, len(territories) - 1)]
        s += f'({term_date}, {com_date}, {pos}, {status}, {ter}), '
    status = expedition_statuses_data[random.randint(0, len(expedition_statuses_data) - 1)]
    com_date = random_date(datetime.date(2020, 1, 1), datetime.date(2022, 12, 19))
    term_date = None
    if status == 'Done':
        term_date = random_date(datetime.date(2020, 1, 1), datetime.date(2022, 12, 19))
        com_date = random_date(datetime.date(2020, 1, 1), term_date)
    pos =  expedition_positions_data[random.randomint(0, len(expedition_positions_data) - 1)]
    s += f'({term_date}, {com_date}, {pos}, {status}, {ter});'
    stream = open("DB_lab_4\INSERTS\insert_expiditions.txt", 'w')
    stream.write(s)
    return expedition_number

def expidition_crew_filling(employee_number, expidition_number):
    s = 'INSERT INTO s311288.Expedition_crew(ID_Employee, ID_Expedition, Leader_ID) VALUES '
    for i in range(1, expidition_number + 1):
        expiditors_num = random.randint(10, 30)
        group = []
        for j in range(expiditors_num):
            id_emp = random.randint(1, employee_number)
            group.append(id_emp)
        leader = group[random.randint(0, len(group)-1)]
        for j in range(len(group)):
            if j == len(group) - 1 and i == expidition_number:
                s += f'({group[j]}, {i}, {leader});'  
            else:
                s += f'({group[j]}, {i}, {leader}), '
    stream = open("DB_lab_4\INSERTS\insert_expidition_crew.txt", 'w')
    stream.write(s)
    return

def equipment_filling(laboratory_number, expidition_number):
    equipment_names = open("DB_lab_4\RAW_DATA\equipment_names.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Equipment(Name, Cost, ID_laboratory, ID_Expedition VALUES '
    for i in range(len(equipment_names) - 1):
        cost = random.randint(0, 100000)
        id_lab = random.randint(1, laboratory_number)
        id_exp = random.randint(1, expidition_number)
        s += f'({equipment_names[i]}, {cost}, {id_lab}, {id_exp}), '
    cost = random.randint(0, 100000)
    id_lab = random.randint(1, laboratory_number)
    id_exp = random.randint(1, expidition_number)
    s += f'({equipment_names[-1]}, {cost}, {id_lab}, {id_exp});'
    stream = open("DB_lab_4\INSERTS\insert_laboratories.txt", 'w')
    stream.write(s)
    return len(equipment_names)

def equipment_movement_filling(equipment_number):
    locations= open("DB_lab_4\RAW_DATA\locations.txt", 'r', encoding="utf-8").read().splitlines()
    territories = open("DDB_lab_4\RAW_DATA\wild_territory.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Equipment_movement(ID_Equipment, Start_point, End_point, Start_time, End_time VALUES '
    movements_num = (4000, 5000)
    start_point, end_point = '', ''
    for i in range(movements_num - 1):
        id_equip = random.randint(1, equipment_number)
        start = random.randint(1, 2)
        if start == 1:
            start_point = locations[random.randomint(0, len(locations) - 1)]
            end_point = territories[random.randomint(0, len(territories) - 1)]
        else:
            start_point = territories[random.randomint(0, len(territories) - 1)]
            end_point = locations[random.randomint(0, len(locations) - 1)]
        start_time = gen_datetime()
        end_time = gen_datetime(start_time)
        s += f'({id_equip}, {start_point}, {end_point}, {start_time}, {end_time}), '
    id_equip = random.randint(1, equipment_number)
    start = random.randint(1, 2)
    if start == 1:
        start_point = locations[random.randomint(0, len(locations) - 1)]
        end_point = territories[random.randomint(0, len(territories) - 1)]
    else:
        start_point = territories[random.randomint(0, len(territories) - 1)]
        end_point = locations[random.randomint(0, len(locations) - 1)]
    start_time = gen_datetime()
    end_time = gen_datetime(start_time)
    s += f'({id_equip}, {start_point}, {end_point}, {start_time}, {end_time});'
    stream = open("DB_lab_4\INSERTS\insert_movements.txt", 'w')
    stream.write(s)
    return movements_num