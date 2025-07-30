import json
from sklearn.cluster import KMeans
from utils.table_analyzer import extract_features_from_table

def detect_patterns(sections, num_patterns=7):
    all_tables = []
    features = []

    for section in sections:
        for table in section["tables"]:
            all_tables.append(table)
            features.append(extract_features_from_table(table))

    model = KMeans(n_clusters=num_patterns)
    labels = model.fit_predict(features)

    rules = {}
    for idx, label in enumerate(labels):
        rules.setdefault(f"Pattern_{label}", []).append(all_tables[idx])

    with open("rules/extracted_rules.json", "w") as f:
        json.dump(rules, f, indent=2)

    return rules
