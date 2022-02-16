# Linked List

*Stack is a linear data structure that stores items in a **Last-In/First-Out** manner*

In stack, a new element is added at one end and an element is removed from that end only.

Stack in Python can be implemented using the following ways: 

- list *(It can run into speed issues as it grows)*  
    .append() -- to add an element <br/>
    .pop() -- to remove an element
- Collections.deque <br/>
    deque provides an **O(1)** time complesity for append and pop operation. However, list which provides O(n) time complexity <br/>
    *still use append() and pop()*
- queue.LifoQueue <br/>
    Queue module also has a **LIFO Queue**, which is basically a Stack<br/>
    *use put() and get() to add or remove elements*

This is a solution summary of what I did for topic Linked List

Question ID | Question Name | Difficulty | Acceptance | Status | Runtime | Memory | Updated Runtime | Updated Memory
:---------: | :-----------: | :--------: | :--------: | :----: | :-----: | :----: | :-------------: | :------------:
1 | [Valid Parentheses] | <font color = green> Easy </font> | 40.6% | ✅ | 36ms | 14MB | | |