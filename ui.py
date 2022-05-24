
    
def initial():
    surname = input('Ввeдите фамилию абонента: ')
    name = input('Введите имя абонента: ')
    num_phone = input('Введите телефон: ')
    comment = input('Введите краткое описание: ')
    variant = input('Каков будет формат заполнения (1 - в столбик, 2 - в строку): ')
    return(surname, name, num_phone, comment,variant )