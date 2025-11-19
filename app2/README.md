# Docker Tutorial: Running an Interactive Python App (myapp2)

This guide demonstrates how to:

- Build the Docker image  
- Run an interactive Python program  
- See what happens when you run it **without -it**  
- View and remove containers  
- Remove the Docker image  
- Includes real example outputs  

This assumes Docker Desktop is running.

---

## 📁 Project Structure

```
Docker_Tutorial/
└── app2/
    ├── Dockerfile
    └── app_2.py
```

---

## 🐳 Building the Image

Run inside **app2**:

```bash
docker build -t myapp2 .
```

### ✔ Example Output

```
[+] Building 1.4s (9/9) FINISHED
 => load build definition
 => load metadata for python:3.9-slim-bullseye
 => WORKDIR /app2
 => COPY . .
 => exporting to image

Successfully tagged myapp2:latest
```

---

## ▶️ Running myapp2 in Interactive Mode (-it)

This application prompts the user for input, so you must use `-it`.

```bash
docker run -it myapp2
```

### ✔ Example Run #1

```
Input two numbers to add together
Enter the first number:
1
Enter the second number:
2
1.0 + 2.0 = 3.0
```

### ✔ Example Run #2

```
Input two numbers to add together
Enter the first number:
5
Enter the second number:
10
5.0 + 10.0 = 15.0
```

---

## ❗ Running Without -it (Non-Interactive Mode)

This is an important demonstration.

```bash
docker run myapp2
```

### ❌ Output

```
Input two numbers to add together
Enter the first number:
Traceback (most recent call last):
  ...
EOFError: EOF when reading a line
```

### Why?

- The program is waiting for user input  
- Without `-it`, the container cannot accept user input  
- Python throws an EOFError  

---

## 📋 Viewing Containers

### Show running containers:

```bash
docker ps
```

### Show all containers (running or exited):

```bash
docker ps -a
```

Example:

```
CONTAINER ID   IMAGE     COMMAND             CREATED              STATUS                      NAMES
7e06c890585c   myapp2    "python app_2.py"   20 seconds ago       Exited (0) 18 seconds ago   gracious_galois
278a2784d5f8   myapp2    "python app_2.py"   1 minute ago         Exited (1) 1 minute ago     trusting_darwin
1d5440d805de   myapp2    "python app_2.py"   1 minute ago         Exited (0) 1 minute ago     suspicious_euclid
83274ea3fcbd   myapp2    "python app_2.py"   1 minute ago         Exited (0) 1 minute ago     unruffled_engelbart
```

The container with **Exited (1)** is the non-interactive failure example.

---

## 🗑 Removing All Stopped Containers

```bash
docker rm $(docker ps -a -q)
```

Example output:

```
7e06c890585c
278a2784d5f8
1d5440d805de
83274ea3fcbd
```

---

## 🧹 Removing the Docker Image (Unbuilding myapp2)

Check images:

```bash
docker images
```

Output:

```
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
myapp2       latest    7c34411eb1be   About a minute ago   123MB
```

Remove the image:

```bash
docker rmi myapp2
```

Example Output:

```
Untagged: myapp2:latest
Deleted: sha256:7c34411eb1bed591130df9518747ee4753aaf8c4b836f8a9f1b71e3b40586b48
```

---
