from collections import defaultdict

def load_data(str, dataset):
	fp = open(str)
	count = 0;
	for line in fp:
		line = line.strip().split("\t")
		uid = int(line[0][5:])
		if uid != count:
			dataset[uid] = [int(line[2])]
			count = uid
		else:
			dataset[uid].append(int(line[2]))


def import_cluster():
	# Load the data:
	fp = open("dump.data.mci.I20.nonoverlap");
	i = 1;
	for line in fp:
		line = line.strip().split("\t")
		line = [ int(x) for x in line ]
		for music in line:
			clustermap[music] = i
		clusterdict[i] = line
		i = i+1

fp = open("mid_music");
wid_word = [x.strip().split("\t") for x in fp];
wid_word = [(int(x),y) for (x,y) in wid_word];
word_wid = dict([(y,x) for (x,y) in wid_word]);
wid_word = dict(wid_word);

clusterdict = defaultdict(int)
clustermap = defaultdict(int)

trainingdata = defaultdict(int)
testingdata = defaultdict(int)

load_data('1000/training.txt', trainingdata)
load_data('1000/testing.txt', testingdata)

import_cluster();
