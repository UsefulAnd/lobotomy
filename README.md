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

Lobotomy is an Android security toolkit that will automate different Android assessments and reverse engineering tasks.  The goal of the Lobotomy toolkit is to provide a console environment, which would allow a user to load their target Android APK once, then have all the necessary tools without needing to exit that environment.  

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
  
In order to use the Frida instrumentation module please make sure you have pushed the frida-server binary over to your target device and executed it.

```$ adb push frida-server /data/local/tmp/```

```root@android:/ # /data/local/tmp/frida-server```

Make sure you change the IP in **framework/config** to your local network IP.  This is used for the interactions with the deployed web services.

## Usage

### Help

```
(lobotomy) help

Documented commands (type help <topic>):
----------------------------------------
_load           components  edit     li      pause        run        show
_relative_load  d2j         frida    list    permissions  save
attacksurface   debuggable  hi       load    profiler     set
bowser          decompile   history  loader  py           shell
cmdenvironment  ed          l        logcat  r            shortcuts

Undocumented commands:
----------------------
EOF  eof  exit  help  q  quit
```

### Start Web Server

```
[~/Tools/mobile/android/lobotomy]> python web/run.py runserver -h 0.0.0.0
```

UI endpoints are located at: ```/ui/home```

### Loading an APK

```
[~/Tools/mobile/android/lobotomy]> python lobotomy.py


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


(lobotomy) loader /Users/benjaminwatson/Android-Web-Browsers/opera-mini/apk/com.opera.mini.native.apk
[2015-08-03 19:16:44.866870] Loading : /Users/benjaminwatson/Android-Web-Browsers/opera-mini/apk/com.opera.mini.native.apk
(lobotomy)

```

### List Permissions

```
(lobotomy) permissions list
[2015-08-03 19:27:31.175369] Permission: android.permission.ACCESS_FINE_LOCATION
[2015-08-03 19:27:31.175409] Permission: android.permission.ACCESS_NETWORK_STATE
[2015-08-03 19:27:31.175421] Permission: android.permission.INTERNET
[2015-08-03 19:27:31.175430] Permission: android.permission.NFC
[2015-08-03 19:27:31.175438] Permission: android.permission.WRITE_EXTERNAL_STORAGE
[2015-08-03 19:27:31.175446] Permission: com.android.launcher.permission.INSTALL_SHORTCUT
[2015-08-03 19:27:31.175454] Permission: com.opera.GET_BRANDING
[2015-08-03 19:27:31.175461] Permission: com.opera.mini.native.permission.CRASHHANDLER
[2015-08-03 19:27:31.175469] Permission: com.android.browser.permission.READ_HISTORY_BOOKMARKS
[2015-08-03 19:27:31.175477] Permission: android.permission.SYSTEM_ALERT_WINDOW
[2015-08-03 19:27:31.175484] Permission: android.permission.WAKE_LOCK
[2015-08-03 19:27:31.175491] Permission: com.google.android.c2dm.permission.RECEIVE
[2015-08-03 19:27:31.175498] Permission: com.opera.mini.native.permission.C2D_MESSAGE
[2015-08-03 19:27:31.175505] Permission: android.permission.READ_CONTACTS
[2015-08-03 19:27:31.175571] Permission: android.permission.VIBRATE
```

### Map Permissions

```
(lobotomy) permissions map
[2015-08-03 19:28:07.078496] Found permission mapping : android.permission.ACCESS_FINE_LOCATION
[2015-08-03 19:28:07.078543] Searching for : android.telephony.TelephonyManager
[2015-08-03 19:28:12.686411] Searching for : android.location.LocationManager
1 Lbo/app/bs;-><init>(Landroid/content/Context; Landroid/location/LocationManager; Lbo/app/bb; Lcom/appboy/configuration/XmlAppConfigurationProvider;)V (0x120) ---> Landroid/location/LocationManager;->requestLocationUpdates(Ljava/lang/String; J F Landroid/app/PendingIntent;)V
1 Lpz;->a()V (0x20) ---> Landroid/location/LocationManager;->requestLocationUpdates(Ljava/lang/String; J F Landroid/location/LocationListener;)V
1 Lbo/app/bs;->c()Lbo/app/da; (0x2e) ---> Landroid/location/LocationManager;->getProviders(Landroid/location/Criteria; Z)Ljava/util/List;
1 Lbo/app/bs;->c()Lbo/app/da; (0x54) ---> Landroid/location/LocationManager;->getProviders(Landroid/location/Criteria; Z)Ljava/util/List;
1 Lpy;->a(Llb;)Landroid/location/Location; (0x50) ---> Landroid/location/LocationManager;->getProviders(Z)Ljava/util/List;
1 Lbo/app/bs;->c()Lbo/app/da; (0x2e) ---> Landroid/location/LocationManager;->getProviders(Landroid/location/Criteria; Z)Ljava/util/List;
1 Lbo/app/bs;->c()Lbo/app/da; (0x54) ---> Landroid/location/LocationManager;->getProviders(Landroid/location/Criteria; Z)Ljava/util/List;
1 Lkf;->detectlocation(Ljava/lang/String;)V (0x9e) --->
```

### Attack Surface

```
(lobotomy) attacksurface
[2015-08-03 19:29:02.272276] ---------
[2015-08-03 19:29:02.272317] Activites
[2015-08-03 19:29:02.272327] ---------
[2015-08-03 19:29:02.272472] com.opera.android.MiniActivity : Found Activity with launchMode!
[2015-08-03 19:29:02.272507] com.opera.android.MiniActivity : launchMode : singleTask
[2015-08-03 19:29:02.272778] com.opera.mini.android.Browser : Found Activity with launchMode!
[2015-08-03 19:29:02.272793] com.opera.mini.android.Browser : launchMode : singleTask
[2015-08-03 19:29:02.272900] com.opera.mini.android.Browser : Found Activity with schemes!
[2015-08-03 19:29:02.272912] com.opera.mini.android.Browser : scheme : ftp
[2015-08-03 19:29:02.272932] com.opera.mini.android.Browser : scheme : about
[2015-08-03 19:29:02.272943] com.opera.mini.android.Browser : scheme : http
[2015-08-03 19:29:02.272952] com.opera.mini.android.Browser : scheme : opera
[2015-08-03 19:29:02.272961] com.opera.mini.android.Browser : scheme : adx
[2015-08-03 19:29:02.272970] com.opera.mini.android.Browser : scheme : https
[2015-08-03 19:29:02.273250] com.opera.mini.android.Browser : action : android.intent.action.MAIN
[2015-08-03 19:29:02.273263] com.opera.mini.android.Browser : action : android.intent.action.VIEW
[2015-08-03 19:29:02.273272] com.opera.mini.android.Browser : action : android.nfc.action.NDEF_DISCOVERED
[2015-08-03 19:29:02.273280] com.opera.mini.android.Browser : action : android.speech.action.VOICE_SEARCH_RESULTS
[2015-08-03 19:29:02.273289] com.opera.mini.android.Browser : action : android.intent.action.WEB_SEARCH
[2015-08-03 19:29:02.273297] com.opera.mini.android.Browser : category : android.intent.category.LAUNCHER
[2015-08-03 19:29:02.273305] com.opera.mini.android.Browser : category : android.intent.category.DEFAULT
[2015-08-03 19:29:02.273313] com.opera.mini.android.Browser : category : android.intent.category.BROWSABLE
[2015-08-03 19:29:02.273321] ---------
[2015-08-03 19:29:02.273328] Receivers
[2015-08-03 19:29:02.273335] ---------
[2015-08-03 19:29:02.273712] com.AdX.tag.AdXAppTracker : Found exported receiver!
[2015-08-03 19:29:02.273724] com.AdX.tag.AdXAppTracker : exported : true
[2015-08-03 19:29:02.273880] com.AdX.tag.AdXAppTracker : action : com.android.vending.INSTALL_REFERRER
[2015-08-03 19:29:02.274348] com.opera.android.gcm.GcmBroadcastReceiver : action : com.google.android.c2dm.intent.RECEIVE
[2015-08-03 19:29:02.274361] com.opera.android.gcm.GcmBroadcastReceiver : category : com.opera.mini.native
[2015-08-03 19:29:02.274821] com.opera.android.appboy.AppboyBroadcastReceiver : action : com.opera.mini.native.intent.APPBOY_PUSH_RECEIVED
[2015-08-03 19:29:02.274833] com.opera.android.appboy.AppboyBroadcastReceiver : action : com.opera.mini.native.intent.APPBOY_NOTIFICATION_OPENED
[2015-08-03 19:29:02.274842] ---------
[2015-08-03 19:29:02.274848] Providers
[2015-08-03 19:29:02.274855] ---------
[2015-08-03 19:29:02.275486] ---------
[2015-08-03 19:29:02.275494] Services
[2015-08-03 19:29:02.275511] ---------
```
