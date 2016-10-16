# Unsupervised Context-Based Similarity Learning for Music Recommendation

The mathematical nature of music, that is each song can be characterized by some vectors, has been widely used for music recommendation systems. However, the social nature of music has comparatively received less attention. There are some patterns from the music listening context of various users can be learned to construct the relationship graph of music. In other word, based on enough data, the characteristics information within thousands of millions pieces of music can be exposed by people’s behaviors during listening to music. This paper proposed an approach based on the music listening sequence collected from social music networks, like Last.fm, to predict interesting songs for the user. This method can be implemented without any knowledge about the music itself.

### Prediction 
run the following commands in order:
cd code
ipython
run load_map.py # load the matrix, clustering table and datasets
run -i counting.py # calculate PMI
run -i predicting.py # use different configuration to run the prediction algorithm

You can adjust the following parameters in predicting.py
voters = 20
beam = 5
recommendations = 20
clusteringmode = False

The result of different beams with clusteringmode = True/False is in result.txt

All the accuracy and efficiency plots are based on these data.


### Clustering
There clustering result data is loaded into clusterdict in load_map.py. You can look into this dict in Python without much effort.

The clustering distribution plot is based on this dict and the code in testing.py.

It’s cool if you wan to run the clustering algorithm use the following commands:

   mcl/bin/mcxload -abc data.abc --stream-mirror -write-tab data.tab -o data.mci  

   mcl/bin/mcl data.mci -I 1.4
   mcl/bin/mcl data.mci -I 2
   mcl/bin/mcl data.mci -I 4

   mcl/bin/mcxdump -icl out.data.mci.I14 -tabr data.tab -o dump.data.mci.I14
   mcl/bin/mcxdump -icl out.data.mci.I20 -tabr data.tab -o dump.data.mci.I20
   mcl/bin/mcxdump -icl out.data.mci.I40 -tabr data.tab -o dump.data.mci.I40

For more, http://micans.org/mcl/

We worked together: Yi Huang, Yue Yu
