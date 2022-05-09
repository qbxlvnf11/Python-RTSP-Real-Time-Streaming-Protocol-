import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

import cv2
import os
import copy
import numpy as np

from frame import Frame

class RtspFrameDisplayProcessor():
	def __init__(self, frame_queue, resize_width, resize_height):
		
		figManager = plt.get_current_fig_manager()
		figManager.full_screen_toggle()
			
		self.frame_queue = frame_queue
		self.resize_width = resize_width
		self.resize_height = resize_height
	
	def start(self):
		
		set_flag = False
		
		while True:
			
			#create two subplots
			ax = plt.subplot(1,1,1)
			
			plt.ion()
			
			if not self.frame_queue.empty():
				
				# Get frame
				frame = self.frame_queue.get()
				img = frame.get_img()
				img_id = frame.get_img_id()
				#print('img_id:', img_id)
				
				# Processing img		
				img = cv2.resize(img, dsize=(self.resize_width, self.resize_height), interpolation=cv2.INTER_AREA)
				
				# Open board
				if not set_flag:
					im = ax.imshow(img)
					set_flag = True
				
				# Change data
				im.set_data(img)
				
				# Wait
				plt.pause(0.0001)
		
		plt.ioff()
					
