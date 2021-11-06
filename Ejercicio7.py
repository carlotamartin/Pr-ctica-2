def gradingStudents(grades):
    num_estudiante = 0
    for i in grades:
        num_estudiante +=1
        if i<40:
            return print ('Estudiante '+ str(num_estudiante) + ' recibió '+ str(i)+ ' una califiación por debajo de 40, por lo que la calificación no se modificará y la calificación final del estudiante es '+ str(i))
        if i>=40:
            multiplo = i % 5
            num_mult = i+ multiplo
            resta = num_mult-multiplo
            if resta<3:
                #num_final = i+ multiplo
                return print ('Estudiante '+ str(num_estudiante) + ' recibió un '+ str(i)+ ' y el siguiente múltiplo de 5 de ' +str(i) +' es '+ str(num_mult)+ '. Ya que '+ str(num_mult)+'-'+str(i) +'<3, la calificación del estudiante se redondeará a '+str(num_mult))
            elif resta==3:
                #num_final = i
                return print ('Estudiante '+ str(num_estudiante) + ' recibió un '+ str(i)+ ' y el siguiente múltiplo de 5 de ' +str(i) +' es '+ str(num_mult)+ '. Ya que '+ str(num_mult)+'-'+str(i) +'=3, la calificación del estudiante no se modificará y la calificación final del estudiante es: '+str(i))
            else:
                #num_final = i
                return print ('Estudiante '+ str(num_estudiante) + ' recibió un '+ str(i)+ ' y el siguiente múltiplo de 5 de ' +str(i) +' es '+ str(num_mult)+ '. Ya que '+ str(num_mult)+'-'+str(i) +'>3, la calificación del estudiante no se modificará y la calificación final del estudiante es: '+str(i))

#Probamos el método
grades = [73,67,38,33]
gradingStudents(grades)
