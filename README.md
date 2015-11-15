ReadMe

Pls. add the necessary keywords in streamTwitter.py before running it
The keywords are:

Bridges: 'bridge collapsed', 'bridge damaged', 'bridge closure', 'bridge closed', 'bridge flooded', 'bridge accident'

Highways: 'highway damaged', 'highway closed', 'highway mud', 'highway blocked', 'highway concrete buckled'


Run streamTwitter.py and save its output to output.txt

Run tweetToJSON.py and save its output to JSON.txt to get the data in the required format

Run filterData.py on JSON.txt to remove irrelevant tweets

Run crudeLabelling.py on "<name>_geo.txt" and save its output to crudeLabels.txt. In crudeLabels.txt, manually label at end of each cell. Refer crudeLabels.txt for the exact labelling syntax. Add a tab not a space after ']'

Run annotation.py on crudeLabel.txt and save its output to "<name>_labels.txt"
