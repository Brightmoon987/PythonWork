lista = []


while True:

    print("0 = fermerai il programma;")
          
    print("\n 1 = aggiungi elemento alla lista;")      
          
    print("\n 2 = visualizza elementi della lista")      

    print("\n 3 = elimina elementi nella lista")

    programQuestion = int(input("inserisci numero:"))


    if programQuestion == 0:
          
        stop_programma()
    
    
    elif programQuestion == 1:      
        aggiungi_elementi_lista() 
          
    elif programQuestion == 2:      
        visualizza_lista()  
    
    elif programQuestion == 3:      
          
            
        elimina_elemento_lista()















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





    def stop_programma():

        break
        
        
    
    
    
    



        
    



















































