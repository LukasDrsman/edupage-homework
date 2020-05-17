# edupage-homework (eduhw)
## Installation
#### Requirements:
* edupage account
* python3 with pip
  * selenium
* chrome or firefox
* geckodriver (when using firefox)

#### Install selenium:
```sh
pip install selenium --user
```

#### Install and run:
```sh
git clone https://github.com/LukasDrsman/edupage-homework.git
cd edupage-homework
# edit and rename config-example.py to config.py
./build
eduhw
```

## Usage:
```
eduhw [mode]
```
| Mode (long)   |Mode (short)| Function                                    |
| ------------- |:----------:|--------------                               |
| normal        |            | assignments separated by chosen separator   |
| simple        | s          | assignments separated by empty newlines     |
| minimal       | m          | assignments take up 1 line                  |
<br>
