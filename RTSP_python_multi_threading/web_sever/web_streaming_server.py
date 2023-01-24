from flask import Flask, render_template, Response
import cv2
import webbrowser
import time

class WebStreamingServer:

	def __init__(self, host, port, browser_path, result_queue, \
		resize_width, resize_height):
		
		self.host = host
		self.port = port
		self.browser_path = browser_path
		self.result_queue = result_queue
		
		self.app = Flask(__name__)
		
		print('Start web server ...')
		
		def get_result_frame():
			
			while True:
				
				try:					
					time.sleep(0.001)
					if not self.result_queue.empty():

						# Get frame
						frame = self.result_queue.get()
						img = frame.get_img()
						img_id = frame.get_img_id()
						#print('img_id:', img_id)

						# Processing img
						img = cv2.resize(img, dsize=(resize_width, resize_height), interpolation=cv2.INTER_AREA)
						img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

						ret, buffer = cv2.imencode('.jpg', img)
						img = buffer.tobytes()
						yield (b'--frame\r\n'
						b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')  # concat frame one by one and show result

				except Exception as e:
					print('WebStreamingServer error!', e)
					print('reopen web!')
					
		@self.app.route('/video_feed')
		def video_feed():
			# Video streaming route. Put this in the src attribute of an img tag
			return Response(get_result_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

		@self.app.route('/')
		def index():
			# Rendering video streaming home page
			return render_template('streaming.html')

	def run_web_server(self):
		self.app.run(host=self.host,
		port=self.port)
		
