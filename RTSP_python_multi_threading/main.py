from param import get_parser
from frame_queue import FrameQueue
from rtsp_frame_display_processor import RtspFrameDisplayProcessor
from rtsp_frame_receive_processor import RtspFrameReceiveProcessor

if __name__ == '__main__':
	
	# Params
	args = get_parser()
	
	# Frame queue
	frame_queue  = FrameQueue(args.max_size, args.skip_count)
	
	# Processor
	rtsp_frame_display_processor = RtspFrameDisplayProcessor(frame_queue, args.img_width, args.img_height)
	rtsp_frame_receive_processor = RtspFrameReceiveProcessor(frame_queue, \
									args.ip, args.port, args.path, args.id, args.password, \
									args.rtsp_transport, args.buffer_size, args.stimeout, args.max_delay)
	
	# Multi threading
	rtsp_frame_receive_processor.start()
	rtsp_frame_display_processor.start()
	
	rtsp_frame_receive_processor.join()
		
