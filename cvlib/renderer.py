from docx import Document

from .models import CVData
from .styles import COLORS, FONT_SIZES, SPACING, MARGINS
from . import elements


def _setup_margins(doc: Document) -> None:
    for section in doc.sections:
        section.top_margin = MARGINS.TOP
        section.bottom_margin = MARGINS.BOTTOM
        section.left_margin = MARGINS.LEFT
        section.right_margin = MARGINS.RIGHT


def _render_header(doc: Document, data: CVData) -> None:
    elements.add_centered_text(
        doc, data.full_name, FONT_SIZES.TITLE, COLORS.BLUE, bold=True
    )
    elements.add_centered_text(
        doc, data.headline, FONT_SIZES.SUBTITLE, COLORS.GRAY
    )
    contact_line = (
        f"{data.contact.email} | {data.contact.linkedin} | "
        f"{data.contact.github} | {data.contact.location}"
    )
    elements.add_centered_text(
        doc, contact_line, FONT_SIZES.BODY, space_after=SPACING.CONTACT_AFTER
    )


def _render_summary(doc: Document, data: CVData) -> None:
    elements.add_section_heading(doc, data.labels.summary)
    elements.add_justified_paragraph(
        doc, data.summary, FONT_SIZES.BODY, SPACING.SECTION_BEFORE
    )


def _render_experience(doc: Document, data: CVData) -> None:
    elements.add_section_heading(doc, data.labels.experience)
    for job in data.jobs:
        elements.add_job_header(doc, job.title, job.company, job.dates)
        elements.add_bullet_list(doc, job.bullets)
        elements.add_tech_stack(doc, job.tech, data.labels.tech_stack)


def _render_education(doc: Document, data: CVData) -> None:
    elements.add_section_heading(doc, data.labels.education)
    for edu in data.education:
        elements.add_education_entry(
            doc, edu.degree, edu.school, edu.location, edu.dates, edu.gpa,
            coursework=edu.relevant_coursework,
            coursework_label=data.labels.coursework,
        )
    if data.education:
        doc.paragraphs[-1].paragraph_format.space_after = SPACING.GROUP_AFTER


def _render_projects(doc: Document, data: CVData) -> None:
    elements.add_section_heading(doc, data.labels.projects)
    for project in data.projects:
        elements.add_project_entry(
            doc,
            project.name,
            project.description,
            project.tech,
            project.link,
            tech_label=data.labels.tech,
            link_label=data.labels.link,
        )


def _render_research(doc: Document, data: CVData) -> None:
    if not data.research:
        return
    elements.add_section_heading(doc, data.labels.research)
    for research in data.research:
        elements.add_titled_entry(
            doc,
            research.title,
            research.description,
            research.date,
            research.link,
            data.labels.link,
        )


def _render_skills(doc: Document, data: CVData) -> None:
    elements.add_section_heading(doc, data.labels.skills)
    for skill in data.skills:
        elements.add_labeled_line(
            doc,
            f"{skill.category}: ",
            skill.skills,
            space_after=SPACING.PARAGRAPH_AFTER,
        )
    if data.languages:
        elements.add_labeled_line(
            doc,
            f"{data.labels.languages}: ",
            data.languages,
            space_before=SPACING.LANG_BEFORE,
        )


def _render_achievements(doc: Document, data: CVData) -> None:
    if not data.achievements:
        return
    elements.add_section_heading(doc, data.labels.achievements)
    for achievement in data.achievements:
        elements.add_titled_entry(
            doc, achievement.title, achievement.description, achievement.date
        )


def render(data: CVData) -> Document:
    doc = Document()
    _setup_margins(doc)
    _render_header(doc, data)
    _render_summary(doc, data)
    _render_experience(doc, data)
    _render_education(doc, data)
    _render_projects(doc, data)
    _render_research(doc, data)
    _render_skills(doc, data)
    _render_achievements(doc, data)
    return doc
