#from lxml import html
import lxml.html

# Sample HTML fragment data
element_html = """
<pl-sqlite>
   Before QQ
   <quietquery>
      CREATE TABLE t(a);
   </quietquery>
   After QQ
   Before Sandbox
   <sandbox>
      Sandbox stuff here
   </sandbox>
   After Sandbox
   <p>This is unaffected.</p>
</pl-sqlite>
"""

element = lxml.html.fragment_fromstring(element_html)
for child in element:
   if child.tag == "sandbox":
      sandbox = lxml.html.fromstring("<div>THIS IS REPLACED SANDBOX\n\n\n</div>")
      sandbox.tail = child.tail
      child.getparent().replace(child, sandbox)

#modified_html = lxml.html.tostring(element, method="html", encoding="utf-8")
#print(modified_html.decode("utf-8"))

print(content)
