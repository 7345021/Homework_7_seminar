from datetime import datetime
# import ui


def var( surname, name, num_phone, comment, variant):
    if variant == '1':
        file = open('in log.csv', 'a')
        file.write(f'{datetime.today()}\n{surname}\n{name}\n{num_phone}\n{comment}\n\n')
        file.close()
    if variant == '2':
        with open('in log.csv', 'a') as file:
            file.write(f'{datetime.today()};{surname};{name};{num_phone};{comment}\n\n')
            file.close()