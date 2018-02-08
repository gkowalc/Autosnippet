# Project Description
___
Autoclipper is a Linux/Windows tool which can be used to paste frequently used text snippets from the local files. It is quite similar to Texexpander (for Mac) AutoHotKey, AutoKey
Tested on Ubuntu 16.04 LTS and Windows 10.
### Prerequisites Linux
Python in version 3 or higher must be installed.
In addition to this, following python modules are required:

```
sudo apt-get install python3-pip
```

```
 sudo apt-get install python3-tk
```

```
sudo pip3 install pathlib
```

```
 sudo pip3 install pyautogui
```

### Installation Linux
* Download script files:
wget https://github.com/gkowalc/Autosnippet/archive/master.zip
* Unzip script files
* Create directory for snippets files:

 ```
cd ~
```

 ```
mkdir .snippets
```

 note: if you want to use different directory for snippets than default ~/.snippets open autoclipper.py file  in texteditor and edit directory path in line:

 ```
base_dir = '~/.snippets/'
 ```

* Add some text files to the directory:

```
cd ~/.snippets
```

```
vi sample_snippet1
```

* Add custom keyboard shortcut which triggers autosnippet.py file.
  Sample workflow for KDE:

 *  search for "Custom Shortcuts" -> Edit -> New -> Global Shortcut -> Command/URL
 *  In trigger tab add keyboard shortcut which will be used to call the program.
 *   In Action tab provide path to autosnippet.py file:
 ```
 python3 /home/<path/to/installation/ directory/autosnippet.py
 ```


### Prerequisites Windows
 Download  and install latest python 3.X:
https://www.python.org/downloads/

Open windows command line and install required python packages:

```
 py -m pip install pyautogui
```

```
 py -m pip install pyperclip
```

```
 py -m pip install pathlib
```
### Installation Windows
* Download script files:
https://github.com/gkowalc/Autosnippet/archive/master.zip
* Unzip files
* Create directory for snippets files in (default C:/snippets)
note: if you want to use different directory for snippets than default C:/snippets/ open autosnippet_windows.py file and edit path in line:
```
base_dir = 'C:/snippets/'
```
* Add some text files to the directory by using favorite text editor
* Copy autosnippet_windows.py file to dekstop
* Right click on autosnippet_windows.py -> Create Shortcut
* Right click on newly created shortcut.
Change "Run" to Mitimized. Add preferred Shortcut key (for example Ctrl + Alt + 2)


## Usage
Adding/editing existing  text snippets:

* Currently possible only via any text editor

Using existing snippets:

* Go to snippets directory (Linux default  ~/.snippets, Windwos default c:/snippets) add create some text files using favorite text editor.
* Open place where your text snippets should be pasted (can be a webbrowser or text editor)
* Press shortcut combination specified in Installation section.
* Select from the list some item and click on "Paste snippet". Content of selected file should be pasted into webbrowser/text editor :)

Note: you can select multiple items to paste content from multiple files at once. Searchbox is active after program is initialized. Use it to search for specified snippets (this feature is feature when total number of snippets is higher than 20-30)
## Contributing

1. Fork Autoclipper
2. Create your feature branch: git checkout -b my-new-feature
3. Commit your changes: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request

## Authors

*   Grzegorz (Greg) Kowalczyk

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
Inspired by https://github.com/leehblue/texpander



 
