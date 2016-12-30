# onion-omega2-garage-door-webcam

Work In Progress: A remote garage door opener, plus night-vision webcam to ensure garage is clear, controlled by an Onion Omega2+.


Parts
=====
* Onion Omega2
* Onion expansion dock
* 5v relay
* Power supply
* Cleapo 1.3 MP WebCam with night vision (Gear Head WC1300BLK)
* ...

Installation
============

```
# Log into your Omega2 via the terminal, then checkout the code
opkg update && opkg install git python mjpg-streamer
git clone git://github.com/bikegriffith/onion-omega2-garage-door-webcam
...
```

Notes
=====
* Streaming

    ```
    > mjpg_streamer mjpg_streamer -i "input_uvc.so -d /dev/video0 -y" -o "output_http.so"
    open http://192.168.1.15:8080/?action=stream
    ```
