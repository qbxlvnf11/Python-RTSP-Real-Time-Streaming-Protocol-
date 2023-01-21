
Description
=============

#### - RTSP (Real Time Streaming Protocol)
  - An application-level network protocol designed for multiplexing and packetizing multimedia transport streams (such as interactive media, video and audio) over a suitable transport protocol
  - Details about RTSP: https://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol

#### - VLC Media Plyaer
  - Tools of uploading test video to RTSP server 
  - Building RTSP server which sends test video using VLC Media Player before run this code.

Contents
=============

#### - [PyAV RTSP streaming](https://github.com/qbxlvnf11/RTSP-streaming-multi-threading/blob/RTSP_streaming_web_server/RTSP_python_test.ipynb)
  - Simple RTSP streaming code with PyAV
  
#### - [RTSP streaming with multi threading](https://github.com/qbxlvnf11/RTSP-streaming-multi-threading/tree/RTSP_streaming_web_server/RTSP_python_multi_threading)
  - Streaming results
  
  <img src="https://user-images.githubusercontent.com/52263269/167385545-d4338dd8-0a63-4409-a64c-35f6d91a15f1.png" width="60%"></img>
  
  - Separating the thread that reads the frame from rtsp server and the thread that shows the read frame 
  - Main thread: displaying the frame read from rtsp server
  - RTSP frame receiver thread: queue the frame read from rtsp server
  - Parameters: referencing the param.py
  
How to use
=============

#### - Streaming web server

```
python main.py --ip 192.168.1.1 --port 8554 --path /test/test --id admin --password admin --rtsp_transport udp --buffer_size 425984
```

References
=============

#### - Python av package

https://pypi.org/project/av/

#### - How to use VLC media

https://blog.naver.com/qbxlvnf11/222723870300

Author
=============

#### - LinkedIn: https://www.linkedin.com/in/taeyong-kong-016bb2154

#### - Blog URL: https://blog.naver.com/qbxlvnf11

#### - Email: qbxlvnf11@google.com, qbxlvnf11@naver.com
