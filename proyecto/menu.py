'''
Función principal con un menú, donde el usuario elige lo que desea realizar, con una serie de opciones. 
Se importan los diferentes módulos que contienen las funciones que manejan las bases de datos.
'''
import Curso as C
import Estudiante as E
import Profesor as P
import Grupo as G

def menu():
    while True:
        opcion=int(input("❀ Ingrese la opción donde desea acceder ❀:\n\t1)Curso\n\t2)Estudiante\n\t3)Profesor\n\t4)Grupo\n\t5)Salir\n"))
        if opcion ==1:#Todo lo relacionado a la base de datos de Curso
            print("Curso")
            curso=C.Database()
            curso_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n")
            curso_op.lower()
            if curso_op== 'a':#Muestra los datos de una lista grande general
                curso.getCurso()
            elif curso_op== 'b':#Muestra los datos de un id en especifico
                id_consulta= input("Ingrese el ID que desea obtener la información:\n")
                if  id_consulta.isnumeric():
                    curso.getCurso_ID(id_consulta)
                else:
                    print("Debe ingresar un ID numérico")
            elif curso_op== 'c':#Opcion para actualizar los diferentes parámetros, el usuario elige cuál desea actualizar
                actualizarC_op= input("Indique lo que desea actualizar:\n\ta)Nombre\n\tb)Tiempo\n\tc)Todos los datos")
                actualizarC_op.lower()
                if actualizarC_op== 'a':
                    id_actualizaName= input("Ingrese el ID que desea actualizar:\n")
                    if id_actualizaName.isnumeric():
                        nombre_Name= input("Escriba el nombre:\n")
                        curso.updateCurso_ID(id_actualizaName, nombre_Name)
                    else:
                        print("Debe ingresar un ID numérico")
                elif actualizarC_op== 'b':
                    id_actualizaTime= input("Ingrese el ID que desea actualizar:\n")
                    if id_actualizaTime.isnumeric():
                        tiempo_Time= input("Indique el nuevo tiempo:\n")
                        curso.updateCurso_TiempoID(id_actualizaTime, tiempo_Time)
                    else:
                        print("Debe ingresar un ID numérico")
                elif actualizarC_op== 'c':
                    id_actualizaTotal= input("Ingrese el ID que desea actualizar:\n")
                    if id_actualizaTotal.isnumeric():
                        nombre= input("Escriba el nombre:\n")
                        descripcion= input("Escriba la nueva descripcion:\n")
                        tiempo= input("Indique el nuevo tiempo:\n")
                        usuario= input("Escriba el usuario:\n")
                        curso.updateCurso_TotalID(id_actualizaTotal, nombre, descripcion, tiempo, usuario)
                    else:
                        print("Debe ingresar un ID numérico")
                else:
                    print("Error, ingrese una opcion válida")
                pass
            elif curso_op== 'd':#Permite al usuario crear un nuevo registro
                new_name= input("Ingrese el nombre del usuario que quiere crear:\n")
                new_desc= input("Ingrese la descripcion:\n")
                new_time= input("Ingrese el tiempo:\n")
                new_usuario= input("Ingrese el usuario:\n")
                curso.createCurso(new_name, new_desc, new_time, new_usuario)
            elif curso_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                delete_id= input("Ingrese el ID que desea eliminar: ")
                if delete_id.isnumeric():
                    curso.deleteCurso(delete_id)
                else:
                    print("Debe ingresar un ID numérico")
            else:
                print("Debe ingresar una opción correcta")
        elif opcion==2:
            print("Estudiante")
            student=E.Database()
            estudiante_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n")
            estudiante_op.lower()
            if estudiante_op== 'a':
                student.getStudent()
            elif estudiante_op== 'b':
                id_consultaStudent= input("Ingrese el ID que desea obtener la información:\n")
                if  id_consultaStudent.isnumeric():
                    student.getStudent_ID(id_consultaStudent)
                else:
                    print("Debe ingresar un ID numérico")
            elif estudiante_op== 'c':
                actualizarE_op= input("Indique lo que desea actualizar:\n\ta)Cedula\n\tb)Correo Electrónico\n\tc)Telefono\n\td)Telefono Celular\n\te)Fecha de Nacimiento\n\tf)Sexo\n\tg)Dirección\n\th)Nombre\n\ti)Apellido Paterno\n\tj)Apellido Materno\n\tk)Nacionalidad\n\tl)ID Carreras\n\tm)Usuario\n\tn)Todos los datos")
                actualizarE_op.lower()
                if actualizarE_op== 'a':
                    pass
                elif actualizarE_op== 'b':
                    pass
                elif actualizarE_op== 'c':
                    pass
                elif actualizarE_op== 'd':
                    pass
                elif actualizarE_op== 'e':
                    pass
                elif actualizarE_op== 'f':
                    pass
                elif actualizarE_op== 'g':
                    pass
                elif actualizarE_op== 'h':
                    pass
                elif actualizarE_op== 'i':
                    pass
                elif actualizarE_op== 'j':
                    pass
                elif actualizarE_op== 'k':
                    pass
                elif actualizarE_op== 'l':
                    pass
                elif actualizarE_op== 'm':
                    pass
                elif actualizarE_op== 'n':
                    pass
                else:
                    print("Error, ingrese una opcion válida")
            elif estudiante_op== 'd':
                pass
            elif estudiante_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                pass
            else:
                print("Debe ingresar una opción correcta")
        elif opcion==3:
            print("Profesor")
            profe=P.Database()
            profe_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n")
            profe_op.lower()
            if profe_op== 'a':
                pass
            elif profe_op== 'b':
                pass
            elif profe_op== 'c':
                actualizarP_op= input("Indique lo que desea actualizar:\n\ta)Cedula\n\tb)Correo Electrónico\n\tc)Telefono\n\td)Telefono Celular\n\te)Fecha de Nacimiento\n\tf)Sexo\n\tg)Dirección\n\th)Nombre\n\ti)Apellido Paterno\n\tj)Apellido Materno\n\tk)Nacionalidad\n\tl)ID Carreras\n\tm)Usuario\n\tn)Todos los datos")
                actualizarP_op.lower()
                if actualizarP_op== 'a':
                    pass
                elif actualizarP_op== 'b':
                    pass
                elif actualizarP_op== 'c':
                    pass
                elif actualizarP_op== 'd':
                    pass
                elif actualizarP_op== 'e':
                    pass
                elif actualizarP_op== 'f':
                    pass
                elif actualizarP_op== 'g':
                    pass
                elif actualizarP_op== 'h':
                    pass
                elif actualizarP_op== 'i':
                    pass
                elif actualizarP_op== 'j':
                    pass
                elif actualizarP_op== 'k':
                    pass
                elif actualizarP_op== 'l':
                    pass
                elif actualizarP_op== 'm':
                    pass
                elif actualizarP_op== 'n':
                    pass
                else:
                    print("Error, ingrese una opcion válida")
            elif profe_op== 'd':
                pass
            elif profe_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                pass
            else:
                print("Debe ingresar una opción correcta")
        elif opcion==4:
            print("Grupo")
            group=G.Database()
            grupo_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n")
            grupo_op.lower()
            if grupo_op== 'a':
                group.getGroup()
            elif grupo_op== 'b':
                id_consultaGroup= input("Ingrese el ID que desea obtener la información:\n")
                if  id_consultaGroup.isnumeric():
                    group.getGroup_ID(id_consultaGroup)
                else:
                    print("Debe ingresar un ID numérico")
            elif grupo_op== 'c':
                id_actualizaGroup= input("Ingrese el ID que desea actualizar:\n")
                if id_actualizaGroup.isnumeric():
                    nombreGroup= int("Ecriba el nombre:\n")
                    group.uptadeGroup_ID(id_actualizaGroup, nombreGroup)
                else:
                    print("Debe ingresar un ID numérico")
            elif grupo_op== 'd':
                new_groupname=("Ingrese el nuevo nombre:\n")
                group.createGroup(new_groupname)
            elif grupo_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                deletegroup_id= input("Ingrese el ID que desea eliminar: ")
                if deletegroup_id.isnumeric():
                    group.deleteGroup(deletegroup_id)
                else:
                    print("Debe ingresar un ID numérico")
            else:
                print("Debe ingresar una opción correcta")
        elif opcion==5:#Salir del menu
            print("Hasta luego!❀")
            break
        else:
            print("Opción inválida, intente de nuevo")


menu()