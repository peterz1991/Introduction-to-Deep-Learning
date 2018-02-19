# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 23:57:43 2018

@author: User
"""

import torch 
import torch.nn as nn
import torch.autograd as autograd
import numpy as np

#m = nn.BatchNorm2d(100)
# Without Learnable Parameters
m = nn.BatchNorm2d(1, affine=False, eps=0, momentum=1)
t = torch.rand(2, 1, 2, 2)
t[0,0,:,:] = 1
t[0,0,0,0] = 2
#t[0,1,:,:] = 1
#t[0,1,0,0] = 2
t[1,0,:,:] = 0.5
t[1,0,0,0] = 0
input = autograd.Variable(t)
output = m(input)

#a = np.array([[2,1], [1 ,1]])
#b = np.array([[0,0.5],[0,0.5]])
c = np.zeros((2,1,2,2))
c[0,0,:,:] = 1
c[0,0,0,0] = 2
c[1,0,:,:] = 0.5
c[1,0,0,0] = 0
a = (c-np.mean(c,axis=0))/np.std(c,axis=0)
(a - np.mean(a))/np.std(a)

(c-np.mean(c))/np.std(c)