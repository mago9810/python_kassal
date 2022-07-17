DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # empleados_python = [empleados['name'] for empleados in DATA  if empleados['language'] == "python"]
    empleados_python = list(filter(lambda empleados: empleados['language'] == "python", DATA)) 
    empleados_python = list(map(lambda empleado: empleado['name'] ,empleados_python ))
    # all_platzi_workers = [empleados['name'] for empleados in DATA if empleados['organization'] == 'Platzi']
    all_platzi_workers = list(filter(lambda empleados: empleados['organization'] == 'Platzi' ,DATA))
    all_platzi_workers = list(map(lambda empleados: empleados['name'], all_platzi_workers))


    # adults = list(filter(lambda trabajador: trabajador['age'] > 18 ,DATA))
    # adults = list(map(lambda trabajador: trabajador['name'], DATA))

    adults = [trabajador['name'] for trabajador in DATA if trabajador['age'] > 18]


    # for empleados in empleados_python:
    #     print(empleados)

    # for empleados_platzi in all_platzi_workers:
    #     print(empleados_platzi)

    for empleados in adults:
        print(empleados)


if __name__ == '__main__':
    run()