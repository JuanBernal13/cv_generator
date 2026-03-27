from .models import CVData, ContactInfo, Job, Education, Project, SkillCategory
from .renderer import render
from .exporter import save_docx, save_pdf


def generate_cv(data: CVData, docx_path: str = "CV.docx", pdf: bool = True) -> None:
    doc = render(data)
    save_docx(doc, docx_path)
    if pdf:
        save_pdf(docx_path)
