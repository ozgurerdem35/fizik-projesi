# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:58:18 2026

@author: Erdem
"""

import numpy as np
from numpy import log as ln

def total_interaction_coef(mu_a,mu_s):
    """
    This function calculates total interaction coefficient
    
    Parameters: 
        mu_a : Absorption coefficient
        mu_s : Scattering coefficient
        
    Return : 
        mu_t : Total interaction coefficient
    """
    
    mu_t = mu_a + mu_s
    return mu_t

def step_size(mu_t):
    """
      This function determines the distance that photons will 
      travel in the environmnt before its next interaction.
      
      Parameters: 
          mu_t : Total interaction coefficient
          
      Return:
          s : step size 
    """
    xi = 1 - np.random.random()
    s = - (np.ln(xi) / mu_t)
    
    return s 

def updating_coordinates(x,y,z,s,mu_x,mu_y,mu_z):
    
    """Açıklama"""
    x += mu_x
    y += mu_y
    z += mu_z
    
    return x,y,z
    
def photon_absorption(mu_a,mu_t,W):
    """Açıklama"""
    delta_W =  W*(mu_a/mu_t)
    
    return delta_W

def  Henyey_Greenstein_function(g):
    """Açıklama"""

    
    