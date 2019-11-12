#Import libraries
#run cloud sdk
#cloudfiles/google-cloud-sdk-270.0.0-linux-x86_64/google-cloud-sdk/bin/gcloud init
import argparse
from google.cloud import videointelligence
#Load the full path of JSON file obtained in step 1. Replace '/Users/harry/Downloads/SampleProject-1abc.json' with your filepath
import os

import io
import csv
import tqdm

""" Detects camera shot changes for a video """
def shot_detection(path,csvpath):
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.SHOT_CHANGE_DETECTION]

    with io.open(path, 'rb') as movie:
        input_content = movie.read()

    operation = video_client.annotate_video(
        features=features, input_content=input_content)

    print('\nProcessing video for shot change annotations:',path)

    result = operation.result(timeout=200)
    print('\nFinished processing.')
    fields = ['Shot Number', 'Start', 'End']
    rows=[]
    # first result is retrieved because a single video was processed
    for i, shot in enumerate(result.annotation_results[0].shot_annotations):
        start_time = (shot.start_time_offset.seconds +
                      shot.start_time_offset.nanos / 1e9)
        end_time = (shot.end_time_offset.seconds +
                    shot.end_time_offset.nanos / 1e9)
        rows.append([i+1,start_time,end_time])
    # writing to csv file
    with open(csvpath, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

""" Detects camera shot changes for a directory of videos """
def shot_detection_dir(in_dir,out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(in_dir):
        path=os.path.join(in_dir,name)
        if not os.path.isdir(path):
            out_path=os.path.join(out_dir,name[:-3]+'csv')
            if not os.path.isfile(out_path):
                shot_detection(path,out_path)


def transform_dataset(in_root_dir,out_root_dir,function_dir,name):
    directories = [os.path.abspath(x[0]) for x in os.walk(in_root_dir)]
    out_root_dir=os.path.join(out_root_dir,name)
    for i in tqdm.tqdm(directories):
        out_dir=out_root_dir + i.split(in_root_dir)[1]
        function_dir(i,out_dir)      # Run your function

if __name__=="__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cloudfiles/MMproject-825fad148fdd.json"
    in_root_dir='DatasetSubclip'
    out_root_dir='./'
    function_dir=shot_detection_dir
    name='shot_detection'
    transform_dataset(in_root_dir,out_root_dir,function_dir,name)
