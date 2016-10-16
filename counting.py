from __future__ import division;
from math import log;
from pylab import mean;
import numpy as np;
import scipy.sparse as sparse;

def PMI(c_xy, c_x, c_y, N):
    # Computes PMI(x, y) where
    # c_xy is the number of times x co-occurs with y
    # c_x is the number of times x occurs.
    # c_y is the number of times y occurs.
    # N is the number of observations.
    return log((c_xy*N)/(c_x*c_y), 2);

#Do a simple error check using value computed by hand
if(PMI(2,4,3,12) != 1): # these numbers are from our y,z example
    print "Warning: PMI is incorrectly defined"
else:
    print "PMI check passed"

# Define the data structures used to store the counts:
o_counts = {}; # Occurrence counts
co_counts = {}; # Co-occurrence counts

# Load the data:
fp = open("counts");
N = float(fp.next()); # First line contains the number of observations.
for line in fp:
    line = line.strip().split("\t");
    wid0 = int(line[0]);
    o_counts[wid0] = int(line[1]); # Store occurence counts
    co_counts[wid0] = dict([[int(y) for y in x.split(":")] for x in line[2:]]); # Store co-occurence counts

# output matrix
adj_matrix = [];
for music1 in co_counts:
    for music2 in co_counts[music1]:
        newitem = [music1, music2, PMI(co_counts[music1][music2], o_counts[music1], o_counts[music2], N)]
        # print newitem
        adj_matrix.append(newitem)

arr = np.array(adj_matrix)
shape = tuple(arr.max(axis=0)[:2]+1)
# coo = sparse.coo_matrix((arr[:, 2], (arr[:, 0], arr[:, 1])), shape=shape,
#                         dtype=arr.dtype)

# print(repr(coo))

csr = sparse.csr_matrix((arr[:, 2], (arr[:, 0], arr[:, 1])), shape=shape,
                        dtype=arr.dtype)
print(repr(csr))

# coo.save('output.mat', format='%d %d %fn')

# # output abc file
# output = ''
# for music1 in co_counts:
#     for music2 in co_counts[music1]:
#         line = "%d %d %f" % (music1, music2, PMI(co_counts[music1][music2], o_counts[music1], o_counts[music2], N))
#         output = output + line + '\n' 

# f = open('data.abc', 'w')
# f.write(output)

# output abc file
# f = open('data.abc', 'w')
# for music1 in co_counts:
#     for music2 in co_counts[music1]:
#         if music1 in co_counts[music2].keys() and co_counts[music2][music1] != -1:
#             line = "%d %d %f" % (music1, music2, PMI(co_counts[music1][music2], o_counts[music1], o_counts[music2], N))
#             f.write(line+'\n')
#             co_counts[music1][music2] = -1
# f.close()

# # This code currently does nothing, students will fill in
# for target in targets:
#     targetid = word_wid[target]
#     posPMIs = []
#     negPMIs = []
#     # compute PMI between target and each positive word, and
#     # add it to the list of positive PMI values
#     for pos in pos_words:
#         posPMIs.append(PMI(co_counts[targetid][word_wid[pos]], o_counts[targetid], o_counts[word_wid[pos]], N))
#     # same for negative words
#     for neg in neg_words:
#         negPMIs.append(PMI(co_counts[targetid][word_wid[neg]], o_counts[targetid], o_counts[word_wid[neg]], N))
# #uncomment the following line when posPMIs and negPMIs are no longer empty.
#     print target, ": ", mean(posPMIs), "(pos), ", mean(negPMIs), "(neg)"