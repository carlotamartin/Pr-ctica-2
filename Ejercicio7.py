def gradingStudents(grades):
    num_estudiante = 0
    for i in grades:
        num_estudiante +=1
        if i<40:
            return print ('Estudiante '+ str(num_estudiante) + ' recibió '+ str(i)+ ' una califiación por debajo de 40, por lo que la calificación no se modificará y la calificación final del estudiante es '+ str(i))
        if i>=40:
            multiplo = i % 5
            if multiplo<3:
                num_final = i+ multiplo
                return print ('Estudiante '+ num_estudiante + ' recibió un '+ str(i)+ ' y el siguiente múltiplo de 5 de ' +str(i) +' es '+ str(num_final)+ '. Ya que '+ str(num_final)+'-'+str(i) +'<3, la calificación del estudiante se redondeará a '+str(num_final))
            elif multiplo==3:
                num_final = i
                return print ('Estudiante '+ num_estudiante + ' recibió un '+ str(i)+ ' y el siguiente múltiplo de 5 de ' +str(i) +' es '+ str(num_final)+ '. Ya que '+ str(num_final)+'-'+str(i) +'=3, la calificación del estudiante no se modificará y la calificación final del estudiante es: '+str(num_final))
            else:
                num_final = i
                return print ('Estudiante '+ num_estudiante + ' recibió un '+ str(i)+ ' y el siguiente múltiplo de 5 de ' +str(i) +' es '+ str(num_final)+ '. Ya que '+ str(num_final)+'-'+str(i) +'>3, la calificación del estudiante no se modificará y la calificación final del estudiante es: '+str(num_final))

#Probamos el método
grades = [73,67,38,33]
gradingStudents(grades)
