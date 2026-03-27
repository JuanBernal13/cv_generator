from dataclasses import dataclass, field


@dataclass
class ContactInfo:
    email: str
    linkedin: str
    github: str
    location: str


@dataclass
class Job:
    title: str
    company: str
    dates: str
    bullets: list[str]
    tech: str


@dataclass
class Education:
    degree: str
    school: str
    location: str
    dates: str
    gpa: str
    relevant_coursework: list[str] = field(default_factory=list)


@dataclass
class Project:
    name: str
    description: str
    tech: str
    link: str = ""


@dataclass
class SkillCategory:
    category: str
    skills: str


@dataclass
class CVData:
    full_name: str
    headline: str
    contact: ContactInfo
    summary: str
    jobs: list[Job] = field(default_factory=list)
    education: list[Education] = field(default_factory=list)
    projects: list[Project] = field(default_factory=list)
    skills: list[SkillCategory] = field(default_factory=list)
    languages: str = ""
