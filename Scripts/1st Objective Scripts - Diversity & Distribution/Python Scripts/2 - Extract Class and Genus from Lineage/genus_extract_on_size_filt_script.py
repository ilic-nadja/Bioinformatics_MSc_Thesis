import pandas as pd

# Read the TSV file into a pandas DataFrame
df = pd.read_csv('ahl_sbd.tsv', sep='\t')

# Function to extract the name preceding "(class)" from the "Taxonomic lineage" column
def extract_class(name):
    class_index = name.find("(genus)")
    if class_index != -1:
        return name[:class_index].rsplit(',', 1)[-1].strip()
    else:
        return None

# Apply the function to create the "Class" column
df['Genus'] = df['Taxonomic lineage'].apply(extract_class)

# Save the updated DataFrame back to a new TSV file
df.to_csv('ahl_sbd_with_genus.tsv', sep='\t', index=False)
