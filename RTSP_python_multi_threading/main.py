from param import get_parser
from frame_queue import FrameQueue
from rtsp_frame_display_processor import RtspFrameDisplayProcessor
from rtsp_frame_receive_processor import RtspFrameReceiveProcessor
from web_sever.web_streaming_server import WebStreamingServer

if __name__ == '__main__':
	
	# Params
	args = get_parser()
	
	# Frame queue
	frame_queue  = FrameQueue(args.max_size, args.skip_count)

	# Web server
	if args.activate_web_server:
		web_streaming_server = WebStreamingServer(args.web_server_host, args.web_server_port, args.browser_path, frame_queue, \
									args.img_width, args.img_height)
	
	# Processor
	if not args.activate_web_server:
		rtsp_frame_display_processor = RtspFrameDisplayProcessor(frame_queue, args.img_width, args.img_height)
	rtsp_frame_receive_processor = RtspFrameReceiveProcessor(frame_queue, args.fps, \
									args.ip, args.port, args.path, args.id, args.password, \
									args.rtsp_transport, args.buffer_size, args.stimeout, args.max_delay)
	
	# Multi threading
	rtsp_frame_receive_processor.start()
	if not args.activate_web_server:
		rtsp_frame_display_processor.start()
	if args.activate_web_server:
		web_streaming_server.run_web_server()
	
	rtsp_frame_receive_processor.join()
		
