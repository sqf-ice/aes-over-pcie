#!/usr/bin/python

delta_inv   = ((1,1,1,0,0,0,1,0),
               (0,1,0,0,0,1,0,0),
               (0,1,1,0,0,0,1,0),
               (0,1,1,1,0,1,1,0),
               (0,0,1,1,1,1,1,0),
               (1,0,0,1,1,1,1,0),
               (0,0,1,1,0,0,0,0),
               (0,1,1,1,0,1,0,1));

affine_a    = ((1,1,1,1,1,0,0,0),
               (0,1,1,1,1,1,0,0),
               (0,0,1,1,1,1,1,0),
               (0,0,0,1,1,1,1,1),
               (1,0,0,0,1,1,1,1),
               (1,1,0,0,0,1,1,1),
               (1,1,1,0,0,0,1,1),
               (1,1,1,1,0,0,0,1));

affine_b    =  (0,1,1,0,0,0,1,1);

def binary_matrix_mul(a, b):
   n = len(a)
   m = len(a[0])
   assert m == len(b)
   p = len(b[0])
   for i in range(0, n):
      assert len(a[i]) == m
   