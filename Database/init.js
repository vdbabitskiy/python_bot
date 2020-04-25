db.createCollection('russian_covid_info')
db.createCollection('world_covid_info')
db.createCollection('covid_users')


db.getCollection('russian_covid_info').createIndex(
{
    "_id": 1.0
},
{
    "background": true,
    "unique": true
})

db.getCollection('world_covid_info').createIndex(
{
    "_id": 1.0
},
{
    "background": true,
    "unique": true
})

db.getCollection('covid_users').createIndex(
{
    "_id": 1.0
},
{
    "background": true,
    "unique": true
})
