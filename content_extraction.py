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

"""Detect labels given a file path."""
def content_extraction(path,pklpath):
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.enums.Feature.LABEL_DETECTION]

    with io.open(path, 'rb') as movie:
        input_content = movie.read()

    mode = videointelligence.enums.LabelDetectionMode.FRAME_MODE
    config = videointelligence.types.LabelDetectionConfig(
            label_detection_mode=mode)
    context = videointelligence.types.VideoContext(
            label_detection_config=config)


    operation = video_client.annotate_video(
        features=features, input_content=input_content, video_context=context)
    print('\nProcessing video for label annotations:',path)

    result = operation.result(timeout=200000)
    print('\nFinished processing.')
    file_pi = open(pklpath, 'wb')
    pickle.dump(result, file_pi)
    print('Pickle file saved')


""" Content extraction for a directory of videos """
def content_extraction_dir(in_dir,out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(in_dir):
        path=os.path.join(in_dir,name)
        if not os.path.isdir(path):
            out_path=os.path.join(out_dir,name[:-3]+'obj')
            if not os.path.isfile(out_path):
                content_extraction(path,out_path)
def transform_dataset(in_root_dir,out_root_dir,function_dir,name):
    directories = [os.path.abspath(x[0]) for x in os.walk(in_root_dir)]
    out_root_dir=os.path.join(out_root_dir,name)
    for i in tqdm.tqdm(directories):
        out_dir=out_root_dir + i.split(in_root_dir)[1]
        function_dir(i,out_dir)      # Run your function

if __name__=="__main__":
    in_root_dir='DatasetSubclip'
    out_root_dir='./'
    function_dir=content_extraction_dir
    name='content_extraction'
    transform_dataset(in_root_dir,out_root_dir,function_dir,name)
