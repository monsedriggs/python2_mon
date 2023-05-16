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
            while True:
                print("Curso")
                curso=C.Database()
                curso_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n\tf)Volver al menu principal\n")
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
                            nombre_Name= input("Escriba el nuevo nombre del registro que desea actualizar:\n")
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
                            nombre_Total= input("Escriba el nuevo nombre del registro que desea actualizar:\n")
                            descripcion_Total= input("Escriba la nueva descripcion:\n")
                            tiempo_Total= input("Indique el nuevo tiempo:\n")
                            usuario_Total= input("Escriba el usuario:\n")
                            curso.updateCurso_TotalID(id_actualizaTotal, nombre_Total, descripcion_Total, tiempo_Total, usuario_Total)
                        else:
                            print("Debe ingresar un ID numérico")
                    else:
                        print("Error, ingrese una opcion válida")
                elif curso_op== 'd':#Permite al usuario crear un nuevo registro
                    new_name= input("Ingrese el nombre del registro que quiere crear:\n")
                    new_desc= input("Ingrese la descripcion:\n")
                    new_time= input("Ingrese el tiempo:\n")
                    new_usuario= input("Ingrese el usuario:\n")
                    curso.createCurso(new_name, new_desc, new_time, new_usuario)
                elif curso_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                    delete_id= input("Ingrese el ID que desea eliminar:\n")
                    if delete_id.isnumeric():
                        curso.deleteCurso(delete_id)
                    else:
                        print("Debe ingresar un ID numérico")
                elif curso_op== 'f':#Opcion para regresar al menú principal 
                    break
                else:
                    print("Debe ingresar una opción correcta")
        elif opcion==2:#Todo lo relacionado a la base de datos de Estudiante
            while True:
                print("Estudiante")
                student=E.Database()
                estudiante_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n\tf)Volver al menu principal\n")
                estudiante_op.lower()
                if estudiante_op== 'a':#Muestra los datos de una lista grande general
                    student.getStudent()
                elif estudiante_op== 'b':#Muestra los datos de un id en especifico
                    id_consultaStudent= input("Ingrese el ID que desea obtener la información:\n")
                    if  id_consultaStudent.isnumeric():
                        student.getStudent_ID(id_consultaStudent)
                    else:
                        print("Debe ingresar un ID numérico")
                elif estudiante_op== 'c':#Opcion para actualizar los diferentes parámetros, el usuario elige cuál desea actualizar
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
                        id_actualizaTotalStudent= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTotalStudent.isnumeric():
                            nombre_StudentTotal=input("Ingrese el nuevo nombre del registro que quiere actualizar:\n")
                            apellidoPaterno_StudentTotal= input("Apellido Paterno:\n")
                            apellidoMaterno_StudentTotal= input("Apellido Materno:\n")
                            cedula_StudentTotal= input("Cédula:\n")
                            correo_StudentTotal= input("Correo Electrónico:\n")
                            telefono_StudentTotal= input("Telefono:\n")
                            celular_StudentTotal= input("Telefono Celular:\n")
                            fecha_StudentTotal= input("Fecha de Nacimiento:\n")
                            sexo_StudentTotal= input("Sexo:\n")
                            direccion_StudentTotal= input("Direccion:\n")
                            nacionalidad_StudentTotal= input("Nacionalidad:\n")
                            carreras_StudentTotal= input("ID de Carrera:\n")
                            usuario_StudentTotal= input("Usuario:\n")
                            student.updateStudent_TotalID(id_actualizaTotalStudent, cedula_StudentTotal, correo_StudentTotal, telefono_StudentTotal, celular_StudentTotal, fecha_StudentTotal, sexo_StudentTotal, direccion_StudentTotal, nombre_StudentTotal, apellidoPaterno_StudentTotal, apellidoMaterno_StudentTotal, nacionalidad_StudentTotal, carreras_StudentTotal, usuario_StudentTotal)
                        else:  
                            print("Debe ingresar un ID numérico")
                    else:
                        print("Error, ingrese una opcion válida")
                elif estudiante_op== 'd':#Permite al usuario crear un nuevo registro
                    new_StudentName=input("Ingrese el nombre del registro que quiere crear:\n")
                    new_StudentAPatern= input("Apellido Paterno:\n")
                    new_StudentAMatern= input("Apellido Materno:\n")
                    new_StudentCedula= input("Cédula:\n")
                    new_StudentCorreo= input("Correo Electrónico:\n")
                    new_StudentTel= input("Telefono:\n")
                    new_StudentCel= input("Telefono Celular:\n")
                    new_StudentFecha= input("Fecha de Nacimiento:\n")
                    new_StudentSexo= input("Sexo:\n")
                    new_StudentDirec= input("Direccion:\n")
                    new_StudentNacional= input("Nacionalidad:\n")
                    new_StudentIDCarrera= input("ID de Carrera:\n")
                    new_StudentUsuario= input("Usuario:\n")
                    student.createStudent(new_StudentCedula, new_StudentCorreo, new_StudentTel, new_StudentCel, new_StudentFecha, new_StudentSexo, new_StudentDirec, new_StudentName, new_StudentAPatern, new_StudentAMatern, new_StudentNacional, new_StudentIDCarrera, new_StudentUsuario)
                elif estudiante_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                    deleteStudent_id= input("Ingrese el ID que desea eliminar:\n")
                    if deleteStudent_id.isnumeric():
                        student.deleteStudent(deleteStudent_id)
                    else:
                        print("Debe ingresar un ID numérico")
                elif estudiante_op== 'f':#Opcion para regresar al menú principal 
                    break
                else:
                    print("Debe ingresar una opción correcta")
        elif opcion==3:
            while True:
                print("Profesor")
                profe=P.Database()
                profe_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n\tf)Volver al menu principal\n")
                profe_op.lower()
                if profe_op== 'a':#Muestra los datos de una lista grande general
                    profe.getProfe()
                elif profe_op== 'b':#Muestra los datos de un id en especifico
                    id_consultaProfessor= input("Ingrese el ID que desea obtener la información:\n")
                    if  id_consultaProfessor.isnumeric():
                        profe.getProfe_ID(id_consultaProfessor)
                    else:
                        print("Debe ingresar un ID numérico")
                elif profe_op== 'c':#Opcion para actualizar los diferentes parámetros, el usuario elige cuál desea actualizar
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
                elif profe_op== 'd':#Permite al usuario crear un nuevo registro
                    new_ProfeName=input("Ingrese el nombre del registro que quiere crear:\n")
                    new_ProfeAPatern= input("Apellido Paterno:\n")
                    new_ProfeAMatern= input("Apellido Materno:\n")
                    new_ProfeCedula= input("Cédula:\n")
                    new_ProfeCorreo= input("Correo Electrónico:\n")
                    new_ProfeTel= input("Telefono:\n")
                    new_ProfeCel= input("Telefono Celular:\n")
                    new_ProfeFecha= input("Fecha de Nacimiento:\n")
                    new_ProfeSexo= input("Sexo:\n")
                    new_ProfeDirec= input("Direccion:\n")
                    new_ProfeNacional= input("Nacionalidad:\n")
                    new_ProfeIDCarrera= input("ID de Carrera:\n")
                    new_ProfeUsuario=input("Usuario:\n")
                    profe.createProfe(new_ProfeCedula, new_ProfeCorreo, new_ProfeTel, new_ProfeCel, new_ProfeFecha, new_ProfeSexo, new_ProfeDirec, new_ProfeName, new_ProfeAPatern, new_ProfeAMatern, new_ProfeNacional, new_ProfeUsuario, new_ProfeIDCarrera )
                elif profe_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                    deleteProfe_id= input("Ingrese el ID que desea eliminar:\n")
                    if deleteProfe_id.isnumeric():
                        profe.deleteProfe(deleteProfe_id)
                    else:
                        print("Debe ingresar un ID numérico")
                elif profe_op== 'f':#Opcion para regresar al menú principal                     
                    break
                else:
                    print("Debe ingresar una opción correcta")
        elif opcion==4:
            while True:
                print("Grupo")#Todo lo que tiene que ver con la base de datos de Grupo
                group=G.Database()
                grupo_op= input("Indique la opción de lo que desea hacer:\n\ta)Consulta datos general\n\tb)Consulta datos individual por ID\n\tc)Actualiza un registro por medio del ID\n\td)Crea un registro\n\te)Elimina un registro por ID\n\tf)Volver al menu principal\n")
                grupo_op.lower()
                if grupo_op== 'a':#Muestra los datos de una lista grande general
                    group.getGroup()
                elif grupo_op== 'b':#Muestra los datos de un id en especifico
                    id_consultaGroup= input("Ingrese el ID que desea obtener la información:\n")
                    if  id_consultaGroup.isnumeric():
                        group.getGroup_ID(id_consultaGroup)
                    else:
                        print("Debe ingresar un ID numérico")
                elif grupo_op== 'c':#Opcion para actualizar los diferentes parámetros, el usuario elige cuál desea actualizar
                    id_actualizaGroup= input("Ingrese el ID que desea actualizar:\n")
                    if id_actualizaGroup.isnumeric():
                        nombreGroup= int("Ecriba el nombre:\n")
                        group.uptadeGroup_ID(id_actualizaGroup, nombreGroup)
                    else:
                        print("Debe ingresar un ID numérico")
                elif grupo_op== 'd':#Permite al usuario crear un nuevo registro
                    new_GroupName=("Ingrese el nuevo nombre:\n")
                    group.createGroup(new_GroupName)
                elif grupo_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                    deleteGroup_id= input("Ingrese el ID que desea eliminar:\n")
                    if deleteGroup_id.isnumeric():
                        group.deleteGroup(deleteGroup_id)
                    else:
                        print("Debe ingresar un ID numérico")
                elif grupo_op== 'f':#Opcion para regresar al menú principal 
                    break
                else:
                    print("Debe ingresar una opción correcta")
        elif opcion==5:#Salir del menu
            print("Hasta luego!❀")
            break
        else:
            print("Opción inválida, intente de nuevo")


menu()