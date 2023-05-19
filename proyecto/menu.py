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
                print("❀ Curso")
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
                        print("Debe ingresar un ID numérico\n")
                elif curso_op== 'c':#Opcion para actualizar los diferentes parámetros, el usuario elige cuál desea actualizar
                    actualizarC_op= input("Indique lo que desea actualizar:\n\ta)Nombre\n\tb)Tiempo\n\tc)Todos los datos\n")
                    actualizarC_op.lower()
                    if actualizarC_op== 'a':
                        id_actualizaName= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaName.isnumeric():
                            nombre_Name= input("Escriba el nuevo nombre del registro que desea actualizar:\n")
                            if nombre_Name.isspace() or len(nombre_Name)==0:
                                print("Error, debe escribir algo\n")
                            else:
                                curso.updateCurso_ID(id_actualizaName, nombre_Name)
                        else:
                            print("Debe ingresar un ID numérico\n")
                    elif actualizarC_op== 'b':
                        id_actualizaTime= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTime.isnumeric():
                            tiempo_Time= input("Indique el nuevo tiempo:\n")
                            if tiempo_Time.isspace() or len(tiempo_Time)==0:
                                print("Error, debe escribir algo\n")
                            else:
                                curso.updateCurso_TiempoID(id_actualizaTime, tiempo_Time)
                        else:
                            print("Debe ingresar un ID numérico\n")
                    elif actualizarC_op== 'c':
                        id_actualizaTotal= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTotal.isnumeric():
                            nombre_Total= input("Escriba el nuevo nombre del registro que desea actualizar:\n")
                            descripcion_Total= input("Escriba la nueva descripcion:\n")
                            tiempo_Total= input("Indique el nuevo tiempo:\n")
                            usuario_Total= input("Escriba el usuario:\n")
                            curso.updateCurso_TotalID(id_actualizaTotal, nombre_Total, descripcion_Total, tiempo_Total, usuario_Total)
                        else:
                            print("Debe ingresar un ID numérico\n")
                    else:
                        print("Error, ingrese una opcion válida\n")
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
                        print("Debe ingresar un ID numérico\n")
                elif curso_op== 'f':#Opcion para regresar al menú principal 
                    break
                else:
                    print("Debe ingresar una opción correcta\n")
        elif opcion==2:#Todo lo relacionado a la base de datos de Estudiante
            while True:
                print("❀ Estudiante")
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
                        print("Debe ingresar un ID numérico\n")
                elif estudiante_op== 'c':#Opcion para actualizar los diferentes parámetros, el usuario elige cuál desea actualizar
                    actualizarE_op= input("Indique lo que desea actualizar:\n\ta)Cedula\n\tb)Correo Electrónico\n\tc)Telefono\n\td)Telefono Celular\n\te)Fecha de Nacimiento\n\tf)Sexo\n\tg)Dirección\n\th)Nombre\n\ti)Apellido Paterno\n\tj)Apellido Materno\n\tk)Nacionalidad\n\tl)ID Carreras\n\tm)Usuario\n\tn)Todos los datos\n")
                    actualizarE_op.lower()
                    if actualizarE_op== 'a':
                        id_actualizaCedulaStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCedulaStudent.isnumeric():
                            cedula_CedulaStudent=input("Escriba la actualización de la cedula:\n")
                            student.updateStudent_CedulaID(id_actualizaCedulaStudent, cedula_CedulaStudent)
                        else:
                            print("Debe ingresar un ID numérico\n ")
                    elif actualizarE_op== 'b':
                        id_actualizaCorreoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCorreoStudent.isnumeric():
                            correo_CorreoStudent=input("Ingrese la actualización del correo:\n")
                            student.updateStudent_CorreoID(id_actualizaCorreoStudent, correo_CorreoStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'c':
                        id_actualizaTelefonoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTelefonoStudent.isnumeric():
                            tel_TelefonoStudent=input("Ingrese la actualización del telefono:\n")
                            student.updateStudent_TelefonoID(id_actualizaTelefonoStudent, tel_TelefonoStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'd':
                        id_actualizaCelularStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCelularStudent.isnumeric():
                            cel_TelCelStudent=input("Ingrese la actualización del celular:\n")
                            student.updateStudent_TelCelularID(id_actualizaCelularStudent, cel_TelCelStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'e':
                        id_actualizaFechaNacStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaFechaNacStudent.isnumeric():
                            fecha_NacimientoStudent=input("Ingrese la actualización de la fcha de nacimiento:\n")
                            student.updateStudent_FechaNacimientoID(id_actualizaFechaNacStudent, fecha_NacimientoStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'f':
                        id_actualizaSexoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaSexoStudent.isnumeric():
                            sexo_SexoStudent=input("Ingrese la actualización del sexo:\n")
                            student.updateStudent_SexoID(id_actualizaSexoStudent, sexo_SexoStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'g':
                        id_actualizaDireccionStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaDireccionStudent.isnumeric():
                            direc_DireccionStudent=input("Ingrese la actualización de la direccion:\n")
                            student.updateStudent_DireccionID(id_actualizaDireccionStudent, direc_DireccionStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'h':
                        id_actualizaNameStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaNameStudent.isnumeric():
                            nombre_NameStudent=input("Ingrese la actualización del nombre:\n")
                            student.updateStudent_ID(id_actualizaNameStudent, nombre_NameStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'i':
                        id_actualizaApPaternoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaApPaternoStudent.isnumeric():
                            apellido_PaternoStudent=input("Ingrese la actualización del apellido paterno:\n")
                            student.updateStudent_ApellidoPaternoID(id_actualizaApPaternoStudent, apellido_PaternoStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'j':
                        id_actualizaApMaternoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaApMaternoStudent.isnumeric():
                            apellido_MaternoStudent=input("Ingrese la actualización del apellido materno:\n")
                            student.updateStudent_ApellidoMaternoID(id_actualizaApMaternoStudent, apellido_MaternoStudent)
                        else:
                            print("Debe ingresar un ID numerico\n" )
                    elif actualizarE_op== 'k':
                        id_actualizaNacionalidadStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaNacionalidadStudent.isnumeric():
                            nac_NacionalidadStudent=input("Ingrese la actualización de la nacionalidad:\n")
                            student.updateStudent_NacionalidadID(id_actualizaNacionalidadStudent, nac_NacionalidadStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'l':
                        id_actualizaCarrerasStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCarrerasStudent.isnumeric():
                            carrera_IDCarreraStudent=input("Ingrese la actualización del ID de Carrera:\n")
                            student.updateStudent_CarrerasID(id_actualizaCarrerasStudent, carrera_IDCarreraStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'm':
                        id_actualizaUsuarioStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaUsuarioStudent.isnumeric():
                            usuario_UserStudent=input("Ingrese la actualización del usuario:\n")
                            student.updateStudent_UsuarioID(id_actualizaUsuarioStudent, usuario_UserStudent)
                        else:
                            print("Debe ingresar un ID numerico\n")
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
                            print("Debe ingresar un ID numérico\n")
                    else:
                        print("Error, ingrese una opcion válida\n")
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
                        print("Debe ingresar un ID numérico\n")
                elif estudiante_op== 'f':#Opcion para regresar al menú principal 
                    break
                else:
                    print("Debe ingresar una opción correcta\n")
        elif opcion==3:
            while True:
                print("❀ Profesor")
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
                    actualizarP_op= input("Indique lo que desea actualizar:\n\ta)Cedula\n\tb)Correo Electrónico\n\tc)Telefono\n\td)Telefono Celular\n\te)Fecha de Nacimiento\n\tf)Sexo\n\tg)Dirección\n\th)Nombre\n\ti)Apellido Paterno\n\tj)Apellido Materno\n\tk)Nacionalidad\n\tl)ID Carreras\n\tm)Usuario\n\tn)Todos los datos\n")
                    actualizarP_op.lower()
                    if actualizarP_op== 'a':
                        id_actualizaCedulaProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCedulaProfe.isnumeric():
                            cedula_CedulaProfe=input("Escriba la actualización de la cedula:\n")
                            profe.updateProfe_CedulaID(id_actualizaCedulaProfe, cedula_CedulaProfe)
                        else:
                            print("Debe ingresar un ID numérico\n ")
                    elif actualizarP_op== 'b':
                        id_actualizaCorreoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCorreoProfe.isnumeric():
                            correo_CorreoProfe=input("Ingrese la actualización del correo:\n")
                            profe.updateProfe_CorreoID(id_actualizaCorreoProfe, correo_CorreoProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'c':
                        id_actualizaTelefonoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTelefonoProfe.isnumeric():
                            tel_TelefonoProfe=input("Ingrese la actualización del telefono:\n")
                            profe.updateProfe_TelefonoID(id_actualizaTelefonoProfe, tel_TelefonoProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'd':
                        id_actualizaCelularProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCelularProfe.isnumeric():
                            cel_TelCelProfe=input("Ingrese la actualización del celular:\n")
                            profe.updateStudent_TelCelularID(id_actualizaCelularProfe, cel_TelCelProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'e':
                        id_actualizaFechaNacProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaFechaNacProfe.isnumeric():
                            fecha_NacimientoProfe=input("Ingrese la actualización de la fcha de nacimiento:\n")
                            profe.updateProfe_FechaNacimientoID(id_actualizaFechaNacProfe, fecha_NacimientoProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'f':
                        id_actualizaSexoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaSexoProfe.isnumeric():
                            sexo_SexoProfe=input("Ingrese la actualización del sexo:\n")
                            profe.updateProfe_SexoID(id_actualizaSexoProfe, sexo_SexoProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'g':
                        id_actualizaDireccionProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaDireccionProfe.isnumeric():
                            direc_DireccionProfe=input("Ingrese la actualización de la direccion:\n")
                            profe.updateProfe_DireccionID(id_actualizaDireccionProfe, direc_DireccionProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'h':
                        id_actualizaNameProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaNameProfe.isnumeric():
                            nombre_NameProfe=input("Ingrese la actualización del nombre:\n")
                            profe.updateProfe_ID(id_actualizaNameProfe, nombre_NameProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'i':
                        id_actualizaApPaternoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaApPaternoProfe.isnumeric():
                            apellido_PaternoProfe=input("Ingrese la actualización del apellido paterno:\n")
                            profe.updateProfe_ApellidoPaternoID(id_actualizaApPaternoProfe, apellido_PaternoProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'j':
                        id_actualizaApMaternoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaApMaternoProfe.isnumeric():
                            apellido_MaternoProfe=input("Ingrese la actualización del apellido materno:\n")
                            profe.updateProfe_ApellidoMaternoID(id_actualizaApMaternoProfe, apellido_MaternoProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'k':
                        id_actualizaNacionalidadProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaNacionalidadProfe.isnumeric():
                            nac_NacionalidadProfe=input("Ingrese la actualización de la nacionalidad:\n")
                            profe.updateProfe_NacionalidadID(id_actualizaNacionalidadProfe, nac_NacionalidadProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'l':
                        id_actualizaCarrerasProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCarrerasProfe.isnumeric():
                            carrera_IDCarreraProfe=input("Ingrese la actualización del ID de Carrera:\n")
                            profe.updateProfe_CarrerasID(id_actualizaCarrerasProfe, carrera_IDCarreraProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'm':
                        id_actualizaUsuarioProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaUsuarioProfe.isnumeric():
                            usuario_UserProfe=input("Ingrese la actualización del usuario:\n")
                            profe.updateProfe_UsuarioID(id_actualizaUsuarioProfe, usuario_UserProfe)
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'n':
                        id_actualizaTotalProfe= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTotalProfe.isnumeric():
                            nombre_ProfeTotal=input("Ingrese el nuevo nombre del registro que quiere actualizar:\n")
                            apellidoPaterno_ProfeTotal= input("Apellido Paterno:\n")
                            apellidoMaterno_ProfeTotal= input("Apellido Materno:\n")
                            cedula_ProfeTotal= input("Cédula:\n")
                            correo_ProfeTotal= input("Correo Electrónico:\n")
                            telefono_ProfeTotal= input("Telefono:\n")
                            celular_ProfeTotal= input("Telefono Celular:\n")
                            fecha_ProfeTotal= input("Fecha de Nacimiento:\n")
                            sexo_ProfeTotal= input("Sexo:\n")
                            direccion_ProfeTotal= input("Direccion:\n")
                            nacionalidad_ProfeTotal= input("Nacionalidad:\n")
                            carreras_ProfeTotal= input("ID de Carrera:\n")
                            usuario_ProfeTotal= input("Usuario:\n")
                            profe.updateProfe_TotalID(id_actualizaTotalProfe, cedula_ProfeTotal, correo_ProfeTotal, telefono_ProfeTotal, celular_ProfeTotal, fecha_ProfeTotal, sexo_ProfeTotal, direccion_ProfeTotal, nombre_ProfeTotal, apellidoPaterno_ProfeTotal, apellidoMaterno_ProfeTotal, nacionalidad_ProfeTotal, carreras_ProfeTotal, usuario_ProfeTotal)
                        else:  
                            print("Debe ingresar un ID numérico\n")
                    else:
                        print("Error, ingrese una opcion válida\n")
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
                        print("Debe ingresar un ID numérico\n")
                elif profe_op== 'f':#Opcion para regresar al menú principal                     
                    break
                else:
                    print("Debe ingresar una opción correcta\n")
        elif opcion==4:
            while True:
                print("❀ Grupo")#Todo lo que tiene que ver con la base de datos de Grupo
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
                        print("Debe ingresar un ID numérico\n")
                elif grupo_op== 'c':#Opcion para actualizar los diferentes parámetros, el usuario elige cuál desea actualizar
                    id_actualizaGroup= input("Ingrese el ID que desea actualizar:\n")
                    if id_actualizaGroup.isnumeric():
                        nombreGroup= int("Ecriba el nombre:\n")
                        group.uptadeGroup_ID(id_actualizaGroup, nombreGroup)
                    else:
                        print("Debe ingresar un ID numérico\n")
                elif grupo_op== 'd':#Permite al usuario crear un nuevo registro
                    new_GroupName=("Ingrese el nuevo nombre:\n")
                    group.createGroup(new_GroupName)
                elif grupo_op== 'e':#Permite al usuario eliminar un registro mediante el ID 
                    deleteGroup_id= input("Ingrese el ID que desea eliminar:\n")
                    if deleteGroup_id.isnumeric():
                        group.deleteGroup(deleteGroup_id)
                    else:
                        print("Debe ingresar un ID numérico\n")
                elif grupo_op== 'f':#Opcion para regresar al menú principal 
                    break
                else:
                    print("Debe ingresar una opción correcta\n")
        elif opcion==5:#Salir del menu
            print("Hasta luego! ❀")
            break
        else:
            print("Opción inválida, intente de nuevo\n")

menu()