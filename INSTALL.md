## Installation and Setup

- Lobotomy was built upon **Python 2.7.9** and was also validated against **2.7.10**
- Building the **apktool** requires Java and has been validated against **1.8**
- Lobotomy assumes that you have already downloaded the Android SDK and added the following tools to your path: 
  - **adb**  

### Run Setup: 

```./setup.sh ```
  
In order to use the Frida instrumentation module please make sure you have pushed the frida-server binary over to your target device and executed it.

```$ adb push frida-server /data/local/tmp/```

```root@android:/ # /data/local/tmp/frida-server```

Make sure you change the IP in **framework/config** to your local network IP.  This is used for the interactions with the deployed web services.


## Issues 

*Androguard's current MASTER seems to have internal broken import paths.  This unfortunately breaks the ability to use it within Lobotomy as the core functionality for loading an APK.*

*We have included the working* ***1.9*** *build in this repository so that Lobotomy can still remain stable.*
