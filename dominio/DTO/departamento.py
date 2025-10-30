class departamento:
    def __init__(self,nombre,empleados,gerente,id_departamento):
        self.nombre=nombre
        self.empleados=empleados
        self.gerente=gerente
        self.id_departamento=id_departamento

    def __str__(self):
        return "Nombre:{}\nEmpleados:{}\nGerente::{}\nId_departamento:{}\n".format(self.nombre,self.empleados,self.gerente,self.id_departamento)