
## Installation and Setup

- Lobotomy was built upon **Python 2.7.9** and was also validated against **2.7.10**
- Building the **apktool** requires Java and has been validated against **1.8**
- Lobotomy assumes that you have already downloaded the Android SDK and added the following tools to your path: 
  - **adb**  

### Run Setup: 

```./setup.sh ```

## Issues 

*Androguard's current MASTER seems to have internal broken import paths.  This unfortunately breaks the ability to use it within Lobotomy as the core functionality for loading an APK.*

*We have included the working build in this repository so that Lobotomy can still remain stable and will update accordingly if any fix is identified.*
