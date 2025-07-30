def extract_features_from_table(table):
    rows = len(table)
    cols = len(table[0]) if rows else 0
    checkboxes = sum(cell["checkbox"] for row in table for cell in row)
    unit_vals = sum(1 for row in table for cell in row if cell["unit_value"])
    bg_colors = len(set(cell["bg_color"] for row in table for cell in row if cell["bg_color"]))
    return [rows, cols, checkboxes, unit_vals, bg_colors]
