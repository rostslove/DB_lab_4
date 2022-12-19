import filling_tables

def createFullInsertFile():
    string = open("DB_lab_4\INSERTS\insert_position.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_employee.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_documents.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_documents_participants.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_laboratories.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_employee_in_lab.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_expeditions.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_expedition_crew.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_equipment.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_movements.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_samples.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_research_crew.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_products.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_testing.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_accidents.txt", 'r', encoding="utf-8").read()
    string += open("DB_lab_4\INSERTS\insert_spec_ops.txt", 'r', encoding="utf-8").read()

    stream = open("DB_lab_4\INSERTS\Insert_FULL.txt", 'w', encoding="utf-8")
    stream.write(string)
    stream.close()
    return

createFullInsertFile()