# Requirements

You will be implementing a Practical Byzantine Fault Tolerance (PBFT) prototype in Python3.

- For the node-2-node communication, you can use either UDP or [ZeroMQ](http://zguide.zeromq.org/py:all) protocol.
- Once a node receives a message, it will print out PBFT protocol messages to console while storing data into a local key-value store called [PickleDB](https://pythonhosted.org/pickleDB/).
- At the end of every DB change, you will print out all key-value entries to the console.
- You need to write a small client to send data and the client will send the following messages to the PBFT cluster.
- The client will also print out the reply messages to the console along with node id. before sending the another one. You can hardcode the below messages in the client and can loop through them to send to the cluster.

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

- Run your implementation in 4 nodes and capture the outputs from all nodes.


```
# Run the server nodes.
python3 pbft_server.py 3000
python3 pbft_server.py 3001
python3 pbft_server.py 3002
python3 pbft_server.py 3003
```

```
# Run the client.
python3 pbft_client.py 3000
```

> Client selects 3000 node as primary and sends data to the primary node.

- Finally, run the same steps except the last _3003_ node. 
