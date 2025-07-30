docstruct-ai/
├── app.py                    # Streamlit review interface
├── pattern_detector.py       # Core AI logic to detect patterns
├── document_parser.py        # DOCX reader & table extractor
├── utils/
│   ├── table_analyzer.py     # Table rule analysis and pattern classification
│   ├── visual_utils.py       # For color detection, checkbox, unit box detection
│   └── pattern_editor.py     # Editable pattern interface
├── rules/
│   └── extracted_rules.json  # Stored structural patterns
├── samples/
│   └── sample_structured.docx
├── output/
│   └── extracted_data.json
└── requirements.txt
