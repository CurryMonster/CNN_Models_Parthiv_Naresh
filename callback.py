# -*- coding: utf-8 -*-

import tensorflow as tf
from constants import external_drive_location, callback_cutoff_accuracy

'''
This callback stops training if the accuracy reaches 90%
'''

class myCallback(tf.keras.callbacks.Callback):
    
    def on_epoch_end(self, epoch, logs={}):
        
        if(logs.get('acc')>callback_cutoff_accuracy):
            self.model.save_weights(external_drive_location + "\\V3_Parthiv_Attempt_1.h5")
            print("\nReached 60% accuracy so cancelling training!")
            self.model.stop_training = True
