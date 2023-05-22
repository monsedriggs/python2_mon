'''
Función principal con un menú, donde el usuario elige lo que desea realizar, con una serie de opciones. 
Se importan los diferentes módulos que contienen las funciones que manejan las bases de datos.
'''
import Curso as C
import Estudiante as E
import Profesor as P
import Grupo as G
import Validacion as V
    
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
                            V.validar_input(nombre_Name, curso.updateCurso_ID(id_actualizaName, nombre_Name))  
                        else:
                            print("Debe ingresar un ID numérico\n")
                    elif actualizarC_op== 'b':
                        id_actualizaTime= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTime.isnumeric():
                            tiempo_Time= input("Indique el nuevo tiempo:\n")
                            V.validar_input(tiempo_Time, curso.updateCurso_TiempoID(id_actualizaTime, tiempo_Time))
                        else:
                            print("Debe ingresar un ID numérico\n")
                    elif actualizarC_op== 'c':
                        id_actualizaTotal= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTotal.isnumeric():
                            nombre_Total= input("Escriba el nuevo nombre del registro que desea actualizar:\n")
                            if nombre_Total.isspace() or len(nombre_Total)==0:
                                print("Error, debe escribir algo\n")
                            else:
                                descripcion_Total= input("Escriba la nueva descripcion:\n")
                                if descripcion_Total.isspace() or len(descripcion_Total)==0:
                                    print("Error, debe escribir algo\n")
                                else:
                                    tiempo_Total= input("Indique el nuevo tiempo:\n")
                                    if tiempo_Total.isspace() or len(tiempo_Total)==0:
                                        print("Error, debe escribir algo\n")
                                    else:
                                        usuario_Total= input("Escriba el usuario:\n")
                                        V.validar_input(usuario_Total, curso.updateCurso_TotalID(id_actualizaTotal, nombre_Total, descripcion_Total, tiempo_Total, usuario_Total))  
                        else:
                            print("Debe ingresar un ID numérico\n")
                    else:
                        print("Error, ingrese una opcion válida\n")
                elif curso_op== 'd':#Permite al usuario crear un nuevo registro
                    new_name= input("Ingrese el nombre del registro que quiere crear:\n")
                    if new_name.isspace() or len(new_name)==0:
                        print("Error, debe escribir algo\n")
                    else:
                        new_desc= input("Ingrese la descripcion:\n")
                        if new_desc.isspace() or len(new_desc)==0:
                            print("Error, debe escribir algo\n")
                        else:
                            new_time= input("Ingrese el tiempo:\n")
                            if new_time.isspace() or len(new_time)==0:
                                print("Error, debe escribir algo\n")
                            else:
                                new_usuario= input("Ingrese el usuario:\n")
                                V.validar_input(new_usuario, curso.createCurso(new_name, new_desc, new_time, new_usuario)) 
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
                            V.validar_input(cedula_CedulaStudent, student.updateStudent_CedulaID(id_actualizaCedulaStudent, cedula_CedulaStudent))
                        else:
                            print("Debe ingresar un ID numérico\n ")
                    elif actualizarE_op== 'b':
                        id_actualizaCorreoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCorreoStudent.isnumeric():
                            correo_CorreoStudent=input("Ingrese la actualización del correo:\n")
                            V.validar_input(correo_CorreoStudent, student.updateStudent_CorreoID(id_actualizaCorreoStudent, correo_CorreoStudent)) 
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'c':
                        id_actualizaTelefonoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTelefonoStudent.isnumeric():
                            tel_TelefonoStudent=input("Ingrese la actualización del telefono:\n")
                            V.validar_input(tel_TelefonoStudent, student.updateStudent_TelefonoID(id_actualizaTelefonoStudent, tel_TelefonoStudent))    
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'd':
                        id_actualizaCelularStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCelularStudent.isnumeric():
                            cel_TelCelStudent=input("Ingrese la actualización del celular:\n")
                            V.validar_input(cel_TelCelStudent, student.updateStudent_TelCelularID(id_actualizaCelularStudent, cel_TelCelStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'e':
                        id_actualizaFechaNacStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaFechaNacStudent.isnumeric():
                            fecha_NacimientoStudent=input("Ingrese la actualización de la fcha de nacimiento:\n")
                            V.validar_input(fecha_NacimientoStudent, student.updateStudent_FechaNacimientoID(id_actualizaFechaNacStudent, fecha_NacimientoStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'f':
                        id_actualizaSexoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaSexoStudent.isnumeric():
                            sexo_SexoStudent=input("Ingrese la actualización del sexo:\n")
                            V.validar_input(sexo_SexoStudent, student.updateStudent_SexoID(id_actualizaSexoStudent, sexo_SexoStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'g':
                        id_actualizaDireccionStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaDireccionStudent.isnumeric():
                            direc_DireccionStudent=input("Ingrese la actualización de la direccion:\n")
                            V.validar_input(direc_DireccionStudent, student.updateStudent_DireccionID(id_actualizaDireccionStudent, direc_DireccionStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'h':
                        id_actualizaNameStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaNameStudent.isnumeric():
                            nombre_NameStudent=input("Ingrese la actualización del nombre:\n")
                            V.validar_input(nombre_NameStudent, student.updateStudent_ID(id_actualizaNameStudent, nombre_NameStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'i':
                        id_actualizaApPaternoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaApPaternoStudent.isnumeric():
                            apellido_PaternoStudent=input("Ingrese la actualización del apellido paterno:\n")
                            V.validar_input(apellido_PaternoStudent, student.updateStudent_ApellidoPaternoID(id_actualizaApPaternoStudent, apellido_PaternoStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'j':
                        id_actualizaApMaternoStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaApMaternoStudent.isnumeric():
                            apellido_MaternoStudent=input("Ingrese la actualización del apellido materno:\n")
                            V.validar_input(apellido_MaternoStudent, student.updateStudent_ApellidoMaternoID(id_actualizaApMaternoStudent, apellido_MaternoStudent))
                        else:
                            print("Debe ingresar un ID numerico\n" )
                    elif actualizarE_op== 'k':
                        id_actualizaNacionalidadStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaNacionalidadStudent.isnumeric():
                            nac_NacionalidadStudent=input("Ingrese la actualización de la nacionalidad:\n")
                            V.validar_input(nac_NacionalidadStudent, student.updateStudent_NacionalidadID(id_actualizaNacionalidadStudent, nac_NacionalidadStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'l':
                        id_actualizaCarrerasStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCarrerasStudent.isnumeric():
                            carrera_IDCarreraStudent=input("Ingrese la actualización del ID de Carrera:\n")
                            V.validar_input(carrera_IDCarreraStudent, student.updateStudent_CarrerasID(id_actualizaCarrerasStudent, carrera_IDCarreraStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'm':
                        id_actualizaUsuarioStudent=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaUsuarioStudent.isnumeric():
                            usuario_UserStudent=input("Ingrese la actualización del usuario:\n")
                            V.validar_input(usuario_UserStudent, student.updateStudent_UsuarioID(id_actualizaUsuarioStudent, usuario_UserStudent))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarE_op== 'n':
                        id_actualizaTotalStudent= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTotalStudent.isnumeric():
                            nombre_StudentTotal=input("Ingrese el nuevo nombre del registro que quiere actualizar:\n")
                            if nombre_StudentTotal.isspace() or len(nombre_StudentTotal)==0:
                                print("Error, debe escribir algo\n")
                            else:
                                apellidoPaterno_StudentTotal= input("Apellido Paterno:\n")
                                if apellidoPaterno_StudentTotal.isspace() or len(apellidoPaterno_StudentTotal)==0:
                                    print("Error, debe escribir algo\n")
                                else:
                                    apellidoMaterno_StudentTotal= input("Apellido Materno:\n")
                                    if apellidoMaterno_StudentTotal.isspace() or len(apellidoMaterno_StudentTotal)==0:
                                        print("Error, debe escribir algo\n")
                                    else:
                                        cedula_StudentTotal= input("Cédula:\n")
                                        if cedula_StudentTotal.isspace() or len(cedula_StudentTotal)==0:
                                            print("Error, debe escribir algo\n")
                                        else:
                                            correo_StudentTotal= input("Correo Electrónico:\n")
                                            if correo_StudentTotal.isspace() or len(correo_StudentTotal)==0:
                                                print("Error, debe escribir algo\n")
                                            else:
                                                telefono_StudentTotal= input("Telefono:\n")
                                                if telefono_StudentTotal.isspace() or len(telefono_StudentTotal)==0:
                                                    print("Error, debe escribir algo\n")
                                                else:
                                                    celular_StudentTotal= input("Telefono Celular:\n")
                                                    if celular_StudentTotal.isspace() or len(celular_StudentTotal)==0:
                                                        print("Error, debe escribir algo\n")
                                                    else:
                                                        fecha_StudentTotal= input("Fecha de Nacimiento:\n")
                                                        if fecha_StudentTotal.isspace() or len(fecha_StudentTotal)==0:
                                                            print("Error, debe escribir algo\n")
                                                        else:
                                                            sexo_StudentTotal= input("Sexo:\n")
                                                            if sexo_StudentTotal.isspace() or len(sexo_StudentTotal)==0:
                                                                print("Error, debe escribir algo\n")
                                                            else:
                                                                direccion_StudentTotal= input("Direccion:\n")
                                                                if direccion_StudentTotal.isspace() or len(direccion_StudentTotal)==0:
                                                                    print("Error, debe escribir algo\n")
                                                                else:
                                                                    nacionalidad_StudentTotal= input("Nacionalidad:\n")
                                                                    if nacionalidad_StudentTotal.isspace() or len(nacionalidad_StudentTotal)==0:
                                                                        print("Error, debe escribir algo\n")
                                                                    else:
                                                                        carreras_StudentTotal= input("ID de Carrera:\n")
                                                                        if carreras_StudentTotal.isspace() or len(carreras_StudentTotal)==0:
                                                                            print("Error, debe escribir algo\n")
                                                                        else:
                                                                            usuario_StudentTotal= input("Usuario:\n")
                                                                            V.validar_input(usuario_StudentTotal, student.updateStudent_TotalID(id_actualizaTotalStudent, cedula_StudentTotal, correo_StudentTotal, telefono_StudentTotal, celular_StudentTotal, fecha_StudentTotal, sexo_StudentTotal, direccion_StudentTotal, nombre_StudentTotal, apellidoPaterno_StudentTotal, apellidoMaterno_StudentTotal, nacionalidad_StudentTotal, carreras_StudentTotal, usuario_StudentTotal))
                        else:  
                            print("Debe ingresar un ID numérico\n")
                    else:
                        print("Error, ingrese una opcion válida\n")
                elif estudiante_op== 'd':#Permite al usuario crear un nuevo registro
                    new_StudentName=input("Ingrese el nombre del registro que quiere crear:\n")
                    if new_StudentName.isspace() or len(new_StudentName)==0:
                        print("Error, debe escribir algo\n")
                    else:
                        new_StudentAPatern= input("Apellido Paterno:\n")
                        if new_StudentAPatern.isspace() or len(new_StudentAPatern)==0:
                            print("Error, debe escribir algo\n")
                        else:
                            new_StudentAMatern= input("Apellido Materno:\n")
                            if new_StudentAMatern.isspace() or len(new_StudentAMatern)==0:
                                print("Error, debe escribir algo\n")
                            else:
                                new_StudentCedula= input("Cédula:\n")
                                if new_StudentCedula.isspace() or len(new_StudentCedula)==0:
                                    print("Error, debe escribir algo\n")
                                else:
                                    new_StudentCorreo= input("Correo Electrónico:\n")
                                    if new_StudentCorreo.isspace() or len(new_StudentCorreo)==0:
                                        print("Error, debe escribir algo\n")
                                    else:
                                        new_StudentTel= input("Telefono:\n")
                                        if new_StudentTel.isspace() or len(new_StudentTel)==0:
                                            print("Error, debe escribir algo\n")
                                        else:
                                            new_StudentCel= input("Telefono Celular:\n")
                                            if new_StudentCel.isspace() or len(new_StudentCel)==0:
                                                print("Error, debe escribir algo\n")
                                            else:
                                                new_StudentFecha= input("Fecha de Nacimiento:\n")
                                                if new_StudentFecha.isspace() or len(new_StudentFecha)==0:
                                                    print("Error, debe escribir algo\n")
                                                else:
                                                    new_StudentSexo= input("Sexo:\n")
                                                    if new_StudentSexo.isspace() or len(new_StudentSexo)==0:
                                                        print("Error, debe escribir algo\n")
                                                    else:
                                                        new_StudentDirec= input("Direccion:\n")
                                                        if new_StudentDirec.isspace() or len(new_StudentDirec)==0:
                                                            print("Error, debe escribir algo\n")
                                                        else:
                                                            new_StudentNacional= input("Nacionalidad:\n")
                                                            if new_StudentNacional.isspace() or len(new_StudentNacional)==0:
                                                                print("Error, debe escribir algo\n")
                                                            else:
                                                                new_StudentIDCarrera= input("ID de Carrera:\n")
                                                                if new_StudentIDCarrera.isspace() or len(new_StudentIDCarrera)==0:
                                                                    print("Error, debe escribir algo\n")
                                                                else:
                                                                    new_StudentUsuario= input("Usuario:\n")
                                                                    V.validar_input(new_StudentUsuario, student.createStudent(new_StudentCedula, new_StudentCorreo, new_StudentTel, new_StudentCel, new_StudentFecha, new_StudentSexo, new_StudentDirec, new_StudentName, new_StudentAPatern, new_StudentAMatern, new_StudentNacional, new_StudentIDCarrera, new_StudentUsuario))
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
                            V.validar_input(cedula_CedulaProfe, profe.updateProfe_CedulaID(id_actualizaCedulaProfe, cedula_CedulaProfe))
                        else:
                            print("Debe ingresar un ID numérico\n ")
                    elif actualizarP_op== 'b':
                        id_actualizaCorreoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCorreoProfe.isnumeric():
                            correo_CorreoProfe=input("Ingrese la actualización del correo:\n")
                            V.validar_input(correo_CorreoProfe, profe.updateProfe_CorreoID(id_actualizaCorreoProfe, correo_CorreoProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'c':
                        id_actualizaTelefonoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTelefonoProfe.isnumeric():
                            tel_TelefonoProfe=input("Ingrese la actualización del telefono:\n")
                            V.validar_input(tel_TelefonoProfe, profe.updateProfe_TelefonoID(id_actualizaTelefonoProfe, tel_TelefonoProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'd':
                        id_actualizaCelularProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCelularProfe.isnumeric():
                            cel_TelCelProfe=input("Ingrese la actualización del celular:\n")
                            V.validar_input(cel_TelCelProfe, profe.updateStudent_TelCelularID(id_actualizaCelularProfe, cel_TelCelProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'e':
                        id_actualizaFechaNacProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaFechaNacProfe.isnumeric():
                            fecha_NacimientoProfe=input("Ingrese la actualización de la fcha de nacimiento:\n")
                            V.validar_input(fecha_NacimientoProfe, profe.updateProfe_FechaNacimientoID(id_actualizaFechaNacProfe, fecha_NacimientoProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'f':
                        id_actualizaSexoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaSexoProfe.isnumeric():
                            sexo_SexoProfe=input("Ingrese la actualización del sexo:\n")
                            V.validar_input(sexo_SexoProfe, profe.updateProfe_SexoID(id_actualizaSexoProfe, sexo_SexoProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'g':
                        id_actualizaDireccionProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaDireccionProfe.isnumeric():
                            direc_DireccionProfe=input("Ingrese la actualización de la direccion:\n")
                            V.validar_input(direc_DireccionProfe, profe.updateProfe_DireccionID(id_actualizaDireccionProfe, direc_DireccionProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'h':
                        id_actualizaNameProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaNameProfe.isnumeric():
                            nombre_NameProfe=input("Ingrese la actualización del nombre:\n")
                            V.validar_input(nombre_NameProfe, profe.updateProfe_ID(id_actualizaNameProfe, nombre_NameProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'i':
                        id_actualizaApPaternoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaApPaternoProfe.isnumeric():
                            apellido_PaternoProfe=input("Ingrese la actualización del apellido paterno:\n")
                            V.validar_input(apellido_PaternoProfe, profe.updateProfe_ApellidoPaternoID(id_actualizaApPaternoProfe, apellido_PaternoProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'j':
                        id_actualizaApMaternoProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaApMaternoProfe.isnumeric():
                            apellido_MaternoProfe=input("Ingrese la actualización del apellido materno:\n")
                            V.validar_input(apellido_MaternoProfe, profe.updateProfe_ApellidoMaternoID(id_actualizaApMaternoProfe, apellido_MaternoProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'k':
                        id_actualizaNacionalidadProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaNacionalidadProfe.isnumeric():
                            nac_NacionalidadProfe=input("Ingrese la actualización de la nacionalidad:\n")
                            V.validar_input(nac_NacionalidadProfe, profe.updateProfe_NacionalidadID(id_actualizaNacionalidadProfe, nac_NacionalidadProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'l':
                        id_actualizaCarrerasProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaCarrerasProfe.isnumeric():
                            carrera_IDCarreraProfe=input("Ingrese la actualización del ID de Carrera:\n")
                            V.validar_input(carrera_IDCarreraProfe, profe.updateProfe_CarrerasID(id_actualizaCarrerasProfe, carrera_IDCarreraProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'm':
                        id_actualizaUsuarioProfe=input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaUsuarioProfe.isnumeric():
                            usuario_UserProfe=input("Ingrese la actualización del usuario:\n")
                            V.validar_input(usuario_UserProfe, profe.updateProfe_UsuarioID(id_actualizaUsuarioProfe, usuario_UserProfe))
                        else:
                            print("Debe ingresar un ID numerico\n")
                    elif actualizarP_op== 'n':
                        id_actualizaTotalProfe= input("Ingrese el ID que desea actualizar:\n")
                        if id_actualizaTotalProfe.isnumeric():
                            nombre_ProfeTotal=input("Ingrese el nuevo nombre del registro que quiere actualizar:\n")
                            if nombre_ProfeTotal.isspace() or len(nombre_ProfeTotal)==0:
                                print("Error, debe escribir algo\n")
                            else:
                                apellidoPaterno_ProfeTotal= input("Apellido Paterno:\n")
                                if apellidoPaterno_ProfeTotal.isspace() or len(apellidoPaterno_ProfeTotal)==0:
                                    print("Error, debe escribir algo\n")
                                else:
                                    apellidoMaterno_ProfeTotal= input("Apellido Materno:\n")
                                    if apellidoMaterno_ProfeTotal.isspace() or len(apellidoMaterno_ProfeTotal)==0:
                                        print("Error, debe escribir algo\n")
                                    else:
                                        cedula_ProfeTotal= input("Cédula:\n")
                                        if cedula_ProfeTotal.isspace() or len(cedula_ProfeTotal)==0:
                                            print("Error, debe escribir algo\n")
                                        else:
                                            correo_ProfeTotal= input("Correo Electrónico:\n")
                                            if correo_ProfeTotal.isspace() or len(correo_ProfeTotal)==0:
                                                print("Error, debe escribir algo\n")
                                            else:
                                                telefono_ProfeTotal= input("Telefono:\n")
                                                if telefono_ProfeTotal.isspace() or len(telefono_ProfeTotal)==0:
                                                    print("Error, debe escribir algo\n")
                                                else:
                                                    celular_ProfeTotal= input("Telefono Celular:\n")
                                                    if celular_ProfeTotal.isspace() or len(celular_ProfeTotal)==0:
                                                        print("Error, debe escribir algo\n")
                                                    else:
                                                        fecha_ProfeTotal= input("Fecha de Nacimiento:\n")
                                                        if fecha_ProfeTotal.isspace() or len(fecha_ProfeTotal)==0:
                                                            print("Error, debe escribir algo\n")
                                                        else:
                                                            sexo_ProfeTotal= input("Sexo:\n")
                                                            if sexo_ProfeTotal.isspace() or len(sexo_ProfeTotal)==0:
                                                                print("Error, debe escribir algo\n")
                                                            else:
                                                                direccion_ProfeTotal= input("Direccion:\n")
                                                                if direccion_ProfeTotal.isspace() or len(direccion_ProfeTotal)==0:
                                                                    print("Error, debe escribir algo\n")
                                                                else:
                                                                    nacionalidad_ProfeTotal= input("Nacionalidad:\n")
                                                                    if nacionalidad_ProfeTotal.isspace() or len(nacionalidad_ProfeTotal)==0:
                                                                        print("Error, debe escribir algo\n")
                                                                    else:
                                                                        carreras_ProfeTotal= input("ID de Carrera:\n")
                                                                        if carreras_ProfeTotal.isspace() or len(carreras_ProfeTotal)==0:
                                                                            print("Error, debe escribir algo\n")
                                                                        else:
                                                                            usuario_ProfeTotal= input("Usuario:\n")
                                                                            V.validar_input(usuario_ProfeTotal, profe.updateProfe_TotalID(id_actualizaTotalProfe, cedula_ProfeTotal, correo_ProfeTotal, telefono_ProfeTotal, celular_ProfeTotal, fecha_ProfeTotal, sexo_ProfeTotal, direccion_ProfeTotal, nombre_ProfeTotal, apellidoPaterno_ProfeTotal, apellidoMaterno_ProfeTotal, nacionalidad_ProfeTotal, carreras_ProfeTotal, usuario_ProfeTotal))
                        else:  
                            print("Debe ingresar un ID numérico\n")
                    else:
                        print("Error, ingrese una opcion válida\n")
                elif profe_op== 'd':#Permite al usuario crear un nuevo registro
                    new_ProfeName=input("Ingrese el nombre del registro que quiere crear:\n")
                    if new_ProfeName.isspace() or len(new_ProfeName)==0:
                        print("Error, debe escribir algo\n")
                    else:
                        new_ProfeAPatern= input("Apellido Paterno:\n")
                        if new_ProfeAPatern.isspace() or len(new_ProfeAPatern)==0:
                            print("Error, debe escribir algo\n")
                        else:
                            new_ProfeAMatern= input("Apellido Materno:\n")
                            if new_ProfeAMatern.isspace() or len(new_ProfeAMatern)==0:
                                print("Error, debe escribir algo\n")
                            else:
                                new_ProfeCedula= input("Cédula:\n")
                                if new_ProfeCedula.isspace() or len(new_ProfeCedula)==0:
                                    print("Error, debe escribir algo\n")
                                else:
                                    new_ProfeCorreo= input("Correo Electrónico:\n")
                                    if new_ProfeCorreo.isspace() or len(new_ProfeCorreo)==0:
                                        print("Error, debe escribir algo\n")
                                    else:
                                        new_ProfeTel= input("Telefono:\n")
                                        if new_ProfeTel.isspace() or len(new_ProfeTel)==0:
                                            print("Error, debe escribir algo\n")
                                        else:
                                            new_ProfeCel= input("Telefono Celular:\n")
                                            if new_ProfeCel.isspace() or len(new_ProfeCel)==0:
                                                print("Error, debe escribir algo\n")
                                            else:
                                                new_ProfeFecha= input("Fecha de Nacimiento:\n")
                                                if new_ProfeFecha.isspace() or len(new_ProfeFecha)==0:
                                                    print("Error, debe escribir algo\n")
                                                else:
                                                    new_ProfeSexo= input("Sexo:\n")
                                                    if new_ProfeSexo.isspace() or len(new_ProfeSexo)==0:
                                                        print("Error, debe escribir algo\n")
                                                    else:
                                                        new_ProfeDirec= input("Direccion:\n")
                                                        if new_ProfeDirec.isspace() or len(new_ProfeDirec)==0:
                                                            print("Error, debe escribir algo\n")
                                                        else:
                                                            new_ProfeNacional= input("Nacionalidad:\n")
                                                            if new_ProfeNacional.isspace() or len(new_ProfeNacional)==0:
                                                                print("Error, debe escribir algo\n")
                                                            else:
                                                                new_ProfeIDCarrera= input("ID de Carrera:\n")
                                                                if new_ProfeIDCarrera.isspace() or len(new_ProfeIDCarrera)==0:
                                                                    print("Error, debe escribir algo\n")
                                                                else:
                                                                    new_ProfeUsuario=input("Usuario:\n")
                                                                    V.validar_input(new_ProfeUsuario, profe.createProfe(new_ProfeCedula, new_ProfeCorreo, new_ProfeTel, new_ProfeCel, new_ProfeFecha, new_ProfeSexo, new_ProfeDirec, new_ProfeName, new_ProfeAPatern, new_ProfeAMatern, new_ProfeNacional, new_ProfeUsuario, new_ProfeIDCarrera )) 
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
                        nombreGroup= input("Ecriba el nombre:\n")
                        V.validar_input(nombreGroup, group.uptadeGroup_ID(id_actualizaGroup, nombreGroup))
                    else:
                        print("Debe ingresar un ID numérico\n")
                elif grupo_op== 'd':#Permite al usuario crear un nuevo registro
                    new_GroupName=("Ingrese el nuevo nombre:\n")
                    V.validar_input(new_GroupName, group.createGroup(new_GroupName))
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