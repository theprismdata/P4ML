var db = connect("mongodb://admin:paas4ml@localhost:27017/admin");
db = db.getSiblingDB('ML_DB');
db.createUser(
    {
        user: "paas4ml",
        pwd: "paas4ml",
        roles: [ { role: "readWrite", db: "ML_DB"} ]
    }
)