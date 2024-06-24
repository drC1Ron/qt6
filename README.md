Installation:
```
cmd> conda install conda=24.5.0
cmd> conda create -n pyqt6 python=3.9
cmd> conda activate pyqt6
cmd> pip install pyqt6-tools
cmd> pip install pyqtgraph
cmd> pip install pyads
```

Run designer:
```
cmd> pyqt6-tools designer main.ui
cmd> pyuic6 -x main.ui -o designer.py
```