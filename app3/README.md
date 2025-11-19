# App 3 — Flask Web Application (myapp3)

This app demonstrates how to run a **simple Flask web server in Docker**.  
It shows how containers host web applications, expose ports, and handle HTTP requests.

---

## 📦 What This App Does

| Feature | Description |
|--------|-------------|
| **Type** | Web application using Flask |
| **Input** | Browser request (HTTP GET) |
| **Output** | Renders a simple webpage |
| **Port Behavior** | Flask runs on **8080 inside the container**, mapped to **80 on your host** |

---

## 📁 Project Structure

```
app3/
├── Dockerfile
└── app_3.py
```

---

## 🐳 Building the Docker Image

Run inside the **app3** directory:

```bash
docker build -t myapp3 .
```

Example (shortened):

```
[3/4] RUN pip install Flask
[4/4] COPY . .
exporting to image
```

---

## ▶️ Running the Container

Map container port **8080** → host port **80**:

```bash
docker run -p 80:8080 myapp3
```

Example output:

```
* Serving Flask app 'app_3.py'
* Running on http://127.0.0.1:8080
* Running on http://172.17.0.2:8080
Press CTRL+C to quit
```

Pressing **CTRL + C** stops the running container.

---

## 🌐 Viewing the Webpage

Open:

👉 **http://localhost**

Example request logs:

```
172.17.0.1 - - "GET / HTTP/1.1" 200 -
172.17.0.1 - - "GET /favicon.ico HTTP/1.1" 404 -
```

---

## 🗑 Stopping & Removing Containers

### View all containers (including exited):

```bash
docker ps -a
```

Example:

```
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                     NAMES
882d231ba375   myapp3    "flask run --host=0.…"   3 minutes ago   Exited (0) 7 seconds ago   bold_brown
86f3a306243a   myapp3    "flask run --host=0.…"   6 minutes ago   Exited (0) 3 minutes ago   magical_hermann
```

### Remove all stopped containers:

```bash
docker rm $(docker ps -a -q)
```

Example:

```
882d231ba375
86f3a306243a
```

---

## 🧹 Removing the Docker Image (Canceling/Unbuilding the Image)

List images:

```bash
docker images
```

Example:

```
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
myapp3       latest    3a71dc83a5e6   7 minutes ago   134MB
```

Remove the image:

```bash
docker rmi myapp3
```

Example:

```
Untagged: myapp3:latest
Deleted: sha256:3a71dc83a5e6ac9ec29706a4e5c715a1a9990b4a97d7c01fb9528c4011de4309
```


