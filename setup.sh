#!/bin/sh

# Upgrade PIP
pip2.7 install --upgrade pip

# Install requirements
pip2.7 install -r requirements

# Download Androguard
git clone https://github.com/androguard/androguard.git

# Setup Androguard
cd androguard
python setup.py install
cd ..

# Download and build apktool
git clone git://github.com/iBotPeaches/Apktool.git
cd Apktool
./gradlew build fatJar
mv brut.apktool/apktool-cli/build/libs/apktool-cli.jar ../apktool.jar
cd ..
rm -rf Apktool/

# Download and unzip dex2jar
wget https://bitbucket.org/pxb1988/dex2jar/downloads/dex2jar-2.0.zip
unzip dex2jar-2.0.zip
rm dex2jar-2.0.zip
chmod +x dex2jar-2.0/*

# Download frida-server
curl -O http://build.frida.re/frida/android/arm/bin/frida-server
chmod +x frida-server
adb forward tcp:27042 tcp:27042
