from reportlab.pdfgen import canvas

def save_pdf_report(data, filename="report.pdf"):
    c = canvas.Canvas(filename)
    y = 800
    for section, content in data.items():
        c.drawString(50, y, f"[{section}]")
        y -= 20
        for key, value in content.items():
            c.drawString(60, y, f"{key}: {value}")
            y -= 20
            if y < 100:
                c.showPage()
                y = 800
        y -= 10
    c.save()
