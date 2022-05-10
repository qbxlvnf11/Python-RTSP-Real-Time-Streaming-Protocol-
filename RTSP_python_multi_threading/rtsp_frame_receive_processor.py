import threading
import cv2
import os
import copy
import numpy as np
import av
from PIL import Image, ImageStat

from frame import Frame

class RtspFrameReceiveProcessor(threading.Thread):
	def __init__(self, frame_queue, fps, \
			ip, port, path, id, password, \
			rtsp_transport, buffer_size, stimeout, max_delay):
		threading.Thread.__init__(self)
		
		self.frame_queue = frame_queue
		self.fps = fps
		
		self.ip = ip
		self.port = port
		self.path = path
		self.id = id
		self.password = password
		self.rtsp_transport = rtsp_transport
		self.buffer_size = buffer_size
		self.stimeout = stimeout
		self.max_delay = max_delay
	
	def __av_open(self):
		av_open_options = {'rtsp_transport': self.rtsp_transport, 'buffer_size': self.buffer_size, 'stimeout': self.stimeout, 'max_delay': self.max_delay}
		metadata_errors = 'nostrict'
		
		if self.id != 'None':
			self.rtsp_address = 'rtsp://'+str(self.id)+':'+str(self.password)+'@'+str(self.ip)+':'+str(self.port)+str(self.path)
		else:
			self.rtsp_address = 'rtsp://'+str(self.ip)+':'+str(self.port)+str(self.path)
		
		print('-'*30)
		print('RTSP rtsp_address:', self.rtsp_address)
		print('-'*30)
		
		self.video = av.open(self.rtsp_address,
                         options=av_open_options,
                         metadata_errors=metadata_errors)
		self.stream = self.video.streams.video[0]
	
	def __is_gray_scale_image(self, img):

		if len(img.shape) == 3 and np.std([np.std(img[:, :, 0]), np.std(img[:, :, 1]), np.std(img[:, :, 2])]) < 0.01:
			return True
		elif len(img.shape) == 2:
			return True
	    
		return False		
	
	def run(self):
		
		self.__av_open()

		print('-'*30)
		print('Start Streaming ...')
		print('-'*30)	
		
		rfps = int(self.stream.average_rate)
		img_id = 0
		add_num = 0
			
		for packet in self.video.demux():
			for frame in packet.decode():
				
				add_num += 1
				
				if packet.stream.type == 'video' and add_num % int(rfps / self.fps) == 0:
					
					img_id += 1
					
					# Get time
					get_time = float(frame.pts * self.stream.time_base)
					
					# Get img
					img = frame.to_image()
					img = np.array(img)
					
					# Gray scale
					gray_scale_flag = self.__is_gray_scale_image(img)
					
					# Init Frame
					frame = Frame(self.rtsp_address, self.fps, img_id, img, time, gray_scale_flag)
					frame.print_frame()
					
					self.frame_queue.put(frame)
					
					
