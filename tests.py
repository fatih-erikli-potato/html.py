from html import make_html, make_html_w_doctype

assert make_html("div") == "<div/>"
assert make_html("div", {"class": "a"}) == '<div class="a"/>'
assert make_html("div", {"class": ["a", "b"]}) == '<div class="a b"/>'
assert make_html("input", {"disabled": True}) == '<input disabled/>'
assert make_html("input", {"disabled": False}) == '<input/>'
assert make_html("label", {"style": {"background": "black", "color": "white"}}, ["input"]) == \
  '<label style="background:black;color:white"><input/></label>'
assert make_html(
  "form",
  {"action": "/login", "method": "post"},
  ["label", "Username", ["input", {"type": "text"}]],
  ["label", "Password", ["input", {"type": "text"}]],
  ["input", {"type": "submit"}]
) == \
  '<form action="/login" method="post">' \
  '<label>Username<input type="text"/></label>' \
  '<label>Password<input type="text"/></label>' \
  '<input type="submit"/></form>'
