# Notes for day 12

Today was all about Scope in python. While this is a concept I am quite familiar with, it was interesting to see that python does not have block scope, which is present in my main language of JavaScript. Python only has local and global scopes.

Interesting point about scope in python is that when we try to reassign values for global scoped variables in local scope, we actual create a new locally scoped variable with the same name. Of course storing state in global scope is a bad idea, but as a difference between languages it is quite interesting to know. To change a global variable we need to use the global keyword:

```python
variable = 1

def addOne():
  global variable += 1
```

Reading global scope is fine, but modifying it is a bad idea.
