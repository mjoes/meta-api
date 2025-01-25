# meta-api

```bash
# login
sudo docker login ghcr.io -u mjoes

# pull image
sudo docker pull ghcr.io/mjoes/docker-insert-app:latest

# Run image
docker run -p 5001:5001 --mount type=bind,src=/home/mj/repos/meta-api/metadata.db,dst=/var/lib/metadata.db --network=host docker-insert-app:latest

# Port forward from remote to local
ssh -L 5001:localhost:5001 stubuntu@10.0.0.1
```
