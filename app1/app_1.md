# Docker Tutorial: Building, Running, and Managing a Simple Python Container

This guide walks through:

- Building the image  
- Running containers (with and without arguments)  
- Viewing running + stopped containers (with names)  
- Removing specific containers  
- Removing all containers  
- Removing the image (unbuilding)  
- Example outputs  

This guide assumes you have Docker Desktop running in the background.

## Project Structure

```
Docker_Tutorial/
└── app1/
    ├── Dockerfile
    └── app_1.py
```

## Building the Docker Image

Run inside **app1**:

```bash
docker build -t myapp1 .
```

### Example Output

```
[+] Building 17.7s (9/9) FINISHED
 => [internal] load build definition from Dockerfile
 => [internal] load metadata for python:3.9-slim-bullseye
 => [2/3] WORKDIR /app1
 => [3/3] COPY . .
 => exporting to image

REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
myapp1       latest    45ea0e173df5   18 seconds ago   123MB
```

## Running the Container

### With no arguments

```bash
docker run myapp1
```

Output:

```
Number not provided
```

### With a numeric argument

```bash
docker run myapp1 10
```

Output:

```
10.0 to the power of 2 = 100.0
```

Another:

```bash
docker run myapp1 20
```

Output:

```
20.0 to the power of 2 = 400.0
```

## Viewing Containers

### Show ONLY running containers

```bash
docker ps
```

Typical output:

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Show ALL containers (including exited ones)

```bash
docker ps -a
```

Example Output with Names:

```
CONTAINER ID   IMAGE     COMMAND                CREATED              STATUS                          PORTS     NAMES
7d61b656c2a6   myapp1    "python app_1.py 20"   1 minute ago         Exited (0) 1 minute ago                   naughty_nightingale
ec462a833d30   myapp1    "python app_1.py 10"   2 minutes ago        Exited (0) 2 minutes ago                  determined_cohen
d6930c383337   myapp1    "python app_1.py"      3 minutes ago        Exited (0) 3 minutes ago                  blissful_goldwasser
```

## Removing Containers

### Remove a single container by NAME

```bash
docker rm determined_cohen
```

### Remove ALL stopped containers

```bash
docker rm $(docker ps -a -q)
```

Output:

```
7d61b656c2a6
ec462a833d30
d6930c383337
```

### Verify cleanup

```bash
docker ps -a
```

Output:

```
(no containers listed)
```

## Run Again After Cleanup

```bash
docker run myapp1 20
```

Output:

```
20.0 to the power of 2 = 400.0
```

List containers again:

```bash
docker ps -a
```

Example:

```
CONTAINER ID   IMAGE     COMMAND                CREATED         STATUS                     PORTS     NAMES
19c400986413   myapp1    "python app_1.py 20"   9 seconds ago   Exited (0) 8 seconds ago             jovial_yalow
```

Remove it:

```bash
docker rm jovial_yalow
```

---

## Removing the Image (Unbuilding the Docker Image)

After verifying no containers are using it, you can remove the image.

### List your images:

```bash
docker images
```

Example:

```
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
myapp1       latest    45ea0e173df5   23 minutes ago   123MB
```

### Remove the image:

```bash
docker rmi myapp1
```

Example Output:

```
Untagged: myapp1:latest
Deleted: sha256:45ea0e173df54aa96963a61f1a3b003ad8f0363f7c30d2237c0e2ca5721d6991
```

If Docker refuses removal due to stopped containers, first run:

```bash
docker rm $(docker ps -a -q)
```

Then remove the image again.
