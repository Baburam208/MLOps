## Build and Run the Docker Container

First, let's make sure the `Docker Desktop` is running or not. If not open the `Docker Desktop` application.

### Step 1: Build the Docker Image
```
docker-compose build
```

### Step 2: Start the Container
```
docker-compose up
```

### Stop the Container
Press `CTRL + C` to stop the running container.

To stop and remove the container completely.
```
docker-compose down
```

### `docker-compose.yml` file break down
```
services:
  fastapi-app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    restart: always
```

#### 1. `services`:
This defines the services (containers) that Docker Compose will manage. In this case, we have a single service called `fastapi-app`.

#### 2. `fastapi-app`:
This is the name of the service (container) (it should be descriptive).

#### 3. `build: .`
This tells Docker Compose to build the Docker image using the `Dockerfile` located in the **current directory (`.`)**.

* If  we have a `Dockerfile` in the same directory as `docker-compose.yml`, it will be used automatically.
* We can also specify a different directory, e.g., `build: ./app`.

#### 4. `ports`:
```
ports:
    - "8000:8000"
```

This maps port `8000` of the host machine (our computer) to port `8000` inside the **container**.

* This means that if our FastAPI app runs on `http://127.0.0.1:8000`, we can access it **outside** the container on the same port.
* Format: `"host_port:container_port"`

#### 5. `volumes`:
```
volumes:
    - .:/app
```

This mounts the **current directory (`.`) on the host** to `/app` inside the container.
* This allows us to modify the code on our host machine without rebuilding the container.
* Format: `host_path:container_path`
* In this case, any changes we make to the files in our project directory will be reflected inside the container in real-time.

#### 6. `restart: always`
This ensures that the container **automatically restarts** if it crashes or if the system reboots.
* Alternatives:
    * `restart: always` -> Restart the container **always**, even after a system reboot.
    * `restart: unless-stopped` -> Restart unless you **manually stop** the container.
    * `restart: on-failure` -> Restart only if the container **exists with an error.**
    * No restart policy -> The container will stop and won't restart unless we manually restart it.


#### What Happens When You Run `docker-compose up`?
1. Docker Compose reads `docker-compose.yml`.
2. It **builds** the FastAPI using the `Dockerfile`.
3. It starts a container with:
    * The `fastapi-app` service.
    * Port `8000` mapped to our local machine.
    * A live-mounted volume (`.` -> `/app`)
    * An automatic restart policy.
