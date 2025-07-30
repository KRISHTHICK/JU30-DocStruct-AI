# JU30-DocStruct-AI
GEN AI

DocStruct-AI: Intelligent Pattern Detection from MS Word Documents
🧠 Objective:
Automatically detect structural patterns (rules) in an unstructured MS Word document (.docx) that includes:

Multiple sections

Paragraphs

Tables with checkboxes, unit-value boxes

Colored table rows/columns (conditional)

Tables containing icons/images

Up to 5–7 distinct recurring table types

Background-colored content areas

Section 1 containing “General Instructions” to guide pattern detection

Human reviewers will be able to review/edit/approve the detected patterns, which are then used to extract structured data.

🎯 Key Features:
Detect distinct table structures automatically

Recognize color-based semantics (e.g., red = alert, green = pass)

Extract checkboxes (✓/☐) and unit-value pairs from tables

Identify common patterns: text-only tables, text+icons, text+checkboxes+units

Store extracted patterns in a JSON rule file

Allow human-in-the-loop feedback/editing of patterns



************************
🔚 Summary:
Component	Description
📄 parse_docx	Extracts text, tables, cell formatting, checkboxes, units
🎨 visual_utils	Detects color, checkbox, and units
🧠 pattern_detector	Uses AI (KMeans) to detect 5–7 patterns from tables
👤 app.py	Streamlit UI for human approval of pattern rules

🔜 Next Enhancements:
Add editing UI for users to tweak detected patterns

Export to structured CSV/JSON

Integrate template-matching-based extraction
