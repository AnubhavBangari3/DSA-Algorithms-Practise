class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.front = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        # Rear insertion index circles back using modulo.
        rear_index = (self.front + self.count) % self.capacity
        self.queue[rear_index] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        # Move front to the next circular position.
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        rear_index = (self.front + self.count - 1) % self.capacity
        return self.queue[rear_index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


'''
Algorithm

1. Create a fixed-size array of size k.

2. Maintain three values:

   front:
   - Index of the first queue element.

   count:
   - Number of elements currently stored.

   capacity:
   - Maximum size of the queue.

3. For enQueue(value):

   a. If the queue is full:
      - Return False.

   b. Find the next rear position:

      rear_index =
      (front + count) % capacity

   c. Store the value at rear_index.

   d. Increase count.

   e. Return True.

4. For deQueue():

   a. If the queue is empty:
      - Return False.

   b. Move front to the next position:

      front =
      (front + 1) % capacity

   c. Decrease count.

   d. Return True.

5. For Front():

   a. If empty:
      - Return -1.

   b. Return queue[front].

6. For Rear():

   a. If empty:
      - Return -1.

   b. Calculate the rear index:

      rear_index =
      (front + count - 1) % capacity

   c. Return queue[rear_index].

7. Queue is empty when:

   count == 0

8. Queue is full when:

   count == capacity

Pattern:
Circular Queue / Ring Buffer

'''