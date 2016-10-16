import numpy as np
import scipy.sparse as sparse
from mcl_clustering import mcl

# adj_matrix = [];
# for music1 in co_counts:
#     for music2 in co_counts[music1]:
#     	newitem = [music1, music2, PMI(co_counts[music1][music2], o_counts[music1], o_counts[music2], N)]
#     	print newitem
#         adj_matrix.append(newitem)

# arr = np.array(adj_matrix)
# shape = tuple(arr.max(axis=0)[:2]+1)
# coo = sparse.coo_matrix((arr[:, 2], (arr[:, 0], arr[:, 1])), shape=shape,
#                         dtype=arr.dtype)

# print(repr(coo))

# M, clusters = mcl(coo, expand_factor = 2,
#                    inflate_factor = 2,
#                    max_loop = 60,
#                    mult_factor = 2)