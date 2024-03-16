# instantJupyter

## Requirements
* macOS (to auto-open the notebook in browser)
* docker-compose

## Start
```make notebook```

## STOP
```make stop```

## Alternative
- open the notebook with the link shared with token and remember to update the port number to 10001
```docker run -p 10001:8888 jupyter/datascience-notebook```