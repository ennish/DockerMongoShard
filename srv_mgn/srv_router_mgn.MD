ps aux|grep mongos

kill <mongos pid>

mongos --auth --configdb config_rs/configsvr1:27017,config_rs/configsvr2:27017,config_rs/configsvr3:27017 --port 27017
