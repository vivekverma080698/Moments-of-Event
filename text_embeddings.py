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
        
        
documents_list =[ ['birthday',''],['birthday','cake'],['birthday','cake'],['birthday','cake'],['birthday','cake']]
emb = encoding_using_universal_semantic_encoder(documents)
cosine_similarity(np.array(emb), Y=None, dense_output=True)




# Elmo Embeddings

graph2 = tf.Graph()
with graph2.as_default():
    with tf.Session(graph=graph2) as session1:
        text_input = tf.placeholder(dtype=tf.string, shape=[None])
        embedELMO = hub.Module("https://tfhub.dev/google/elmo/3", trainable=False)
        # embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/2")
        init_op = tf.group([tf.global_variables_initializer(), tf.tables_initializer()])
        embeddingsELMO = embedELMO(text_input,signature="default",as_dict=True)["elmo"]
graph2.finalize()

def encoding_using_elmo(documents):
    with tf.Session(graph=graph2) as session1:
        session1.run(init_op)
        result = session1.run(embeddingsELMO, {text_input: documents})
        return result

documents = ['It is my birthday','Happy Birthday to you']
emb = encoding_using_elmo(documents)
X = emb[0,1,:]
Y = emb[1,1,:]
Z = [X,Y]
cosine_similarity(Z, Y=None, dense_output=True)



# Word2vec

from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 
warnings.filterwarnings(action = 'ignore')
import gensim 
from gensim.models import Word2Vec
#!wget -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)


