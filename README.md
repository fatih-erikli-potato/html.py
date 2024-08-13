Example

```python
from html import html, form, input
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
