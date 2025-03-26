import os

html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Generated Page</title>
</head>
<body>
    <h1>Hello, GitHub Pages!</h1>
    <p>This page was generated automatically.</p>
</body>
</html>
"""

# Ensure the output directory exists
os.makedirs("public", exist_ok=True)

# Write the HTML content to a file
with open("public/index.html", "w") as f:
    f.write(html_content)

print("HTML file generated successfully!")