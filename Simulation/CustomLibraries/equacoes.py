#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import *
import numpy as np

class Equacoes:
    
    def __init__(self):
        self.criou = True

    def aXDef(self):
        return 0
    
    def aYDef(self, gravidade):
        return -gravidade
    
    def vXDef(self, angulo, v0, tempo):
        return ( v0*cos(radians(angulo)) )
        
    def vYDef(self, angulo, v0, tempo, gravidade):
        return ( ( v0*sin(radians(angulo)) - gravidade*tempo ) )
    
    def xDef(self, angulo, v0, tempo):
        return ( 0 + v0*cos(radians(angulo)) * tempo )
    
    def yDef(self, angulo, v0, tempo, gravidade):
        return ( (v0*sin(radians(angulo)) * tempo - ((gravidade*(tempo**2))/2)) )
    
    def trajetoriaDef(self, angulo, v0, x, gravidade):
        return ( ( x*tan(radians(angulo)) - 0.5*gravidade * (x/(v0*cos(radians(angulo))))**2 ) )
    
    def aX(self, beta, angulo, v0, tempo):
        return (-beta*self.vX(beta, angulo, v0, tempo))
    
    def aY(self, beta, angulo, v0, tempo, gravidade):
        return (-beta*(self.vY(beta, angulo, v0, tempo, gravidade) + (gravidade/beta)))
    
    def vX(self, beta, angulo, v0, tempo):
        return ( ( v0*cos(radians(angulo)) ) * exp( -beta *tempo ) )
        
    def vY(self, beta, angulo, v0, tempo, gravidade):
        return ( ( v0*sin(radians(angulo)) + (gravidade/beta) ) * exp( -beta*tempo ) - (gravidade/beta) )
    
    def x(self, beta, angulo, v0, tempo):
        return ( v0*cos(radians(angulo)) * ( (1 - exp(-beta*tempo))/beta ) )
    
    def y(self, beta, angulo, v0, tempo, gravidade):
        return ( (v0*sin(radians(angulo)) + (gravidade/beta)) * ( (1 - exp(-beta*tempo))/beta ) - (gravidade/beta)*tempo )
    
    def trajetoria(self, beta, angulo, v0, x, gravidade):
        a = (1 - ((beta*x)/(v0*cos(radians(angulo))) ))
        return ( (tan(radians(angulo)) + (gravidade/(beta*v0*cos(radians(angulo)))))*x + (gravidade/(beta**2)) * np.log(a) )

    def xNumerico(self, s0, vx, ax, t):
        return(s0 + vx*t + 0.5*ax*(t**2))

    def yNumerico(self, s0, vy, ay, t):
        return(s0 + vy*t + 0.5*ay*(t**2))

    def vXNumerico(self, c, b, angulo, vx, vy, passo):
        k1 = -b*vx - c*sqrt(vx**2 + vy**2)*vx
        k2 = -b*(vx + k1*(passo/2)) - c*sqrt((vx + k1*(passo/2))**2 + (vy + k1*(passo/2))**2)*(vx + k1*(passo/2))
        k3 = -b*(vx + k2*(passo/2)) - c*sqrt((vx + k2*(passo/2))**2 + (vy + k2*(passo/2))**2)*(vx + k2*(passo/2))
        k4 = -b*(vx + k3*passo) - c*sqrt((vx + k3*passo)**2 + (vy + k3*passo)**2)*(vx + k3*passo)
        return (vx + ((k1 + 2*k2 + 2*k3 + k4)*passo)/6)

    def vYNumerico(self, c, b, angulo, vx, vy, g, passo):
        k1 = -g - b*vy - c*sqrt(vx**2 + vy**2)*vy
        k2 = -g - b*(vy + k1*(passo/2)) - c*sqrt((vx + k1*(passo/2))**2 + (vy + k1*(passo/2))**2)*(vy + k1*(passo/2))
        k3 = -g - b*(vy + k2*(passo/2)) - c*sqrt((vx + k2*(passo/2))**2 + (vy + k2*(passo/2))**2)*(vy + k2*(passo/2))
        k4 = -g - b*(vy + k3*passo) - c*sqrt((vx + k3*passo)**2 + (vy + k3*passo)**2)*(vy + k3*passo)
        return (vy + ((k1 + 2*k2 + 2*k3 + k4)*passo)/6)

    def aXNumerico(self, c, b, vx, vy):
        return (-b*vx - c*sqrt(vx**2 + vy**2)*vx)
    
    def aYNumerico(self, c, b, vx, vy, g):
        return (-g - b*vy - c*sqrt(vx**2 + vy**2)*vy)

    def cCalculator(self, C, p, r, m):
        return ((1/2)*C*p*pi*r*r)/m

    def bCalculator(self, n, r, m):
        return (6*pi*n*r)/m