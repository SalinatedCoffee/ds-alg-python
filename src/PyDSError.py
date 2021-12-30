class QueueError():
    class EmptyQueue(Exception):
        pass

    class MigrateSize(Exception):
        pass