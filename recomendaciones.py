from tkinter import *
import pandas as pd
datos = pd.read_csv("Datos.csv")
item_similarity=datos.corr(method='pearson')
def get_similar(name,rating):
    similar_score=item_similarity[name]*(rating-2.5)
    similar_score=similar_score.sort_values(ascending=False)

    return similar_score

global usuario
usuario=[]
global clics
clics=0
sim_list=["nada","nada2","nada3"]

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 
        
def main():
    raiz=Tk()
    raiz.title("Ventana de pruebas")
    raiz.iconbitmap("icon.ico")
    raiz.geometry("750x650")
    raiz.configure(bg=_from_rgb((177, 206, 123)))

    frame=Frame(raiz,width=800,height=600)
    frame.configure(bg=_from_rgb((177, 206, 123)))
    frame.pack()
    
    #Label(frame,text="",bg=_from_rgb((177, 206, 123)),font=(14)).place(x=125,y=400)
    global lb1,lb2,lb3
    global text1,text2,text3 
    text1 = StringVar()
    text2 = StringVar()
    text3 = StringVar()
    text1.set('')
    text2.set('')
    text3.set('')
    
    lb1=Label(frame,textvariable=text1,bg=_from_rgb((177, 206, 123)),font=(14)).place(x=125,y=200)
    lb2=Label(frame,textvariable=text2,bg=_from_rgb((177, 206, 123)),font=(14)).place(x=125,y=300)
    lb3=Label(frame,textvariable=text3,bg=_from_rgb((177, 206, 123)),font=(14)).place(x=125,y=400)
                       
    def reducir():
        for lista in usuario:
            lista[1]=lista[1]-1
            
    def calcular1():
        global lb1,lb2,lb3,clics,usuario
        bandera=0
        for lista in usuario:
            if "citricos" in lista:
                lista[1]=lista[1]+1
                bandera=1            
            if lista[1]>5:
                lista[1]=5
        if bandera==0:
            usuario.append(["citricos",2])
        print(usuario)
        similar=pd.DataFrame()

        for name,rating in usuario:
            similar=similar.append(get_similar(name,rating),ignore_index=True)

        similar.head()
        similar=similar.sum()
        similar=similar.sort_values(ascending=False)

        sim_list=similar.index.values
        if len(usuario)!=0:
            text1.set('RECOMENDACION 1 =  '+str(sim_list[0]))
            text2.set('RECOMENDACION 2 =  '+str(sim_list[1]))
            text3.set('RECOMENDACION 3 =  '+str(sim_list[2]))
            lb1=Label(frame,textvariable=text1)
            lb2=Label(frame,textvariable=text2)
            lb3=Label(frame,textvariable=text3)
            clics=clics+1
            if clics==4:
                clics=0
                reducir()
    def calcular2():
        global lb1,lb2,lb3,clics,usuario
        bandera=0
        for lista in usuario:
            if "granos" in lista:
                lista[1]=lista[1]+1
                bandera=1
            
            if lista[1]>5:
                lista[1]=5
        if bandera==0:
            usuario.append(["granos",2])
        print(usuario)
        similar=pd.DataFrame()

        for name,rating in usuario:
            similar=similar.append(get_similar(name,rating),ignore_index=True)

        similar.head()
        similar=similar.sum()
        similar=similar.sort_values(ascending=False)

        sim_list=similar.index.values
        if len(usuario)!=0:
            text1.set('RECOMENDACION 1 =  '+str(sim_list[0]))
            text2.set('RECOMENDACION 2 =  '+str(sim_list[1]))
            text3.set('RECOMENDACION 3 =  '+str(sim_list[2]))
            lb1=Label(frame,textvariable=text1)
            lb2=Label(frame,textvariable=text2)
            lb3=Label(frame,textvariable=text3)
            clics=clics+1
            if clics==4:
                clics=0
                reducir()
    def calcular3():
        global lb1,lb2,lb3,clics,usuario
        bandera=0
        for lista in usuario:
            if "raices" in lista:
                lista[1]=lista[1]+1
                bandera=1            
            if lista[1]>5:
                lista[1]=5
                
        if bandera==0:
            usuario.append(["raices",2])
        print(usuario)
        similar=pd.DataFrame()

        for name,rating in usuario:
            similar=similar.append(get_similar(name,rating),ignore_index=True)

        similar.head()
        similar=similar.sum()
        similar=similar.sort_values(ascending=False)

        sim_list=similar.index.values
        if len(usuario)!=0:
            text1.set('RECOMENDACION 1 =  '+str(sim_list[0]))
            text2.set('RECOMENDACION 2 =  '+str(sim_list[1]))
            text3.set('RECOMENDACION 3 =  '+str(sim_list[2]))
            lb1=Label(frame,textvariable=text1)
            lb2=Label(frame,textvariable=text2)
            lb3=Label(frame,textvariable=text3)
            clics=clics+1
            if clics==4:
                clics=0
                reducir()
    def calcular4():
        global lb1,lb2,lb3,clics,usuario
        bandera=0
        for lista in usuario:
            
            if "origen animal(miel,leche,etc)" in lista:
                lista[1]=lista[1]+1
                bandera=1
            if lista[1]>5:
                lista[1]=5
        if bandera==0:
            usuario.append(["origen animal(miel,leche,etc)",2])
        print(usuario)
        similar=pd.DataFrame()

        for name,rating in usuario:
            similar=similar.append(get_similar(name,rating),ignore_index=True)

        similar.head()
        similar=similar.sum()
        similar=similar.sort_values(ascending=False)

        sim_list=similar.index.values
        if len(usuario)!=0:
            text1.set('RECOMENDACION 1 =  '+str(sim_list[0]))
            text2.set('RECOMENDACION 2 =  '+str(sim_list[1]))
            text3.set('RECOMENDACION 3 =  '+str(sim_list[2]))
            lb1=Label(frame,textvariable=text1)
            lb2=Label(frame,textvariable=text2)
            lb3=Label(frame,textvariable=text3)
            clics=clics+1
            if clics==4:
                clics=0
                reducir()
    def calcular5():
        global lb1,lb2,lb3,clics,usuario
        bandera=0
        for lista in usuario:
            if "verduras" in lista:
                lista[1]=lista[1]+1
                bandera=1            
            if lista[1]>5:
                lista[1]=5
        if bandera==0:
            usuario.append(["verduras",2])
        print(usuario)
        similar=pd.DataFrame()

        for name,rating in usuario:
            similar=similar.append(get_similar(name,rating),ignore_index=True)

        similar.head()
        similar=similar.sum()
        similar=similar.sort_values(ascending=False)

        sim_list=similar.index.values
        if len(usuario)!=0:
            text1.set('RECOMENDACION 1 =  '+str(sim_list[0]))
            text2.set('RECOMENDACION 2 =  '+str(sim_list[1]))
            text3.set('RECOMENDACION 3 =  '+str(sim_list[2]))
            lb1=Label(frame,textvariable=text1)
            lb2=Label(frame,textvariable=text2)
            lb3=Label(frame,textvariable=text3)
            clics=clics+1
            if clics==4:
                clics=0
                reducir()
    def calcular6():
        global lb1,lb2,lb3,clics,usuario
        bandera=0
        for lista in usuario:
            if "Frutos_secos" in lista:
                lista[1]=lista[1]+1
                bandera=1            
            if lista[1]>5:
                lista[1]=5
        if bandera==0:
            usuario.append(["Frutos_secos",2])
        print(usuario)
        similar=pd.DataFrame()

        for name,rating in usuario:
            similar=similar.append(get_similar(name,rating),ignore_index=True)

        similar.head()
        similar=similar.sum()
        similar=similar.sort_values(ascending=False)

        sim_list=similar.index.values
        if len(usuario)!=0:
            text1.set('RECOMENDACION 1 =  '+str(sim_list[0]))
            text2.set('RECOMENDACION 2 =  '+str(sim_list[1]))
            text3.set('RECOMENDACION 3 =  '+str(sim_list[2]))
            lb1=Label(frame,textvariable=text1)
            lb2=Label(frame,textvariable=text2)
            lb3=Label(frame,textvariable=text3)
            clics=clics+1
            if clics==4:
                clics=0
                reducir()
    def calcular7():
        global lb1,lb2,lb3,clics,usuario
        bandera=0
        for lista in usuario:
            if "chiles" in lista:
                lista[1]=lista[1]+1
                bandera=1
            if lista[1]>5:
                lista[1]=5
        if bandera==0:
            usuario.append(["chiles",2])
        print(usuario)
        similar=pd.DataFrame()

        for name,rating in usuario:
            similar=similar.append(get_similar(name,rating),ignore_index=True)

        similar.head()
        similar=similar.sum()
        similar=similar.sort_values(ascending=False)

        sim_list=similar.index.values
        if len(usuario)!=0:
            text1.set('RECOMENDACION 1 =  '+str(sim_list[0]))
            text2.set('RECOMENDACION 2 =  '+str(sim_list[1]))
            text3.set('RECOMENDACION 3 =  '+str(sim_list[2]))
            lb1=Label(frame,textvariable=text1)
            lb2=Label(frame,textvariable=text2)
            lb3=Label(frame,textvariable=text3)
            clics=clics+1
            if clics==4:
                clics=0
                reducir()    

    lb1=Label(frame,text="COMPRA ALGO",bg=_from_rgb((177, 206, 123)),font=(18)).place(x=225,y=10)

    bt_citricos=Button(raiz,text="CITRICOS",command=calcular1).place(x=25,y=50)
    bt_granos=Button(raiz,text="GRANOS",command=calcular2).place(x=125,y=50)
    bt_raices=Button(raiz,text="RAICES",command=calcular3).place(x=225,y=50)
    bt_animal=Button(raiz,text="ANIMAL",command=calcular4).place(x=325,y=50)
    bt_verduras=Button(frame,text="VERDURAS",command=calcular5).place(x=425,y=50)
    bt_secos=Button(frame,text="SECOS",command=calcular6).place(x=525,y=50)
    bt_c=Button(frame,text="CHILES",command=calcular7).place(x=625,y=50)

    raiz.mainloop()
    
    
if __name__ == '__main__':
    main()