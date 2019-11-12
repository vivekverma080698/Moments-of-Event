# Moments-of-Event

# Google cloud setup

- Need credentials file. Cannot be shared publicily.
- Installation of cloud client library. Follow below link.
https://medium.com/harinathselvaraj/step-by-step-tutorial-on-how-to-use-googles-video-intelligence-api-in-python-8e2474ef959e
  
# Shot Detection
- Initialize cloud shell.

To detect shot for whole dataset. Change the path and output dir in the code (48 to 50 line number).  Run directly as:
  Run shot_detection.py
## Output
Folder named 'shot_detection' containing csv files for start and end time.

# Content Extraction
- Initialize cloud shell.

To detect extract content labels for whole dataset. Change the path and output dir in the code (48 to 50 line number).  Run directly as:
  Run shot_detection.py 

## Output
Folder named 'content_extraction' containing '.obj' files containg result onject of video intelligence client library. 

