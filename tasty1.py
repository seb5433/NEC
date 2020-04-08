#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# name:        Tasty_pizzas.py (Python 3.x).
# description: Interfaz grafica para el control de restaurant
# author:      Sebastian Alvarez
#
#------------------------------------------------------------

'''Tasty_pizzas = Interfaz grafica para el control de restaurantes'''
   
__author__ = 'Sebastian Alvarez'
__title__= 'Tasty_pizzas'
__date__ = ''
__version__ = '1.5'
__license__ = 'GNU GPLv3'


from tkinter import *
from tkinter import Toplevel
from tkinter import ttk
import time
from pynput.keyboard import Key ,Controller
import os
from functools import partial
import sqlite3
from datetime import datetime
import subprocess
from tkinter import messagebox
import Prueba_Server 
import Num_text
import platform
import threading


class Login():
    def __init__(self):
        #self.cursor = conexion.cursor ()
        self.color= "red4"  
        #Creacion de la ventana
        self.raiz = Tk()
        self.raiz.config (bg = self.color)
        self.raiz.attributes ("-fullscreen",True)
        #self.raiz.overrideredirect(True)
        #self.process = subprocess.Popen(["python","clock.py"])
        #info4 = time.strftime("%H:%M:%S")
        info1 = platform.system()
        info2 = platform.node()
        info3 = platform.machine()
        info4 = __version__
        info5 =  time.strftime("%H:%M:%S")
        self.mensage = StringVar()
        self.barraest = Label(self.raiz, textvariable=self.mensage, bd=1, relief=SUNKEN, anchor=E,font = ("VERDANA",14))
        self.barraest.pack(side=BOTTOM, fill=X)
        # Otro modo de obtener la información: 
        # (No disponible en algunas versiones de Windows)
        
        #info1 = os.uname().sysname
        #info2 = os.uname().nodename
        #info3 = os.uname().machine
     


        #Configuraciones de ventana
        self.raiz.geometry("{0}x{1}+0+0".format(self.raiz.winfo_screenwidth(), self.raiz.winfo_screenheight()))
        #self.raiz.geometry("800x800")
        self.raiz.title ("Iniciar Sesion")
        self.icono1 = PhotoImage (file = "./images/Logo_Tasty_black.png")
        self.raiz.iconphoto(self.raiz, self.icono1)

        #Creacion y configuracion del maestro frame
        self.frame = Frame (self.raiz)
        self.frame.config (bg = self.color)
        self.frame.pack (fill='both',expand = 1)

        self.ancho = self.frame.winfo_screenwidth()
        self.alto = self.frame.winfo_screenheight()

        #frame que contiene los otros widgets 
        self.centrador = Frame (self.frame)
        self.centrador.config (bg = self.color)
        self.centrador.grid (row = 1,column = 1)
        self.centrador.config(width = 400,height = 400)

        #Contenedor de imagen TASTY
        self.imagen_tasty = PhotoImage (file = "./images/tasty2.PNG")
        self.contenedor_tasty = Frame (self.frame)
        self.contenedor_tasty.grid  (row = 0 ,column = 1 )
        self.contenedor_tasty.config (width = 400, height = 508)
        self.contenedor_imagentasty = Label (self.contenedor_tasty,image = self.imagen_tasty,bd = 0,bg = self.color).place (x=-1,y=-1)

        #creacion de frames de espaciado 
        self.espacio_sup = Frame (self.frame)
        self.espacio_sup.grid (row=0)
        self.espacio_sup.config (width = ((self.ancho - 400)/2),height = 400,bg =self.color)


        self.Usuario = StringVar()
        self.Contraseña = StringVar ()
        #Etiquetas y entradas para usuario y contraseña 
        self.user = Label (self.centrador,text = "Usuario:",fg = "white",bg = self.color,font= ("Negrita",24)).grid (row = 0,sticky = W)
        self.contraseña = Label (self.centrador,text = "Contraseña:",fg = "white",bg = self.color,font = ("Negrita",24)).grid (row = 1)
        self.user_in = Entry (self.centrador,font = (24),textvariable = self.Usuario).grid (row=0,column = 1)
        self.contraseña_in = Entry (self.centrador,show = '*',font = (24),textvariable = self.Contraseña).grid (row=1,column=1)

        #Botones para ingreso y cierre 
        #variable = StringVar()
        self.espacio = Frame (self.frame,bg = self.color,width = "400")
        self.espacio.grid (row = 2, column = 1)
        self.avisos = Label (self.espacio ,bg = self.color,fg = "Red",font = (15))
        self.avisos.grid (sticky = N , pady = 8)
        self.espacio_2 = Frame (self.frame,bg = self.color,width = "400")
        self.espacio_2.grid (row = 3, column = 1)

        self.ingresar = Button (self.espacio_2,text = 'Ingresar',font = (24), command =self.comprobante )
        self.salir = Button (self.espacio_2,text = 'Salir',font = (24),command = self.raiz.destroy)
        self.ingresar.grid (row = 0,column = 0,padx = 35,pady = 10)
        self.salir.grid (row = 0,column = 1, padx = 35,pady = 10)
        print (self.ancho)
        print (self.alto)
        self.thread()

        
        self.raiz.mainloop()
    def hora (self,ind = 0):
        info1 = platform.system()
        info2 = platform.node()
        info3 = platform.machine()
        info4 = __version__
        info5 =  time.strftime("%H:%M:%S")
        x = True
        while x == True:
            time.sleep (1)
            info5 =  time.strftime("%H:%M:%S")
            self.mensage.set(info5+ " | "+"Versión Tasty"+info4+" Estable"+" - "+info2)



    def thread (self):
        self.simplethread=threading.Thread(target=self.hora, args=[1])
        self.simplethread.start()



    #funcion de verificar contraseña y devolver validacion

    def obtener_user (self):
        self.obtenerUsuario = self.Usuario.get() 
        self.obtenerContraseña = self.Contraseña.get()
        if self.obtenerUsuario == "" and self.obtenerContraseña == "":
            self.avisos.configure (text="Abriendo Tasty Pizzas...",fg = "green2")
            print ("Abriendo Tasty Pizzas...")
            self.validacion = True
        elif self.obtenerUsuario == "" or self.obtenerContraseña == "" :
            self.avisos.configure (text="Complete todos los campos",fg = "red")
            print ("Complete todos los campos")
            self.validacion = False

        else:
            self.avisos.configure (text="Contraseña equivocada",fg = "red")
            print ("Contraseña equivocada")
            self.validacion = False
        return self.validacion
        
        
        
        #Creador de ventana principal si es que la contraseña es correcta
    def comprobante (self):
         self.Validacion = self.obtener_user()
         if self.validacion:
             self.abreventana()

    def nueva_ventana (self):
        
        #Creacion de la raiz
        self.color2 = "red4"
        self.raiz.config (bg = self.color2)
        self.raiz.title ("Tasty Pizzas"+ __version__)
        self.raiz.geometry("{0}x{1}".format(self.raiz.winfo_screenwidth(), self.raiz.winfo_screenheight()))

        #Barra de herramientas
        self.menubarra = Menu (self.raiz)
        self.raiz.config (menu = self.menubarra)

        self.archivomenu = Menu(self.menubarra,tearoff = 0)
        self.ayudamenu = Menu(self.menubarra,tearoff =0)
        self.info = Menu(self.menubarra,tearoff = 0)

        self.menubarra.add_cascade (label = "Archivos",menu = self.archivomenu)
        self.menubarra.add_cascade (label = "Ayuda",menu = self.ayudamenu)
        self.menubarra.add_cascade (label = "Informacion",menu =self.info)

        self.archivomenu.add_command (label = "Impresion")




        #Frame principal 
        self.frame_princpial = Frame (self.raiz)
        self.frame_princpial.config (width =self.raiz.winfo_screenwidth() , height = self.raiz.winfo_screenheight(),bg = self.color2)
        self.frame_princpial.pack (side = TOP)


        
        #Creaste la variable que guarda el valor de ancho y alto del frame principal 
        self.ancho = self.frame_princpial.winfo_screenwidth() /2
        self.alto = self.frame_princpial.winfo_screenheight()

        #Creaste los frames que dividen la pantalla y contienen todo
        self.mitad_derecha = Frame (self.frame_princpial)



        self.mitad_derecha.config (width =self.ancho , height = self.frame_princpial.winfo_screenheight(),bg = self.color2)
        self.mitad_derecha.pack (side = RIGHT,fill = "both")

        #fram que contiene el contenedor de los botones de la parte derecha 
        self.contenedor_sup_derecha = Frame (self.mitad_derecha)
        self.contenedor_sup_derecha.config (width= self.frame_princpial.winfo_screenwidth()/2 , height = 200, bg = self.color2)
        self.contenedor_sup_derecha.pack (side = TOP,fill = 'both')
        
        #frame que contiene los botones de la parte derecha
        self.contenedor_botones_derecha = Frame (self.contenedor_sup_derecha)
        self.contenedor_botones_derecha.config (width= self.frame_princpial.winfo_screenwidth()/2 , height = 200, bg = self.color2)
        self.contenedor_botones_derecha.pack (side = TOP)#, padx = (((self.frame_princpial.winfo_screenwidth()/2)-208)/2), pady = 10)

        #frame que contiene el editor de texto 
        self.contenedor_medio_derecha = Frame (self.mitad_derecha)
        self.contenedor_medio_derecha.config (width= self.frame_princpial.winfo_screenwidth()/2 , height = 200, bg = self.color2)
        self.contenedor_medio_derecha.pack (side = TOP,fill = 'both')


        #Creaste botones para la frame derecha
        self.foto_espera = PhotoImage (file = "./images/clock.PNG")
        self.foto_entregado = PhotoImage (file = "./images/box.PNG")
        self.foto_delivery = PhotoImage (file = "./images/motorbike.PNG")

        self.en_espera = Button (self.contenedor_botones_derecha,image = self.foto_espera, command = partial(self.funcionhendy,1))
        self.en_espera.grid (row = 0,pady = 10,padx = 20)

        self.enviado = Button (self.contenedor_botones_derecha,image = self.foto_delivery,command = partial(self.funcionhendy,2))
        self.enviado.grid (row = 0,column = 1,padx = 10)

        self.entregado = Button (self.contenedor_botones_derecha,image = self.foto_entregado,command = partial(self.funcionhendy,3))
        self.entregado.grid (row = 0 , column = 2 , pady = 10,padx = 20)


        #Creasate etiqueta para contener la informacion
        self.etiqueta_lista = Label (self.contenedor_medio_derecha,font = ("Verdana",15))
        self.etiqueta_lista.pack (side = TOP,fill = 'both',padx = 20)


        #Frame contenedor de talba 
        self.contenedor_tabla = Frame (self.mitad_derecha)
        self.contenedor_tabla.config (width = self.frame_princpial.winfo_screenwidth()/2 , height = 200, bg = self.color2)
        self.contenedor_tabla.pack (side = TOP, fill = 'both')

         # Table
        self.tree = ttk.Treeview(self.contenedor_tabla,height = 22, columns = ("one","two","three","ford","five","six","seven"))
        self.tree.pack(side = TOP,fill = 'both',padx = 20)
        self.tree.column ("#0",width = 160)
        self.tree.column ("one",width = 60)
        self.tree.column ("two",width = 40)
        self.tree.column ("three",width = 60)
        self.tree.column ("ford",width = 50)
        self.tree.column ("five",width = 50)
        self.tree.column ("six",width = 50)
        self.tree.column ("seven",width = 200)
        self.tree.heading('#0', text = 'CLIENTE', anchor = CENTER)
        self.tree.heading('one', text = 'PRECIO', anchor = CENTER)
        self.tree.heading ('two', text = 'CANT',anchor = CENTER)
        self.tree.heading('three',text = "PARA",anchor = CENTER)
        self.tree.heading('ford',text = "FACTURA",anchor = CENTER)
        self.tree.heading('five',text = "PAGO",anchor = CENTER)
        self.tree.heading('six',text = 'HORA', anchor = CENTER)
        self.tree.heading('seven',text = "UBICACION",anchor = CENTER)
        #self.tree.insert('',0, text = "SEBASTIAN ALVAREZ", values = ("55000 Gs","1","15 min"))
        #Botones de editar y eliminar
        self.contenedor_aviso = Frame (self.mitad_derecha,bg = self.color2)
        self.contenedor_aviso.pack (side = TOP)
        self.aviso = Label (self.contenedor_aviso,font = ("verdana",15),bg = self.color2,fg = "Snow")
        self.aviso.pack (side = TOP, padx = 10,pady = 10)

        self.contenedor_botones_derecha_abajo = Frame (self.mitad_derecha,bg = self.color2)
        self.contenedor_botones_derecha_abajo.pack (side = TOP,fill = 'y',)
        self.contenedor_botones_derecha_abajo2 = Frame (self.contenedor_botones_derecha_abajo,bg = self.color2)
        self.contenedor_botones_derecha_abajo2.pack (side = TOP,fill = 'both')
        self.boton_editar = Button (self.contenedor_botones_derecha_abajo2,text = "Entregar",font = ("Verdana",15))
        self.boton_editar.grid (row = 0,column = 2,padx = 5)
        self.boton_enviar = Button (self.contenedor_botones_derecha_abajo2,text = "Enviar Delivery",font = ("Verdana",15))
        self.boton_enviar.grid (row = 0,column = 1,padx = 5)
        self.boton_eliminar = Button (self.contenedor_botones_derecha_abajo2,text = "Eliminar",font =("Verdana",15))
        self.boton_eliminar.grid (row = 0,column = 0,padx = 5)
        self.boton_edit = Button (self.contenedor_botones_derecha_abajo2,text = "Editar",font = ("Verdana",15),command  = self.edit)
        self.boton_edit.grid (row = 0,column= 3,padx = 5)

        #Barra de desplazamiento

        self.funcionhendy(1)

        self.mitad_izquierdaactivador()

        print (self.ancho)
        print (self.alto)
        self.anchos = self.mitad_izquierda.winfo_screenwidth()
        print (self.anchos)
        self.altos = self.mitad_izquierda.winfo_screenheight()
        print (self.altos)

    def presion_mouse (self,event):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Pedido ORDER BY Cliente DESC"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))

    def presion_mouse2 (self,event):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Delivery_table ORDER BY Cliente DESC"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))

    def presion_mouse3 (self,event):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Entregado ORDER BY Cliente DESC"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))

    def presion_mouse_1 (self,event):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Pedido ORDER BY Para"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))

    def presion_mouse2_1 (self,event):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Delivery_table ORDER BY Para"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))

    def presion_mouse3_1 (self,event):
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Entregado ORDER BY Para"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))

    def funcionhendy (self,parametro = 0):
        if parametro ==1:
            self.lista_espera()
            self.boton_eliminar.config (fg = "red",command = partial (self.funcion_eliminar,1))
            self.boton_editar.config (fg = "green",command = partial(self.funcion_entregar,1))
            self.boton_enviar.config (command = self.entregar_delivery,text = "Enviar Delivery")
            self.aviso.config(text = '')
            self.boton_enviar.config (state = NORMAL)
            self.boton_editar.config (state = NORMAL)
            self.tree.bind("<Double-Button-1>", self.presion_mouse)
            self.tree.bind("<Triple-Button-1>", self.presion_mouse_1)



        if parametro ==2:
            self.lista_delivery()
            self.boton_eliminar.config (fg = "red",command = partial (self.funcion_eliminar,2))
            self.boton_editar.config (fg = "green",command = partial(self.funcion_entregar,2))
            self.aviso.config(text = '')
            self.boton_enviar.config (state = NORMAL,command = self.reasign_delivery_pestaña,text = "Reasignar Delivery")
            self.boton_editar.config (state = NORMAL)
            self.tree.bind("<Double-Button-1>", self.presion_mouse2)
            self.tree.bind("<Triple-Button-1>", self.presion_mouse2_1)


        if parametro ==3:
            self.lista_entrega()
            self.boton_eliminar.config (fg = "red",command = partial (self.funcion_eliminar,3))
            self.aviso.config(text = '')
            self.boton_enviar.config (state = DISABLED)
            self.boton_editar.config (state = DISABLED)
            self.tree.bind("<Double-Button-1>", self.presion_mouse3)
            self.tree.bind("<Triple-Button-1>", self.presion_mouse3_1)






        
    def lista_espera(self):
        self.insertar_tablageneral(1)
        self.etiqueta_lista.config (text = "LISTA DE ESPERA")
    
    def lista_delivery(self):
        self.insertar_tablageneral(2)
        self.etiqueta_lista.config (text = "LISTA DE SALIDAS")
        
    def lista_entrega (self):
        self.insertar_tablageneral(3)
        self.etiqueta_lista.config (text = "LISTA DE ENTREGAS")


    
    
    def mitad_izquierdaactivador (self):

        #Frame espacio
        self.mitad_izquierda = Frame (self.frame_princpial)
        self.mitad_izquierda.config (width =self.frame_princpial.winfo_screenwidth()/2 , height = self.frame_princpial.winfo_screenheight(),bg = self.color2)
        self.mitad_izquierda.pack  (side = LEFT,fill = "both")
        self.espacio = Frame (self.mitad_izquierda,bg = self.color2)
        self.espacio.config (width = 740, height = 320)
        self.espacio.pack (side = TOP,fill = 'both')

        #Contenedor de botones
        self.contenedor_botones_izquierda = Frame (self.mitad_izquierda,bg = self.color2)
        self.contenedor_botones_izquierda.pack (side = TOP,fill = 'both')

        #Frame contenedor de botones izquierdos
        self.contenedor_superior_izquierda= Frame (self.contenedor_botones_izquierda,bg = self.color2)
        self.contenedor_superior_izquierda.pack  (side = TOP)

        self.imagen_pizza = PhotoImage (file = "./images/pizza.png")
        self.boton_añadir = Button (self.contenedor_superior_izquierda,image = self.imagen_pizza, command = self.ventana_pedidos)
        self.boton_añadir.grid (row = 0,padx = 10,sticky = "N")

        self.imagen_caja = PhotoImage (file = "./images/laptop.png")
        self.boton_caja = Button (self.contenedor_superior_izquierda,image = self.imagen_caja,command = self.pestaña_reportes)
        self.boton_caja.grid (row =0,column = 1,padx = 10)

        self.imagen_salida = PhotoImage (file = "./images/logout.png")
        self.boton_salid = Button (self.contenedor_superior_izquierda,image = self.imagen_salida,command= self.cerrar_app)
        self.boton_salid.grid (row = 0,column = 3,padx = 10,sticky ="N")

        self.image_cliente = PhotoImage (file = "./images/research.png")
        self.cliente = Button (self.contenedor_superior_izquierda,image = self.image_cliente,command = partial(self.pestaña_clientes,0))
        self.cliente.grid(row = 0,column = 2, padx = 10,sticky = "N")
        #Frame espacio de espacio inferior 

        #Frame espacio inferior 
        self.espacio2 = Frame (self.mitad_izquierda,bg = self.color2)
        self.espacio2.pack (side = BOTTOM,fill = "both")

        #Contenedor de imagen tasty


        self.imagen_tasty = PhotoImage (file = "./images/Tasty_blanco.PNG")
        self.contenedor_imagen_tasty = Frame (self.espacio2,bg = self.color2,bd = 0)
        self.contenedor_imagen_tasty.grid  (row = 2,pady = 0)
        self.imagen_tasty_vista = Label (self.contenedor_imagen_tasty,image = self.imagen_tasty,bg = self.color2)
        self.imagen_tasty_vista.grid (row = 0)

    def cerrar_app (self):
        self.raiz.destroy()
        #self.process.kill()
    def enter(self,event):
        self.mitad_izquierda2.bind ("<Return>",self.enter2)
        print ("ENTER EN PEDIDOS")

    def enter2(self,event,ind = 0,ind2 = 0):
        ind = ind
        ind2 = ind2

        if ind == 1:
            reco = self.nameentry.get()
            self.boton_eliminar2.config (command =partial(self.eliminar_clientes,ind = 1) )
            self.boton_editarC.config (command = partial(self.editar_clientes,ind = 1))
            if reco == "":
                return
            print (reco)
            records = self.tabla_cli.get_children()
            for element in records:
                self.tabla_cli.delete(element)
            # getting data
            query = "SELECT * FROM Clientes_Tasty WHERE nombre LIKE "+"'"+reco+"%'"
            #db_rows = self.run_query(query)
            db_rows = Prueba_Server.run_queryServer7 (query)
            # filling data
        
            for row in db_rows:
                print (row)
                self.tabla_cli.insert('',0, text = row[0], values = (str(row[5]),row [4],row [2]))

            

        if ind == 2:
            reco = self.numeroo_entry.get()
            self.boton_eliminar2.config (command =partial(self.eliminar_clientes,ind = 2) )
            self.boton_editarC.config (command = partial(self.editar_clientes,ind = 2))
            if reco == "":
                return
            print (reco)
            records = self.tabla_cli.get_children()
            for element in records:
                self.tabla_cli.delete(element)
            # getting data
            query = "SELECT * FROM Clientes_Tasty WHERE telefono LIKE "+"'"+reco+"%'"
            #db_rows = self.run_query(query)
            db_rows = Prueba_Server.run_queryServer7 (query)
            # filling data
        
            for row in db_rows:
                print (row)
                self.tabla_cli.insert('',0, text = row[0], values = (row[5],row [4],row [2]))

        if ind == 3:
            reco = self.rucc.get()
            self.boton_eliminar2.config (command =partial(self.eliminar_clientes,ind = 3) )
            self.boton_editarC.config (command = partial(self.editar_clientes,ind = 3))
            if reco == "":
                return
            print (reco)
            records = self.tabla_cli.get_children()
            for element in records:
                self.tabla_cli.delete(element)
            # getting data
            query = "SELECT * FROM Clientes_Tasty WHERE ruc LIKE "+"'"+reco+"%'"
            #db_rows = self.run_query(query)
            db_rows = Prueba_Server.run_queryServer7 (query)
            # filling data
        
            for row in db_rows:
                print (row)
                self.tabla_cli.insert('',0, text = row[0], values = (row[5],row [4],row [2]))
                

    def pestaña_clientes (self,val =0):
        fuente = ("Verdana",18)
        fuente2 = ("verdana",15)
        color3 = "cadet blue"
        self.raizzzz = Toplevel()
        self.raizzzz.geometry ("910x800")
        self.raizzzz.config (bg = color3)
        #self.raizzzz.bind ("<Key>",self.enter2)
        frame_principal = LabelFrame (self.raizzzz,text = "              CLIENTES TASTY               ", bg = color3,font = ("CHEESE PIZZA",60), bd = 30,fg = "gray2")
        frame_principal.pack (side = TOP,fill = "both",expand = 1,padx = 15,pady = 10)
        
        frame_sec = Frame (frame_principal,bg = color3)
        frame_sec.pack (side = TOP,fill= 'both')
        nombre = Label (frame_sec,text = "Por Nombre:",font = fuente2,bg = color3)
        nombre.grid (row =0 ,column =0,padx = 5,pady = 5)
        self.nameentry= StringVar()
        nombre_entry = Entry(frame_sec,textvariable = self.nameentry,font = fuente2)
        nombre_entry.grid(row = 1,column = 0,padx = 5,pady = 5)
        nombre_entry.bind ("<Key>",partial (self.enter2,1,1))

        numero = Label (frame_sec,text = "Por Numero:",font = fuente2,bg = color3)
        numero.grid (row = 0,column = 1)

        self.numeroo_entry = StringVar()
        numero_entry = Entry (frame_sec,textvariable = self.numeroo_entry,font= fuente2)
        numero_entry.bind ("<Key>",partial (self.enter2,1,2))
        numero_entry.grid (row = 1,column = 1,padx = 5,pady= 5) 

        ruc = Label (frame_sec,text = "Por RUC:",font = fuente2,bg = color3)
        ruc.grid (row = 0,column =2 )
        self.rucc = StringVar()
        ruc_entry = Entry (frame_sec,textvariable = self.rucc,font = fuente2)
        ruc_entry.bind ("<Key>",partial (self.enter2,1,3))
        ruc_entry.grid (row =1,column =2,padx = 5,pady= 5)
        frame_tabla =Frame (frame_principal,bg = color3)
        frame_tabla.pack (side = TOP,fill = 'both')
        self.tabla_cli = ttk.Treeview(frame_tabla,height = 12, columns = ("one","two","three"))
        self.tabla_cli.pack(side = TOP,fill = 'both',padx = 20,pady = 30)
        self.tabla_cli.heading('#0', text = 'CLIENTE:', anchor = W)
        self.tabla_cli.heading('one', text = 'TELEFONO:', anchor = W)
        self.tabla_cli.heading('two',text = "DIRECCION:",anchor= W)
        self.tabla_cli.heading('three',text = "RUC:",anchor= W)

        botonera =Frame (frame_principal,bg = color3)
        botonera.pack (side = TOP,fill = "both",expand = 1,pady = 20,padx = 10)
        boton_cargar = Button (botonera,text = "Cargar",font = fuente2,fg = "green",command = self.cargar_cliente)
        boton_cargar.pack (side = TOP,fill = 'both',expand =1,pady =5)
        self.boton_editarC = Button (botonera,text = "Editar",font = fuente2,fg = "orange",command = partial(self.editar_clientes,ind = 1))
        self.boton_editarC.pack (side = TOP,fill = 'both',expand =1,pady = 5)
        self.boton_eliminar2 = Button (botonera,text = "Eliminar",font = fuente2,fg = "red",command = partial(self.eliminar_clientes,ind = 1))
        self.boton_eliminar2.pack (side = TOP,fill = 'both',expand =1,pady = 5)

        

    def eliminar_clientes (self,ind=0): #ELIMINA LOS CLIENTES DIRECTAMENTE DESDE LA PESTAÑA DE CLIENTES
        ind = ind
        seleccion = self.tabla_cli.item(self.tabla_cli.selection())
        select = seleccion['values']
        if select[0] == 'NULL' or select[0]=="None":
            try:
                query = "DELETE FROM Clientes_Tasty WHERE ruc LIKE "+"'%"+repr(select[2])+"%'"+"AND nombre LIKE "+"'"+seleccion['text']+"%'"
                db_rows = Prueba_Server.run_queryServer5 (query)
            except:
                query = "DELETE FROM Clientes_Tasty WHERE ruc LIKE "+"'%"+select[2]+"%'"+"AND nombre LIKE "+"'"+seleccion['text']+"%'"
                db_rows = Prueba_Server.run_queryServer5 (query)
        else:
            try:
                query = "DELETE FROM Clientes_Tasty WHERE telefono LIKE "+"'%"+select[0]+"%'"+"AND nombre LIKE "+"'"+seleccion['text']+"%'"
                db_rows = Prueba_Server.run_queryServer5 (query)
            except:
                query = "DELETE FROM Clientes_Tasty WHERE telefono LIKE "+"'%"+repr(select[0])+"%'"+"AND nombre LIKE "+"'"+seleccion['text']+"%'"
                db_rows = Prueba_Server.run_queryServer5 (query)
        ind = ind
        self.enter2(1,ind)

    def editar_clientes (self,ind = 0): #ESTA FUNCION EDITA LOS CLIENTES DE CUALQUIER MANERA POSIBLE
        ind = ind
        fuente2 = ("verdana",15)
        self.raiz_edit = Toplevel()
        color3 = "cadet blue"
        self.raiz_edit.geometry("400x230")
        self.raiz_edit.title ("Edición de datos")
        self.raiz_edit.config (bg = color3)
        frame1 = Frame (self.raiz_edit,bg = color3)
        frame1.pack (side = TOP,fill = "both",expand = 1)
        frame2 = Frame (self.raiz_edit,bg = color3)
        frame2.pack (side = TOP,fill = "both",expand = 1)
        nombre = Label (frame1,text = "Cliente",font = fuente2,bg = color3)
        nombre.grid (row = 0,padx = 10,pady = 5)
        self.nombre_iS = StringVar()
        nombre_i = Entry (frame1,font= fuente2,textvariable = self.nombre_iS)
        nombre_i.grid (row= 0,column = 1)
        telefono = Label (frame1,text = "Télefono",font = fuente2,bg = color3)
        telefono.grid (row = 1,padx = 10,pady = 5)
        self.telefono_iS = StringVar()
        telefono_i = Entry (frame1,font= fuente2,textvariable = self.telefono_iS)
        telefono_i.grid (row = 1,column = 1)
        ubicacion = Label (frame1,text = "Ubicación",font = fuente2,bg = color3)
        ubicacion.grid (row = 2,padx = 10,pady = 5)
        self.ubicacion_iS = StringVar()
        ubicacion_i = Entry (frame1,font= fuente2,textvariable = self.ubicacion_iS)
        ubicacion_i.grid (row = 2,column = 1)
        ruc = Label (frame1,text = "RUC",font = fuente2,bg = color3)
        ruc.grid (row = 3,padx = 10,pady = 5)
        self.ruc_iS = StringVar()
        ruc_i = Entry (frame1,font= fuente2,textvariable = self.ruc_iS)
        ruc_i.grid (row = 3,column = 1)
        editar = Button (frame2,text = "Editar",font = fuente2,fg = "Green",command = partial(self.editar_clientes_B,ind))
        editar.pack (side = TOP,fill = "both",expand = 1,pady = 5)

        seleccion = self.tabla_cli.item(self.tabla_cli.selection())
        select = seleccion['values']
        self.save_name = seleccion['text']
        self.save_tel = select[0]
        self.save_ruc = select[2]
        print (self.save_ruc)
        if select[0] == 'NULL' or select[0] == 'None':
            try:
                query = "SELECT * FROM Clientes_Tasty WHERE ruc LIKE "+"'%"+select[2]+"%'"+"AND nombre LIKE "+"'"+seleccion['text']+"%'"
                db_rows = Prueba_Server.run_queryServer7 (query)
            except:
                query = "SELECT * FROM Clientes_Tasty WHERE ruc LIKE "+"'%"+repr(select[2])+"%'"+"AND nombre LIKE "+"'"+seleccion['text']+"%'"
                db_rows = Prueba_Server.run_queryServer7 (query)
            for row in db_rows:
                self.nombre_iS.set (row [0])
                self.telefono_iS.set (row[5])
                self.ubicacion_iS.set (row[4])
                self.ruc_iS.set (row[2])
        else:
            try:
                query = "SELECT * FROM Clientes_Tasty WHERE telefono LIKE "+"'%"+select[0]+"%'"+"AND nombre LIKE "+"'"+seleccion['text']+"%'"
                db_rows = Prueba_Server.run_queryServer7 (query)
            except:
                query = "SELECT * FROM Clientes_Tasty WHERE telefono LIKE "+"'%"+repr(select[0])+"%'"+"AND nombre LIKE "+"'"+seleccion['text']+"%'"
                db_rows = Prueba_Server.run_queryServer7 (query)         
            for row in db_rows:
                self.nombre_iS.set (row [0])
                self.telefono_iS.set (row[5])
                self.ubicacion_iS.set (row[4])
                self.ruc_iS.set (row[2])
    def editar_clientes_B (self,ind = 0): #ESTA FUNCION EJECUTA EL CAMBIO DE DATOS OJALA NUNCA MAS SE TENGA QUE EDITAR
        nombre = self.nombre_iS.get ()
        tel = self.telefono_iS.get ()
        ubi = self.ubicacion_iS.get ()
        ruc = self.ruc_iS.get ()
        print (self.save_ruc)
        if self.save_ruc == 'NULL' or self.save_ruc == 'None':
            if ruc == 'None':
                ruc = 'NULL'
            try:
                query = "UPDATE Clientes_Tasty SET nombre = "+"'"+nombre.upper()+"'"+", ruc = "+repr(ruc)+", direccion = "+"'"+ubi.upper()+"'"+", telefono = "+repr(tel)+" WHERE telefono LIKE "+"'%"+repr(self.save_tel)+"%'"+"AND nombre LIKE "+"'"+self.save_name+"%'"
                print (query)
                db_rows = Prueba_Server.run_queryServer5 (query)
            except:
                query = "UPDATE Clientes_Tasty SET nombre = "+"'"+nombre.upper()+"'"+", ruc = "+repr(ruc)+", direccion = "+"'"+ubi.upper()+"'"+", telefono = "+repr(tel)+" WHERE telefono LIKE "+"'%"+self.save_tel+"%'"+"AND nombre LIKE "+"'"+self.save_name+"%'"
                print (query)
                db_rows = Prueba_Server.run_queryServer5 (query)
        else:
            if tel == 'None':
                tel = 'NULL'
            try:
                query = "UPDATE Clientes_Tasty SET nombre = "+"'"+nombre.upper()+"'"+", ruc = "+repr(ruc)+", direccion = "+"'"+ubi.upper()+"'"+", telefono = "+repr(tel)+" WHERE ruc LIKE "+"'%"+repr(self.save_ruc)+"%'"+"AND nombre LIKE "+"'"+self.save_name+"%'"
                db_rows = Prueba_Server.run_queryServer5 (query)
            except:
                query = "UPDATE Clientes_Tasty SET nombre = "+"'"+nombre.upper()+"'"+", ruc = "+repr(ruc)+", direccion = "+"'"+ubi.upper()+"'"+", telefono = "+repr(tel)+" WHERE ruc LIKE "+"'%"+self.save_ruc+"%'"+"AND nombre LIKE "+"'"+self.save_name+"%'"
                db_rows = Prueba_Server.run_queryServer5 (query)
        self.raiz_edit.destroy()
        self.enter2(1,ind)




    def cargar_cliente(self): #CARGA LOS CLIENTES DESDE LA PESTAÑA DE CLIENTES A LA PESTAÑA DE PEDIDOS
        seleccion = self.tabla_cli.item(self.tabla_cli.selection())
        print (seleccion['text'])
        separador = seleccion['values']
        print (separador[0])
        self.destructor3()
        self.raizzzz.destroy()
        
        self.NOMBRE.set (seleccion ['text'])
        #self.nombre_clientein.config(state=DISABLED)
        if separador[1] != '':
            self.Ubicacion.set (separador[1])
        if separador[0] !='NULL' :
            self.telefonoIN.set(separador[0])

        if separador[2] != 'NULL' and separador[2] != 'None' :
            self.RUCI.set(separador[2])





    #VENTANA DE PEDIDOS //NUEVO COMIENZO 

    def ventana_pedidos(self,ind = 0):#Esta ventana sirve para tomar los pedidos
        ind = ind
        self.fuente = ("Verdana",9)
        self.mitad_izquierda.destroy ()
        self.color3 = "DarkOrange2"
        self.mitad_izquierda2 = LabelFrame (self.frame_princpial,bg = self.color3,text = "  Agregar pedido  ",font = ("Bebas Neue",40), bd = 20,fg = "snow")
        self.mitad_izquierda2.config (width =self.frame_princpial.winfo_screenwidth()/2 , height = self.frame_princpial.winfo_screenheight()) 
        self.mitad_izquierda2.pack(side = LEFT,fill = 'both',expand = 1,pady = 10)
        #self.mitad_izquierda2.bind ("<Enter>",self.enter)
        

        ##Frame que divide las dos pantallas 

        self.mitad_izquierda2_arriba = Frame (self.mitad_izquierda2,bg = self.color3)
        self.mitad_izquierda2_arriba.config (width =self.frame_princpial.winfo_screenwidth()/2 , height = 200) 
        self.mitad_izquierda2_arriba.pack (side = TOP,fill = "both",expand = 1)

        self.entrada_datos()


        #Contenedor de tipo de envio
        self.contenedordeenvio = LabelFrame (self.mitad_izquierda2,bg = self.color3,text = "Para",font = 20)
        self.contenedordeenvio.pack (side = TOP)
        self.var = IntVar ()
        self.r1 = Radiobutton(self.contenedordeenvio, text = "Llevar",font = self.fuente, variable = self.var, value = 1,bg = self.color3,command = self.comando_llevar)
        self.r1.grid (row = 0,column = 0,padx = 20)
        self.r2 = Radiobutton(self.contenedordeenvio, text = "Delivery",font = self.fuente, variable = self.var, value = 2,bg = self.color3,command = self.ventana_delivery)
        self.r2.grid (row = 0,column = 1,padx = 20)
        self.r4 = Radiobutton(self.contenedordeenvio, text = "Comer en el lugar",font = self.fuente, variable = self.var, value = 3,bg = self.color3,command = self.comando_llevar)
        self.r4.grid (row = 0,column = 2,padx = 20)
        self.factura = IntVar ()
        self.r3 = Checkbutton(self.mitad_izquierda2_arriba, text = "Con Factura",font = self.fuente, variable = self.factura, onvalue = 1,bg = self.color3)
        self.r3.grid (row = 2,column = 0,columnspan = 2)
        self.search_image = PhotoImage  (file = "./images/search.png" )
        self.search_buton = Button (self.mitad_izquierda2_arriba,image = self.search_image,command = self.buscar_cliente)
        self.search_buton.grid (row = 2,column = 2,columnspan = 2)
        self.client_image = PhotoImage (file = "./images/salesman.png")
        self.client = Button (self.mitad_izquierda2_arriba,image = self.client_image, command = partial(self.pestaña_clientes,1))
        self.client.grid (row = 2,column = 3)


        ##Frame para tomar los pedidos 

        self.mitad_izquierda2_bajo = Frame (self.mitad_izquierda2,bg = self.color3)
        self.mitad_izquierda2_bajo.config (width =self.frame_princpial.winfo_screenwidth()/2 , height = 200) 
        self.mitad_izquierda2_bajo.pack (side = TOP,fill = "both")
        
        #Frame contenedor de las cantidad de pizzas}

        self.contenedor_cant_pizzas  = Frame (self.mitad_izquierda2_bajo,bg = self.color3)
        self.contenedor_cant_pizzas.pack (side = TOP)

        """self.imagen_back = PhotoImage  (file = "back.png")
        self.contenedor_back = Button (self.contenedor_cant_pizzas,image = self.imagen_back,bg = self.color3)
        self.contenedor_back.grid (row = 0)"""

        #Se invoca los botones sabores
        self.botones_sabores()

        """"self.imagen_right = PhotoImage  (file = "right.png")
        self.contenedor_right = Button (self.contenedor_cant_pizzas,image = self.imagen_right,bg = self.color3)
        self.contenedor_right.grid (row = 0,column = 4,pady = 20)
        self.add_imagen = PhotoImage (file = "add.png")
        self.add_button = Button (self.contenedor_cant_pizzas,image = self.add_imagen,bg = self.color3)
        self.add_button.grid (row = 0,column =5,padx = 10,pady = 20 )"""




        #Contenedor de los botones back y demas
        self.contenedor_navegacion = Frame (self.mitad_izquierda2,bg = "red4")
        self.contenedor_navegacion.config  (width =self.frame_princpial.winfo_screenwidth()/2 , height = 200)
        self.contenedor_navegacion.pack (side = BOTTOM)

        #contenedor de tabla de pedidos
        self.contenedortabla = Frame (self.mitad_izquierda2,bg = self.color3)
        self.contenedortabla.config  (width =self.frame_princpial.winfo_screenwidth()/2 , height =100 )
        self.contenedortabla.pack (side = TOP,fill = 'both')
         # Table
        self.arbol = ttk.Treeview(self.contenedortabla,height = 5, columns = ("one"))
        self.arbol.pack(side = TOP,fill = 'both',padx = 20)
        self.arbol.heading('#0', text = 'SABOR/SERVICIO:', anchor = W)
        self.arbol.heading('one', text = 'COSTO:', anchor = W)



        #Contenedor de editar eliminar 
        self.frame_botones = Frame (self.mitad_izquierda2,bg = self.color3)
        self.frame_botones.pack (side = TOP,fill = 'both')

        self.frame_botones2 = Frame (self.frame_botones,bg = self.color3)
        self.frame_botones2.pack (side = TOP)


        """self.editar_boton = Button (self.frame_botones2,text = "Editar",font = self.fuente)
        self.editar_boton.grid (row = 0,column =0,padx = 20)""" 
        
        self.eliminar_boton = Button (self.frame_botones2,text = "Eliminar Todo",font = self.fuente,command = self.borrar_pedidot).grid (row = 0,column = 0,padx = 20,pady = 10)
        self.eliminar_seleccion = Button (self.frame_botones2,text = "Eliminar Seleccion",font = self.fuente,command = self.delete_product).grid (row = 0,column = 1)
        #Campo de observacion
        self.observacion_espacio = Frame (self.mitad_izquierda2,bg = self.color3)
        self.observacion_espacio.pack (side = TOP)
        self.observacion = Label (self.observacion_espacio,text = "Observación:",font = self.fuente,bg = self.color3)
        self.observacion.grid (row = 0,padx = 10)
        self.observacionIN = StringVar()
        self.observacionin = Entry (self.observacion_espacio,textvariable = self.observacionIN,font = self.fuente)
        self.observacionin.grid (row = 0,column = 1,padx = 10)

        #Contenedor de etiquetas de conteo y total a pagar

        self.frame_etiquetas = Frame (self.mitad_izquierda2,bg = self.color3)
        self.frame_etiquetas.pack (side = TOP)
        self.frame_etiquetas2_1 = Frame (self.frame_etiquetas,bg = self.color3)
        self.frame_etiquetas2_1.grid (row = 0,column = 0,padx = 70,pady = 5)
        self.frame_etiquetas2_2 = Frame (self.frame_etiquetas,bg = self.color3)
        self.frame_etiquetas2_2.grid (row = 0,column = 1,padx = 50,pady = 5)
        self.etiqueta_cantidad = Label (self.frame_etiquetas2_1,text = "CANTIDAD TOTAL:",font = self.fuente,bg = self.color3).grid (row = 0)
        self.etiqueta_cantidadT = Label (self.frame_etiquetas2_1,font = self.fuente,bg = self.color3)
        self.etiqueta_cantidadT.grid (row =0,column = 1)
        self.etiqueta_precio = Label (self.frame_etiquetas2_2,text = "PRECIO TOTAL:",font = self.fuente,bg = self.color3).grid(row = 0)
        self.etiqueta_precioT = Label (self.frame_etiquetas2_2,font = self.fuente,bg = self.color3)
        self.etiqueta_precioT.grid (row =0,column =1)

        # Etiqueta para avisos y alertas:
        self.etiqueta_aviso = Frame (self.mitad_izquierda2,bg = self.color3)
        self.etiqueta_aviso.pack (side= TOP)
        self.mensaje = Label (self.etiqueta_aviso,font= self.fuente,bg = self.color3,fg = "Red4")
        self.mensaje.pack (side = TOP)
        #botones back y demas

        self.contenedor_botonback = Frame (self.contenedor_navegacion ,bg = self.color3)
        self.contenedor_botonback.grid (row = 0)
        self.imagen_back1 = PhotoImage (file = "./images/left-arrow.png")
        self.boton_back = Button (self.contenedor_botonback,bg = self.color3,image = self.imagen_back1,command = self.destructor,borderwidth=0)
        self.boton_back.grid (row = 0,pady = 20,padx = 20)
        self.espacio4 = Frame (self.contenedor_botonback,bg = self.color3)
        self.espacio4.config (width = 320,height = 20)
        self.espacio4.grid (row = 0, column = 1)
        """self.mensaje = Label (self.espacio4)
        self.mensaje.pack (side = TOP) """
        self.imagen_check = PhotoImage (file = './images/correct.png')
        self.boton_aceptar = Button (self.contenedor_botonback,bg = self.color3,image = self.imagen_check,command = partial(self.validar,ind),borderwidth=0)
        self.boton_aceptar.grid (row = 0, column = 3,padx = 20)

        self.borrar_pedidot()
    
    def entrada_datos (self):
        #Etiquetas y entradas

        self.nombre_cliente = Label (self.mitad_izquierda2_arriba,text = "Cliente:",font =self.fuente,bg = self.color3).grid (row=0,pady = 10)
        self.NOMBRE = StringVar()
        self.nombre_clientein = Entry (self.mitad_izquierda2_arriba,textvariable = self.NOMBRE,font = self.fuente)
        self.nombre_clientein.grid (row = 0,column =1,pady = 10,padx = 5)
        self.numero = Label (self.mitad_izquierda2_arriba, text = "Telefono:",font = self.fuente,bg = self.color3).grid (row = 0,column = 2,padx = 5,pady = 20 )
        self.telefonoIN = StringVar()
        self.numeroin = Entry (self.mitad_izquierda2_arriba,textvariable = self.telefonoIN,font = self.fuente).grid (row = 0,column = 3,padx = 5,pady = 5)
        self.RUCI = StringVar()
        self.ruc = Label (self.mitad_izquierda2_arriba, text = "RUC:",font = self.fuente,bg = self.color3).grid (row = 1,column = 0,padx = 5,pady = 5)

        self.rucin = Entry (self.mitad_izquierda2_arriba,textvariable = self.RUCI,font = self.fuente).grid (row = 1,column = 1,padx = 5,pady = 10)
        self.apellido = Label (self.mitad_izquierda2_arriba,text = "Ubicacion:",font = self.fuente,bg = self.color3).grid (row =1,column = 2,pady= 5,padx = 10)
        self.Ubicacion = StringVar()
        self.ubicacion = Entry (self.mitad_izquierda2_arriba,textvariable = self.Ubicacion,font = self.fuente).grid (row =1,column = 3,pady = 5,padx = 10)


    def ventana_delivery (self):
        self.color5 = "gold"
        self.raicita = Toplevel()
        self.raicita.geometry ("200x50")
        self.frame_raicita = Frame (self.raicita,bg = self.color5)
        self.frame_raicita.pack (side = TOP,fill = "both",expand = 1)
        self.var3 = IntVar ()
        self.r1 = Radiobutton(self.frame_raicita, text = "Centro",font = self.fuente, variable = self.var3, value = 1,bg = self.color5,command = self.agg_delivery)
        self.r1.grid (row = 0,column = 0,padx =2,pady = 10)
        self.r2 = Radiobutton(self.frame_raicita, text = "Alrededores",font = self.fuente, variable = self.var3, value = 2,bg = self.color5,command = self.agg_delivery)
        self.r2.grid (row = 0,column = 1,padx =2,pady = 10)

    def agg_delivery (self):
        if self.var3.get () == 1:
            reci = self.run_query("SELECT * FROM Costo_Delivery WHERE id =",repr(1))
            for val in reci:
                print (val)
                INSERT = [(val[1],val[2],3)]
                self.run_querymultiple ("INSERT INTO PedidoT VALUES(NULL,?,?,?)",INSERT)                
        if self.var3.get () == 2:
            reci = self.run_query("SELECT * FROM Costo_Delivery WHERE id =",repr(2))
            for val in reci:
                print (val)
                INSERT = [(val[1],val[2],3)]
                self.run_querymultiple ("INSERT INTO PedidoT VALUES(NULL,?,?,?)",INSERT)
        self.insertar_tabla()
        self.sumador()
        self.cantidad_pizzas()
        self.raicita.destroy()

    def comando_llevar (self):
        self.run_query ("DELETE FROM PedidoT WHERE Precio = 5000 OR Precio = 10000",)
        self.insertar_tabla()
        self.cantidad_pizzas()
        self.sumador()


        #Declaracion de sabores tasty
    def sabores (self,parametro,posicion):
        self.parametro = parametro
        self.muzzarella = StringVar()
        self.palmito = StringVar()
        self.carnivora = StringVar()
        self.pollo_catu = StringVar()
        self.pepperoni = StringVar()
        self.alemana = StringVar()
        self.choclo = StringVar()
        self.jamonymorron = StringVar()
        self.napolitana = StringVar()
        self.pollo_bbq = StringVar()
        self.calabresa = StringVar()
        self.chesseburger = StringVar()
        self.doblequeso = StringVar()
        self.chilitasty = StringVar()
        self.vegetariana = StringVar()
        self.chocloconjamonyqueso = StringVar()
        self.rucula = StringVar()
        self.posicion = posicion
        self.eleccion = 0
        self.colorseleccion = "Red4"
        #Alemana tasty
        self.parametro.sabores.add_checkbutton (label = "Alemana Tasty",variable = self.alemana,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.alemanat,self.posicion))
        #Carnivora tasty
        self.parametro.sabores.add_checkbutton (label = "Carnivora Tasty",variable = self.carnivora,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.carni,self.posicion))
        #Calabresa
        self.parametro.sabores.add_checkbutton (label = "Calabresa",variable = self.calabresa,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.CALABRESA,self.posicion))
        #Chesseburger
        self.parametro.sabores.add_checkbutton (label = "Chesseburger",variable = self.chesseburger,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.CHESEBURGUER,self.posicion))
        #Chili tasty
        self.parametro.sabores.add_checkbutton (label = "Chily Tasty",variable = self.chilitasty,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.CHILI,self.posicion))
        #Choclo
        self.parametro.sabores.add_checkbutton (label = "Choclo",variable = self.choclo,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.choclot,self.posicion))
        #Choclo con jamon y panceta
        self.parametro.sabores.add_checkbutton (label = "Choclo con Jamón",variable = self.chocloconjamonyqueso,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.CHOCLOJAMON,self.posicion))
        #Doble queso
        self.parametro.sabores.add_checkbutton (label = "Doble queso",variable = self.doblequeso,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.DOBLEQUESO,self.posicion))
        #Jamon y morron
        self.parametro.sabores.add_checkbutton (label = "Jamon y Morrón",variable = self.jamonymorron,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.jamonmorron,self.posicion))
        #Sabor muzzarella
        self.parametro.sabores.add_checkbutton (label = "Muzzarella",variable = self.muzzarella,font = self.fuente,activebackground = self.colorseleccion ,command = partial (self.muzza ,self.posicion))
        #Napolitana
        self.parametro.sabores.add_checkbutton (label = "Napolitana",variable = self.napolitana,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.NAPOLITANA,self.posicion))
        #Palmito
        self.parametro.sabores.add_checkbutton (label = "Palmito",variable = self.palmito,font= self.fuente,activebackground = self.colorseleccion,command = partial(self.palmi,self.posicion))
        #Pepperoni
        self.parametro.sabores.add_checkbutton (label = "Pepperoni",variable = self.pepperoni,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.peppe,self.posicion))
        #Pollo con catupiry
        self.parametro.sabores.add_checkbutton (label = "Pollo con Catupiry",variable = self.pollo_catu,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.pollo_catupiry,self.posicion))
        #Pollo con barbacoa
        self.parametro.sabores.add_checkbutton (label = "Pollo BBQ",variable = self.pollo_bbq,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.POLLOBBQ,self.posicion))
        #Rucula
        self.parametro.sabores.add_checkbutton (label = "Rucula",variable = self.rucula,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.RUCU,self.posicion))
        #Vegetariana
        self.parametro.sabores.add_checkbutton (label = "Vegetariana",variable = self.vegetariana,font= self.fuente,activebackground = self.colorseleccion,command = partial (self.VEGETARIANA,self.posicion))

    #
    def muzza (self,posicion):
        puesto = posicion
        if puesto == 2:
            self.pizzaentera('1')

        print ("Se agrego una pizza de muzza ")

        if puesto == 1:
            self.pizza_mitad('1')

        if puesto == 3:
            self.pizza_mitad2('1')
    def palmi (self,posicion):
        puesto = posicion
        if puesto == 2:
            self.pizzaentera('2') 
        print ("Se agrego una pizza de palmito")
        if puesto == 1:
            self.pizza_mitad('2')

        if puesto == 3:
            self.pizza_mitad2('2')

    def carni (self,posicion):
        puesto = posicion
        if puesto == 2:
            self.pizzaentera('3')
        if puesto == 1:
            self.pizza_mitad('3')

        if puesto == 3:
            self.pizza_mitad2('3')

        print ("Se agrego una pizza de carnivora")
        

    def pollo_catupiry (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('4')
        if puesto == 1:
            self.pizza_mitad('4')

        if puesto == 3:
            self.pizza_mitad2('4')

        print ("Se agrego una pizza de pollo con catupiry")

    def peppe (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('5')
        if puesto == 1:
            self.pizza_mitad('5')

        if puesto == 3:
            self.pizza_mitad2('5')

        print ("Se agrego una pizza de pollo con catupiry")

    def alemanat (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('6')
        if puesto == 1:
            self.pizza_mitad('6')

        if puesto == 3:
            self.pizza_mitad2('6')

        print ("Se agrego una pizza de pollo con catupiry")

    def choclot (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('7')
        if puesto == 1:
            self.pizza_mitad('7')

        if puesto == 3:
            self.pizza_mitad2('7')

        print ("Se agrego una pizza de pollo con catupiry")

    def jamonmorron (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('8')
        if puesto == 1:
            self.pizza_mitad('8')

        if puesto == 3:
            self.pizza_mitad2('8')

        print ("Se agrego una pizza de pollo con catupiry")
    
    def NAPOLITANA (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('9')
        if puesto == 1:
            self.pizza_mitad('9')

        if puesto == 3:
            self.pizza_mitad2('9')

        print ("Se agrego una pizza de pollo con catupiry")

    def POLLOBBQ (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('10')
        if puesto == 1:
            self.pizza_mitad('10')

        if puesto == 3:
            self.pizza_mitad2('10')

        print ("Se agrego una pizza de pollo con catupiry")

    def CALABRESA (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('11')
        if puesto == 1:
            self.pizza_mitad('11')

        if puesto == 3:
            self.pizza_mitad2('11')

        print ("Se agrego una pizza de pollo con catupiry")

    def CHESEBURGUER (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('12')
        if puesto == 1:
            self.pizza_mitad('12')

        if puesto == 3:
            self.pizza_mitad2('12')

        print ("Se agrego una pizza de pollo con catupiry")

    def DOBLEQUESO (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('13')
        if puesto == 1:
            self.pizza_mitad('13')

        if puesto == 3:
            self.pizza_mitad2('13')

        print ("Se agrego una pizza de pollo con catupiry")

    def CHILI (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('14')
        if puesto == 1:
            self.pizza_mitad('14')

        if puesto == 3:
            self.pizza_mitad2('14')

        print ("Se agrego una pizza de pollo con catupiry")

    def VEGETARIANA (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('15')
        if puesto == 1:
            self.pizza_mitad('15')

        if puesto == 3:
            self.pizza_mitad2('15')

        print ("Se agrego una pizza de pollo con catupiry")

    def CHOCLOJAMON(self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('16')
        if puesto == 1:
            self.pizza_mitad('16')

        if puesto == 3:
            self.pizza_mitad2('16')

        print ("Se agrego una pizza de pollo con catupiry")
    
    def RUCU (self,posicion):
        puesto = posicion 
        if puesto == 2:
            self.pizzaentera('17')
        if puesto == 1:
            self.pizza_mitad('17')

        if puesto == 3:
            self.pizza_mitad2('17')

        print ("Se agrego una pizza de pollo con catupiry")

    #INGRESA A LA BASE DE DATOS 
    def run_query(self,query,parameters = ''):
        self.db_name = ('./db/TastyDB.db')
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()
            result = self.cursor.execute(query + parameters)
            self.conn.commit()
        return result

    #INSERTA A LA BASE DE DATOS SI ES UN INT
    def run_query2(self,query,parameters = ''):
        self.db_name = ('./db/TastyDB.db')
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()
            result = self.cursor.execute(query + repr(parameters))
            self.conn.commit()
        return result

    #INSERA A LA BASE DE DATOS MULTIPLES DATOS
    def run_querymultiple (self,query,parameters = ''):
        self.db_name = ('./db/TastyDB.db')
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()
            result = self.cursor.executemany(query,parameters)
            self.conn.commit()
        return result

    def run_querymultiple2 (self,query,parameters = ''):
        self.db_name = ('./db/TastyDB.db')
        with sqlite3.connect(self.db_name) as self.conn:
            self.cursor = self.conn.cursor()
            result = self.cursor.executemany(query,parameters)
        return result



    def pizzaentera (self,ind):
        self.botones_sabores()
        query = "SELECT Sabor,Precio FROM Pizzas WHERE Id ="
        resultado = self.run_query(query,ind)
        for valor in resultado:
            lista = [(valor[0],valor[1],1)]
            self.run_querymultiple("INSERT INTO PedidoT VALUES (NULL,?,?,?)",lista)
            self.insertar_tabla()
            self.cantidad_pizzas()
            self.sumador()
            self.conn.commit()
        self.conn.close()

        

    def pizza_mitad (self,ind):
        self.botones_sabores()
        print (ind)
        print ("mitad1")
        self.run_query ("DELETE FROM sqlite_sequence")#LO ULTIMO QUE ESTABAS HACIENDO ES LA SECUENCIA
        self.run_query ("DELETE FROM MITAD")
        query = "SELECT Sabor,Precio FROM Pizzas WHERE Id ="
        resultado = self.run_query(query,ind)
        for valor in resultado:
            lista = [(valor[0],valor[1])]
            print (lista)
            self.run_querymultiple("INSERT INTO MITAD VALUES (NULL,?,?)",lista)
            self.conn.commit()
        self.conn.close()

    def pizza_mitad2 (self,ind):
        print (ind)
        self.botones_sabores()
        print ("mitad2")
        query = "SELECT Sabor,Precio FROM Pizzas WHERE Id ="
        resultado = self.run_query(query,ind)
        for valor in resultado:
            lista = [(valor[0],valor[1])]
            print (lista)
            self.run_querymultiple("INSERT INTO MITAD VALUES (NULL,?,?)",lista)
            self.creador_mitad()
            self.insertar_tabla()
            self.cantidad_pizzas()
            self.sumador()
            self.conn.commit()
        self.conn.close()
    
    def creador_mitad (self):
        pizzas = self.run_query ("SELECT Sabor1 FROM MITAD WHERE id = 1")
        sabor = StringVar()
        for valor in pizzas:
            sabor = valor[0]
        pizzas = self.run_query ("SELECT Sabor1 FROM MITAD WHERE id = 2")
        for valor in pizzas:
            sabor = sabor +"/"+ valor[0]
        pizzas = self.run_query ("SELECT Precio1 FROM MITAD WHERE id = 1")
        precio = IntVar()
        for valor in pizzas:
            precio = valor[0]
        pizzas = self.run_query ("SELECT Precio1 FROM MITAD WHERE id = 2")
        for valor in pizzas:
            print (valor[0])
            if precio == 38000 and valor[0] ==42000 or precio == 42000 and valor[0] ==38000:
                precio = 40000

            elif precio == 38000 and valor[0] ==44000 or precio == 44000 and valor[0] ==38000:
                precio = 42000

            elif precio == 38000 and valor[0] ==45000 or precio == 45000 and valor[0] ==38000:
                precio = 42000
                
            elif precio == 38000 and valor[0] ==48000 or precio == 48000 and valor[0] ==38000:
                precio = 43000

            elif precio == 38000 and valor[0] ==50000 or precio == 50000 and valor[0] ==38000:
                precio = 45000

            elif precio == 38000 and valor[0] ==60000 or precio == 60000 and valor[0] == 38000:
                precio = 50000

            elif precio == 42000 and valor[0] ==44000 or precio == 44000 and valor[0] ==42000:
                precio = 43000

            elif precio == 42000 and valor[0] ==45000 or precio == 45000 and valor[0] ==42000:
                precio = 44000
            
            elif precio == 42000 and valor[0] ==48000 or precio == 48000 and valor[0] ==42000:
                precio = 45000

            elif precio == 42000 and valor[0] ==50000 or precio == 50000 and valor[0] ==42000:
                precio = 46000

            elif precio == 42000 and valor[0] ==60000 or precio == 60000 and valor[0] ==42000:
                precio = 55000
                
            elif precio == 44000 and valor[0] ==45000 or precio == 45000 and valor[0] ==44000:
                precio = 45000

            elif precio == 44000 and valor[0] ==48000 or precio == 48000 and valor[0] ==44000:
                precio = 46000

            elif precio == 44000 and valor[0] ==50000 or precio == 50000 and valor[0] ==44000:
                precio = 47000

            elif precio == 44000 and valor[0] ==60000 or precio == 60000 and valor[0] ==44000:
                precio = 55000

            elif precio == 45000 and valor[0] ==48000 or precio == 48000 and valor[0] ==45000:
                precio = 47000
            
            elif precio == 45000 and valor[0] ==50000 or precio == 50000 and valor[0] ==45000:
                precio = 48000

            elif precio == 45000 and valor[0] ==60000 or precio == 60000 and valor[0] ==45000:
                precio = 55000

            elif precio == 48000 and valor[0] ==50000 or precio == 50000 and valor[0] ==48000:
                precio = 50000
                
            elif precio == 48000 and valor[0] ==60000 or precio == 60000 and valor[0] ==48000:
                precio = 55000
            
            elif precio == 50000 and valor[0] ==60000 or precio == 60000 and valor[0] ==50000:
                precio = 55000
            else: 
                print ("NO EXITS")

        mitad = [(sabor,precio,1)]
        self.run_querymultiple("INSERT INTO PedidoT VALUES (NULL,?,?,?)",mitad)
        self.run_query ("DELETE FROM MITAD")
        self.botones_sabores()
        self.insertar_tabla()
        self.sumador()
        self.cantidad_pizzas()
        print (sabor)
        print (precio)
            

    def insertar_tabla (self):  #INSERTA DATOS EN LA TABLA
        # cleaning Table 
        records = self.arbol.get_children()
        for element in records:
            self.arbol.delete(element)
        # getting data
        query = "SELECT * FROM PedidoT"
        db_rows = self.run_query(query)
        # filling data
        
        for row in db_rows:
            self.arbol.insert('',0, text = row[1], values = (repr(row[2])+" Gs"))

    def insertar_tabla_beb (self):  #INSERTA DATOS EN LA TABLA
        # cleaning Table 
        records = self.arbol.get_children()
        for element in records:
            self.arbol.delete(element)
        # getting data
        query = "SELECT * FROM Bebidas ORDER BY id DESC"
        db_rows = self.run_query(query)
        # filling data
        
        for row in db_rows:
            self.beb.insert('',0, text = row[1], values = (row[2],repr(row [3])+ "Gs"))


    def insertar_tabla_beb1 (self):  #INSERTA DATOS EN LA TABLA
        # cleaning Table 
        records = self.beb1.get_children()
        for element in records:
            self.beb1.delete(element)
        # getting data
        query = "SELECT * FROM Pedidot  WHERE punt == '2'"
        db_rows = self.run_query(query)
        # filling data
        
        for row in db_rows:
            self.beb1.insert('',0, text = row[1], values = (repr(row [2])+ "Gs"))

    def insertar_tablageneral(self,codigo=0):
        if codigo==1:
            self.insertar_tabla2()
        if codigo ==2:
            self.insertar_tabla4()
        if codigo ==3:
            self.insertar_tabla3()
    def insertar_tabla2 (self):  #INSERTA DATOS EN LA TABLA
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Pedido ORDER BY ID"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))

    def insertar_tabla3 (self):  #INSERTA DATOS EN LA TABLA
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Entregado ORDER BY id"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))
    def insertar_tabla4 (self):  #INSERTA DATOS EN LA TABLA
        # cleaning Table 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = "SELECT * FROM Delivery_table ORDER BY id"
        #db_rows = self.run_query(query)
        db_rows = Prueba_Server.run_queryServer7 (query)
        # filling data
        
        for row in db_rows:
            self.tree.insert('',0, text = row[1], values = (repr(row[3])+"Gs",row [2],row [4],row[5],row[6],row[7],row[8]))

    def borrar_pedidot (self):  #BORRA LAS BASES DE DATOS PEDIDOT Y REINICIA LA TABLA
        self.run_query ("DELETE FROM PedidoT")
        self.run_query ("DELETE FROM MITAD")
        self.run_query ("DELETE FROM sqlite_sequence")#LO ULTIMO QUE ESTABAS HACIENDO ES LA SECUENCIA
        self.botones_sabores()
        self.insertar_tabla()
        self.sumador()
        self.cantidad_pizzas()

    def cantidad_pizzas (self):    #CUENTA LA CANTIDAD DE PIZZAS
        result = self.run_query("SELECT COUNT (*)FROM PedidoT WHERE punt =1")
        valor = result
        for valor in result:
            self.etiqueta_cantidadT.config (text = valor[0])
        return valor


    def sumador (self):    #SUMA PARA OBTENER EL COSTO TOTAL DE PIZZAS
        suma = self.run_query("SELECT SUM (Precio) FROM PedidoT")
        valor = suma
        for valor in suma:
            if valor [0]==None:
                self.etiqueta_precioT.config (text = 0)
            self.etiqueta_precioT.config (text = valor[0])
        return valor
    

    def botones_sabores(self):  #RESTAURA EL BOTON DE SABORES

        #CHECK BUTTON PARA ELECCION DE SABORES
        self.toping = PhotoImage(file = "./images/mas.png")
        self.boton_toppings = Button (self.contenedor_cant_pizzas,image = self.toping,bg = self.color3,fg = "snow",command = self.toppings,borderwidth=0)
        self.boton_toppings.grid (row =0,column = 0,padx = 20)

        self.pizza_image = PhotoImage (file = './images/pizza2.png')
        self.cantpizzas = Menubutton (self.contenedor_cant_pizzas,image = self.pizza_image,font = ("Verdana",20),bg = self.color3,fg = "snow" )
        self.cantpizzas.grid (row = 0,column = 2,pady = 15,padx = 5)
        self.cantpizzas.sabores = Menu (self.cantpizzas,tearoff =0 )
        self.cantpizzas ["menu"] = self.cantpizzas.sabores
        self.sabores (self.cantpizzas,2)



        self.pizza_image1 = PhotoImage (file = './images/pizzamizquierda.png')
        self.cantpizzas1 = Menubutton (self.contenedor_cant_pizzas,image = self.pizza_image1,font = ("Verdana",20),bg = self.color3,fg = "snow" )
        self.cantpizzas1.grid (row = 0,column = 1,pady = 5,padx = 5)
        self.cantpizzas1.sabores = Menu (self.cantpizzas1,tearoff =0 )
        self.cantpizzas1 ["menu"] = self.cantpizzas1.sabores
        self.sabores (self.cantpizzas1,1)


        self.pizza_image2 = PhotoImage (file = './images/pizzamderecha.png')
        self.cantpizzas2 = Menubutton (self.contenedor_cant_pizzas,image = self.pizza_image2,font = ("Verdana",20),bg = self.color3,fg = "snow" )
        self.cantpizzas2.grid (row = 0,column = 3,pady = 5,padx = 5)
        self.cantpizzas2.sabores = Menu (self.cantpizzas2,tearoff =0 )
        self.cantpizzas2 ["menu"] = self.cantpizzas2.sabores
        self.sabores (self.cantpizzas2,3)

        self.bebi = PhotoImage (file = "./images/refresco.png")
        self.boton_bebidas = Button (self.contenedor_cant_pizzas,image = self.bebi,bg = self.color3,fg = "snow",command = self.pestaña_bebidas,borderwidth=0)
        self.boton_bebidas.grid (row = 0,column = 4,padx = 20)

    def insertar_pedido(self,ind = 0):   #INSERTA EL PEDIDO EN LA TABLA DE PEDIDO TEMPORAL 
        ind = ind 
        factura_in = ""
        if self.factura.get() ==1:
            factura_in = "Si"
        else:
            factura_in = "No"
        para = ""
        if self.var.get() == 1:
            para = "Llevar"
        elif self.var.get()==2:
            para = "Delivery"
        else:
            para = "Comer en el lugar"
        pago = ""
        if self.billetepago.get() == 0:
            pago = "No"
        else:
            pago = "Si"

        nombre_clienteup = self.NOMBRE.get ()
        nombre_cliente = [nombre_clienteup.upper(),0,0,para,factura_in,pago]

        result = self.cantidad_pizzas()
        for valor in result:

            nombre_cliente[1]=valor

        suma = self.sumador()
        for valor in suma:
            nombre_cliente[2]= valor
        instanteInicial = datetime.now()
        ubi = self.Ubicacion.get()
        insercion = [(nombre_cliente[0],nombre_cliente[1],nombre_cliente[2],nombre_cliente[3],nombre_cliente[4],nombre_cliente[5],"{}:{}:{}".format(instanteInicial.hour, instanteInicial.minute, instanteInicial.second),ubi.upper())]
        print (insercion)
        suma = Prueba_Server.run_queryServer4("SELECT COUNT (*) FROM En_espera")
        su = suma[0]+1

        telefono = ''
        if self.telefonoIN.get() == '':
            telefono = 'NULL'
        else:
            telefono = self.telefonoIN.get()
        ruc = ''
        if self.RUCI.get() == '':
            ruc = 'NULL'
        else:
            ruc = self.RUCI.get()
        if ind ==0:
            #self.run_querymultiple("INSERT INTO Pedido VALUES (NULL,?,?,?,?,?,?,?,?)",insercion)
            Prueba_Server.run_queryServer3("INSERT INTO Pedido VALUES ("+repr(su)+",?,?,?,?,?,?,?,?)",insercion)
            Prueba_Server.run_queryServer3("INSERT INTO En_espera VALUES (?,?,?,?,?,?,?,?,"+repr(su)+","+repr(ruc)+","+repr(telefono)+")",insercion)
            guardado = self.run_query ("SELECT Sabor,Precio,punt FROM PedidoT")
            for valor in guardado:
                tupla = [(nombre_clienteup.upper(),valor[0],valor[1],valor[2])]
                print (tupla)
                Prueba_Server.run_queryServer3("INSERT INTO Pizzas VALUES (?,?,?,?)",tupla)
        if ind ==1:
            #self.run_query("UPDATE Pedido SET Cantidad = "+ repr (nombre_cliente [1])+" ,Precio = "+ repr (nombre_cliente [2])+" ,Para = "+ repr (nombre_cliente [3])+" ,Factura = "+ repr (nombre_cliente [4])+" ,Pago = "+ repr (nombre_cliente [5])+" ,Ubicacion = "+ repr(ubi.upper())+" WHERE Cliente = "+"'"+nombre_cliente[0]+"'" )
            Prueba_Server.run_queryServer5("UPDATE Pedido SET Cantidad = "+ repr (nombre_cliente [1])+" ,Precio = "+ repr (nombre_cliente [2])+" ,Para = "+ repr (nombre_cliente [3])+" ,Factura = "+ repr (nombre_cliente [4])+" ,Pago = "+ repr (nombre_cliente [5])+" ,Ubicacion = "+ repr(ubi.upper())+" WHERE Cliente = "+"'"+nombre_cliente[0]+"'" )
            Prueba_Server.run_queryServer5("UPDATE En_espera SET Cantidad = "+ repr (nombre_cliente [1])+" ,Precio = "+ repr (nombre_cliente [2])+" ,Para = "+ repr (nombre_cliente [3])+" ,Factura = "+ repr (nombre_cliente [4])+" ,Pago = "+ repr (nombre_cliente [5])+" ,Ubicacion = "+ repr(ubi.upper()) +" ,ruc = "+ repr(ruc) +" ,telefono = "+ repr(telefono) +" WHERE Cliente = "+"'"+nombre_cliente[0]+"'")
            parametro = "DELETE FROM Pizzas WHERE Punt_cliente ="+"'"+nombre_cliente[0]+"'"
            Prueba_Server.run_queryServer5 (parametro)
            guardado = self.run_query ("SELECT Sabor,Precio,punt FROM PedidoT")
            for valor in guardado:
                tupla = [(nombre_clienteup.upper(),valor[0],valor[1],valor[2])]
                print (tupla)
                Prueba_Server.run_queryServer3("INSERT INTO Pizzas VALUES (?,?,?,?)",tupla)

        self.raiz2.destroy()
        self.insertar_tabla2()
        self.funcionhendy(1)


    


    def pestaña_pago (self,ind = 0):   #ESTA FUNCION CREA UNA PESTAÑA PARA PAGO E IMPRESION DE TICKET
        self.color4 = "DarkSeaGreen2"
        ind = ind

        self.nombre_clienteup = self.NOMBRE.get ()
        nombre_cliente = [self.nombre_clienteup.upper(),0,0]
        result = self.cantidad_pizzas()
        for valor in result:
            nombre_cliente[1]=valor
        suma = self.sumador()
        for valor in suma:
            nombre_cliente[2]= valor
        self.raiz2 = Toplevel()
        self.raiz2.title ("Pago")
        self.raiz2.geometry ("800x410")
        self.raiz2.focus()
        self.contenedor_pago = Frame (self.raiz2,bg = self.color4)
        self.contenedor_pago.pack (side = TOP,fill = "both",expand = 1)
        contenedor_nombre = LabelFrame (self.contenedor_pago,text = "Datos del cliente",font = self.fuente,bd = 5,bg = self.color4)
        contenedor_nombre.pack (side = TOP,fill = "both",pady = 10,padx = 20)
        nombre = Label (contenedor_nombre,text = "Cliente:",font = self.fuente,bg = self.color4)
        nombre.grid (row = 0,padx = 5,sticky = "w")
        self.nombret = Label (contenedor_nombre,text = nombre_cliente[0],font = self.fuente,bg = self.color4)
        self.nombret.grid (row = 0,column = 1,padx = 5,sticky = "w")

        self.RUC = Label (contenedor_nombre,text = "RUC:",font = self.fuente,bg = self.color4)
        self.RUC.grid (row = 1,padx = 5,sticky = "w")
        ruc = self.RUCI.get ()
        self.RUCin = Label (contenedor_nombre,text = ruc ,font= self.fuente,bg = self.color4)
        self.RUCin.grid (row = 1,column = 1,sticky = "w")

        self.telefono = Label (contenedor_nombre,text = "Telefono:",font = self.fuente,anchor = "w",bg = self.color4)
        self.telefono.grid (row = 2,sticky = "w")
        self.telefonoin = Label (contenedor_nombre,text = self.telefonoIN.get(),font = self.fuente,bg = self.color4)
        self.telefonoin.grid (row = 2,column = 1,sticky = "w")
        button_pago = Frame (self.contenedor_pago,bg = self.color4)
        button_pago.pack (side = TOP,fill = 'both',padx = 20)
        self.image_money = PhotoImage(file = "./images/money.PNG")
        self.button_money = Button (button_pago,image = self.image_money,command = self.efectivo)
        self.button_money.grid (row = 0,column = 0,padx = 10,pady = 10)
        self.image_creditcard = PhotoImage(file = "./images/credit_card.png")
        self.button_credit= Button (button_pago,image = self.image_creditcard,command = self.tarjeta)
        self.button_credit.grid (row = 0,column = 1,padx = 10)
        self.variador = StringVar()
        self.indicador = Label (button_pago,textvariable = self.variador)
        self.indicador.grid (row = 0,column = 2,padx = 20)

        """
        self.pago = LabelFrame (contenedor_pago,text = "Pago en efectivo",font = self.fuente,bd = 5,bg = self.color4)
        self.pago.pack (side = TOP,fill = "both",padx = 20)
        self.Cant_pizzas =Label (self.pago,text = "Cant.Pizzas:",font = self.fuente,anchor = "w",bg = self.color4)
        self.Cant_pizzas.grid (row = 0,pady = 5,sticky = "w")
        self.Cant_pizzas_in = Label (self.pago,font = self.fuente ,bg = self.color4)
        self.Cant_pizzas_in.grid (row = 0,column = 1,sticky = "w")
        cantidad = self.cantidad_pizzas()
        for valor in cantidad:
            self.Cant_pizzas_in.config (text = valor,anchor = "w")

        espacio = Frame (self.pago)
        espacio.grid (row = 0,column = 2,padx = 20)
        precio= Label (self.pago,text = "Precio Total:",font = self.fuente,bg = self.color4)
        precio.grid (row = 0,column = 3,pady = 5,sticky = "w")
        precioin = Label (self.pago,font = self.fuente,bg = self.color4)
        precioin.grid (row = 0,column = 4,sticky = "w") 
        suma = self.sumador()
        Gs = Label (self.pago,text = "Gs",font = self.fuente,bg = self.color4)
        Gs.grid (row = 0,column = 5,sticky = "w")
        for valor in suma:
            precioin.config (text = valor )

        billete = Label (self.pago,text = "Billete:",font = self.fuente,bg = self.color4)
        billete.grid (row = 1,sticky = "w")
        self.billetepago = IntVar()
        self.billetein = Entry (self.pago,textvariable = self.billetepago,font =self.fuente)
        self.billetein.grid (row = 1,column = 1,sticky = "w")
        espacio2 = Frame (self.pago)
        espacio2.grid (row = 1,column = 2)
        vuelto = Label (self.pago,text = "Vuelto:",font = self.fuente,bg = self.color4)
        vuelto.grid (row = 1,column = 3,padx = 20,sticky = "w")
        self.vueltoin = Label (self.pago,font = self.fuente,bg = self.color4)
        self.vueltoin.grid (row = 1,column = 4,sticky = "w")
        self.gs = Label (self.pago,font = self.fuente,bg =self.color4)
        self.gs.grid (row = 1,column = 5)
        self.contenedor_botones = Frame (self.pago,bg = self.color4)
        self.contenedor_botones.grid (row = 2,column = 0,columnspan = 8)
        boton100 = Button (self.contenedor_botones,text = "100.000Gs",font = self.fuente,command = partial (self.obtener_vuelto,2))
        boton100.grid (row = 0,pady = 5,padx = 10)

        boton50 = Button (self.contenedor_botones,text = "50.000Gs",font = self.fuente,command = partial (self.obtener_vuelto,1))
        boton50.grid (row = 0,column = 1,pady= 5,padx = 10)
        self.update = PhotoImage (file = './images/PAGO.PNG')
        boton_update = Button (self.contenedor_botones,image = self.update,command = self.obtener_vuelto)
        boton_update.grid (row = 0,column = 2,pady = 5,padx = 10)
        epsacio5 = Frame (self.contenedor_botones)
        epsacio5.grid (row = 0,column = 3,padx = 90)
        boton_fin = Button (self.contenedor_botones,text = "Listo",font = self.fuente,command =partial(self.generador_ticket,ind))
        boton_fin.grid (row = 0,column = 5)
        ind2 = ind
        self.raiz2.bind("<Return>",partial(self.atajo,ind,ind2))"""

        self.admin_pago(ind)
        self.efectivo()
    def efectivo (self):
        self.button_money.config (state = DISABLED)
        self.button_credit.config (state = NORMAL)
        self.valorador = 1
        self.pago.config (text = "Pago en efectivo")
        self.billete.config (text = "Billete:")
        self.boton100.config (state = NORMAL)
        self.boton50.config (state = NORMAL)
        self.boton_update.config (state = NORMAL)
        self.variador.set("EFECTIVO")
        self.indicador.config (bg = "Yellow",fg = "Black",font = ("Verdana",24))
        self.boton_fin.config(command =partial(self.generador_ticket,self.ind,1))
        self.raiz2.bind("<Return>",partial(self.atajo,self.ind,ind2= self.ind,ind3 = 1))
    
    def tarjeta (self):
        self.button_credit.config (state = DISABLED)
        self.button_money.config (state = NORMAL)
        self.valorador = 2
        self.pago.config (text = "Pago por tarjeta")
        self.billete.config (text = "N° de transaccion:")
        self.boton100.config (state = DISABLED)
        self.boton50.config (state = DISABLED)
        self.boton_update.config (state = DISABLED)
        self.variador.set("CRÉDITO")
        self.indicador.config (bg = "Green2",fg = "Black",font = ("Verdana",24))
        self.boton_fin.config(command =partial(self.generador_ticket,self.ind,2))
        self.raiz2.bind("<Return>",partial(self.atajo,self.ind,ind2 = self.ind,ind3 = 2))

    
    def admin_pago (self,ind):
        self.ind = ind
        self.pago = LabelFrame (self.contenedor_pago,text = "Pago en efectivo",font = self.fuente,bd = 5,bg = self.color4)
        self.pago.pack (side = TOP,fill = "both",padx = 20)
        self.Cant_pizzas =Label (self.pago,text = "Cant.Pizzas:",font = self.fuente,anchor = "w",bg = self.color4)
        self.Cant_pizzas.grid (row = 0,pady = 5,sticky = "w")
        self.Cant_pizzas_in = Label (self.pago,font = self.fuente ,bg = self.color4)
        self.Cant_pizzas_in.grid (row = 0,column = 1,sticky = "w")
        cantidad = self.cantidad_pizzas()
        for valor in cantidad:
            self.Cant_pizzas_in.config (text = valor,anchor = "w")

        espacio = Frame (self.pago)
        espacio.grid (row = 0,column = 2,padx = 20)
        precio= Label (self.pago,text = "Precio Total:",font = self.fuente,bg = self.color4)
        precio.grid (row = 0,column = 3,pady = 5,sticky = "w")
        precioin = Label (self.pago,font = self.fuente,bg = self.color4)
        precioin.grid (row = 0,column = 4,sticky = "w") 
        suma = self.sumador()
        Gs = Label (self.pago,text = "Gs",font = self.fuente,bg = self.color4)
        Gs.grid (row = 0,column = 5,sticky = "w")
        for valor in suma:
            precioin.config (text = valor )

        self.billete = Label (self.pago,text = "Billete:",font = self.fuente,bg = self.color4)
        self.billete.grid (row = 1,sticky = "w")
        self.billetepago = IntVar()
        self.billetein = Entry (self.pago,textvariable = self.billetepago,font =self.fuente)
        self.billetein.grid (row = 1,column = 1,sticky = "w")
        espacio2 = Frame (self.pago)
        espacio2.grid (row = 1,column = 2)
        self.vuelto = Label (self.pago,text = "Vuelto:",font = self.fuente,bg = self.color4)
        self.vuelto.grid (row = 1,column = 3,padx = 20,sticky = "w")
        self.vueltoin = Label (self.pago,font = self.fuente,bg = self.color4)
        self.vueltoin.grid (row = 1,column = 4,sticky = "w")
        self.gs = Label (self.pago,font = self.fuente,bg =self.color4)
        self.gs.grid (row = 1,column = 5)
        self.contenedor_botones = Frame (self.pago,bg = self.color4)
        self.contenedor_botones.grid (row = 2,column = 0,columnspan = 8)
        self.boton100 = Button (self.contenedor_botones,text = "100.000Gs",font = self.fuente,command = partial (self.obtener_vuelto,2))
        self.boton100.grid (row = 0,pady = 5,padx = 10)

        self.boton50 = Button (self.contenedor_botones,text = "50.000Gs",font = self.fuente,command = partial (self.obtener_vuelto,1))
        self.boton50.grid (row = 0,column = 1,pady= 5,padx = 10)
        self.update = PhotoImage (file = './images/PAGO.PNG')
        self.boton_update = Button (self.contenedor_botones,image = self.update,command = self.obtener_vuelto)
        self.boton_update.grid (row = 0,column = 2,pady = 5,padx = 10)
        epsacio5 = Frame (self.contenedor_botones)
        epsacio5.grid (row = 0,column = 3,padx = 70)
        if self.factura.get() ==1:
            self.boton_print =Button (self.contenedor_botones,text = "Factura",font = self.fuente,command = self.factu_print)
            self.boton_print.grid (row = 0,column =5,padx = 5)
        self.boton_fin = Button (self.contenedor_botones,text = "Listo",font = self.fuente)
        self.boton_fin.grid (row = 0,column = 6)

    def factu_print (self):
        factura = open ("factura.txt","w")
        sumas = 0
        for t in range (3):
            instanteInicial = datetime.now()
            mes = ''
            meses = {1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Setiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
            factura.write ("                                     {}      {}         {}                        ".format(instanteInicial.day, meses[instanteInicial.month], instanteInicial.year)+"")
            if self.valorador ==1:
                factura.write ("X\n")
            else:
                factura.write ("           X\n")
            name = self.NOMBRE.get ()
            factura.write ("                              "+self.NOMBRE.get ())
            print (len(name))
            
            espacio = 35-len(name)
            print (espacio)
            for x in range(espacio):
                factura.write (" ")
                print (x+1)
            factura.write ("        "+self.RUCI.get()+"\n")
            factura.write ("                               ")
            ubi = self.Ubicacion.get()
            #factura.write (ubi)
            espacio = 34-len(ubi)
            if espacio <= 0:
                factura.write (ubi[0:34])
            else:
                factura.write (ubi)
                for x in range(espacio):
                    factura.write (" ")
                    print (x+1)
            factura.write ("        "+self.telefonoIN.get()+"\n\n\n\n")
            query = "SELECT * FROM PedidoT"
            db_rows = self.run_query(query)
            cont = 0
            restante = 12
            for valor in db_rows:
                restante = restante -1
                cont = 1
                factura.write ("                          "+repr(cont)+"         ")
                obj = len(valor[1])#+"-"+repr(valor[2])+"\n\n")
                extension = 32 - obj
                factura.write (valor[1])
                for x in range (extension):
                    factura.write (" ")
                factura.write (" "+repr(valor[2]))

                obj = len(repr(valor[2]))
                extension = 8 - obj
                for x in range (extension):
                    factura.write (" ")
                factura.write("                         "+repr(valor[2]))
                factura.write ("\n")
            print (restante)
            for x in range (restante):
                factura.write ("\n")
            factura.write ("                                                                                                      ")
            suma = self.run_query("SELECT SUM (Precio) FROM PedidoT")
            text = ''
            sumado = 0
            for valor in suma:
                factura.write (repr(valor[0])+"\n")
                text = Num_text.num (valor[0])
                sumado = valor[0]
            factura.write ("                                         "+text)
            espa = len (text)
            espacio = 46 - espa
            for x in range (espacio):
                factura.write (" ")
            factura.write ("    "+repr (sumado)+"\n")
            iva = sumado / 11
            factura.write ("                                                                 "+repr (int(iva))+"                     "+repr (int(iva)))
            if sumas == 0:
                factura.write ("\n\n\n\n\n\n\n\n\n")
            else:
                factura.write ("\n\n\n\n\n\n\n\n")
            sumas = sumas +1
        
        
        






        subprocess.Popen(["notepad","factura.txt"])


    def atajo (self,event,ind,ind2 = 1,ind3 = 0):
        ind = ind
        ind2 = ind2
        ind3 = ind3
        print (ind)
        print (ind2)
        print(ind3)
        self.generador_ticket(ind2,ind3)

    def agg_cliente_boton (self):
        if self.telefonoIN.get() == '' and self.RUCI.get() == '':
            print ("Cliente Casual")
            return 
        variable = Prueba_Server.run_queryServer("SELECT * FROM Clientes_Tasty WHERE Telefono = ","'"+self.telefonoIN.get()+"'")
        estado = variable.fetchone()
        variable2 = Prueba_Server.run_queryServer("SELECT * FROM Clientes_Tasty WHERE ruc = ","'"+self.RUCI.get()+"'")
        estado2 = variable2.fetchone()
        if estado == None and estado2 != None : #estabas colocando lo
            self.boton_agregar = Button (self.contenedor_botones,text = "Rellenar",command = partial(self.rellenar_cliente,self.RUCI.get()),font = self.fuente)
            self.boton_agregar.grid (row = 0,column =4,padx = 10)
        if estado == None and estado2 ==  None:
            self.image_client = PhotoImage (file = "./images/agguser.png")
            self.boton_agregar = Button (self.contenedor_botones,image = self.image_client,command = self.agg_cliente)
            self.boton_agregar.grid (row = 0,column =4,padx = 10)
        else:
            print ("EXISTE")
        
    def can_entregados (self):
        valor = Prueba_Server.run_queryServer4("SELECT COUNT (*) FROM Entregado")
        return valor
    
    def can_deliverys (self):
        valor = Prueba_Server.run_queryServer4("SELECT COUNT (*) FROM Entregado WHERE Para = 'LUIS' OR Para = 'ADAM'")
        return valor

    def cant_luis (self):
        val = Prueba_Server.run_queryServer4("SELECT SUM (Servicio) FROM dbo.Deliverys WHERE  Nombre = 'Luis'")
        return val

    def cant_adam (self):
        val = Prueba_Server.run_queryServer4("SELECT SUM (Servicio) FROM dbo.Deliverys WHERE  Nombre = 'Adam'")
        return val

    def can_llevar (self):
        valor = Prueba_Server.run_queryServer4("SELECT COUNT (*) FROM Entregado WHERE Para = 'Llevar'")
        return valor
        
    def can_comer (self):
        valor = Prueba_Server.run_queryServer4("SELECT COUNT (*) FROM Entregado WHERE Para = 'Comer en el lugar'")
        return valor

    def can_pizzas (self):
        valor = Prueba_Server.run_queryServer4("select count (*) from dbo.Pizzas WHERE Punt = 1")
        print (valor)
        self.eti_cantidad_p_entry.config (text =valor[0])
        return valor
    
    def can_pizzas_sinfact (self):
        valor = Prueba_Server.run_queryServer4("select SUM (Cantidad) from Entregado WHERE Factura = 'No'")
        return valor


    def suma_precios (self):
        valor = Prueba_Server.run_queryServer4("SELECT SUM (Precio) FROM Entregado")
        return valor

    def can_sinfact (self):
        valor = Prueba_Server.run_queryServer4("SELECT SUM (Precio) FROM Entregado WHERE Factura = 'No'")
        return valor


    def pestaña_reportes (self):
        self.fuente2 = ("Clarendon Blk ",15)
        color = "gray9"
        letra = "snow"
        val = self.can_entregados()
        val1 = self.can_deliverys()
        val2 = self.can_llevar()
        val3 = self.can_comer()
        val4 = self.suma_precios()
        val5 = self.cant_luis()
        val6 = self.cant_adam()
        raiz = Toplevel()
        raiz.geometry("400x550")
        raiz.resizable (0,0)
        frame_principal = Frame (raiz,bg = "gray9")
        frame_principal.pack (side = TOP,fill = "both",expand = 1)
        frame_etiquetas = LabelFrame (frame_principal,bg = "gray9",text = "Reporte Final",font = ("CHEESE PIZZA",40), bd = 10,fg = "snow" )
        frame_etiquetas.pack (side = TOP,fill= "both",expand = 1,pady = 10,padx = 10)
        #Etiquta que muestra la cantidad de ordenes tomadas
        eti_cantidad = Label (frame_etiquetas,text = "Pedidos entregados: ",font = self.fuente2,bg = color,fg = letra)
        eti_cantidad.grid (row =0 ,column =0 ,padx = 10,pady = 10)
        eti_cantidad_entry = Label (frame_etiquetas,text = val[0] ,font = self.fuente2,bg = color,fg = letra)
        eti_cantidad_entry.grid (row = 0,column = 1, padx = 10, pady = 10)
        #ETIQUETA QUE MUESTRA LA CANTIDAD DE PIZZAS VENDIDAS
        eti_cantidad_p = Label (frame_etiquetas,text = "Pizzas Vendidas: ",font = self.fuente2,bg = color,fg = letra)
        eti_cantidad_p.grid (row = 1,column =0,pady = 10)
        self.eti_cantidad_p_entry = Label (frame_etiquetas,font = self.fuente2,bg = color,fg = letra)
        self.eti_cantidad_p_entry.grid (row = 1,column = 1,pady = 10)
        self.can_pizzas()
        can_deliverys = Label (frame_etiquetas,text = "Cantidad Deliverys:",font = self.fuente2,bg = color,fg = letra)
        can_deliverys.grid (row = 2,column = 0,pady = 10)
        can_deliverys_entry = Label (frame_etiquetas,text = val1[0],font = self.fuente2,bg = color,fg = letra)
        can_deliverys_entry.grid (row = 2,column = 1,pady = 10)
        can_llevar = Label (frame_etiquetas,text = "Cantidad Llevar:",font = self.fuente2,bg = color,fg = letra)
        can_llevar.grid (row = 3,column = 0)
        can_llevar_entry = Label (frame_etiquetas,text = val2[0],font = self.fuente2,bg = color,fg = letra)
        can_llevar_entry.grid (row = 3,column = 1,pady = 10)
        can_comer = Label (frame_etiquetas,text = "Cantidad Lugar:",font = self.fuente2,bg = color,fg = letra)
        can_comer.grid (row = 4,column = 0,pady = 10)
        can_comer_entry = Label (frame_etiquetas,text = val3[0] ,font = self.fuente2,bg = color,fg = letra)
        can_comer_entry.grid (row = 4,column = 1,pady = 10)
        can_precio = Label (frame_etiquetas,text = "Ingreso Total:" ,font = self.fuente2,bg = color,fg = letra)
        can_precio.grid (row = 5,column = 0)
        can_precio_entry  = Label (frame_etiquetas,text = repr(val4[0])+" Gs" ,font = self.fuente2,bg = color,fg = letra)
        can_precio_entry.grid (row = 5,column = 1,pady = 10)
        can_luis = Label (frame_etiquetas,text = "Entregas Luis:",font = self.fuente2,bg = color,fg = letra)
        can_luis.grid (row = 6,column = 0,padx = 10)
        can_luis_entry = Label (frame_etiquetas,text =val5[0],font = self.fuente2,bg = color,fg = letra)
        can_luis_entry.grid (row = 6,column = 1,pady = 10)
        can_adam = Label (frame_etiquetas,text = "Entregas Adam:",font = self.fuente2,bg = color,fg = letra)
        can_adam.grid (row = 7,column = 0,padx = 10)
        can_adam_entry = Label (frame_etiquetas,text =val6[0],font = self.fuente2,bg = color,fg = letra)
        can_adam_entry.grid (row = 7,column = 1,pady = 10)


        boton_ver = Button (frame_etiquetas,text = "Reporte",font = self.fuente2,bg = color ,fg = letra,command = self.pestaña_pizzas)
        boton_ver.grid (row = 8,column= 0)
        boton_cerrar = Button (frame_etiquetas,text = "Cerrar",font = self.fuente2,bg = color ,fg = letra,command =  self.cerrar)
        boton_cerrar.grid (row = 8,column = 1)




    def pestaña_pizzas (self):
        """raiz3 = Toplevel()
        raiz3.geometry ('500x400')
        self.trees = ttk.Treeview(raiz3,height = 19, columns = ("one"))
        self.trees.pack(side = TOP,fill = 'both')
        self.trees.column ("#0",width =10)
        self.trees.column ("one",width =10)
        self.trees.heading('#0', text = 'PIZZAS', anchor = CENTER)
        self.trees.heading('one', text = 'CANT', anchor = CENTER)"""
        #var = Prueba_Server.run_queryServer7('SELECT COUNT(Sabor), Sabor FROM Pizzas WHERE Punt = ''1'' GROUP BY Sabor ORDER BY COUNT(Sabor) ASC')
        var2 = Prueba_Server.run_queryServer7('SELECT Sabor FROM Pizzas WHERE Punt = ''1''')
        for x in var2:
            #print (x)
            if '/' in x[0]:
                self.Separ = x[0].split ('/')
                #print (self.Separ[0]+"____0.5")
                #print (self.Separ[1]+"____0.5")
                for i in self.Separ:
                    cont = [(i,0.5)]
                    self.run_querymultiple ("INSERT INTO recol_pizzas VALUES (?,?)",cont)
            else:
                #print (x[0]+"____1")
                cont = [(x[0],1)]
                self.run_querymultiple ("INSERT INTO recol_pizzas VALUES (?,?)",cont)
        self.sinte_pizzas ()

        self.generador_reporte()
        self.generador_pagos()
    def sinte_pizzas (self):
        pizzas = ("MUZARELLA","PALMITO","CARNIVORA TASTY","POLLO CATUPIRY","PEPPERONI","ALEMANA TASTY","CHOCLO","JAMON Y MORRON","NAPOLITANA","POLLO BBQ","CALABRESA","CHEESEBURGER","DOBLE QUESO","CHILI TASTY","VEGETARIANA","CHOCLO JAMON Y PANCETA","RUCULA")
        pizza = open ("pizza.txt","w")
        instanteInicial = datetime.now()
        pizza.write ("Fecha de Conteo: "+"{}/{}/{}".format(instanteInicial.day, instanteInicial.month, instanteInicial.year)+"\n")
        for x in pizzas:
            var = self.run_query ("SELECT SUM(Valor) FROM recol_pizzas WHERE Sabor = "+"'"+x+"'")
            for i in var:
                #print (repr(x)+repr(i))
                #self.records = self.trees.get_children()
                if i[0] == None:
                    print ("No existe")
                else:
                    #self.trees.insert('',0, text = x, values = i)
                    reco = x
                    reco = 23 - len(reco)
                    pizza.write (x)
                    for t in range (reco):
                        pizza.write ("-")
                    pizza.write (repr(i[0])+"\n")
        self.run_query ("DELETE FROM recol_pizzas")
        subprocess.Popen(["notepad","pizza.txt"]) 


    def rellenar_cliente (self,ruc  = ''):
        ruc = ruc
        consulta = "UPDATE Clientes_Tasty SET telefono = "+self.telefonoIN.get()+" WHERE ruc = "+"'"+ruc+"'"
        variable = Prueba_Server.run_queryServer5(consulta)




    def agg_cliente(self):  #FUNCION QUE AGREGA CLIENTES NUEVOS A LA BASE DE DATOS
        self.boton_agregar.config (state = DISABLED)
        nombre = self.NOMBRE.get()
        telefono = ''
        if self.telefonoIN.get() == '':
            telefono = 'NULL'
        else:
            telefono = self.telefonoIN.get()
        ruc = ''
        if self.RUCI.get() == '':
            ruc = 'NULL'
        else:
            ruc = self.RUCI.get()
        dire = ''
        if self.Ubicacion.get() == '':
            dire = 'NULL'
        else:
            dire = self.Ubicacion.get()
        #cliente_datos = [(nombre.upper(),'',ruc,'',ubi.upper(),telefono)]
        consulta = "INSERT INTO Clientes_Tasty VALUES ("+"'"+nombre.upper()+"'"+",NULL,"+repr(ruc)+",NULL"+","+"'"+dire+"'"+","+repr(telefono)+")"
        print (consulta)
        Prueba_Server.run_queryServer6(consulta)

    def generador_reporte (self):
        va = self.can_pizzas()
        val = self.can_entregados()
        val1 = self.can_deliverys()
        val2 = self.can_llevar()
        val3 = self.can_comer()
        val4 = self.suma_precios()
        val5 = self.cant_luis()
        val6 = self.cant_adam()
        val7 = self.can_sinfact ()
        val8 = self.can_pizzas_sinfact()
        ticket = open ("report.txt","w")
        ticket.write("           Tasty Pizzas\n")
        ticket.write ("         INFORME DEL DIA\n ")
        ticket.write ("\n")
        instanteInicial = datetime.now()
        ticket.write ("Fecha de Cierre: "+"{}/{}/{}".format(instanteInicial.day, instanteInicial.month, instanteInicial.year)+"\n")
        ticket.write ("Hora de Cierre: "+"{}:{}:{}".format(instanteInicial.hour, instanteInicial.minute, instanteInicial.second)+"\n")
        ticket.write ("Pedidos Entregados: "+ repr (val[0])+"\n")
        ticket.write ("Pizzas Vendidas: "+ repr (va[0])+"\n")
        ticket.write ("Cantidad Deliverys: "+ repr (val1[0])+"\n")
        ticket.write ("Cantidad Llevar: "+ repr (val2[0])+"\n")
        ticket.write ("Cantidad Lugar: "+ repr (val3[0])+"\n")
        ticket.write ("Ingreso Total: "+ repr (val4[0])+"Gs""\n")
        ticket.write ("Sin Factura: "+repr(val7[0])+"Gs"+"("+repr(val8[0])+"P)"+"\n")
        ticket.write ("Entregas Luis: "+ repr (val5[0])+"\n")
        ticket.write ("Entregas Adam: "+ repr (val6[0])+"\n")
        subprocess.Popen(["notepad","report.txt"])     
    def generador_pagos (self):
        ticket = open ("pago.txt","w")
        ticket.write("           Tasty Pizzas\n")
        ticket.write ("         INFORME DEL PAGOS\n ")
        ticket.write ("\n")
        instanteInicial = datetime.now()
        ticket.write ("Fecha de Cierre: "+"{}/{}/{}".format(instanteInicial.day, instanteInicial.month, instanteInicial.year)+"\n")
        ticket.write ("Hora de Cierre: "+"{}:{}:{}".format(instanteInicial.hour, instanteInicial.minute, instanteInicial.second)+"\n")
        valor = Prueba_Server.run_queryServer4("select count (*) from Pago_tarjeta")
        ticket.write ("Cantidad de transacciones:"+repr(valor[0])+"\n")
        #ticket.write ("N°----N° Transaccion----Monto\n")
        ticket.write ("Gestor----N° Trans--Monto\n")
        cont = Prueba_Server.run_queryServer7 ("SELECT * FROM Pago_tarjeta")
        for tas in cont:
            larg = 10-len(tas[3])
            ticket.write (tas[3])
            for x in range (larg):
                ticket.write (" ")
            larg = 10 - len(tas[1])
            ticket.write (tas[1])
            for i in range (larg):
                ticket.write (" ")
            larg = 10 - tas[2]
            ticket.write (repr(tas[2]))
            for x in range (larg):
                ticket.write (" ")
            ticket.write ("\n")
        subprocess.Popen(["notepad","pago.txt"]) 

    def cerrar (self):
        cerrar = messagebox.askquestion("Confirmacion de cierre", "¿Desea cerrar Tasty Pizzas? Se borraran todos los datos")
        if cerrar == 'yes':
            self.raiz.destroy()
            Prueba_Server.run_queryServer5 ("DELETE FROM Pizzas")
            Prueba_Server.run_queryServer5 ("DELETE FROM Delivery_table")
            Prueba_Server.run_queryServer5 ("DELETE FROM En_espera")
            Prueba_Server.run_queryServer5 ("DELETE FROM Pedido")
            Prueba_Server.run_queryServer5 ("DELETE FROM Entregado")
            Prueba_Server.run_queryServer5 ("DELETE FROM deliverys")
            Prueba_Server.run_queryServer5 ("DELETE FROM pago_tarjeta")



    def generador_ticket(self,ind = 0,state = 0):  #GENERA UN TICKET
        ind = ind
        state = state
        
        cur = Prueba_Server.run_queryServer4("SELECT COUNT(*) FROM En_espera")
        ticket = open ("ticket1.txt","w")
        ticket.write("           Tasty Pizzas\n")
        ticket.write ("CONTROL INTERNO. NO VALIDO\nCOMO FACTURA\n\n")
        if ind == 1:
            nombre_clienteup = self.NOMBRE.get ()
            curi = Prueba_Server.run_queryServer4("SELECT id FROM En_espera WHERE Cliente = "+"'"+nombre_clienteup.upper()+"'")
            ticket.write ("Pedido N°:"+repr(curi[0])+"\n")
            if state == 2:
                transaccion = self.billetepago.get()
                suma = self.run_query("SELECT SUM (Precio) FROM PedidoT")
                sumas = suma.fetchone()
                insert = [(repr(curi[0]),repr (transaccion),sumas[0])]
                Prueba_Server.run_queryServer3("INSERT INTO Pago_tarjeta VALUES (?,?,?,'Caja')",insert)
        elif ind == 0:
            ticket.write ("Pedido N°:"+repr(cur[0]+1)+"\n")
            if state == 2:
                transaccion = self.billetepago.get()
                suma = self.run_query("SELECT SUM (Precio) FROM PedidoT")
                sumas = suma.fetchone()
                insert = [(repr(cur[0]+1),repr (transaccion),sumas[0])]
                Prueba_Server.run_queryServer3("INSERT INTO Pago_tarjeta VALUES (?,?,?,'Caja')",insert)
        instanteInicial = datetime.now()
        ticket.write ("Fecha de entrada:"+" {}/{}/{}".format(instanteInicial.day, instanteInicial.month, instanteInicial.year)+"\n")
        ticket.write ("Hora de entrada: "+"{}:{}:{}".format(instanteInicial.hour, instanteInicial.minute, instanteInicial.second)+"\n")

        self.nombre_clienteup = self.NOMBRE.get ()
        ticket.write ("Cliente: "+self.nombre_clienteup+"\n")
        if self.factura.get() ==1:
            ticket.write ("CON FACTURA\n")
            ticket.write ("RUC: "+self.RUCI.get()+"\n")
        
        ticket.write ("Para: ")
        if self.var.get() == 1:
            ticket.write ("*******LLEVAR*****\n")
        elif self.var.get()==2:
            ticket.write ("******DELIVERY*******\n")
            ticket.write ("Ubicacion: "+self.Ubicacion.get()+"\n")
            ticket.write ("Telefono: "+self.telefonoIN.get()+"\n")
        else:
            ticket.write ("*****COMER EN EL LUGAR*****\n")
        ticket.write ("------------------------------\n\n")
        ticket.write ("           Pedido:\n")
        if self.observacionIN.get () == "":
            print ("Sin observacion")
        else:
            ticket.write ("------------------------------\n")
            ticket.write ("Observacion: "+ self.observacionIN.get()+"\n")
            ticket.write ("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")   
        query = "SELECT * FROM PedidoT WHERE punt <> 3"
        db_rows = self.run_query(query)
        cont = 0
        for valor in db_rows:
            cont += 1
            ticket.write (repr(cont)+" - "+valor[1]+"-"+repr(valor[2])+" Gs"+"\n\n")

        """query2 = "SELECT * FROM PedidoT WHERE punt = 2"
        db_rows2 = self.run_query(query2)
        var = db_rows2
        cont2 = 0
        if db_rows2.fetchone() != None:
            ticket.write ("           Bebidas:\n")
            for valor in var:
                cont2 += 1
                ticket.write (repr(cont2)+" - "+valor[1]+"-"+repr(valor[2])+" Gs"+"\n\n")"""


        
        ticket.write ("Precio Total: ")
        suma = self.run_query("SELECT SUM (Precio) FROM PedidoT")
        for valor in suma:
            ticket.write (repr(valor[0])+"Gs\n")
        ticket.write ("Cantidad Total: ")
        result = self.run_query("SELECT COUNT(*)FROM PedidoT WHERE punt = 1") 
        for valor in result:
            ticket.write (repr(valor[0])+" Pizzas\n")

        if self.billetepago.get() == 0:
            ticket.write ("           Falta Abonar\n")
        else:
            if state == 1:
                ticket.write ("PAGO EN EFECTIVO\n")
                ticket.write ("Ingreso: "+ repr (self.billetepago.get())+" Gs\n")
                vuelto = self.obtener_vuelto()
                ticket.write ("Vuelto: "+ repr (vuelto)+" Gs\n")
            else:
                ticket.write ("PAGO POR TARJETA\n") 
                transaccion = self.billetepago.get()  
                ticket.write ("Transaccion N°: "+ repr (transaccion)+"\n")
            ticket.write ("           Abonado\n")
            ticket.write ("------------------------------\n")
        if ind == 1:
            ticket.write ("     ***TICKET REIMPRESO***\n")
            ticket.write ("------------------------------")
        ticket.close()
        subprocess.Popen(["notepad","ticket1.txt"])
        """keyboard = Controller()
        time.sleep(0.1)
        with keyboard.pressed(Key.ctrl):
            keyboard.press('p')
            keyboard.release('p')
            time.sleep(0.5)
        with keyboard.pressed(Key.enter):
            print ("hpña")"""
        self.insertar_pedido (ind)
        self.insertar_tabla2()
        self.destructor()
        

    def delete_product(self):    #ELIMINA LOS PEDIDOS QUE SE ESTAN HACIENDO DE MANERA SELECTIVA 
        seleccion = self.arbol.item(self.arbol.selection())['text']
        parametro = "'"+seleccion+"'"
        self.run_query ("DELETE FROM PedidoT WHERE Sabor =",parametro)
        self.conn.commit()
        self.sumador()
        self.cantidad_pizzas()

        self.insertar_tabla()

    def insert_beb(self):    #ELIMINA LOS PEDIDOS QUE SE ESTAN HACIENDO DE MANERA SELECTIVA       
        seleccion = self.beb.item(self.beb.selection())['text']
        print (seleccion)
        seleccion1 = self.beb.item(self.beb.selection())['values']
        print (seleccion1[0])
        #parametro = "'"+seleccion+"'"
        val =self.run_query ("SELECT * FROM Bebidas WHERE Sabor = "+"'"+seleccion+"'"+" and"+" Tamaño ="+"'"+seleccion1[0]+"'")
        parametro = [("",0,2)]
        for valor in val:
            print (valor)
            parametro = [(valor[1]+" "+valor[2],valor[3],2)]
        print (parametro)
        self.run_querymultiple ("INSERT INTO Pedidot VALUES (NULL,?,?,?)",parametro)
        self.conn.commit()

        self.insertar_tabla_beb1()
        

    def funcion_eliminar(self,codigo =0): #FUNCION QUE RECIBE PARAMETROS DE LOS BOTONES PARA ELIMINAR DE LA BASE DE DATOS LOS PEDIDOS SELECCIONADOS EN LA TABLA
        if codigo ==1:
            self.delete_product1()
        if codigo ==2:
            seleccion = self.tree.item(self.tree.selection())['text']
            parametro = "DELETE FROM Pizzas WHERE Punt_cliente ="+"'"+seleccion+"'"

            parametro1 = "'"+seleccion+"'"
            self.run_query ("DELETE FROM Delivery WHERE Cliente =",parametro1)
            Prueba_Server.run_queryServer5 ("DELETE FROM Delivery_table WHERE Cliente ="+parametro1)
            Prueba_Server.run_queryServer5 (parametro)

            self.insertar_tabla4()
        if codigo ==3:
            seleccion = self.tree.item(self.tree.selection())['text']
            parametro1 = "'"+seleccion+"'"
            parametro = "DELETE FROM Pizzas WHERE Punt_cliente ="+"'"+seleccion+"'"
            self.run_query ("DELETE FROM Entegrado WHERE Cliente =",parametro1)
            Prueba_Server.run_queryServer5 ("DELETE FROM Entregado WHERE Cliente ="+parametro1)
            Prueba_Server.run_queryServer5 (parametro)
            self.insertar_tabla3()
            

    def funcion_entregar(self,codigo =0):   #FUNCION QUE RECIBE LOS PARAMETRO DE LOS BOTONES CAMBIANTES DE LA NAVEGACION PARA ENTREGAR LAS PIZZAS EN SU RESPECTIVA TABLA
        if codigo == 1:
            self.entregar_pizza()
        if codigo ==2:
            self.pestaña_entregarD()
    
    def pestaña_entregarD (self):
        font = ("Bebas Neue",18)
        font2 = ("Bebas Neue",15)
        color = "Lightblue3"
        self.pestañaDE = Toplevel()
        self.pestañaDE.title ("Pago Delivery")
        self.pestañaDE.geometry ('300x200')
        self.pestañaDE.config (bg = color)
        self.pestañaDE.focus ()
        #self.pestañaDE.attributes('-alpha', 0.9)
        pos_x = self.raiz.winfo_screenwidth()/2
        pos_y = self.raiz.winfo_screenheight() /2
        self.pestañaDE.geometry("+%d+%d" % (pos_x,pos_y))
        
        contenedor = Frame (self.pestañaDE,bg = color)
        contenedor.pack (side = TOP,fill = "both",expand = 1)
        contenedor_botones = Frame (contenedor,bg = color)
        contenedor_botones.pack (side = TOP,fill = "both")
        self.boton_efe = Button (contenedor_botones,text = "Efectivo",font = font,command = self.boton_efectivoD)
        self.boton_efe.pack (side = LEFT,fill = "both",padx = 5,pady = 5)
        self.boton_tarjeta = Button (contenedor_botones,text = "Tarjeta",font = font,command = self.boton_tarjetaD)
        self.boton_tarjeta.pack (side = RIGHT,fill = "both",padx = 5,pady = 5)
        contenedor_eti = Frame (contenedor,bg = color)
        contenedor_eti.pack (side = TOP,fill = "both",expand = 1,pady = 10)
        self.indicador_tipo = StringVar()
        indicador = Label (contenedor_eti,textvariable = self.indicador_tipo,font = font2,fg = "Snow",bg = "Gray2")
        indicador.pack (side = TOP,fill = "both")
        contenedor_eti2 = Frame (contenedor,bg = color)
        contenedor_eti2.pack (side = TOP,fill = "both")
        self.insert_var = StringVar()
        insert_eti = Label (contenedor_eti2,textvariable = self.insert_var,font = font2,bg = color)
        insert_eti.grid (row = 1,column = 1,padx = 5)
        contenedor_entry = Frame (contenedor,bg = color)
        contenedor_entry.pack (side = TOP,fill = "both")
        self.entry_data = StringVar()
        self.entry_PD = Entry (contenedor_entry,textvariable = self.entry_data,font = font2)
        self.entry_PD.grid (row = 0,column = 0,padx = 5)
        self.next = PhotoImage (file = "./images/next.png")
        self.boton_next = Button (contenedor_entry,image = self.next)
        self.boton_next.grid(row = 0,column = 1,pady = 5,padx = 5)
        self.boton_efectivoD()
    def boton_efectivoD (self):
        self.boton_efe.config (state = DISABLED)
        self.boton_tarjeta.config (state = NORMAL)
        self.indicador_tipo.set ("PAGO EFECTIVO")
        self.insert_var.set ("Monto Pagado:")
        self.boton_next.config(command = partial (self.boton_nextF,1))
        self.pestañaDE.bind("<Return>",partial(self.atajo_enter,1))
        

    def boton_tarjetaD (self):
        self.boton_efe.config (state = NORMAL)
        self.boton_tarjeta.config (state = DISABLED)
        self.indicador_tipo.set ("PAGO TARJETA")
        self.insert_var.set ("N° Transacción:")
        self.boton_next.config(command = partial (self.boton_nextF,2))
        self.pestañaDE.bind("<Return>",partial(self.atajo_enter,2))
    
    def atajo_enter (self,event,ind = 0):
        ind = ind
        if event == 1:
            self.boton_nextF(1)
        else:
            self.boton_nextF(2)
    def boton_nextF (self,val = 0):
        val = val
        seleccion = self.tree.item(self.tree.selection())['text']
        parametro = "'"+seleccion+"'"
        cursor = "SELECT * FROM Delivery_table WHERE Cliente= "
        #val = self.run_query(cursor,parametro)
        valor = Prueba_Server.run_queryServer8 (cursor + parametro)
        insercion = [(valor[0],valor[1],valor[2],valor[3],valor[4],valor[5],valor[6],valor[7],valor[8])]
        #self.run_querymultiple ("INSERT INTO Entegrado VALUES(NULL,?,?,?,?,?,?,?,?)",insercion)
        Prueba_Server.run_queryServer3("INSERT INTO Entregado VALUES(?,?,?,?,?,?,?,?,?)",insercion)
        #self.run_query ("DELETE FROM Delivery WHERE Cliente =",parametro)
        Prueba_Server.run_queryServer5 ("DELETE FROM Delivery_table WHERE Cliente = " + parametro)
        self.insertar_tabla4()
        if val ==2:
            transaccion = self.entry_data.get()
            suma = self.run_query("SELECT SUM (Precio) FROM PedidoT")
            sumas = suma.fetchone()
            insert = [(repr (valor[0]),transaccion,repr(valor[3]))]
            Prueba_Server.run_queryServer3("INSERT INTO Pago_tarjeta VALUES (?,?,?,'Delivery')",insert)
        self.pestañaDE.destroy()
        



    
    
    def delete_product1(self):   #ELIMINA LOS PEDIDOS DE LA BASE DE DATOS DEL CLIENTE 

        seleccion = self.tree.item(self.tree.selection())['text']
        parametro1="'"+seleccion+"'"

        parametro = "DELETE FROM Pizzas WHERE Punt_cliente ="+"'"+seleccion+"'"
        parametro2 = "DELETE FROM Pedido WHERE Cliente ="+"'"+seleccion+"'"
        print (type (seleccion))
        #self.run_query ("DELETE FROM Pedido WHERE Cliente =",parametro1)
        Prueba_Server.run_queryServer5 (parametro)
        Prueba_Server.run_queryServer5 (parametro2)
        self.insertar_tabla2()

    def entregar_pizza (self):  #Envia las pizzas de la tabla pedido a entregados
        seleccion = self.tree.item(self.tree.selection())['text']
        parametro = "'"+seleccion+"'"
        cursor = "SELECT * FROM Pedido WHERE Cliente = "
        #val = self.run_query(cursor,parametro)
        valor = Prueba_Server.run_queryServer8 (cursor + parametro)
        if valor [4] == 'Delivery':
            self.aviso.config (text = "PRIMERO ASIGNAR DELIVERY.")
            return
        self.aviso.config(text = '')
        insercion = [(valor[0],valor[1],valor[2],valor[3],valor[4],valor[5],valor[6],valor[7],valor[8])]
        print (insercion)
        #self.run_querymultiple ("INSERT INTO Entegrado VALUES(NULL,?,?,?,?,?,?,?,?)",insercion)
        Prueba_Server.run_queryServer3("INSERT INTO Entregado VALUES(?,?,?,?,?,?,?,?,?)",insercion)
        print ("Entre")
        #self.run_query ("DELETE FROM Pedido WHERE Cliente =",parametro)
        Prueba_Server.run_queryServer5 ("DELETE FROM Pedido WHERE Cliente = " + parametro)
        self.insertar_tabla2()
        

    def entregar_delivery(self):   #Envia las pizzas de la lista de espera a las lista de deliverys
        self.raizz = Toplevel()
        self.raizz.geometry ("300x80")
        self.raizz.resizable (0,0)
        self.aviso.config(text = '')
        fuente = ("Clarendon Blk ",15)
        color = "gold"
        frame_raicita = LabelFrame (self.raizz,bg = "gold",text = "Selecciona un Delivery",font = fuente)
        frame_raicita.pack (side = TOP ,fill = 'both',expand = 1)
        self.varr3 = IntVar ()
        self.rr1 = Radiobutton(frame_raicita, text = "Luis",font = fuente, variable = self.varr3, value = 1,bg = color,command = self.asign_delivery )
        self.rr1.grid (row = 0,column = 0,padx =10,pady = 10)
        self.rr2 = Radiobutton(frame_raicita, text = "Adam",font = fuente, variable = self.varr3, value = 2,bg = color,command = self.asign_delivery)
        self.rr2.grid (row = 0,column = 1,padx =10,pady = 10)
        self.rr2 = Radiobutton(frame_raicita, text = "Otros",font = fuente, variable = self.varr3, value = 3,bg = color,command = self.asign_delivery)
        self.rr2.grid (row = 0,column = 2,padx =10,pady = 10)


    def reasign_delivery_pestaña(self):
        self.rraizz = Toplevel()
        self.rraizz.geometry ("300x80")
        self.rraizz.resizable (0,0)
        self.aviso.config(text = '')
        fuente = ("Clarendon Blk ",15)
        color = "gold"
        frame_raicita = LabelFrame (self.rraizz,bg = "gold",text = "Reasignar Delivery",font = fuente)
        frame_raicita.pack (side = TOP ,fill = 'both',expand = 1)
        self.varrr3 = IntVar ()
        self.rrr1 = Radiobutton(frame_raicita, text = "Luis",font = fuente, variable = self.varrr3, value = 1,bg = color,command = self.reasign_delivery )
        self.rrr1.grid (row = 0,column = 0,padx =10,pady = 10)
        self.rrr2 = Radiobutton(frame_raicita, text = "Adam",font = fuente, variable = self.varrr3, value = 2,bg = color,command = self.reasign_delivery)
        self.rrr2.grid (row = 0,column = 1,padx =10,pady = 10)
        self.rrr2 = Radiobutton(frame_raicita, text = "Otros",font = fuente, variable = self.varrr3, value = 3,bg = color,command = self.reasign_delivery)
        self.rrr2.grid (row = 0,column = 2,padx =10,pady = 10)


    def reasign_delivery(self):
        Nombre = ""
        asig= ''
        if self.varrr3.get() == 1:
            Nombre = "Luis"
            asig = 'LUIS'
        if self.varrr3.get() ==2:
            Nombre = "Adam"
            asig = 'ADAM'
        if self.varrr3.get() ==3:
            Nombre = "Otros"
            asig = 'Otros'
        seleccion = self.tree.item(self.tree.selection())['text']
        parametro = "'"+seleccion+"'"
        print (parametro)
        retu = Prueba_Server.run_queryServer5 ("UPDATE Deliverys SET Nombre = "+repr(Nombre)+" WHERE Punt_client = "+parametro)
        Prueba_Server.run_queryServer5 ("UPDATE Delivery_table SET Para = "+repr(asig)+" WHERE Cliente = "+parametro)
        self.insertar_tablageneral(codigo = 2)



        self.rraizz.destroy()


    def asign_delivery(self):
        seleccion = self.tree.item(self.tree.selection())['text']
        parametro = "'"+seleccion+"'"
        retu = Prueba_Server.run_queryServer4 ("SELECT * FROM Pizzas WHERE Punt_cliente = "+parametro+" and Punt = 3")
        if retu[1] == "DELIVERY CENTRO":
            cargo = 1
        elif retu[1] == "DELIVERY ALREDEDORES":
            cargo = 2
        print (retu)
        Nombre = [("",cargo)]
        asig = ''
        if self.varr3.get() == 1:
            Nombre = [("Luis",cargo)]
            asig = 'LUIS'
        if self.varr3.get() ==2:
            Nombre = [("Adam",cargo)]
            asig = 'ADAM'
        if self.varr3.get() ==3:
            Nombre = [("Otros",cargo)]
            asig = 'Otros'
        print (Nombre)

        self.raizz.destroy()
        seleccion2 = self.tree.item(self.tree.selection())['text']
        parametro2 = "'"+seleccion2+"'"
        cursor2 = "SELECT * FROM Pedido WHERE Cliente = "
        #val = self.run_query(cursor,parametro)
        valor = Prueba_Server.run_queryServer8 (cursor2+parametro2)
        print ("ENTRE EN DELIVERY")
        if valor[4] != "Delivery":
            self.aviso.config (text = "NO SE PUEDE ENVIAR, NO ES DELIVERY.")
            return
        insercion = [(valor[0],valor[1],valor[2],valor[3],asig,valor[5],valor[6],valor[7],valor[8])]
        print (insercion)
        #self.run_querymultiple ("INSERT INTO Delivery VALUES(NULL,?,?,?,?,?,?,?,?)",insercion)
        Prueba_Server.run_queryServer3 ("INSERT INTO Delivery_table VALUES(?,?,?,?,?,?,?,?,?)",insercion)
        Prueba_Server.run_queryServer3 ("INSERT INTO Deliverys VALUES (?,?,"+repr(valor[1])+")",Nombre)
        #self.run_query ("DELETE FROM Pedido WHERE Cliente =",parametro)
        Prueba_Server.run_queryServer5 ("DELETE FROM Pedido WHERE Cliente = " + parametro)
        self.insertar_tabla2()
        


    def obtener_vuelto (self,cincuenta = 0):    #FUNCION QUE OBTIENE EL VUELTO CON LOS BOTONES DE MANERA AUTOMATICA
        suma = self.sumador()
        for valor in suma:
            print (self.billetepago.get())
            if cincuenta == 0 :
                vuelto = self.billetepago.get ()- valor
                self.vueltoin.config (text = vuelto,fg = "Black",bg = "Yellow",font = ("Verdana",23) )
                self.gs.config (text = "Gs",fg = "Black",bg = "Yellow",font = ("Verdana",23) )
            elif cincuenta == 1:
                vuelto = 50000 - valor
                self.billetepago.set (50000)
                self.vueltoin.config (text = vuelto,fg = "Black",bg = "Yellow",font = ("Verdana",23))
                self.gs.config (text = "Gs",fg = "Black",bg = "Yellow",font = ("Verdana",23) )
            elif cincuenta == 2:
                vuelto = 100000 - valor
                self.billetepago.set (100000)
                self.vueltoin.config (text = vuelto,fg = "Black",bg = "Yellow",font = ("Verdana",23))
                self.gs.config (text = "Gs",fg = "Black",bg = "Yellow",font = ("Verdana",23) )
        return vuelto
            
    def buscar_cliente (self):    #FUNCION QUE BUSCA CLIENTES EN LA BASE DE DATOS LOCAL //EN EL FUTURO ENLAZAR ESTA FUNCION CON SQL SERVER
        nombre = ''
        apellido =''
        ruc = ''
        ubi = ''
        telefono = ''
        if self.telefonoIN.get() =="":
            valor = Prueba_Server.run_queryServer ("SELECT * FROM Clientes_Tasty WHERE ruc =",repr(self.RUCI.get()))
            for var in valor:
                print (var)
                if var [1] != None: 
                    self.NOMBRE.set (var[0]+" "+var[1])
                else:
                    self.NOMBRE.set (var[0])

                if var [4] != None:
                    self.Ubicacion.set (var[4])
                else:
                    self.Ubicacion.set ('')

                if var[5]!= None:
                    self.telefonoIN.set(var[5])
                else:
                    self.telefonoIN.set('')
            return
        tel = "'"+self.telefonoIN.get()+"'"
        
        val = Prueba_Server.run_queryServer ("SELECT * FROM Clientes_Tasty WHERE telefono = ",tel) 
        for var in val:
                if var [1] != None: 
                    self.NOMBRE.set (var[0]+" "+var[1])
                else:
                    self.NOMBRE.set (var[0])

                if var [4] != None:
                    self.Ubicacion.set (var[4])
                else:
                    self.Ubicacion.set ('')

                if var[5]!= None:
                    self.telefonoIN.set(var[5])
                else:
                    self.telefonoIN.set('')
                
                if var [2] != None:
                    self.RUCI.set(var[2])
                else:
                    self.RUCI.set('')
                   
    def validar(self,ind = 0):  
        ind = ind 
        #VALIDA LOS DATOS INGRESADOS EN LA COMANDA PARA SU DEBIDO INGRESO
        if self.var.get () == 0:
            self.mensaje.config (text = "SELECCIONE ALGUN PARA:")
            return
        if self.factura.get() == 1 and self.RUCI.get() =="":
            self.mensaje.config (text = "FALTA INGRESAR RUC")
            return
        if self.var.get() == 2 and self.Ubicacion.get() =="":
            self.mensaje.config (text = "FALTA INGRESAR UBICACION")
            return
        if self.var.get() == 2 and self.telefonoIN.get() =="":
            self.mensaje.config (text = "FALTA INGRESAR TELEFONO")
            return
        nombre = self.NOMBRE.get()
        consul = "SELECT * FROM Pedido WHERE Cliente = "
        #vari = self.run_query(consul,"'"+nombre.upper()+"'") 
        vari = Prueba_Server.run_queryServer4(consul + "'"+nombre.upper()+"'")
        if vari != None and ind == 0:
            self.mensaje.config (text = "CLIENTE EXISTENTE")
            return
        nombre1 = self.NOMBRE.get()
        consul1 = "SELECT * FROM Delivery_table WHERE Cliente = "
        #vari1 = self.run_query(consul1,"'"+nombre1.upper()+"'") 
        vari1 = Prueba_Server.run_queryServer4(consul1 + "'"+nombre.upper()+"'")
        if vari1 != None and ind == 0:
            self.mensaje.config (text = "CLIENTE EXISTENTE")
            return
        nombre2 = self.NOMBRE.get()
        consul2 = "SELECT * FROM Entregado WHERE Cliente = "
        #vari2 = self.run_query(consul2,"'"+nombre2.upper()+"'")
        vari2 = Prueba_Server.run_queryServer4(consul2 + "'"+nombre.upper()+"'") 
        if vari2 != None and ind == 0:
            self.mensaje.config (text = "CLIENTE EXISTENTE")
            return
        self.boton_aceptar.config (state = DISABLED)
        self.pestaña_pago(ind)
        self.agg_cliente_boton()

    
    def destructor (self):   #FUNCION QUE DESTRUYE LA VENTANA DE AÑADIR PEDIDO 
        try:
            self.mitad_izquierda2.destroy ()
        except AttributeError:
            print("Aun no se creo la funcion") 
        self.mitad_izquierdaactivador()

    def destructor2 (self):   #FUNCION QUE DESTRUYE LA VENTANA DE AÑADIR PEDIDO 
        try:
            self.mitad_izquierda2.destroy ()
        except AttributeError:
            print("Aun no se creo la funcion") 
        self.ventana_pedidos(1)
        self.mitad_izquierda2.config (text = "Editar Pedido")   
    
    def destructor3 (self):   #FUNCION QUE DESTRUYE LA VENTANA DE AÑADIR PEDIDO 
        try:
            self.mitad_izquierda2.destroy ()
        except AttributeError:
            print("Aun no se creo la funcion") 
        self.ventana_pedidos()
        self.mitad_izquierda2.config (text = "Agregar Pedido") 
    def abreventana (self): #FUNCION QUE DESTRUYE EL FRAME DEL LOGIN PARA CREAR LA INTERFAZ DE PEDIDO
        self.frame.destroy()
        self.nueva_ventana()

    def pestaña_bebidas (self):
        self.run_query ("DELETE FROM Bebidas_t")
        self.raizzz = Toplevel()
        self.raizzz.geometry ("750x500")
        frame_principal = Frame (self.raizzz,bg = "SkyBlue1")
        frame_principal.pack (side = TOP,fill ='both',expand = 1)
        label_frame = LabelFrame(frame_principal, text = "Seleccion de Bebidas",font = ("Summer Candy",35),bg = "SkyBlue1",bd = 20)
        label_frame.pack (side = TOP,fill = "both",expand = 1,padx=10,pady = 10 )

        contenedor_s = Frame (label_frame,bg = "SkyBlue1",bd = 10)
        contenedor_s.pack (side = TOP,anchor = N,fill = "both",padx = 10,pady = 10)

        self.beb = ttk.Treeview(contenedor_s,height = 10, columns = ("one","two",))
        self.beb.grid(row = 0,padx = 10)
        self.beb.column ("#0",width = 150)
        self.beb.column ("one",width = 50)
        self.beb.column ("two",width = 100)
        self.beb.heading('#0', text = 'SABOR', anchor = CENTER)
        self.beb.heading('one', text = 'TAMAÑO', anchor = CENTER)
        self.beb.heading ('two', text = 'PRECIO',anchor = CENTER)
        
        self.insertar_tabla_beb()


        self.beb1 = ttk.Treeview(contenedor_s,height = 10, columns = ("one"))
        self.beb1.grid(row = 0,column = 1,padx= 10)
        self.beb1.column ("#0",width = 150)
        self.beb1.column ("one",width = 150)
        self.beb1.heading('#0', text = 'SABOR', anchor = CENTER)
        self.beb1.heading('one', text = 'PRECIO', anchor = CENTER)


        contenedor_botones = Frame (label_frame,bg = "SkyBlue1",bd = 10 )
        contenedor_botones.pack (side = TOP,expand = 1,fill = "both")

        boton_cargar = Button (contenedor_botones,text = "Cargar",font = self.fuente,command = self.insert_beb)
        boton_cargar.pack (side = TOP,pady = 10,fill = "both")

        boton_listo = Button (contenedor_botones,text = "Listo",font = self.fuente,command = self.comando_listo)
        boton_listo.pack (side = TOP,pady = 10,fill = "both")

    def comando_listo (self):
        self.insertar_tabla()
        self.raizzz.destroy()
        self.sumador()
        self.cantidad_pizzas

    def edit (self):
        self.destructor2()
        seleccion = self.tree.item(self.tree.selection())['text']
        parametro1="'"+seleccion+"'"
        consulta = "SELECT * FROM En_espera WHERE Cliente ="+parametro1
        print (consulta)
        consulta2 = "SELECT * FROM Pizzas WHERE Punt_cliente ="+parametro1
        recolector = Prueba_Server.run_queryServer4(consulta)
        print (recolector)
        cliente = recolector[0]

        self.NOMBRE.set (cliente)
        self.nombre_clientein.config(state=DISABLED)
        if recolector[7] != '':
            self.Ubicacion.set (recolector[7])
        records = self.arbol.get_children()
        for element in records:
            self.arbol.delete(element)
        # getting data
        
        rin = Prueba_Server.run_queryServer7(consulta2)
        # filling data
        for row in rin:
            insert = [(row [1],row [2],row[3])]
            self.run_querymultiple ("INSERT INTO PedidoT VALUES (NULL,?,?,?)",insert)
            #self.arbol.insert('',0, text = row[1], values = (repr(row[2])+" Gs"))
        self.insertar_tabla()
        self.sumador()
        self.cantidad_pizzas()
        if recolector [3] ==  "Llevar":
            self.r1.select ()
        elif recolector[3] == "Delivery":
            self.r2.select ()
        elif recolector[3] =="Comer en el lugar":
            self.r4.select()

        if recolector [4] == "Si":
            self.r3.select()
        if recolector[10] !='NULL' :
            self.telefonoIN.set(recolector[10])

        if recolector[9] != 'NULL':
            print (type(recolector[9]))
            self.RUCI.set(recolector[9])

    def toppings (self):
        self.run_query('DELETE FROM Crea_top')
        seleccion = self.arbol.item(self.arbol.selection())['text']
        if seleccion == "":
            self.mensaje.config (text = "SELECCIONE ALGUN SABOR")
            return
        if seleccion == "DELIVERY ALREDEDORES" or seleccion == "DELIVERY CENTRO":
            self.mensaje.config (text = "SELECCION NO VALIDA")
            return
        fuente = ("Clarendon Blk ",15)
        font = ("Verdana",10)
        color = 'dark khaki'
        raiz_topping = Toplevel()
        self.colocar = raiz_topping
        raiz_topping.geometry('700x500')
        raiz_topping.config (bg = color)
        #seleccionar la pizza para ponerle el precio
        self.select = seleccion
        ret = self.run_query("SELECT * FROM PedidoT WHERE Sabor = "+"'"+seleccion+"'")
        precio = 0
        insert = [('',0)]
        for x in ret:
            precio =x[2]
            insert = [('',x[2])]
        self.run_querymultiple('INSERT INTO Crea_top VALUES (?,?)',insert)
        if '/' in seleccion:
            self.separ = seleccion.split ('/')
            raiz_topping_big = Frame (raiz_topping,bg = color)
            raiz_topping_big.pack (side = TOP,fill = 'both',expand = 1)
            raiz_frameizq = Frame (raiz_topping_big,bg = color)
            raiz_frameizq.pack (side = LEFT,fill = 'both',expand = 1)
            raiz_frameder = Frame (raiz_topping_big,bg = color)
            raiz_frameder.pack (side = RIGHT,fill = 'both',expand = 1)
            raiz_frameizq_up = Frame (raiz_frameizq,bg = color)
            raiz_frameizq_up.pack (side = TOP,fill = 'both',expand = 1)
            raiz_frameder_up = Frame (raiz_frameder,bg = color)
            raiz_frameder_up.pack (side = TOP,fill = 'both',expand = 1)
            self.eti_var1 = StringVar()
            self.eti_var2 = StringVar()
            self.raiz_frameizq_up_eti = Label (raiz_frameizq_up,textvariable= self.eti_var1,font = font)

            self.eti_var1.set (self.separ[0])
            self.raiz_frameizq_up_eti.pack (side = TOP,fill = 'both',pady = 20,padx = 5)
            self.raiz_frameder_up_eti = Label (raiz_frameder_up,textvariable= self.eti_var2,font = font)
            self.eti_var2.set (self.separ[1])
            self.raiz_frameder_up_eti.pack (side = TOP,fill = 'both',pady = 20,padx =5)
            boton_cargar_izq = Button (raiz_frameizq_up,text = "Cargar",font = font,command = self.carg_agg1)
            boton_cargar_izq.pack (side = TOP,pady = 5,fill = 'both',padx = 5)
            boton_cargar_der = Button (raiz_frameder_up,text = "Cargar",font = font,command = self.carg_agg2)
            boton_cargar_der.pack (side = TOP,pady = 5,fill = 'both',padx = 5)

            self.tabla_izq = ttk.Treeview(raiz_frameizq_up,height = 10, columns = ("one"))
            self.tabla_izq.pack(side = TOP,fill = 'both',pady = 20,padx = 10)
            self.tabla_izq.column ("#0",width = 20)
            self.tabla_izq.column ("one",width = 20)
            self.tabla_izq.heading('#0', text = 'AGREGADO:', anchor = CENTER)
            self.tabla_izq.heading('one', text = 'COSTO:', anchor = CENTER)
            
            self.tabla_der = ttk.Treeview(raiz_frameder_up,height = 10, columns = ("one"))
            self.tabla_der.pack(side = TOP,fill = 'both',pady = 20,padx = 10)
            self.tabla_der.column ("#0",width = 20)
            self.tabla_der.column ("one",width = 20)
            self.tabla_der.heading('#0', text = 'AGREGADO:', anchor = W)
            self.tabla_der.heading('one', text = 'COSTO:', anchor = W)

            retu = self.run_query ('SELECT Agg,CostoM FROM Toppings')
            for x in retu:
                self.tabla_der.insert('',0, text = x[0], values = (repr(x[1])+" Gs"))
                self.tabla_izq.insert('',0, text = x[0], values = (repr(x[1])+" Gs"))
            self.cost_string = StringVar()
            cost = Label (raiz_topping,textvariable =self.cost_string,font = fuente,bg = color)
            self.cost_string.set ('Precio Total: '+repr (precio)+'Gs')
            cost.pack (side = TOP,fill = 'both',expand = 1)
            listo = Button (raiz_topping,text = 'Listo',font = font,command = self.listo_top)
            listo.pack (side = TOP,fill = 'both',expand = 1,padx = 10,pady = 5)
            cancel = Button (raiz_topping,text = 'Cancelar',font = font,command = raiz_topping.destroy)
            cancel.pack (side = TOP,fill = 'both',expand = 1,padx = 10,pady = 5)

            

            print ("Sabor mitad y mitad")
        else:
            print ("sabor unico")
            raiz_topping_big = Frame (raiz_topping,bg = color)
            raiz_topping_big.pack (side = TOP,fill = 'both',expand = 1)
            raiz_frameizq = Frame (raiz_topping_big,bg = color)
            raiz_frameizq.pack (side = TOP,fill = 'both',expand = 1)
            self.eti_var1 = StringVar()
            self.raiz_frameizq_up_eti = Label (raiz_frameizq,textvariable= self.eti_var1,font = font)
            self.eti_var1.set (seleccion)
            self.raiz_frameizq_up_eti.pack (side = TOP,fill = 'both',pady = 20,padx = 5)
            boton_cargar_izq = Button (raiz_frameizq,text = "Cargar",font = font,command = self.carg_agg)
            boton_cargar_izq.pack (side = TOP,pady = 5,fill = 'both',padx = 5)

            self.tabla_izq = ttk.Treeview(raiz_frameizq,height = 10, columns = ("one"))
            self.tabla_izq.pack(side = TOP,fill = 'both',pady = 20,padx = 10)
            self.tabla_izq.column ("#0",width = 20)
            self.tabla_izq.column ("one",width = 20)
            self.tabla_izq.heading('#0', text = 'AGREGADO:', anchor = CENTER)
            self.tabla_izq.heading('one', text = 'COSTO:', anchor = CENTER)
            retu = self.run_query ('SELECT Agg,Costo FROM Toppings')
            for x in retu:
                self.tabla_izq.insert('',0, text = x[0], values = (repr(x[1])+" Gs"))
            self.cost_string = StringVar()
            cost = Label (raiz_frameizq,textvariable =self.cost_string,font = fuente,bg = color)
            self.cost_string.set ('Precio Total: '+repr (precio)+'Gs')
            cost.pack (side = TOP,fill = 'both',expand = 1)

            listo = Button (raiz_topping,text = 'Listo',font = font,command = self.listo_top1)
            listo.pack (side = TOP,fill = 'both',expand = 1,padx = 10,pady = 5)
            cancel = Button (raiz_topping,text = 'Cancelar',font = font,command = raiz_topping.destroy)
            cancel.pack (side = TOP,fill = 'both',expand = 1,padx = 10,pady = 5)


    def listo_top (self):
        union = self.eti_var1.get()+'/'+self.eti_var2.get()
        retu=self.run_query ("SELECT SUM (Costo) FROM Crea_top")
        precio = 0
        for x in retu:
            precio = x[0]
        consulta = "UPDATE PedidoT SET Sabor = "+repr(union)+",Precio = "+repr(precio)+" WHERE Sabor = "+"'"+self.select+"'"
        print (consulta)
        self.run_query(consulta)
        self.insertar_tabla()
        self.cantidad_pizzas()
        self.sumador()
        self.colocar.destroy()

    def listo_top1 (self):
        union = self.eti_var1.get()
        retu=self.run_query ("SELECT SUM (Costo) FROM Crea_top")
        precio = 0
        for x in retu:
            precio = x[0]
        consulta = "UPDATE PedidoT SET Sabor = "+repr(union)+",Precio = "+repr(precio)+" WHERE Sabor = "+"'"+self.select+"'"
        print (consulta)

        self.run_query(consulta)
        self.insertar_tabla()
        self.cantidad_pizzas()
        self.sumador()
        self.colocar.destroy()


    def carg_agg1(self):
        seleccion = self.tabla_izq.item(self.tabla_izq.selection())['text']
        var = self.eti_var1.get()
        retu = self.run_query ('SELECT Agg,CostoM FROM Toppings WHERE Agg = '+"'"+seleccion+"'")
        tupla = [('',0)]
        for x in retu:
            tupla = [(x[0],x[1])]
        self.run_querymultiple ('INSERT INTO Crea_top VALUES (?,?)',tupla)
        print (seleccion)
        self.eti_var1.set (var+'##'+seleccion)
        self.sum_precio()

    def carg_agg(self):
        seleccion = self.tabla_izq.item(self.tabla_izq.selection())['text']
        var = self.eti_var1.get()
        retu = self.run_query ('SELECT Agg,Costo FROM Toppings WHERE Agg = '+"'"+seleccion+"'")
        tupla = [('',0)]
        for x in retu:
            tupla = [(x[0],x[1])]
        self.run_querymultiple ('INSERT INTO Crea_top VALUES (?,?)',tupla)
        print (seleccion)
        self.eti_var1.set (var+'##'+seleccion)
        self.sum_precio()
    
    def sum_precio(self):
        retu=self.run_query ("SELECT SUM (Costo) FROM Crea_top")
        for x in retu:
            self.cost_string.set("Precio Total: "+repr (x[0])+'Gs')


    def carg_agg2(self):
        seleccion = self.tabla_der.item(self.tabla_der.selection())['text']
        var = self.eti_var2.get()
        retu = self.run_query ('SELECT Agg,CostoM FROM Toppings WHERE Agg = '+"'"+seleccion+"'")
        tupla = [('',0)]
        for x in retu:
            tupla = [(x[0],x[1])]
        self.run_querymultiple ('INSERT INTO Crea_top VALUES (?,?)',tupla)
        print (seleccion)
        self.eti_var2.set (var+'##'+seleccion)
        self.sum_precio()
        



        




if __name__ == "__main__":  #EJECUTA EL PROGRAMA SI EL SKECTH ESTA SIENDO EJECUTADO EN MAIN
    encendido = Login ()
