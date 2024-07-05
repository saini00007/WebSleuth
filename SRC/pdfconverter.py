import subprocess
import pdfkit
import os
import sys
import time

# Get the URL from the command line argument
url = sys.argv[1]

# Check if output.txt exists
if not os.path.exists("output.txt"):
    print(" ")
    sys.exit(1)

# Convert the recorded session to HTML using aha
try:
    subprocess.run("aha --black < output.txt > output.html", shell=True)
except FileNotFoundError:
    sys.exit()

# Generate a unique filename based on the URL and current timestamp
timestamp = time.strftime("%Y%m%d-%H%M%S")
pdf_filename = f"{url.replace('/', '_')}_{timestamp}.pdf"

# Convert HTML to PDF using pdfkit
pdfkit.from_file("output.html", pdf_filename)

print("PDF created successfully:", pdf_filename)

# Remove intermediate files
os.remove("output.txt")
os.remove("output.html")
