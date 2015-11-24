ReadMe

This is the repository for the CS 6235 Class Project- LITMUS for Public Infrastructure Damage.

The damages/failures we have looked at are:
1) Highway Damages

2) Bridge Failures

3) Damages to Roads- like cracks, buckles, potholes

4) Power Outages

5) Traffic Lights Failures

The keywords are:

1)Highway Damages: 'highway damaged', 'highway accident', 'highway closed', 'highway mud', 'highway blocked', 'highway pothole', 'highway snow', 'highway gridlock'

2) Bridge Failures: 'bridge collapse', 'bridge damaged', 'bridge closure', 'bridge closed', 'bridge flooded', 'bridge accident'

3) Damages to Roads:

4) Power Outages:

5) Traffic Lights Failures:

Please follow the steps below:

Run streamTwitter.py and save its output to output.txt

Run tweetToJSON.py and save its output to JSON.txt to get the data in the required format

Run filterData.py on JSON.txt to remove irrelevant tweets

Run crudeLabelling.py on "<name>_geo.txt" and save its output to crudeLabels.txt. In crudeLabels.txt, manually label at end of each cell. Refer crudeLabels.txt for the exact labelling syntax. Add a tab not a space after ']'

Run annotation.py on crudeLabel.txt and save its output to "<name>_labels.txt"
