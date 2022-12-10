<h1 align="center">win32misc</h1>
<br>

> **win32misc** is a python library to mess with windows api.
> <br>
> Developped by [majvax](https://github.com/majvax)
> <br>
> Credit to [@Peticali](https://github.com/Peticali/PythonBlurBehind) for his BlurWindow library

## Install

```sh
pip install win32misc
```
<br>

# FEATURES

    -> Window Animation              -   ✔️
    -> Hide/Show window              -   ✔️
    -> Center window                 -   ✔️
    -> Change Title                  -   ✔️
    -> Disable min, max, exit btn    -   ✔️
    -> Redirect stdout to null       -   ✔️
    -> Gather System Information     -   ✔️
<br>

## Disable window's max, min, exit button
```python
from win32misc import Window

window = Window()
window.disable_keyboard_exit()
window.disable_max_btn()
window.disable_min_btn()

```
<img src="https://cdn.discordapp.com/attachments/992508929714159727/1051235132104790127/image.png">
<br>
<br>


## Get System info
```python
from win32misc import System

system = System.get_windows_version()
print("windows version:", system.dwMajorVersion)
```

##### output
```
windows version: 10
```

<br>
<br>

