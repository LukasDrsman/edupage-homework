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
sudo ./install
eduhw
```

## Usage:
```
eduhw [mode]
```
| mode (long)   | mode (short)| description                                 |
| ------------- |:-----------:|--------------                               |
|               |             | simple output                               |
| --formatted   | -f          | formatted output                            |
| --minimal     | -m          | 1 assignment per line                       |
<br>
