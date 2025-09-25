1️⃣ Components

Doubly Linked List (DLL)

Maintains order of usage (most recently used ↔ least recently used).

O(1) insertion/removal at both ends using head/tail pointers.

Allows moving a “current” node to the head in O(1) when accessed.

HashMap / Hash Table

Maps keys → nodes in the DLL.

Provides O(1) access to any cached item.

2️⃣ How It Works

Accessing an item:

Use the HashMap to find the node in O(1).

Move the node to the head of the DLL to mark it as recently used.

Adding a new item:

Insert node at the head of the DLL.

Add key → node entry in the HashMap.

If cache exceeds capacity, remove tail node (least recently used) and delete from HashMap.

3️⃣ Why This Increases Efficient Coverage

By maintaining head, tail, and quick access via HashMap, you now have:

O(1) access to any key (via HashMap)

O(1) updates to usage order (via DLL)

You effectively cover the entire cached structure with efficient access points, meaning you never need to traverse the DLL to find a node — every relevant operation is O(1).

4️⃣ Mental Model
HashMap: key → DLL node

DLL (most recent → least recent):
head → nodeA ↔ nodeB ↔ nodeC ↔ tail

Access nodeB via HashMap → move it to head → tail now is least recently used

Add nodeD → insert at head → remove tail if over capacity

5️⃣ Takeaway

DLL + HashMap = optimal caching structure:

Combines order tracking (DLL) + fast key lookup (HashMap).

Maximizes O(1) coverage of all “interesting” elements.

This pattern generalizes to many optimized data structures in competitive programming and systems design.
