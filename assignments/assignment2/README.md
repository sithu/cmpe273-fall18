## Requirements

In this assignment, you will be learning how different techniques of data sharding work by building a RESTful key-value datastore API and hashing client.

## I. RESTful Datastore API

In the first part of the assignment 2, you will be implementing a [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api) application which has the following two endpoints.

### Store Entry

Put a new entry into the datastore via HTTP POST. Unique key is a hash of

```hash(Year:Cause Name:State) => xxxx```

__Request__

```
curl http://localhost:5000/api/v1/entries -X POST -d '{"xxxx":"2016,All Causes,All causes,Alabama,52466,920.40
"}' -H "Content-Type: application/json"
```

__Response__

```
201 Created
```

### Retrieve All Entries

Retrieve existing entries via HTTP GET.

__Request__

```
curl http://localhost:5000/api/v1/entries
```

__Response__

```
200 OK
.
.
```

```
{
    "num_entries" : 3,
    "entries" : 
    [
        { "key": "value" },
        { "key": "value" },
        { "key": "value" }
    ]
}
```

Last, add the Flask server port as a command-line argument so that you can run mulitple servers on different ports.

Example:

```
python3 api.py 5000
python3 api.py 5001
python3 api.py 5002
python3 api.py 5003
```

## II. Hashed Clients

In the part II, you will be writing CSV file parser to read each column from the input csv file.
Then, feed the data into:

1. Consistent hashing client
2. Rendezvous (HRW) hashing client

in where you will be uploading data into the RESTful datastore you built in the previous section.
In both clients, you will be sharding via HTTP POST to http://localhost:5000/api/v1/entries data into all four instances: 

```python
servers = ['http://localhost:5000','http://localhost:5001','http://localhost:5002','http://localhost:5003']
```

Once you have sharded all data into the cluster, you can finally print out the uploaded data from:
http://localhost:5000/api/v1/entries.


Example:

```
python3 consistent_hash.py causes-of-death.csv
Uploaded all 10296 entries.
Verifying the data.
GET http://localhost:5000
{
    ....
}

GET http://localhost:5001
{
    ...
}

GET http://localhost:5002
{
    ...
}

GET http://localhost:5003
{
    ...
}

python3 hrw_hash.py causes-of-death.csv
...
```

You might want to implement CSV parser in a separate file called csv_paser.py so that both clients are shared the implementation.
