def html(*tags):
  return "<!doctype html><html>%s</html>" % "\n".join(tags)

def strip_quote(value):
  return value.replace("\"", "&quot;")

def strip_lt_gt(value):
  return value.replace("<", "&lt;").replace(">", "&gt;");

def tag(name, *args):
  if args:
    if isinstance(args[0], dict):
      attrs = args[0]
      children = args[1:]
      self_closing = len(children) == 0
    else:
      attrs = None
      children = args
      self_closing = False
  else:
    attrs = None
    children = None
    self_closing = True
  html_output = "<"
  html_output += name
  if attrs:
    for k, v in attrs.items():
      if html_output.endswith(name):
        html_output += " "
      html_output += k
      html_output += "="
      html_output += "\"%s\"" % (strip_quote(v) if isinstance(v, str) else v)
  if self_closing:
    html_output += "/>"
  else:
    html_output += ">"
    html_output += "\n".join(filter(bool, children))
    html_output += "</"
    html_output += name
    html_output += ">"
  return html_output

def head(*args): return tag('head', *args)
def body(*args): return tag('body', *args)
def title(*args): return tag('title', *args)
def link(*args): return tag('link', *args)
def a(*args): return tag('a', *args)
def img(*args): return tag('img', *args)
def form(*args): return tag('form', *args)
def input(*args): return tag('input', *args)
def label(*args): return tag('label', *args)
def body(*args): return tag('body', *args)
def div(*args): return tag('div', *args)
def style(*args): return tag('style', *args)
def svg(*args): return tag('svg', *args)
def polygon(*args): return tag('polygon', *args)
