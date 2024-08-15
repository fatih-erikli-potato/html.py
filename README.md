Example

```python
from html import make_html
print(
  make_html(
    "form",
    {"action": "/login", "method": "post"},
    ["label", "Username", ["input", {"type": "text"}]],
    ["label", "Password", ["input", {"type": "password"}]],
    ["input", {"type": "submit"}]
  ) 
)
```
