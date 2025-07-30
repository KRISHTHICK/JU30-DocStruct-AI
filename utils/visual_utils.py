def detect_background_color(cell):
    try:
        shading = cell._element.tcPr.shading
        return shading.get("fill") if shading is not None else None
    except:
        return None

def detect_checkbox(cell):
    return '☑' in cell.text or '✓' in cell.text

def detect_unit_value(text):
    import re
    match = re.findall(r'\d+(\.\d+)?\s*(mg|kg|ml|mm|cm|%)', text)
    return match[0] if match else None
