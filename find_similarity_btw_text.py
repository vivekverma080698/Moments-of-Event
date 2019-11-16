import tensorflow_hub as hub
import tensorflow as tf
import time
import keras.backend as K
from keras.models import load_model
import numpy as np
import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras import optimizers
import keras
import nltk
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity


graph1 = tf.Graph()
with graph1.as_default():
    with tf.Session(graph=graph1) as session1:
        text_input = tf.placeholder(dtype=tf.string, shape=[None])
        embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/2")
        init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
        embeddingsUSE = embed(text_input)
graph1.finalize()

def encoding_using_universal_semantic_encoder(documents):
    with tf.Session(graph=graph1) as session1:
        session1.run(init_op)
        result = session1.run(embeddingsUSE, {text_input: documents})
        return result

def find_similarity_btw_text(text1,text2):
  documents =[text1,text2]
  emb = encoding_using_universal_semantic_encoder(documents)
  sim = 1 - spatial.distance.cosine(emb[0], emb[1])
  return sim
  
