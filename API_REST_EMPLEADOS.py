import requests
def ExtraerEmpleados(url):
    ###ACCESO API
    empleados = requests.get(url,headers={'User-Agent':'insomnia/2022.1.1', 'accept': '/'})
    ###EXTRACCION RESPUESTA API
    empleados = empleados.json()

    ###EXTRACCION DE DATOS API
    datos = empleados['data']

###LISTAS DE DATOS
    NombresEmpleados = []
    SalariosEmpleados = []
    EdadesEmpleados = []

###ALMACENAR INFORMACION EN LAS LISTAS
    for d in datos:
        NombresEmpleados.append(d['employee_name'])
        SalariosEmpleados.append(d['employee_salary'])
        EdadesEmpleados.append(d['employee_age'])

###1.CUANTOS EMPLEADOS SON
    def TotalEmpleados(lista):
        contador = 0
        for i in lista:
            contador += 1
        return contador
    print(f"EL TOTAL DE LOS EMPLEADOS ES : {TotalEmpleados(NombresEmpleados)} ")

###2.PROMEDIO DE SALARIO DE LOS EMPLEADOS
    def promedio(lista):
        return sum(lista) / len(lista)
    print(f"EL PROMEDIO DE SALARIO DE LOS EMPLEADOS ES DE: ${promedio(SalariosEmpleados)} ")

###3.PROMEDIO DE EDAD DE LOS EMPLEADOS
    print(f"EL PROMEDIO DE EDAD DE LOS EMPLEADOS ES DE: {promedio(EdadesEmpleados)}")

###4.SALARIO MINIMO Y MAXIMO
    def mayor(lista):
        return max(lista)
    def menor(lista):
        return min(lista)
    print(f"EL SALARIO MÍNIMO ES DE: $ {menor(SalariosEmpleados)} Y EL SALARIO MÁXIMO ES DE: ${mayor(SalariosEmpleados)}")

###5.EDAD MENOR Y MAYOR DE LOS EMPLEADOS
    print(f"LA EDAD MENOR DE UN EMPLEADO ES: {menor(EdadesEmpleados)} Y LA EDAD MAYOR DE UN EMPLEADO ES: {mayor(EdadesEmpleados)}")

url = 'https://dummy.restapiexample.com/api/v1/employees'
ExtraerEmpleados(url)




