from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime

import os


def generate_challan(
        plate_number,
        owner_name,
        violation,
        fine_amount):

    folder = r"D:\Yams\College\Sem_7\CV\challans"

    os.makedirs(folder, exist_ok=True)

    pdf_path = os.path.join(
        folder,
        f"{plate_number}_challan.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = [

        Paragraph(
            "TRAFFIC VIOLATION CHALLAN",
            styles["Title"]
        ),

        Spacer(1, 20),

        Paragraph(
            f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        ),

        Spacer(1, 10),

        Paragraph(
            f"<b>Vehicle Number:</b> {plate_number}",
            styles["Normal"]
        ),

        Paragraph(
            f"<b>Owner Name:</b> {owner_name}",
            styles["Normal"]
        ),

        Paragraph(
            f"<b>Violation:</b> {violation}",
            styles["Normal"]
        ),

        Paragraph(
            f"<b>Fine Amount:</b> Rs.{fine_amount}",
            styles["Normal"]
        ),

        Spacer(1, 20),

        Paragraph(
            "Please pay the fine within the stipulated period.",
            styles["Normal"]
        )
    ]

    doc.build(content)

    return pdf_path