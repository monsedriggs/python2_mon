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
                pass
            elif curso_op== 'c':
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
            elif curso_op== 'd':
                pass
            elif curso_op== 'e':
                delete_id= input("Ingrese el ID que desea eliminar: ")
                curso.deleteCurso(delete_id)
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
            grupo_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n")
            grupo_op.lower()
            if grupo_op== 'a':
                pass
            elif grupo_op== 'b':
                pass
            elif grupo_op== 'c':
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
            elif grupo_op== 'd':
                pass
            elif grupo_op== 'e':
                pass
            else:
                print("Debe ingresar una opción correcta")
        elif opcion==5:
            print("Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo")


menu()