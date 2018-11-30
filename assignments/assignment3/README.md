# Requirements

You will be implementing a Federated Byzantine Agreement (FBA) prototype in Python3. First, read [this article](https://medium.com/a-stellar-journey/on-worldwide-consensus-359e9eb3e949) and [the Stellar white paper](https://www.stellar.org/papers/stellar-consensus-protocol.pdf) before proceeding the assignment.

## Part I

In the part I, you will be building a key-value datastore service that persists user wallet info: username and balance. If a user does not exist in DB yet, the service will create a new entry with a given value. Otherwise, the user wallet will be updated with the new amount.

- For the node-2-node communication, you must use [UDP](https://twistedmatrix.com/documents/9.0.0/core/howto/udp.html) protocol.
- Once a node receives a message, it will print out FBA protocol messages to console while storing data into a local key-value store called [PickleDB](https://pythonhosted.org/pickleDB/).
- You must name PickleDB file to assignment3_{port_num}.db . 
- At the end of every DB change, you will print out all key-value entries to the console.
- You need to write a small client to send data and the client will send the following messages to the FBA cluster.
- The client will also print out the reply messages to the console along with node id. before sending the another one. You can hardcode the below messages in the client and can loop through them to send to the cluster.
- Run your implementation in 4 nodes and capture the outputs from all nodes.


```
# Run the server nodes.
python3 fba_server.py 3000
python3 fba_server.py 3001
python3 fba_server.py 3002
python3 fba_server.py 3003
```

On the client side, you will be sending the following messages to a server in order:

```
Format: {key} => {value}
Messages in order:
1. foo:$10
2. bar:$30
3. foo:$20
4. bar:$20
5. foo:$30
6. bar:$10
```

For the client to server communication, you need to use the same UDP protocol for accepting requests from the client.

```
# Run the client.
python3 fba_client.py 3000
```

> Client selects 3000 node as primary and sends data to the primary node.

- Finally, run the same steps except the last _3003_ node. 

## Part II

Now, you will be adding FBA to the server so that the data can be replicated across all nodes. You can use any part of this [FBA implementation](https://github.com/spikeekips/simple-fba) to enable data replication via FBA.

Once you run the client to load the data to the cluster, you can check each DB file and see they have the same content.

```
cat assignment3_3000.db
cat assignment3_3001.db
cat assignment3_3002.db
cat assignment3_3003.db
```
