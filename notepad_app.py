'''
  A minimalist Notepad built with the PySimpleGUI TKinter framework
  Author:     Israel Dryer
  Email:      israel.dryer@gmail.com
  Modified:   2020-06-20

  Editor: Patrick Stampler
  Email: patrick@ow
  Features added:
    - Folder Structure Browser for easier note organizations

'''
import PySimpleGUI as sg
import pathlib
import os
sg.ChangeLookAndFeel('BrownBlue')  # change style

WIN_W = 90
WIN_H = 25
file = None

fnames = []

# Definition of top menu band
menu_layout = [['File', ['New (Ctrl+N)', 'Open (Ctrl+O)', 'Save (Ctrl+S)', 'Save As', '---', 'Exit']],
               ['Tools', ['Word Count']],
               ['Help', ['About']]]

# Definition of file list column (includes the browse button)
file_list_column = [
    [
        sg.Text("Notes Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse("Browse")
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 50), key="-FILE LIST-"
        )
    ],
    [
        sg.Text('> New file <', font=('Consolas', 10),
                size=(40, 1), key='_INFO_')
    ]
]

# Screen layout
layout = [[sg.Menu(menu_layout)], [sg.Column(file_list_column), sg.Multiline(
    font=('Consolas', 12), size=(100, WIN_H/2), key='_BODY_')]]

window = sg.Window('Notepad', layout=layout, margins=(
    0, 0), resizable=True, return_keyboard_events=True, finalize=True)
# window.maximize()
window['_BODY_'].expand(expand_x=True, expand_y=True)


def new_file():
    '''Reset body and info bar, and clear filename variable'''
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> New File <')
    file = None
    return file


def open_file():
    '''Open file and update the infobar'''
    filename = sg.popup_get_file('Open', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        window['_BODY_'].update(value=file.read_text())
        window['_INFO_'].update(value=file.absolute())
        return file


def save_file(file):
    '''Save file instantly if already open; otherwise use `save-as` popup'''
    if file:
        file.write_text(values.get('_BODY_'))
    else:
        save_file_as()


def save_file_as():
    '''Save new file or save existing file with another name'''
    filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get('_BODY_'))
        window['_INFO_'].update(value=file.absolute())
        return file


def word_count():
    '''Display estimated word count'''
    words = [w for w in values['_BODY_'].split(' ') if w != '\n']
    word_count = len(words)
    sg.popup_no_wait('Word Count: {:,d}'.format(word_count))


def about_me():
    '''A short, pithy quote'''
    sg.popup_no_wait('"All great things have small beginnings" - Peter Senge')


while True:
    event, values = window.read()
    if event in ('Exit', None):
        break
    if event in ('New (Ctrl+N)', 'n:78'):
        file = new_file()
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
    if event in ('Save (Ctrl+S)', 's:83'):
        save_file(file)
    if event in ('Save As',):
        file = save_file_as()
    if event in ('Word Count',):
        word_count()
    if event in ('About',):
        about_me()

    # -- note selector --
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    folder = values["-FOLDER-"]
    try:
        # Get list of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".txt"))
    ]
    window["-FILE LIST-"].update(fnames)

    if event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )

            file = pathlib.Path(filename)
            window['_BODY_'].update(value=file.read_text())
            window['_INFO_'].update(value=file.absolute())

        except:
            pass
