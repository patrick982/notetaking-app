# Note-taking App

Originally from Israel Dryer (credits to him), I extended his app by a folder structure to be able to keep the notes more organized. This project simply done as an exercise to get started with PySimpleGui

## Description

The folder section on the left side gets filled after you browsed for a folder. Afterwards simply click on the detected .txt file (needs to be .txt on purpose) and it gets displayed on the right section of the app. You can edit and save and create new notes as you wish. 
A popup gets displayed if saving was sucessful, so that you don't loose any data by accident.

## Getting Started

### Dependencies

python3 

```
from typing import Text
import PySimpleGUI as sg
import pathlib
import os
```

### Installing and Excuting the program

you can download the notepad_app.py file, make sure the dependencies are installed, and simply run it from the command prompt. 
Of course you can also use tools like pyinstaller to get an executeable fitting your OS.


## Authors

Israel Dryer

edited by Patrick Stampler


## License

from the original author: 
https://github.com/israel-dryer/Notepad/blob/master/LICENSE

## Acknowledgments

Inspiration, code snippets, etc.
https://github.com/israel-dryer
