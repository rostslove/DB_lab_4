import random
from datetime import datetime, timedelta, date

def random_date(start, end):
    delta = (end - start).days
    rng = random.randrange(1, delta)
    return start + timedelta(days=rng)

def gen_datetime(start=datetime(2020,1,1,00,00,00), end=datetime.now()):
    time = start + (end - start) * random.random()
    return datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)

def position_filling():
    position_data = open("RAW_DATA\position_titles.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Position(Salary, Title) VALUES '
    for i in range(len(position_data) - 1):
        salary = random.randint(2500, 3500)
        if position_data[i] == 'Head of company':
            salary = 5000
        s += f"({salary}, '{position_data[i]}'), "
    salary = random.randint(2500, 3500)
    s += f"({salary}, '{position_data[-1]}');"
    stream = open("INSERTS\insert_position.txt", 'w', encoding="utf-8")
    stream.write(s)
    return len(position_data)

def employee_filling(position_number):
    first_names_data = open("RAW_DATA\employee_first_names.txt", 'r', encoding="utf-8").read().splitlines()
    last_names_data = open("RAW_DATA\employee_last_names.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Employee(Name, Surname, ID_Position) VALUES '
    s += "('Ozwell', 'Spencer', 1), "
    employee_number = random.randint(4000, 5000)
    test_subjects = []
    spec_ops = []
    for i in range(1, employee_number):
        first_name = first_names_data[random.randint(0, len(first_names_data) - 1)]
        last_name = last_names_data[random.randint(0, len(last_names_data) - 1)]
        pos = random.randint(2, position_number)
        s += f"('{first_name}', '{last_name}', '{pos}'), "
        if pos == position_number:
            test_subjects.append(i + 1)
        if pos in range(position_number - 6, position_number):
            spec_ops.append(i + 1)
    first_name = first_names_data[random.randint(0, len(first_names_data) - 1)]
    last_name = last_names_data[random.randint(0, len(last_names_data) - 1)]
    pos = random.randint(1, position_number - 8)
    s += f"('{first_name}', '{last_name}', {pos});"
    stream = open("INSERTS\insert_employee.txt", 'w', encoding="utf-8")
    stream.write(s)
    return employee_number + 1, test_subjects, spec_ops

def documents_filling():
    documents_types_data = open("RAW_DATA\document_types.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Documents(Type, Date) VALUES '
    documents_number = random.randint(4000, 5000)
    for i in range(documents_number - 1):
        doc_type = documents_types_data[random.randint(0, len(documents_types_data) - 1)]
        date_doc = random_date(date(2020, 1, 1), date(2022, 12, 19))
        s += f"('{doc_type}', '{date_doc}'), "
    doc_type = documents_types_data[random.randint(0, len(documents_types_data) - 1)]
    date_doc = random_date(date(2020, 1, 1), date(2022, 12, 19))
    s += f"('{doc_type}', '{date_doc}');"
    stream = open("INSERTS\insert_documents.txt", 'w', encoding="utf-8")
    stream.write(s)
    return documents_number

def documents_participants_filling(employee_number, documents_number):
    s = 'INSERT INTO s311288.Document_participants(ID_Employee, ID_Document) VALUES '
    for i in range(1, documents_number):
        num_participants = random.randint(1, 5)
        for j in range(num_participants):
            id_employee = random.randint(1, employee_number)
            s += f"({id_employee}, {i}), "
    id_employee = random.randint(1, employee_number)
    s += f"({id_employee}, {documents_number});"
    stream = open("INSERTS\insert_documents_participants.txt", 'w', encoding="utf-8")
    stream.write(s)
    return

def laboratory_filling():
    location_data = open("RAW_DATA\locations.txt", 'r', encoding="utf-8").read().splitlines()
    building_states_data = open("RAW_DATA\\building_states.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Laboratory(Location, Building_state) VALUES '
    for i in range(len(location_data) - 1):
        building_state = building_states_data[random.randint(0, len(building_states_data) - 1)]
        s += f"('{location_data[i]}', '{building_state}'), "
    building_state = building_states_data[random.randint(0, len(building_states_data) - 1)]
    s += f"('{location_data[-1]}', '{building_state}');"
    stream = open("INSERTS\insert_laboratories.txt", 'w', encoding="utf-8")
    stream.write(s)
    return len(location_data)

def employee_in_lab_filling(employee_number, laboratory_number):
    s = 'INSERT INTO s311288.Employee_in_lab(ID_Employee, ID_Laboratory) VALUES '
    for i in range(1, employee_number):
        num_labs = random.randint(1, laboratory_number)
        for j in range(num_labs):
            id_lab = random.randint(1, laboratory_number)
            s += f"({i}, {id_lab}), "
    id_lab = random.randint(1, laboratory_number)
    s += f"({employee_number}, {id_lab});"
    stream = open("INSERTS\insert_employee_in_lab.txt", 'w', encoding="utf-8")
    stream.write(s)
    return

def expedition_filling():
    expedition_statuses_data = open("RAW_DATA\expedition_statuses.txt", 'r', encoding="utf-8").read().splitlines()
    expedition_positions_data = open("RAW_DATA\locations.txt", 'r', encoding="utf-8").read().splitlines()
    territories = open("RAW_DATA\wild_territory.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Expedition(Termination_date, Commencement_date, Position, Status, Territory) VALUES '
    expedition_number = random.randint(20,30)
    for i in range(expedition_number - 1):
        status = expedition_statuses_data[random.randint(0, len(expedition_statuses_data) - 1)]
        com_date = random_date(date(2020, 1, 1), date(2022, 12, 19))
        term_date = None
        if status == 'Done':
            term_date = random_date(date(2020, 1, 1), date(2022, 12, 19))
            com_date = random_date(date(2020, 1, 1), term_date)
        pos =  expedition_positions_data[random.randint(0, len(expedition_positions_data) - 1)]
        ter = territories[random.randint(0, len(territories) - 1)]
        if not term_date:
            s += f"('{term_date}', '{com_date}', '{pos}', '{status}', '{ter}'), "
        else:
            s += f"('NULL', '{com_date}', '{pos}', '{status}', '{ter}'), "
    status = expedition_statuses_data[random.randint(0, len(expedition_statuses_data) - 1)]
    com_date = random_date(date(2020, 1, 1), date(2022, 12, 19))
    term_date = None
    if status == 'Done':
        term_date = random_date(date(2020, 1, 1), date(2022, 12, 19))
        com_date = random_date(date(2020, 1, 1), term_date)
    pos =  expedition_positions_data[random.randint(0, len(expedition_positions_data) - 1)]
    if not term_date:
        s += f"('{term_date}', '{com_date}', '{pos}', '{status}', '{ter}');"
    else:
        s += f"('NULL', '{com_date}', '{pos}', '{status}', '{ter}');"
    stream = open("INSERTS\insert_expeditions.txt", 'w', encoding="utf-8")
    stream.write(s)
    return expedition_number

def expidition_crew_filling(employee_number, expedition_number):
    s = 'INSERT INTO s311288.Expedition_crew(ID_Employee, ID_Expedition, Leader_ID) VALUES '
    for i in range(1, expedition_number + 1):
        expiditors_num = random.randint(10, 30)
        group = []
        for j in range(expiditors_num):
            id_emp = random.randint(1, employee_number)
            group.append(id_emp)
        leader = group[random.randint(0, len(group)-1)]
        for j in range(len(group)):
            if j == len(group) - 1 and i == expedition_number:
                s += f"({group[j]}, {i}, {leader});"  
            else:
                s += f"({group[j]}, {i}, {leader}), "
    stream = open("INSERTS\insert_expedition_crew.txt", 'w', encoding="utf-8")
    stream.write(s)
    return

def equipment_filling(laboratory_number, expedition_number):
    equipment_names = open("RAW_DATA\equipment_names.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Equipment(Name, Cost, ID_laboratory, ID_Expedition) VALUES '
    for i in range(len(equipment_names) - 1):
        cost = random.randint(0, 100000)
        id_lab = random.randint(1, laboratory_number)
        id_exp = random.randint(1, expedition_number)
        s += f"('{equipment_names[i]}', {cost}, {id_lab}, {id_exp}), "
    cost = random.randint(0, 100000)
    id_lab = random.randint(1, laboratory_number)
    id_exp = random.randint(1, expedition_number)
    s += f"('{equipment_names[-1]}', {cost}, {id_lab}, {id_exp});"
    stream = open("INSERTS\insert_equipment.txt", 'w', encoding="utf-8")
    stream.write(s)
    return len(equipment_names)

def equipment_movement_filling(equipment_number):
    locations = open("RAW_DATA\locations.txt", 'r', encoding="utf-8").read().splitlines()
    territories = open("RAW_DATA\wild_territory.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Equipment_movement(ID_Equipment, Start_point, End_point, Start_time, End_time) VALUES '
    movements_num = random.randint(4000, 5000)
    start_point, end_point = '', ''
    for i in range(movements_num - 1):
        id_equip = random.randint(1, equipment_number)
        start = random.randint(1, 2)
        if start == 1:
            start_point = locations[random.randint(0, len(locations) - 1)]
            end_point = territories[random.randint(0, len(territories) - 1)]
        else:
            start_point = territories[random.randint(0, len(territories) - 1)]
            end_point = locations[random.randint(0, len(locations) - 1)]
        start_time = gen_datetime()
        end_time = gen_datetime(start_time)
        s += f"({id_equip}, '{start_point}', '{end_point}', '{start_time}', '{end_time}'), "
    id_equip = random.randint(1, equipment_number)
    start = random.randint(1, 2)
    if start == 1:
        start_point = locations[random.randint(0, len(locations) - 1)]
        end_point = territories[random.randint(0, len(territories) - 1)]
    else:
        start_point = territories[random.randint(0, len(territories) - 1)]
        end_point = locations[random.randint(0, len(locations) - 1)]
    start_time = gen_datetime()
    end_time = gen_datetime(start_time)
    s += f"({id_equip}, '{start_point}', '{end_point}', '{start_time}', '{end_time}');"
    stream = open("INSERTS\insert_movements.txt", 'w', encoding="utf-8")
    stream.write(s)
    return movements_num

def sample_filling(exp_number):
    sample_names_data = open("RAW_DATA\sample_names.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Sample(Name, Weight, Detection_timestamp, ID_Expedition) VALUES '
    for i in range(len(sample_names_data) - 1):
        weight = random.uniform(2.0, 20.0)
        detect_time = gen_datetime()
        id_exp = random.randint(1, exp_number)
        s += f"('{sample_names_data[i]}', {weight}, '{detect_time}', {id_exp}), "
    weight = random.uniform(2.0, 20.0)
    detect_time = gen_datetime()
    id_exp = random.randint(1, exp_number)
    s += f"('{sample_names_data[-1]}', {weight}, '{detect_time}', {id_exp});"
    stream = open("INSERTS\insert_samples.txt", 'w', encoding="utf-8")
    stream.write(s)
    return len(sample_names_data)

def research_crew_filling(employee_number, sample_number):
    s = 'INSERT INTO s311288.Research_crew(ID_Employee, ID_Sample, Instructions) Values '
    instructions = open('RAW_DATA\\research_crew_instructions.txt', 'r', encoding="utf-8").read().splitlines()
    for i in range(1, sample_number+1):
        samples_num = random.randint(10, 30)
        group = []
        for j in range(samples_num):
            id_emp = random.randint(1, employee_number)
            group.append(id_emp)
        instruction = instructions[random.randint(0, len(instructions) - 1)]
        for j in range(len(group)):
            if j == len(group) - 1 and i == sample_number:
                s += f"({group[j]}, {i}, '{instruction}');"
            else:
                s += f"({group[j]}, {i}, '{instruction}'), "
    stream = open("INSERTS\insert_research_crew.txt", 'w', encoding="utf-8")
    stream.write(s)
    return


def product_filling(sample_number):
    s = 'INSERT INTO s311288.Product(Class, Version, ID_Sample) Values '
    classes = open("RAW_DATA\product_classes.txt", 'r', encoding="utf-8").read().splitlines()
    for i in range(len(classes) - 1):
        version = str(round(random.uniform(2.0, 20.0), 2))
        id_samp = random.randint(1, sample_number)
        s += f"('{classes[i]}', '{version}', {id_samp}), "
    version = str(round(random.uniform(2.0, 20.0), 2))
    id_samp = random.randint(1, sample_number)
    s += f"('{classes[-1]}', '{version}', {id_samp});"
    stream = open("INSERTS\insert_products.txt", 'w')
    stream.write(s)
    return len(classes)


def testing_filling(test_subjects, product_number):
    s = 'INSERT INTO s311288.Testing(ID_Product, ID_Employee, Results) Values '
    results = open("RAW_DATA\\testing_results.txt", 'r', encoding="utf-8").read().splitlines()
    for i in range(1, product_number+1):
        products_num = random.randint(10, 30)
        group = []
        for j in range(products_num):
            id_emp = random.choice(test_subjects)
            group.append(id_emp)
        result = results[random.randint(0, len(results) - 1)]
        for j in range(len(group)):
            if j == len(group) - 1 and i == product_number:
                s += f"({group[j]}, {i}, '{result}');"
            else:
                s += f"({group[j]}, {i}, '{result}'), "
    stream = open("INSERTS\insert_testing.txt", 'w', encoding="utf-8")
    stream.write(s)
    return

def accidents_filling(products_number):
    locations = open("RAW_DATA\locations.txt", 'r', encoding="utf-8").read().splitlines()
    accident_statuses = open("RAW_DATA\\accident_statuses.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Accident(ID_Product, Territory, Accident_date, News_release_date, Estimated_damage, Victims, Status) VALUES '
    accident_num = random.randint(10, 20)
    for i in range(accident_num - 1):
        id_product = random.randint(0, products_number - 1)
        terr = random.choice(locations)
        acc_date = random_date(date(2020, 1, 1), date(2022, 12, 18))
        news_date = random_date(acc_date, date(2022, 12, 19))
        damage = random.randint(10000000, 100000000)
        victims = random.randint(1000, 500000)
        status = random.choice(accident_statuses)
        s += f"({id_product}, '{terr}', '{acc_date}', '{news_date}', {damage}, {victims}, '{status}'), "
    id_product = random.randint(0, products_number - 1)
    terr = random.choice(locations)
    acc_date = random_date(date(2020, 1, 1), date(2022, 12, 18))
    news_date = random_date(acc_date, date(2022, 12, 19))
    damage = random.randint(10000000, 100000000)
    victims = random.randint(1000, 500000)
    status = random.choice(accident_statuses)
    s += f"({id_product}, '{terr}', '{acc_date}', '{news_date}', {damage}, {victims}, '{status}');"
    stream = open("INSERTS\insert_accidents.txt", 'w', encoding="utf-8")
    stream.write(s)
    return accident_num

def spec_ops_filling(accident_num, spec_ops):
    instructions = open("RAW_DATA\instructions.txt", 'r', encoding="utf-8").read().splitlines()
    s = 'INSERT INTO s311288.Spec_ops(ID_Employee, ID_Accident, Instructions) VALUES '
    for i in range(1, accident_num):
        group_num = random.randint(10, len(spec_ops))
        for j in range(group_num):
            id_emp = random.choice(spec_ops)
            instructs = random.choice(instructions)
            s += f"({id_emp}, {i}, '{instructs}'), "
    id_emp = random.choice(spec_ops)
    instructs = random.choice(instructions)
    s += f"({id_emp}, {accident_num}, '{instructs}');"
    stream = open("INSERTS\insert_spec_ops.txt", 'w', encoding="utf-8")
    stream.write(s)
    return

positions_number = position_filling()
employee_number, test_subjects, spec_ops = employee_filling(positions_number)
documents_number = documents_filling()
documents_participants_filling(employee_number, documents_number)
laboratory_number = laboratory_filling()
employee_in_lab_filling(employee_number, laboratory_number)
expedition_number = expedition_filling()
expidition_crew_filling(employee_number, expedition_number)
equipment_number = equipment_filling(laboratory_number, expedition_number)
movements_number = equipment_movement_filling(equipment_number)
samples_number = sample_filling(expedition_number)
research_crew_filling(employee_number, samples_number)
product_number = product_filling(samples_number)
testing_filling(test_subjects, product_number)
accidents_number = accidents_filling(product_number)
spec_ops_filling(accidents_number, spec_ops)