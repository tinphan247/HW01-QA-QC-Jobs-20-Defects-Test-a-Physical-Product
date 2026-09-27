import markdown
import os
import subprocess

def convert_md_to_pdf():
    with open("REPORT.md", "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'nl2br', 'sane_lists'])

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>HW01 - Phan Trung Tin - 23120372</title>
<style>
    @page {{
        size: A4;
        margin: 20mm 15mm 20mm 15mm;
        @bottom-right {{
            content: counter(page);
        }}
    }}
    body {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        font-size: 13px;
        line-height: 1.6;
        color: #24292e;
        padding: 0;
        margin: 0;
    }}
    h1 {{
        font-size: 22px;
        border-bottom: 2px solid #1f497d;
        padding-bottom: 8px;
        color: #1f497d;
        margin-top: 24px;
        page-break-after: avoid;
    }}
    h2 {{
        font-size: 17px;
        border-bottom: 1px solid #eaecef;
        padding-bottom: 6px;
        color: #2b579a;
        margin-top: 20px;
        page-break-after: avoid;
    }}
    h3 {{
        font-size: 14px;
        color: #333;
        margin-top: 16px;
        page-break-after: avoid;
    }}
    h4 {{
        font-size: 13px;
        color: #444;
        margin-top: 12px;
        page-break-after: avoid;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 14px 0;
        page-break-inside: avoid;
        font-size: 11px;
    }}
    th, td {{
        border: 1px solid #d0d7de;
        padding: 6px 8px;
        text-align: left;
        vertical-align: top;
    }}
    th {{
        background-color: #f2f5f9;
        font-weight: 600;
        color: #1f497d;
    }}
    tr:nth-child(even) {{
        background-color: #f8fafc;
    }}
    blockquote {{
        border-left: 4px solid #1f497d;
        padding: 4px 12px;
        color: #4a5568;
        background-color: #f7fafc;
        margin: 12px 0;
    }}
    code {{
        font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
        font-size: 11px;
        background-color: #f3f4f6;
        padding: 2px 4px;
        border-radius: 3px;
    }}
    pre {{
        background-color: #f6f8fa;
        padding: 10px;
        border-radius: 6px;
        overflow-x: auto;
        font-size: 11px;
        border: 1px solid #e1e4e8;
        page-break-inside: avoid;
    }}
    pre code {{
        background: none;
        padding: 0;
    }}
    img {{
        max-width: 85%;
        height: auto;
        display: block;
        margin: 15px auto;
        border: 1px solid #d0d7de;
        border-radius: 4px;
    }}
    hr {{
        border: 0;
        height: 1px;
        background: #e1e4e8;
        margin: 20px 0;
    }}
    ul, ol {{
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 4px;
    }}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""

    with open("REPORT.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("REPORT.html written.")

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if os.path.exists(edge_path):
        cwd = os.path.abspath(".")
        html_file = os.path.join(cwd, "REPORT.html")
        pdf_file = os.path.join(cwd, "REPORT.pdf")
        cmd = [
            edge_path,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_file}",
            html_file
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
            print(f"REPORT.pdf generated successfully! Size: {os.path.getsize(pdf_file)} bytes")
        else:
            print("Edge print failed:", res.stderr)
    else:
        print("Edge binary not found.")

if __name__ == "__main__":
    convert_md_to_pdf()
