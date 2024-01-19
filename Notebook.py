def work_with_notebook(notebook):
     while True:
        print('М е н ю :')
        choice = input('1 - Просмотреть все заметки\n2 - Создать заметку\n3 - Найти заметку\n\
4 - Редактировать заметку\n5 - Удалить заметку\n6 - Копировать данные \n0 - Выйти из приложения\n')
        if choice == '1':
            print_result(notebook)
        elif choice == '2':
            add_note(notebook)
        elif choice == '3':
            note_list = read_file_to_dict(notebook)
            find_note(note_list)
        elif choice == '4':
            edit_note(notebook)
        elif choice == '5':
            delete_note(notebook)
        elif choice == '6':
            file_to_copy = input('Введите название копируемого файла: ')
            copy_data(file_to_copy, notebook) 
        elif choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!') 
            continue
def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Идентификатор','Заголовок' ,'Описание','Дата/Время создания']
    note_list = []
    for line in lines:
        line = line.strip().split()
        note_list.append(dict(zip(headers,line)))
    return note_list

def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        note_list = []
        for line in file.readlines():
            note_list.append(line.split())
    return note_list

def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - Идентификатор\n2 - Заголовок\n3 - Дата/Время создания\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите "Идентификатор" для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите "Заголовок"для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите "Дату/Время создания" для поиска: ')
        print()
    return search_field, search_value

def find_note(note_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Идентификатор', '2': 'Заголовок', '3': 'Дата/Время создания'}
    found_notes = []
    for note in note_list:
        if note[search_value_dict[search_field]] == search_value:
            found_notes.append(note)
    if len(found_notes) == 0:
        print('Заметка не найдена!')
    else:
        print_notes(found_notes)
    print()

def get_new_note():
    id = input('Введите Идентификатор: ')
    title = input('Введите Заголовок: ')
    description = input('Введите Описание: ')
    date_time = input('Введите Дату/Время создания: ')
    print("Заметка  успешно добавлена!")
    return id, title,  description ,date_time

def add_note(file_name):
    info = ';'.join(get_new_note())
    with open(file_name, 'a', encoding='utf-8') as file:
        
        file.write(f'{info}\n' )

def print_result(file_name):
    list_of_notes = sorted(read_file_to_dict(file_name), key=lambda x: x['Идентификатор'])
    print_notes(list_of_notes)
    print()
    return list_of_notes

def search_contact(note_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for note in note_list:
        if note[int(search_field) - 1] == search_value:
            search_result.append(note)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()

def edit_note(file_name):
    note_list = read_file_to_list(file_name)
    note_to_change = search_contact(note_list)
    note_list.remove(note_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        note_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        note_to_change[1] = input('Введите имя: ')
    elif field == '3':
        note_to_change[2] = input('Введите номер телефона: ')
    note_list.append(note_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for note in note_list:
            line = ' '.join(note) + '\n'
            file.write(line)

def delete_note(file_name):
    note_list = read_file_to_list(file_name)
    note_to_change = search_contact(note_list)
    note_list.remove(note_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for note in note_list:
            line = ' '.join(note) + '\n'
            file.write(line)

def print_notes(note_list: list):
    for note in note_list:
        words = []
        for value in note.values():
            words.append(str(value))
        print(" ".join(words))

def copy_data(file_to_add, notebook):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_notes, open(notebook, 'a', encoding='utf-8') as file:
            notes_to_add = new_notes.readlines()
            file.writelines(notes_to_add)
            
            line_note = int(input("Введите номер строки для переноса: "))
            if line_note <= len(notes_to_add):
                file.write(notes_to_add[line_note - 1])
                print("Данные успешно перенесены.")
            else:
                print("Недопустимый номер строки.")
    except FileNotFoundError:
        print(f'{file_to_add} не найден')

if __name__ == '__main__':
    file = 'Phonebook.txt'
    work_with_notebook(file)