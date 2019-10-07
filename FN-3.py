# funcion que remueva los elementos repetidos en un arreglo 
# y regrese un nuevo arreglo con los elemntos restantes

Arreglo_N = []
Arreglo=[9,3,1,3,2,9]
conta=0
def remover_Repetidos(Arreglo):
        for j in range (len(Arreglo)):
            conta=0
            for i in range (0,len(Arreglo)):
                if( Arreglo[j]==Arreglo[i]):
                    conta=conta+1
                    print("cont"+ str(conta))
                    print("j"+ str(Arreglo[j]))
                    print("i"+ str(Arreglo[i]))
                                        
            if(conta==1):   
                Arreglo_N.append(Arreglo[j])
                print("nuevo"+ str(Arreglo_N))
    
remover_Repetidos(Arreglo)        
print(""+ str(Arreglo_N))    