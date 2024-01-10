import sys
from numpy import *
import numpy as np
from scipy.sparse import coo_matrix,csr_matrix,csc_matrix
from scipy.io import mmread,mminfo,mmwrite

mat_input = sys.argv[1]
src_mat = mmread(mat_input)
src_mat_csr = coo_matrix(src_mat).tocsr()
print(mminfo(mat_input))
mmwrite(mat_input.split('.')[0]+"_csr.mtx", src_mat_csr, symmetry='general')
