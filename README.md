<h1>DaVinci Resolve timeline markers to images exporter. </h1>

<p><h2>This application allow you to export markers to images files.</p>
<p> You can choose JPEG, PNG, DPX, TIFF, CIN, PPM, BMP, XPM file type.</p></h2>

![Timeline markers](img/still_exporter_timeline.jpg)
![File type](img/still_exporter_markers.jpg)
![Markers](img/still_exporter_file_type.jpg)

---

<a href="http://www.youtube.com/watch?feature=player_embedded&v=M0hxF1skYvM" target="_blank">
 <img src="http://img.youtube.com/vi/M0hxF1skYvM/mqdefault.jpg" alt="Watch the video" width="1024" height="576" border="10" />
</a>

---
<h3>Export file name convention:</h3>

<p>Path Name:</p>
<p>Choose path to export. App will make a folder - {time}_{timeline name}/</p>
<p>File Name:</p>
<p>{clip_name_without_extention}_TC_{timecode}_{marker name}_.{file type}</p>

---
<p>
<p>Timecode conversion is made by - "SMPTE timecode conversion module by Igor Ridanovic".</p>
<p>https://github.com/IgorRidanovic/smpte/blob/master/SMPTE.py</p>
</p>

---
<h3>Has been tested on :</h3>
<p>- macOS Ventura 13.5 and Windows 10 Pro with Davinci Resolve Studio 18.6 and Python 3.11.4</p>
<p>Script is working with:</p>
</p>- 23.976, 24p, 25p, 30p, 50p, 60p</p>
<p>- 50i, 29.97, 59.94</p>
<p>- DF non DF </p>
<p>- Test it in your conditions. I mostly work with Pal area project like 25p, 50p and 50i</p>

---
<h3>Requirements:</h3>
<p>Davinci Resolve Studio 18.5, Python >=3.6 , PySide6., SMPTE timecode conversion module</p>

---
<h3>Installation:</h3>

<p>Follow DRS developer readme.txt to setup python path.</p>
<p>Set the environment variables.</p>

>
    Mac OS X:
    RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
    RESOLVE_SCRIPT_LIB="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
    PYTHONPATH="$PYTHONPATH:$RESOLVE_SCRIPT_API/Modules/"

    Windows:
    RESOLVE_SCRIPT_API="%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting"
    RESOLVE_SCRIPT_LIB="C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll"
    PYTHONPATH="%PYTHONPATH%;%RESOLVE_SCRIPT_API%\Modules\"
>

<p>Put Script folder to:</p>

>
    Mac OS X:
          - All users: /Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts
          - Specific user:  /Users/<UserName>/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts

    Windows:
          - All users: %PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts
          - Specific user: %APPDATA%\Roaming\Blackmagic Design\DaVinciResolve\Support\Fusion\Scripts
          and start it from Davinci Workspace\ Scripts.
>

---
<h3>To do:</h3>
    <p>- user defined name convention</p>
    <p>- export with grade versions</p>
    <p>- export with burn-in preset(this will work under DRS >=18.6)</p>
    <p>- clean code</p>

---
<h3>Known issue:</h3>
    <p>- Application work from Cut, Edit, Color Page but not from Deliver Page</p>
    <p>- Playhead must be located on any clip in timeline not outside</p>
    <p>- Application does not export clip markers - only timeline markers.</p>


---


[☕️ Fuel my coffee mug 😀](https://www.paypal.com/paypalme/njupixel)


<p>NJUPIXEL Maciej Frydrych 2023</p>
<p>njupixel@gmail.com</p>
