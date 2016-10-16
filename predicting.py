import time
from collections import defaultdict
from collections import Counter

PMIcache = defaultdict(set)

def top(mid, N):
	adjdict = defaultdict(int)
	for music in csr[mid].nonzero()[1]:
		val = getPMI(mid, music)
		if val > 0:
			adjdict[music] = val
	return topN(adjdict, N)


def topN(d, N):
	sorted_dict = sorted(d.items(), key = lambda x: x[1], reverse=True)
	if len(sorted_dict) > N:
		sorted_dict = sorted_dict[:N]
	return dict(sorted_dict)

def predict(uid, length, N):
	music_list = trainingdata[uid]
	c = Counter(music_list)
	c = c.most_common(voters)
	result_list = defaultdict(int)
	for music in c:
		if clusteringmode:
			# clster based
			related_music = topN(cluster_search(music[0]), N)
		else:
			related_music = top(music[0], N)
		
		for key in related_music.keys():
			if key in result_list.keys():
				result_list[key] = result_list[key] + related_music[key] * music[1]
			else:
				result_list[key] = related_music[key] * music[1]
	
	# remove predicitons in the training set of the user
	# for item in result_list.keys():
	# 	if item in trainingdata[uid]:
	# 		del result_list[item]

	# reset cache
	# PMIcache.clear()
	return topN(result_list, length)

def test(uid, output_list):
	counts = 0;
	points = 0;
	for item in output_list.keys():
		if item in testingdata[uid]:
			points = points+1
		counts = counts+1
	return [points, counts]

def getPMI(mid1, mid2):
	if not (mid1, mid2) in PMIcache:
		PMIcache[(mid1, mid2)] = csr[mid1][(0,mid2)]
	return PMIcache[(mid1, mid2)]

def cluster_search(mid):
	resultdict = defaultdict(int)
	if mid in clustermap.keys():
		for music in clusterdict[clustermap[mid]]:
			val = getPMI(mid, music)
			if val > 0:
				resultdict[music] = val
	return resultdict

totalpoints = 0
totalcounts = 0
# change these settings
voters = 20
beam = 5
recommendations = 20
clusteringmode = True


start_time = time.time()
for user in trainingdata.keys():
	print 'processing user_'+str(user)+' input length: '+str(len(trainingdata[user]))+'\n'
	result = test(user,predict(user, recommendations, beam))
	totalpoints = totalpoints + result[0]
	totalcounts = totalcounts + result[1]
	print 'accuracy: '+str(result[0])+'/'+str(result[1])+'\n'
elapsed_time = time.time() - start_time

print 'running time: ' + str(elapsed_time) + '\n'
print 'total accuracy: ' + str(totalpoints)+'/'+str(totalcounts)+'\n'