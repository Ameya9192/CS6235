***ReadMe***

This is the ***code repository*** for 
***CS 6235 Class Project- LITMUS for Public Infrastructure Damage***

***Team members: Ameya Ghadi and David Benas***

The damages/failures we have looked at, are:

1) Highway Damages

2) Bridge Failures

3) Power Outages

4) Traffic Lights Failures

5) Gas Leaks


The ***keywords*** used for Twitter Search are:

-- Highway Damages: 'highway damaged', 'highway accident', 'highway closed', 'highway mud', 'highway blocked', 'highway pothole', 'highway snow', 'highway gridlock'

-- Bridge Failures: 'bridge collapse', 'bridge damaged', 'bridge closure', 'bridge closed', 'bridge flooded', 'bridge accident'

-- Power Outages: 'power outage'

-- Traffic Lights Failures: 'traffic lights out', 'traffic lights damaged', 'traffic signals out'

-- Gas Leaks: 'gas leak', 'gas line'


***Steps to be followed:***

***Folder name: StreamTwitter***

-- Modify twitterGapDownload.py and twitterGapParse.py using the appropriate keywords

-- Run twitterGapDownload.py and save the result HTML file in folder TwitterGap

-- Run twitterGapParse.py on all keywords related to a particular event- say Bridge Failures. Combine all the text files into a single text file. The name of this file should be "infrastructure_failures.txt", where infrastructure can be "bridge", "gas", "highway", "power", "traffic_lights". The shell script to concatenate the data in all folders, subdirectories is given in script.txt


***Folder name: JSON_Formatting***

-- Run tweetToJSON.py. The input of this stage is "infrastructure_failures.txt" and save its output to infrastructure_JSON.txt to get the data in the required format. Now divide the text file into two files- sample_test.txt and sample_train.txt (1:1 ratio). The shell script to split the files is given in script.txt.

***Folder name: Geocoding***

-- Run geoNLP.java. The input of this stage is sample_test.txt and sample_train.txt as input files. The output of this stage will be sample_test_nlp.txt and sample_train_nlp.txt. Run geocode.py on sample_train-OR-test_nlp.txt files after adding your Google Maps Geocode API key in geocode.py. The output of this stage will be "sample_train-OR-test_geo.txt"


***For grouping together tweets and calculating weight of each cell***

***Folder name: Annotation***

--- Run textID.py. The input of this stage is infrastructure_JSON.txt, where infrastructure can be "bridge", "gas", "highway", "power", "traffic_lights". Save its output to infrastructureTextID.txt. This file will have the tweet text and the corresponding tweet id

--- Run labeling.py. The input of this stage is sample_train-OR-test_geo.txt and corresponding infrastructureTextID.txt. The output should be written to infrastructure_train-OR-test_label.txt. The last column in infrastructure_train-OR-test_label.txt will be an indication of the intensity of the event, since the tweets mapped to the cell are higher, some of them could also possibly contain the keywords related to human casualties.

Keywords used in this stage include: 
'killed', 'kills', 'died', 'dead', 'deadly', 'fatal', 'injured', 'hurts', 'hurt'
