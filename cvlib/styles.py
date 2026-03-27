from dataclasses import dataclass
from docx.shared import Pt, RGBColor, Inches


@dataclass(frozen=True)
class Colors:
    BLUE: RGBColor = RGBColor(46, 80, 144)
    GRAY: RGBColor = RGBColor(100, 100, 100)
    BLACK: RGBColor = RGBColor(0, 0, 0)
    BLUE_HEX: str = "2E5090"


@dataclass(frozen=True)
class FontSizes:
    TITLE: Pt = Pt(18)
    SUBTITLE: Pt = Pt(11)
    HEADING: Pt = Pt(12)
    BODY: Pt = Pt(10)
    SMALL: Pt = Pt(9)


@dataclass(frozen=True)
class Spacing:
    SECTION_BEFORE: Pt = Pt(12)
    SECTION_AFTER: Pt = Pt(6)
    ITEM_BEFORE: Pt = Pt(6)
    ITEM_AFTER: Pt = Pt(2)
    BLOCK_AFTER: Pt = Pt(4)
    GROUP_AFTER: Pt = Pt(8)
    PARAGRAPH_AFTER: Pt = Pt(3)
    CONTACT_AFTER: Pt = Pt(6)
    TECH_BEFORE: Pt = Pt(4)
    LANG_BEFORE: Pt = Pt(6)


@dataclass(frozen=True)
class Margins:
    TOP: Inches = Inches(0.6)
    BOTTOM: Inches = Inches(0.6)
    LEFT: Inches = Inches(0.6)
    RIGHT: Inches = Inches(0.6)


BULLET_INDENT = Inches(0.25)

COLORS = Colors()
FONT_SIZES = FontSizes()
SPACING = Spacing()
MARGINS = Margins()
