def strip_quote(value):
  return value.replace("\"", "&quot;")

def strip_lt_gt(value):
  return value.replace("<", "&lt;").replace(">", "&gt;")

def tag(name, *args):
  if not name in allowed_tags:
   raise Exception("Invalid tag %s. Only %s allowed." % (name, ', '.join(allowed_tags)))
  if args:
    if isinstance(args[0], dict):
      attrs = args[0]
      if len(args) > 1:
        content = args[1]
      else:
        content = None
    else:
      attrs = None
      content = args[0]
  else:
    attrs = None
    content = None
  self_closing = content is None
  html_output = "<"
  html_output += name
  if attrs:
    for k, v in attrs.items():
      if isinstance(v, bool):
        if v:
          html_output += " "
          html_output += k
      else:
        html_output += " "
        html_output += k
        html_output += "="
        if isinstance(v, str):
          v = strip_quote(v)
        elif isinstance(v, list):
          v = ' '.join(map(strip_quote, v))
        elif isinstance(v, dict):
          v = ';'.join("%s:%s" % (k, strip_quote(v) if isinstance(v, str) else v) for k, v in v.items())
        html_output += "\"%s\"" % v
  if self_closing:
    html_output += "/>"
  else:
    html_output += ">"
    html_output += content or ""
    html_output += "</"
    html_output += name
    html_output += ">"
  return html_output

def make_html_w_doctype(attrs, tag_definition):
  html = "<!doctype html>"
  html += "<html>"
  html += "<head>"
  if 'stylesheet_url' in attrs:
    html += '<link rel="stylesheet" type="text/css" href="%s" />' % strip_quote(attrs["stylesheet_url"])
  if 'favicon_url' in attrs:
    html += '<link rel="icon" href="%s" />' % strip_quote(attrs["favicon_url"])
  html += "<title>"
  html += strip_lt_gt(attrs.get("title"))
  html += "</title>"
  html += "</head>"
  html += "<body>"
  html += make_html(tag_definition)
  html += "</body>"
  html += "</html>"
  return html

allowed_tags = ["form", "div", "label", "input", "a", "img"]

allowed_attrs = ["src", "style", "class", "alt", "href", "action", "disabled",
                 "method", "type", "value", "width", "height"]

def make_html(array):
  tag_name = array[0]
  if len(array) > 1:
    if isinstance(array[1], dict):
      attrs = array[1]
      for key in attrs.keys():
        if key not in allowed_attrs:
          raise Exception("Invalid attribute %s. Only %s allowed." % (key, ', '.join(allowed_attrs)))
      content = array[2:]
    else:
      attrs = None
      content = array[1:]
  else:
    attrs = None
    content = None
  html_content = ""
  if content:
    for definition in content:
      if not definition and not isinstance(definition, int):
        continue
      elif isinstance(definition, list):
        html_content += make_html(definition)
      else:
        if isinstance(definition, int):
          html_content += str(definition)
        else:
          html_content += strip_lt_gt(definition)
  tag_args = [tag_name]
  if attrs:
    tag_args.append(attrs)
  if html_content:
    tag_args.append(html_content)
  return tag(*tag_args)

def form(*args): return ['form', *args]
def div(*args): return ['div', *args]
def img(*args): return ['img', *args]
def label(*args): return ['label', *args]
def input(*args): return ['input', *args]
def a(*args): return ['a', *args]