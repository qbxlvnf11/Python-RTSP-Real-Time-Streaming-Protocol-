class Frame:
	def __init__(self, rtsp_address, fps, img_id, img, time, gray_scale_flag):

		self.__rtsp_address = rtsp_address
		self.__fps = fps
		
		# Frame
		self.__img_id = img_id
		self.__img = img
		self.__time = time
		self.__img_shape = img.shape
		self.__gray_scale_flag = gray_scale_flag

	def get_img_id(self):
		return self.__img_id
    
	def get_img(self):
		return self.__img
		
	def print_frame(self):
		print('-'*20)
		print(f"fps: {self.__fps}")
		print(f"time: {self.__time}")
		print(f"Image id: {self.__img_id}")
		print(f"Image shape: {self.__img_shape}")
		print('-'*20)		


