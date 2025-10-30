class empleado:
    def __init__(self,nombre,direccion,telefono,correo,fecha_contrato,salario,departamento,id_empleado):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.correo=correo
        self.fecha_contrato=fecha_contrato
        self.salario=salario
        self.departamento=departamento
        self.if_empleado=id_empleado

    def __str__(self):
        return "nombre:{}\ndireccion:{}\ntelefono:{}\ncorreo:{}\nfecha_contrato:{}\nSalario:${}\n,Departamento:{}\nId_empleado".format(self.nombre,self.direccion,self.telefono,self.correo,
                                                                                                                                    self.fecha_contrato,self.salario,self.departamento,self.if_empleado)