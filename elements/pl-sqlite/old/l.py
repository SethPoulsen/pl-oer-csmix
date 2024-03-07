from lxml import html

# Sample HTML fragment data
html_fragment_data = """
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

sandbox_html = "<div>THIS IS REPLACED SANDBOX</div>"
sandbox = html.fromstring(sandbox_html)

print(html_fragment_data)

# Parse the HTML fragment
fragment = html.fragment_fromstring(html_fragment_data)

# Iterate over elements in the fragment
for element in fragment:

    if (element.tag == "sandbox"):
        sandbox.tail = element.tail
        element.getparent().replace(element, sandbox)

# Convert the modified fragment back to a string
modified_html_fragment = html.tostring(fragment, method="html", encoding="utf-8", pretty_print=True)

print(modified_html_fragment.decode("utf-8"))
