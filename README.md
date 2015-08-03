# Lobotomy
```
                  :                   :                  :
                 t#,                 t#,                t#,
            i   ;##W.   .           ;##W.              ;##W.
           LE  :#L:WE   Ef.        :#L:WE  GEEEEEEEL  :#L:WE             ..       : f.     ;WE.
          L#E .KG  ,#D  E#Wi      .KG  ,#D ,;;L#K;;. .KG  ,#D           ,W,     .Et E#,   i#G
         G#W. EE    ;#f E#K#D:    EE    ;#f   t#E    EE    ;#f         t##,    ,W#t E#t  f#f
        D#K. f#.     t#iE#t,E#f. f#.     t#i  t#E   f#.     t#i       L###,   j###t E#t G#i
       E#K.  :#G     GK E#WEE##Wt:#G     GK   t#E   :#G     GK      .E#j##,  G#fE#t E#jEW,
     .E#E.    ;#L   LW. E##Ei;;;;.;#L   LW.   t#E    ;#L   LW.     ;WW; ##,:K#i E#t E##E.
    .K#E       t#f f#:  E#DWWt     t#f f#:    t#E     t#f f#:     j#E.  ##f#W,  E#t E#G
   .K#D         f#D#;   E#t f#K;    f#D#;     t#E      f#D#;    .D#L    ###K:   E#t E#t
  .W#G           G#t    E#Dfff##E,   G#t      t#E       G#t    :K#t     ##D.    E#t E#t
 :W##########Wt   t     jLLLLLLLLL;   t        fE        t     ...      #G      ..  EE.
 :,,,,,,,,,,,,,.                                :                       j           t
```

Lobotomoy is an Android security toolkit that will automate different Android assessments and reverse engineering tasks.  The goal of the Lobotomy toolkit is to provide a console environment, which would allow a user to load their target Android APK once, then have all the necessary tools without needing to exit that environment.  

Lobotomy leverages and provides wrappers around other popular tools such as: 
- **Androguard**
- **apktool**
- **Dex2Jar**
- **Frida**

## Features

- APK decompilation
- APK conversion with Dex2Jar
- Convert APK to a debuggable APK
- APK Profiler
- Enumerate attack surface:
  - Intent Filters
  - URL Schemes
  - Exported Components
- Enumerate application components:
  - Activities 
  - Broadcast Receivers
  - Services
  - Content Providers
- Enumerate application permissions
- Map permissions to API usage
- Bowser toolkit:
  - Enumerates methods: 
    - parseUri() 
    - loadUrl() 
    - addJavascriptInterface()
  - Triggers parseUri()
- Logcat wrapper
- Instrumentation with Frida
- Web UI and Services

## Installation and Setup

- Lobotomy was built upon **Python 2.7.9** and was also validated against **2.7.10**
- Building the **apktool** requires Java and has been validated against **1.8**
- Lobotomy assumes that you have already downloaded the Android SDK and added the following tools to your path: 
  - **adb**  

### Run Setup: 

```./setup.sh ```

## Issues 

*Androguard's current MASTER seems to have internal broken import paths.  This unfortunately breaks the ability to use it within Lobotomy as the core functionality for loading an APK.  We have included the working build in this repository so that Lobotomy can still remain stable and will upate accordingly if any fix is identified.*

