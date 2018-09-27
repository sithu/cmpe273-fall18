# Design Spartan Messenger :speech_balloon:

You will be building Spartan Messenger using GRPC in Python3.

## Features

__Level__ :star: 
- Design one-on-one conversations between users. :couple: [10 points]

Run Spartan Server
```sh
python3 server.py
Spartan server started on port 3000.
```

Alice's Terminal
```sh
> python3 client.py alice
[Spartan] Connected to Spartan Server at port 3000.
[Spartan] User list: bob,charlie,eve,foo,bar,baz,qux
[Spartan] Enter a user whom you want to chat with: __bob__
[Spartan] You are now ready to chat with bob.
[alice] > Hey Bob!
[alice] >
```

Bob's Terminal
```sh
> python3 client.py bob
[Spartan] Connected to Spartan Server.
[Spartan] User list: alice,charlie,eve,foo,bar,baz,qux
[Spartan] alice is requesting to chat with you. Enter 'yes' to accept or different user: __yes__
[Spartan] You are now ready to chat with alice.
[alice] Hey Bob!
[bob] >
```

Bob's Terminal
```sh
...
[bob] > Hi Alice!
[bob] >
```

Alice's Terminal
```sh
...
[bob] Hi Alice!
[alice] >
```


- Implements a LRU Cache to store recent messages in memory. :floppy_disk: [2 points]
- Limit the number of messages a user can send to an API within a time window e.g., 15 requests per second. NOTE: The rate limiting should work for a distributed setup. :vertical_traffic_light: [1 point]


__Level__ :star::star:
- Provide end-to-end message encryption using [AES from PyCrypto library](https://docs.python-guide.org/scenarios/crypto/#pycrypto). :key: [3 points] 
- Add [Decorator](https://www.python-course.eu/python3_decorators.php) for the LRU cache (E.g @lru_cache) and rate limition (E.g. @rate) from the level :star:. :cyclone: [1 point]

__Level__ :star::star::star:
- Extend your design to support group chats. :family: [3 points]

## App Config

- Use given [config.yaml](config.yaml) to load users for the Spartan messenger.



