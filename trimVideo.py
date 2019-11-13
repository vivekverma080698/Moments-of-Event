from moviepy.editor import *
import os
import csv


data = 'drive/My\ Drive/MM/Dataset/birthday/'
subclipdatasetpath = '/content/drive/My Drive/MM/DatasetSubclip/'
for files in os.listdir(data):
  if files[-3:] == 'csv':
    print(files)
    start = []
    end = []
    filepath = data+files 
    with open(filepath, 'r') as csvfile: 
      csvreader = csv.reader(csvfile)   
      for row in csvreader: 
        start.append(row[0])
        end.append(row[1])

    video = VideoFileClip(filepath[:-3]+'mp4')
    i=0
    try:
      os.makedirs(subclipdatasetpath+files[:-4])
    except:
      pass
    for s,e in zip(start,end):
      print(s,e)
      s = s.split(':')
      smin = int(s[0])
      ssec = int(s[1])
      stosec = smin*60+ssec
      e = e.split(':')
      emin = int(e[0])
      esec = int(e[1])
      etosec = emin*60+esec
      clip = video.subclip(stosec,etosec)
      clip.write_videofile(subclipdatasetpath+ files[:-4]+'/'+files[:-3]+str(i)+'.mp4')      
      print(subclipdatasetpath+ files[:-4]+'/'+files[:-3]+str(i)+'.mp4')
      i = i + 1
