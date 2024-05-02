# PreRequisites
* https://github.com/nihitjain11/instantJupyter/tree/master
* docker-compose and docker
* python3

# Start
```
cd instantJupyter
make notebook
```

# Data

* https://archive.ics.uci.edu/dataset/53/iris

# Unzip Data
```
unzip iris.zip -d iris
```

# Notebook
```
work on iris-notebook.ipynb
```

# Install Packages
```
pip install flask flask_restful
```

# Model to production
```
python Model.py
```

# Try it out

http://localhost:5071/logreg?sl=4.9&sw=3.0&pl=1.4&pw=0.2

http://localhost:5071/logreg?sl=5.1&sw=1.0&pl=2.4&pw=0.1

# Stop
```
make stop
```

