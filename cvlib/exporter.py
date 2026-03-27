from pathlib import Path
from docx import Document


def save_docx(doc: Document, path: str) -> str:
    doc.save(path)
    return path


def save_pdf(docx_path: str, pdf_path: str = None) -> str | None:
    if pdf_path is None:
        pdf_path = str(Path(docx_path).with_suffix(".pdf"))
    try:
        from docx2pdf import convert
        convert(docx_path, pdf_path)
        return pdf_path
    except ImportError:
        print("Para generar PDF instala: pip install docx2pdf")
        return None
    except Exception as e:
        print(f"Error al convertir a PDF: {e}")
        print("Asegurate de tener Microsoft Word instalado (docx2pdf lo necesita en Windows)")
        return None
