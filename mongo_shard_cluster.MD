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

## Login router server and add shard in

```bash

sh.addShard("shard1_rs/shardsvr1_1:27017","shard1_rs/shardsvr1_2:27017","shard1_rs/shardsvr1_3:27017")

sh.addShard("shard2_rs/shardsvr2_1:27017","shard2_rs/shardsvr2_2:27017","shard2_rs/shardsvr2_3:27017")
```

## Create database and enable sharding

```bash

use "database"

# Shard your collection, this command will automatically enable sharding if your using versions Mongo 6.0 or later.
sh.enableSharding("database")

sh.shardCollection("database.collection", {"key":hashed or ranged key})
# e.g.
sh.shardCollection('mydb.mycol', {'_id':'hashed'})
```

## MongoDB提供了两种分片收集策略

* 散列分片使用单个字段的 哈希索引作为 分片键，以跨分片群集对数据进行分区

```bash
sh.shardCollection("<database>.<collection>", { <shard key field> : "hashed" } )
```

* 基于范围的分片可以使用多个字段作为分片键，并将数据划分为由分片键值确定的连续范围。具体参考[官方文档](https://mongodb.net.cn/manual/core/ranged-sharding/#sharding-ranged)。

```bash
sh.shardCollection("<database>.<collection>", { <shard key field> : 1, ... } )
```