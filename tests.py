from html import make_html, div, input, label, form

assert make_html(div(1)) == "<div>1</div>"
assert make_html(div(1, div(2))) == "<div>1<div>2</div></div>"
assert make_html(div({"style": {"order": 2}})) == '<div style="order:2"/>'
assert make_html(div({"class": "a"})) == '<div class="a"/>'
assert make_html(div({"class": ["a", "b"]})) == '<div class="a b"/>'
assert make_html(input({"disabled": True})) == '<input disabled/>'
assert make_html(input({"disabled": False})) == '<input/>'
assert make_html(label({"style": {"background": "black", "color": "white"}}, input())) == \
  '<label style="background:black;color:white"><input/></label>'
assert make_html(
  form(
    {"action": "/login", "method": "post"},
    label("Username", input({"type": "text"})),
    label("Password", input({"type": "text"})),
    input({"type": "submit"})
    )
) == \
  '<form action="/login" method="post">' \
  '<label>Username<input type="text"/></label>' \
  '<label>Password<input type="text"/></label>' \
  '<input type="submit"/></form>'
