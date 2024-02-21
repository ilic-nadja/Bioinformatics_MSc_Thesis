import pandas as pd

# Read the two TSV files
file1 = '/Users/nadja/Downloads/size_filt_ahl_classname.tsv'
file2 = '/Users/nadja/Downloads/size_filt_tcs_classname.tsv'
df1 = pd.read_csv(file1, sep='\t')
df2 = pd.read_csv(file2, sep='\t')

# Merge the two dataframes
merged_df = pd.concat([df1, df2], ignore_index=True)

# Save the merged dataframe to a new TSV file
merged_file = 'merged_file.tsv'
merged_df.to_csv(merged_file, sep='\t', index=False)
