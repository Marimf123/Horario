from constraint import *

 # number of locations

problem = Problem()
variables1 = {'t1': 'El lunes de 9:10 se da:',
             't2': 'El martes de 9:10 se da:',
             't3': 'El miercoles de 9:10 se da:',
             't4': 'El jueves de 9:10 se da:'}

variables2 = {'t5': 'El lunes de 10:11 se da:',
             't6': 'El martes de 10:11 se da:',
             't7': 'El miercoles de 10:11 se da:',
             
             }

variables3 = {'t9': 'El lunes de 11:12 se da:',
             't10': 'El martes de 11:12 se da:',
             't11': 'El miercoles de 11:12 se da:',
             't8': 'El jueves de 10:11 se da:'      }

variables4 = {'p1': 'Lucia imparte:',
             'p2': ' y',
             'p3': 'Andrea imparte:',
             'p4': ' y',
             'p5': 'Juan imparte:',
             'p6': ' y'}

#Los tiempos del 1 al 11 son t1:9Lunes t2: 9M t3:9Mi t4:9J t5:10L t6:10M t7:10Mi t8:10J t9:11L t10:11M t11:11Mi
#Los numeros de los dominios son 1:CSociales 2:CNaturales 3:LenguaC 4:Ingles 5:EFisica 6:Mates
problem.addVariables(variables1,[2,3,4,5,6]) 
problem.addVariables(variables2,[2,3,4,5])
problem.addVariables(variables3,[1,2,3,4,5])
problem.addVariables(variables4,[1,2,3,4,5,6])

domain={1:'Ciencias Sociales',2:'Ciencias de la Naturaleza',3:'Lengua Castellana y Literatura',4:'Ingles',5:'Educacion Fisica',6:'Matematicas'}
#Restriccion 1
#for d in range(L):
 #   problem.addConstraint(MaxSumConstraint(6),["x%d" %(loc+1) for loc in range(L)])
    
  #Restriccion 8
  #Juan no quiere encargarse de Ciencias de la Naturaleza o de Ciencias Sociales, si algunas de sus horas se
#imparte a primera hora los lunes y jueves
def Juan_no_Lunes_Jueves_CS_CN(a,b):
    if (a==b==2) or (a==b==1): #Se comprueba que no pase que juan (b) enseñe CS o CN si cae en el dia a
        return False
    else: 
        return True
   
    
#Restriccion 7
#Lucıa solo se encargara de Ciencias Sociales, si Andrea se encarga de Educacion Fısica.
def lucia_CS_andrea_EF(a,b,c,d): 
    if (c!=5)&(d!=5): 
        if (a!=1)&(b==1):
            return False
        if (a==1)&(b!=1):
            return False
        else:
            return True
    else:
        return True
    
    
#Restriccion 6 Que todos los valores de los profesores sean distintos
problem.addConstraint(AllDifferentConstraint(),('p1','p2','p3','p4','p5','p6'))

#Restriccion 5 Hecho de dominio arriba
#Ademas, la materia de Matematicas debe impartirse en las primeras horas, y la de Ciencias Sociales en ´
#las ultimas

#Restriccion 4 
#La materia de Matematicas no puede impartirse el mismo dıa que Ciencias de la Naturaleza e Ingles.
def No_Mates_el_mismo_dia(*args):
     for i in range(len(args)): #Se comparan entre si todos los valores dados
         for j in range(i+1,len(args)):
                 if (i!=j): #Si son diferentes, es decir si las variables no son la misma
                     if((args[i]==6)&(args[j]==4)) or ((args[i]==6)&(args[j]==2)):
                         return False  #Es falso si mates(6) se da el mismo dia que CN(2) o I(4)
     return True   

#Restriccion 3    
#Las 2 horas dedicadas a cada materia podr´ıan impartirse de forma no consecutiva, e incluso en d´ıas
#diferentes, excepto las 2 horas dedicadas a Ciencias de la Naturaleza que s´ı se deben impartir de forma
#consecutiva el mismo dia.  
        
def CN_Seguido(*args):
    for i in range(len(args)): #Se recorren todas las variables 
        if(i!=len(args)-1): #Si no es el ultimo valor dado el de las 11-12
           if((args[i]==2)&(args[i+1]!=2)): #Se comprueba que si el valor es CN, el siguiente
               return False
        else:#Si al contrario estamos a ultima hora
           if(args[i]==2)&(args[i-1]!=2): #Se comprueba que si se da CN el anterior debe ser CN
               return False
    return True  

#Restriccion 2
#Para todas las materias se deben impartir 2 horas semanales,  
def Solo_dos_clase(*args):
    for i in range(len(args)): #Se comparan entre si todos los valores dados
        contador=0
        for j in range(len(args)):
            if(i!=j):
                if(args[i]==args[j]):
                    contador=contador+1      
                    if(contador!=1):#Si son diferentes, es decir si las variables no son la misma
                        return False
    return True #Si solo hay dos por se devuelve que es verdadero
        
#excepto para Educacion Fisica que solo tiene asignada 1 hora semanal. 
def EF_Solo_una_clase(*args):
    for i in range(len(args)):#Se comparan entre si todas las variables dadas
         for j in range(i+1,len(args)):
                 if (i!=j):#Si son diferentes variables
                     if(args[i]==args[j]==5): #Se compara que solo haya 1 de EF
                         return False 
    return True




# Los dias
problem.addConstraint(Solo_dos_clase,('t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11'))
problem.addConstraint(EF_Solo_una_clase,('t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11'))
problem.addConstraint(CN_Seguido,('t1','t5','t9'))
problem.addConstraint(CN_Seguido,('t2','t6','t10'))
problem.addConstraint(CN_Seguido,('t3','t7','t11'))
problem.addConstraint(CN_Seguido,('t4','t8'))
problem.addConstraint(No_Mates_el_mismo_dia,('t1','t5','t9'))
problem.addConstraint(No_Mates_el_mismo_dia,('t2','t6','t10'))
problem.addConstraint(No_Mates_el_mismo_dia,('t3','t7','t11'))
problem.addConstraint(No_Mates_el_mismo_dia,('t4','t8'))       

#Los profesores
problem.addConstraint(Juan_no_Lunes_Jueves_CS_CN, ('t1','p5'))
problem.addConstraint(Juan_no_Lunes_Jueves_CS_CN, ('t4','p5'))
problem.addConstraint(Juan_no_Lunes_Jueves_CS_CN, ('t1','p6'))
problem.addConstraint(Juan_no_Lunes_Jueves_CS_CN, ('t4','p6'))

problem.addConstraint(lucia_CS_andrea_EF, ('p1','p2','p3','p4'))


i=0
#solutions=problem.getSolutions ()
S = problem.getSolutions()
solution = problem.getSolution () #imprime las soluciones
for ivariable in variables1:
   print ("{0} {1}".format (variables1[ivariable], domain[solution[ivariable]]))
for ivariable in variables2:
   print ("{0} {1}".format (variables2[ivariable], domain[solution[ivariable]]))
for ivariable in variables3:
   print ("{0} {1}".format (variables3[ivariable], domain[solution[ivariable]]))
for ivariable in variables4:
   i=i+1
   print ("{0} {1}".format (variables4[ivariable], domain[solution[ivariable]]),end = '')
   if(i==2):
       print ()
       i=0


        

