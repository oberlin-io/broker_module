import atexit
import json
import os


class Broker():
    """Broker class that tracks topics and consumers.
    Consume method yields a generator."""

    def __init__(self):
        
        # Each message in queue has [0] topic, [1] payload, [2] consumers who've read
        self.queue_filepath = 'queue.json'
        
        if os.path.exists(self.queue_filepath):
            with open(self.queue_filepath) as f:
                self.queue = json.load(f)

        else:
            self.queue = list()


    def queue_to_disk(self):
        
        with open(self.queue_filepath, 'w') as f:
            json.dump(self.queue, f, indent=2)
    

    def publish(self, topic, payload):
        
        # The consumers who've read is an empty list
        self.queue.append([topic, payload, list()])


    def consume(self, topic, consumer):
    
        for message in self.queue:
            if topic == message[0] and consumer not in message[2]:
                
                # Add consumer to has-read list
                index = self.queue.index(message)
                self.queue[index][2].append(consumer)

                yield message[1] # The payload



