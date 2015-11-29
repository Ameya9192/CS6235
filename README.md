ReadMe

This is the repository for the CS 6235 Class Project- LITMUS for Public Infrastructure Damage.
The damages/failures we have looked at, are:

1) Highway Damages

2) Bridge Failures

3) Power Outages

4) Traffic Lights Failures

5) Gas Leaks


The keywords used for Twitter Search are:

-- Highway Damages: 'highway damaged', 'highway accident', 'highway closed', 'highway mud', 'highway blocked', 'highway pothole', 'highway snow', 'highway gridlock'

-- Bridge Failures: 'bridge collapse', 'bridge damaged', 'bridge closure', 'bridge closed', 'bridge flooded', 'bridge accident'

-- Power Outages: 'power outage'

-- Traffic Lights Failures: 'traffic lights out', 'traffic lights damaged', 'traffic signals out'

-- Gas Leaks: 'gas leak', 'gas line'


Please follow the steps below:

-- Modify twitterGapDownload.py and twitterGapParse.py using the appropriate keywords

-- Run twitterGapDownload.py and save the result HTML file in folder TwitterGap

-- Run twitterGapParse.py on all keywords related to a particular event- say Bridge Failures. Combine all the text files into a single text file. The name of this file should be "infrastructure_failures.txt", where infrastructure can be "bridge", "gas", "highway", "power", "traffic_lights"

-- Run tweetToJSON.py with "infrastructure_failures.txt"  and save its output to infrastructure_JSON.txt to get the data in the required format. Refer sample_test.txt for the required format. Now divide the text file into two files- sample_test.txt and sample_train.txt (1:1 ratio)

-- Run geoNLP.java using sample_test.txt and sample_train.txt as input files. The output of this stage will be sample_test_nlp.txt and sample_train_nlp.txt. Run geocode.py on sample_<name>_nlp.txt files after adding your Google Maps Geocode API key in geocode.py. The output of this stage will be "sample_<name>_geo.txt"

-- Run labeling.py on "sample_<name>_geo.txt" and save its output to labels.txt. In labels.txt, manually label '1' if relevant or '0' if otherwise, at end of each cell. Refer labels.txt for the exact labelling syntax. Add a tab not a space after ']'

-- Run annotation.py on labels.txt and save its output to "<name>_labels.txt"
