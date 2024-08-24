# Mongo Shard Cluster

## Starup Config Server

```bash
docker-compose -f config_server/docker-compose.yaml up -d
```

```bash
mongosh
#initiate config server
rs.initiate(
  {
    _id: "config_rs",
    configsvr: true,
    members: [
      { _id : 0, host : "configsvr1:27017" },
      { _id : 1, host : "configsvr2:27017" },
      { _id : 2, host : "configsvr3:27017" }
    ]
  }
)

## Startup Shard Server 1&2

```bash
docker-compose -f shard_server_1/docker-compose.yaml up -d 
docker-compose -f shard_server_2/docker-compose.yaml up -d
```

Once the container start up,  pass the instances as members to form a replica set:

```bash
#login into shard server 1
mongosh

#initiate shard1_rs
rs.initiate(
  {
    _id: "shard1_rs",
    members: [
      { _id : 0, host : "shardsvr1_1:27017" },
      { _id : 1, host : "shardsvr1_2:27017" },
      { _id : 2, host : "shardsvr1_3:27017" }
    ]
  }
)

```

```bash
#login in to shard server 2
mongosh

rs.initiate(
  {
    _id: "shard2_rs",
    members: [
      { _id : 0, host : "shardsvr2_1:27017" },
      { _id : 1, host : "shardsvr2_2:27017" },
      { _id : 2, host : "shardsvr2_3:27017" }
    ]
  }
)
```

## Startup Router Server

```bash
docker-compose -f mongo_router/docker-compose.yaml up -d
```

Login router server and add shard in

```bash

sh.addShard("shard1_rs/shardsvr1_1:27017","shard1_rs/shardsvr1_2:27017","shard1_rs/shardsvr1_3:27017")

sh.addShard("shard2_rs/shardsvr2_1:27017","shard2_rs/shardsvr2_2:27017","shard2_rs/shardsvr2_3:27017")

```
<!-- sh.addShard("shard-1-replica-set/shard-1-node-a:27017", "shard-1-replica-set/shard-1-node-b:27017", "shard-1-replica-set/shard-1-node-c:27017")

sh.addShard("shard-2-replica-set/shard-2-node-a:27017", "shard-2-replica-set/shard-2-node-b:27017", "shard-2-replica-set/shard-2-node-c:27017")

sh.addShard("shard-3-replica-set/shard-3-node-a:27017", "shard-3-replica-set/shard-3-node-b:27017", "shard-3-replica-set/shard-3-node-c:27017") -->
