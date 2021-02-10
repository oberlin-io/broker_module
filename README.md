# Broker
Broker class that tracks topics, message payloads, and consumers.
Consume method yields a generator of payloads per topic.

## Considerations
- Consumer namespace management.
- When to write queue to disk and when to read it into buffer.
And what happens to buffered queue, that has not been written to disk,
when program breaks.
