from queue import Queue, Empty

class FrameQueue(Queue):
	def __init__(self, max_size, skip_count):
		
		self.max_size = max_size
		
		if not self.max_size == -1:
			self.queue = Queue(maxsize=max_size)
		else:
			self.queue = Queue()
        
		self.skip_count = skip_count

	def put(self, frame):
		if frame.get_img_id() % self.skip_count == 0:
			if not self.max_size == -1:
				self.queue.put(frame, block=True, timeout=5000)
			else:
				self.queue.put_nowait(frame)
		print(f"Frame queue size : {self.queue.qsize()}")

	def get(self):
		print("FrameQueue get")
		if not self.max_size == -1:
			return self.queue.get(block=True, timeout=5000)
		else:    
			return self.queue.get_nowait()
	
	def empty(self):
		return self.queue.empty()

	def clear(self):
		try:
			while True:
				self.queue.get_nowait()
		except Empty:
			pass

	def size(self):
		return self.queue.qsize()
