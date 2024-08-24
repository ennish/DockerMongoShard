# Docker Mongdb Build

## Docker Image Pull

```bash
docker pull mongodb/mongodb-community-server:5.0.5-ubuntu2004
# -v mount data to local machine
docker run --name mongodb -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=pass mongodb/mongodb-community-server:5.0.5-ubuntu2004

docker run -u root --name mongodb -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=pass mongodb/mongodb-community-server:5.0.5-ubuntu2004
```
--storageEngine  wiredTiger -dbPath /data/db mongodb/
## Validation Installtion

```bash
    mongosh --port 27017
```

[Install on CentOS Guide](https://www.sjkjc.com/posts/install-mongodb-on-centos-7/)

If your application is running inside a container itself, you can run MongoDB as part of the same Docker network as your application using --network. With this method, you will connect to MongoDB on mongodb://mongodb:27017 from the other containerized applications in the network.

```bash
docker run --name mongodb -d --network mongodb mongodb/mongodb-community-server:$MONGODB_VERSION
```

To initialize your MongoDB with a root user, you can use the environment variables MONGO_INITDB_ROOT_USERNAME and MONGO_INITDB_ROOT_PASSWORD. These environment variables will create a user with root permissions with the specified user name and password.

```bash
docker run --name mongodb -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=pass mongodb/mongodb-community-server:$MONGODB_VERSION
```

---

## Manual Installation on CentOS7

### 1. Create "/etc/yum.repos.d/mongodb-org-7.0.repo" file

```bash
echo "[mongodb-org-7.0]
>name=MongoDB Repository
>baseurl=https://repo.mongodb.org/yum/redhat/7/>mongodb-org/7.0/x86_64/
>gpgcheck=1
>enabled=1
>gpgkey=https://pgp.mongodb.com/server-7.0.asc" > /etc/yum.repos.d/mongodb-org-7.0.repo

```

### 2. Install MongoDB

```bash
sudo yum install -y mongodb-org
```

### 3. Install Mongosh

```bash
sudo yum install -y mongodb-mongosh
# connect to local mongodb
mongosh
```
