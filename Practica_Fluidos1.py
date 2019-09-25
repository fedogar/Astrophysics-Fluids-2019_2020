Y# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pint
from pint import UnitRegistry
from mpl_toolkits.basemap import Basemap

"Conversiones de unidades astrofísicas : Al usar el paquete Pint es conveniente estas definiciones"

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

"Example on plots:  To see matplotlyb supports units format "
def example_units():
    
    ureg.setup_matplotlib(True)
    
    y = np.linspace(0, 30) * ureg.miles
    x = np.linspace(0, 5) * ureg.hours
    
    fig, ax = plt.subplots()
    
    ax.yaxis.set_units(ureg.inches)
    ax.xaxis.set_units(ureg.seconds)
    
    ax.plot(x, y, 'tab:blue')
    
"Usos para conversiones de unidades. Definiciones "


"Fluidos .. Programas utilizados en las primeras clases. "  
def field_mesh( A = Q_(20.1, 'kelvin/pc^2') , B = Q_(3, 'kelvin/pc^2'), C = Q_(4.2, 'kelvin/pc^2'), D = 100 * ureg.kelvin):
    
    x = Q_(np.linspace(-2,2),'pc')
    y = Q_(np.linspace(-3,4),'pc')
    X, Y = np.meshgrid(x, y)
    xo=0 ; yo=0;
    
    def Temperature( A , B, C , D, X, Y, xo,yo):
        T = A.magnitude*np.square((X-xo))+B.magnitude*np.square(Y-yo)+C.magnitude*(Y-xo)*(Y-yo)+D.magnitude
        return T
    
    fig, ax = plt.subplots(2)
    ax[0].contour(X, Y, Temperature( A , B, C , D, X, Y, xo,yo))
    ax[1].contourf(X, Y, Temperature( A , B, C , D, X, Y, xo,yo))

    "Here we superpose to the temperature field the velocity field "  
    
    W = 1
    vx = -W*(X-xo)
    vy = -W*(Y-yo)
    
    fig, ax = plt.subplots()
    ax.contour(X, Y, Temperature( A , B, C , D, X, Y, xo,yo))
    ax.quiver(X,Y,vx,vy)
      
" Here we define the change of coordinates that would be usefull to treat the problem"
       
def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y) 
    
" Problem number 8 of the first week" 
       
def flujo_vectorial():
    
    R = 2; U = 1;
    
    ".................................."
    r = np.linspace (R,4*R)
    O = np.linspace  (0,2*np.pi)
    rm,Om = np.meshgrid(r,O)
    "................................."
    
    def velocity_field_vs (R,U,s,O):       
        vs = U*(1-((R**2)/(s**2)))*np.cos(O)
        return vs
    
    def velocity_field_vO (R,U,s,O): 
        vO = -U*(1+((R**2)/(s**2)))*np.sin(O)
        return vO
        
    fig, ax = plt.subplots(2,subplot_kw=dict(projection='polar'))
    
    cax0 = ax[0].contour(Om, rm, velocity_field_vO(rm,Om,R,U) )
    fig.colorbar(cax0, ax = ax[0])
    #cb = plt.colorbar(".....", ax[0])
    #cb.set_label('vO', fontsize='x-large')
    
    cax1 = ax[1].contour(Om, rm, velocity_field_vs(rm,Om,R,U) )
    fig.colorbar(cax1,ax = ax[1])
    #cb = plt.colorbar(".......", ax[1])
    #cb.set_label('vR', fontsize='x-large')
    
    
    circle1 = plt.Circle((0, 0), R, color='r')
    ax[0].add_artist(circle1)
    
    "Now want to draw the map by inserting the arrows mapping in total velocity"
       
    "Now we plot the representation in the isolines of the funcion"
    
    def function (x,y,R,U):
        A = U*y*(1 - np.square(R)/(np.square(x) + np.square(y)))
        return A
    
    r = np.linspace (R,4*R)
    O = np.linspace  (0,2*np.pi)
    rm,Om = np.meshgrid(r,O)
    
    
    xm,ym = np.meshgrid(x,y)
    
    fig, ax = plt.subplots(1)
    cax0 = ax.contour(xm, ym, function(xm,ym,R,U) )
    fig.colorbar(cax0, ax = ax)
    
    
        
        
    
    
    
    


