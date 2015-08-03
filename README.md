# Lobotomy

Lobotomoy is an Android security toolkit with many features that automate different Android assessment and reverse engineering tasks.  The goal of the Lobotomy toolkit is to provide a console environment, which would allow a user to load their target Android APK once then have all the necessary tooling without needing to exit that environment.  Lobotomy leverages and provides wrappers around other popular tools such as **Androguard**, **apktool**, **Dex2Jar**, and **Frida**.  

## Features

- APK decompilation
- APK conversion with Dex2Jar
- Convert APK to a debuggable APK
- APK Profiler
- Enumerate attack surface:
  *- Intent Filters* 
  *- URL Schemes*
  *- Exported Components*
- Enumerate application components:
  *- Activities* 
  *- Broadcast Receivers*
  *- Services*
  *- Content Providers*
- Enumerate application permissions
- Map permissions to API usage
- Bowser toolkit:
  - Enumerates methods: 
    *- parseUri()* 
    *- loadUrl()* 
    *- addJavascriptInterface()*
  - Triggers parseUri()
- Logcat wrapper
- Instrumentation with Frida
- Web UI and Services

