# Basic logging for now
# Change to proper unit tests in the future
from dscol.linked import NodeSingle

# init
try:
    s1 = NodeSingle()
except Exception as e:
    print(e)

# .next default as None
s1 = NodeSingle(5)
s2 = NodeSingle(2, None)
s3 = NodeSingle(1, s1)

print(f"{s1}")
print(f"{s2}")
print(f"{s3}")

print(repr(s3))

print(s3.val)
print(s3.next)
s3.val = 0
s3.next = s2
print(f"{s3}")
