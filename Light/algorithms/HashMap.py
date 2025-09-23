"""
HashMap Implementation in Python
--------------------------------

🔎 What is a HashMap?
- A HashMap is a data structure that stores data in key-value pairs.
- Uses a hash function to map keys to indices in an underlying array.
- Provides average O(1) time complexity for insertion, search, and deletion.

⚡ Key Operations:
1. put(key, value)   -> insert or update a key-value pair.
2. get(key)          -> retrieve value for a key (or None if not found).
3. remove(key)       -> delete a key-value pair.
4. __contains__(key) -> check if a key exists.

📊 Complexity:
- Average case: O(1) for put/get/remove.
- Worst case: O(n), if many keys hash to the same index (collisions).

🎯 Use Cases:
- Fast lookup tables.
- Caching.
- Counting frequencies.
"""

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # Array of buckets (chaining)

    def _hash(self, key):
        """Hash function: returns index for a given key"""
        return hash(key) % self.size

    def put(self, key, value):
        """Insert or update a key-value pair"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update value if key exists
                return
        bucket.append((key, value))  # Insert new pair

    def get(self, key):
        """Retrieve value for a key, or None if not found"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Remove a key-value pair"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __contains__(self, key):
        """Check if a key exists"""
        return self.get(key) is not None

    def __repr__(self):
        return str(self.buckets)


# ================== EXAMPLE ==================

hm = HashMap()

hm.put("apple", 10)
hm.put("banana", 20)
hm.put("orange", 30)

print("HashMap:", hm)
print("Get apple:", hm.get("apple"))
print("Get banana:", hm.get("banana"))

hm.put("apple", 99)  # Update value
print("Updated apple:", hm.get("apple"))

hm.remove("banana")
print("After removing banana:", hm)

print("Does 'orange' exist?", "orange" in hm)
print("Does 'banana' exist?", "banana" in hm)
