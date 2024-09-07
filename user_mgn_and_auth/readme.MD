# Database Management

## Add user

```bash

db.createUser(
  {
    user: "enn",
    pwd:  passwordPrompt(),   // or cleartext password
    roles: [ { role: "readWrite", db: "mydb" },
             { role: "read", db: "reporting" } ]
  }
)

```
