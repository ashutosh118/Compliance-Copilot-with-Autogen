from fpdf import FPDF

text = """
Data Usage and Privacy Policy

1. Introduction
This document outlines the data handling practices of XYZ Corp with regard to user data collection, processing, and usage.

2. Data Collection
We collect user data such as names, emails, and browsing behavior through cookies and web forms. 
User consent is assumed when using the site.

3. Data Storage
All data is stored indefinitely in our internal systems.

4. Data Sharing
We may share data with third-party partners for analytics, advertising, or other purposes. 
We are not responsible for how third parties handle your data.

5. User Rights
Users may request deletion of their data by contacting us, though we cannot guarantee a full deletion in all cases.

6. Security Measures
Basic firewall protections are in place. We do not encrypt data at rest.

7. Updates
We may update this policy at any time without notifying users directly.

8. Contact
For concerns, email privacy@xyzcorp.example.
"""

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

for line in text.strip().split('\n'):
    pdf.multi_cell(0, 10, line)

pdf.output("dummy_policy.pdf")
