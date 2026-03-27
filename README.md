# CV Generator Library

A modular Python library for generating professional CVs in DOCX and PDF format.

Built with `python-docx`, the library separates data, styling, and rendering into independent modules, making it easy to maintain multiple CV versions from a single codebase.

## Installation

```bash
pip install python-docx docx2pdf
```

> `docx2pdf` requires Microsoft Word installed on Windows or LibreOffice on macOS.

## Quick Start

```python
from cvlib import generate_cv, CVData, ContactInfo, Job, Education, Project, SkillCategory

data = CVData(
    full_name="JOHN DOE",
    headline="Software Engineer | Full Stack Developer",
    contact=ContactInfo(
        email="john.doe@email.com",
        linkedin="linkedin.com/in/johndoe",
        github="github.com/johndoe",
        location="New York, USA",
    ),
    summary="Experienced software engineer with 5+ years building scalable web applications.",
    jobs=[
        Job(
            title="Senior Software Engineer",
            company="Tech Corp",
            dates="Jan 2022 - Present",
            bullets=[
                "Led development of microservices architecture serving 1M+ users.",
                "Reduced API response time by 40% through caching and query optimization.",
            ],
            tech="Python, FastAPI, PostgreSQL, Docker, AWS",
        ),
    ],
    education=[
        Education(
            degree="B.S. Computer Science",
            school="MIT",
            location="Cambridge, MA",
            dates="2014 - 2018",
            gpa="3.8/4.0",
            relevant_coursework=["Algorithms", "Distributed Systems", "Machine Learning"],
        ),
    ],
    projects=[
        Project(
            name="Open Source Dashboard",
            description="Real-time analytics dashboard with WebSocket streaming",
            tech="React, Node.js, Redis",
            link="https://github.com/johndoe/dashboard",
        ),
    ],
    skills=[
        SkillCategory("Backend", "Python, Java, Node.js, FastAPI, Spring Boot"),
        SkillCategory("Frontend", "React, TypeScript, Next.js"),
        SkillCategory("Cloud", "AWS, Docker, Kubernetes, Terraform"),
    ],
    languages="English (Native) | Spanish (B2)",
)

generate_cv(data, "John_Doe_CV.docx", pdf=True)
```

## Architecture

```
cvlib/
  __init__.py     Public API: generate_cv(), model re-exports
  models.py       Typed dataclasses for all CV sections
  styles.py       Centralized colors, fonts, spacing, margins
  elements.py     Reusable document-building primitives
  renderer.py     Orchestrates full document from CVData
  exporter.py     DOCX save + PDF conversion
```

### models.py

Defines the data structure for a CV using Python dataclasses:

| Model | Fields | Description |
|---|---|---|
| `CVData` | `full_name`, `headline`, `contact`, `summary`, `jobs`, `education`, `projects`, `skills`, `languages` | Root model that holds all CV content |
| `ContactInfo` | `email`, `linkedin`, `github`, `location` | Contact details rendered in the header |
| `Job` | `title`, `company`, `dates`, `bullets`, `tech` | A work experience entry with bullet points and tech stack |
| `Education` | `degree`, `school`, `location`, `dates`, `gpa`, `relevant_coursework` | An education entry with optional GPA and coursework list |
| `Project` | `name`, `description`, `tech`, `link` | A project entry with optional clickable hyperlink |
| `SkillCategory` | `category`, `skills` | A labeled group of skills |

### styles.py

Frozen dataclass constants for consistent formatting:

- `COLORS` - Blue, gray, black palette with hex values
- `FONT_SIZES` - Title (18pt), subtitle (11pt), heading (12pt), body (10pt), small (9pt)
- `SPACING` - Section, item, block, and paragraph spacing
- `MARGINS` - Page margins (0.6 inches all sides)

### elements.py

Single-purpose functions that wrap `python-docx` mechanics:

| Function | Purpose |
|---|---|
| `add_centered_text()` | Centered paragraph with configurable size, color, bold |
| `add_section_heading()` | Blue heading with bottom border line |
| `add_justified_paragraph()` | Justified text block (used for summary) |
| `add_bullet_list()` | Indented bullet point list |
| `add_labeled_line()` | Bold label + value on same line |
| `add_job_header()` | Job title, company, and italic dates |
| `add_tech_stack()` | Italic tech stack line |
| `add_education_entry()` | Degree, school, dates, GPA, and optional coursework |
| `add_project_entry()` | Project name with optional hyperlink + description |

### renderer.py

`render(data: CVData) -> Document` builds the full document by calling element functions in order:

1. Page margins setup
2. Header (name, headline, contact)
3. Professional summary
4. Professional experience
5. Education
6. Key projects & research
7. Technical expertise + languages

### exporter.py

- `save_docx(doc, path)` - Saves the Document object to a `.docx` file
- `save_pdf(docx_path, pdf_path)` - Converts DOCX to PDF using `docx2pdf` (graceful fallback if Word is unavailable)

## Multiple CV Versions

Create different files for different targets using the same library:

```
generate_cv_swe.py      Software Engineer focused
generate_cv_ai.py       AI Engineer focused
generate_cv_short.py    1-page condensed version
```

Each file defines its own `CVData` with tailored content, bullets, and keywords, then calls `generate_cv()`.

## License

MIT
