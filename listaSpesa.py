lista = []





def aggiungi_elementi_lista():
    
    x = input("aggiungi elemento alla lista: ")
    
    lista.append(x)
    
    




def visualizza_lista(): 
    
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
        



def elimina_elemento_lista():
    
    domanda_Eliminazione = input("come vuoi eliminare l'elemento della lista?(scegli 1 se vuoi scrivere l'elemento,2 se vuoi eliminarlo tramite indice) ")
    
    
    if domanda_Eliminazione == 1:
        
        precisa_eliminazione = input("dimmi l'elemento che vuoi eliminare: ")
    
        lista.remove(precisa_eliminazione)
    
    
    elif domanda_Eliminazione == 2:
        
        eliminazione_indice = input("dimmi la posizione dell'elemento che vuoi eliminare: ")
        
        lista.pop(eliminazione_indice -1) 
        
        
    
    
    
    



        
    



















































