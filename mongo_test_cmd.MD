# Code snips

## Login and view things

```bash

# most useful ;)
help

show dbs

show tables

use <some_db>

#query all from a table 
#db.<table_name>.find()
db.users.find()

```

Operation for Shard

```bash
# find shard members
db.test.find()

```

connect with authenticted user

```bash

mongosh "mongodb://localhost:27017" --username user

```
