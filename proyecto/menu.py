import Curso as C
import Estudiante as E
import Profesor as P
import Grupo as G

def menu():
    while True:
        opcion=int(input("Ingrese la opción donde desea acceder:\n\t1)Curso\n\t2)Estudiante\n\t3)Profesor\n\t4)Grupo\n\t5)Salir\n"))
        if opcion ==1:
            print("Curso")
            curso=C.Database()
            curso_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n")
            curso_op.lower()
            if curso_op== 'a':
                curso.getCurso()
            elif curso_op== 'b':
                id_consulta= input("Ingrese el ID que desea obtener la información:\n")
                if  id_consulta.isnumeric():
                    curso.getCurso_ID(id_consulta)
                else:
                    print("Debe ingresar un ID numérico")
            elif curso_op== 'c':
                actualizar_op= input("Indique lo que desea actualizar:\n\ta)Nombre\n\tb)Tiempo\n\tc)Todos los datos")
                actualizar_op.lower()
                if actualizar_op== 'a':
                    id_actualizaName= input("Ingrese el ID que desea actualizar:\n")
                    if id_actualizaName.isnumeric():
                        nombre_Name= input("Escriba el nombre:\n")
                        curso.updateCurso_ID(id_actualizaName, nombre_Name)
                    else:
                        print("Debe ingresar un ID numérico")
                elif actualizar_op== 'b':
                    id_actualizaTime= input("Ingrese el ID que desea actualizar:\n")
                    if id_actualizaTime.isnumeric():
                        tiempo_Time= input("Indique el nuevo tiempo:\n")
                        curso.updateCurso_TiempoID(id_actualizaTime, tiempo_Time)
                    else:
                        print("Debe ingresar un ID numérico")
                elif actualizar_op== 'c':
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
            elif curso_op== 'd':
                new_name= input("Ingrese el nombre del usuario que quiere crear:\n")
                new_desc= input("Ingrese la descripcion:\n")
                new_time= input("Ingrese el tiempo:\n")
                new_usuario= input("Ingrese el usuario:\n")
                curso.createCurso(new_name, new_desc, new_time, new_usuario)
            elif curso_op== 'e':
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
                pass
            elif estudiante_op== 'c':
                actualizar_op= input("Indique lo que desea actualizar:\n\ta)Nombre\n\tb)Tiempo\n\tc)Todos los datos")
                actualizar_op.lower()
                if actualizar_op== 'a':
                    pass
                elif actualizar_op== 'b':
                    pass
                elif actualizar_op== 'c':
                    pass
                else:
                    print("Error, ingrese una opcion válida")
                pass
            elif estudiante_op== 'd':
                pass
            elif estudiante_op== 'e':
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
                actualizar_op= input("Indique lo que desea actualizar:\n\ta)Nombre\n\tb)Tiempo\n\tc)Todos los datos")
                actualizar_op.lower()
                if actualizar_op== 'a':
                    pass
                elif actualizar_op== 'b':
                    pass
                elif actualizar_op== 'c':
                    pass
                else:
                    print("Error, ingrese una opcion válida")
                pass
            elif profe_op== 'd':
                pass
            elif profe_op== 'e':
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
                id_consulta= input("Ingrese el ID que desea obtener la información:\n")
                if  id_consulta.isnumeric():
                    group.getGroup_ID(id_consulta)
                else:
                    print("Debe ingresar un ID numérico")
            elif grupo_op== 'c':
                id_actualiza= input("Ingrese el ID que desea actualizar:\n")
                if id_actualiza.isnumeric():
                    nombreGroup= int("Ecriba el nombre:\n")
                    group.uptadeGroup_ID(id_actualiza, nombreGroup)
                else:
                    print("Debe ingresar un ID numérico")
            elif grupo_op== 'd':
                new_groupname=("Ingrese el nuevo nombre:\n")
                group.createGroup(new_groupname)
            elif grupo_op== 'e':
                delete_id= input("Ingrese el ID que desea eliminar: ")
                if delete_id.isnumeric():
                    group.deleteCurso(delete_id)
                else:
                    print("Debe ingresar un ID numérico")
            else:
                print("Debe ingresar una opción correcta")
        elif opcion==5:
            print("Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo")


menu()