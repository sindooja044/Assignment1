Question 1: By default, are Django signals executed synchronously or asynchronously?
By default, Django signals are executed synchronously. To demonstrate this, we can create a simple signal and a view that triggers it, then measure the time delay between the signal handler's execution and the view's response.


Question 2: Do Django signals run in the same thread as the caller?
Yes, Django signals run in the same thread as the caller by default. 


Question 3: By default, do Django signals run in the same database transaction as the caller?
Yes, Django signals run in the same database transaction as the caller by default. 
