# Design Spartan Messenger :speech_balloon:

You will be building Spartan Messenger using GRPC in Python3.

## Level `:star:`
- Design one-on-one conversations between users. :couple:
- Implements a LRU Cache to store recent messages in memory. :floppy_disk:
- Limit the number of messages a user can send to an API within a time window e.g., 15 requests per second. NOTE: The rate limiting should work for a distributed setup. :vertical_traffic_light:


## Level `:star::star:`
- Provide end-to-end message encryption using [SHA256](https://docs.python.org/3/library/hashlib.html). :key: 
- Add [Decorator](https://www.python-course.eu/python3_decorators.php) for the LRU cache (E.g @lru_cache) and rate limition (E.g. @rate) from the level :star:. :cyclone:

## Level `:star::star::star:`
- Extend your design to support group chats. :family:

