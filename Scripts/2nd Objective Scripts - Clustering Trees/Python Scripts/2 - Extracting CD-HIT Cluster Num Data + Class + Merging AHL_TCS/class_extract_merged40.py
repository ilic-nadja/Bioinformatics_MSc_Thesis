import pandas as pd

# Read the TSV file into a pandas DataFrame
df = pd.read_csv('merged_ahl_tcs.tsv', sep='\t')

# Function to extract the name preceding "(class)" from the "Taxonomic lineage" column
def extract_class(name):
    class_index = name.find("(class)")
    if class_index != -1:
        return name[:class_index].rsplit(',', 1)[-1].strip()
    else:
        return None

# Apply the function to create the "Class" column
df['Class'] = df['Taxonomic lineage'].apply(extract_class)

# Save the updated DataFrame back to a new TSV file
df.to_csv('merged40_with_class.tsv', sep='\t', index=False)
