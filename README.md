# talana-kombat
Video game JRPG

## Docker run
You can find other tags of docker image into [my docker hub](https://hub.docker.com/repository/docker/alexandrojp/talana-kombat/).
```bash
docker run -it alexandrojp/talana-kombat:0.2 bash

# Inside container
> python main.py
```
Try another kombat
```bash
docker start -i [CONTAINER ID]
```

## Run test
```
docker run -it alexandrojp/talana-kombat:0.2 bash

# Inside container
> python -m unittest discover
```