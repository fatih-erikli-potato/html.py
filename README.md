Example

```python
from html import html, form, input
print(
  html(
    form(
      {"action": "/", "method": "post"},
      input({"type": "text", "name": "text"}),
      input({"type": "submit", "value": "ko"}),
      input({"type": "reset", "value": "koma"}),
    )
  )
)
```
