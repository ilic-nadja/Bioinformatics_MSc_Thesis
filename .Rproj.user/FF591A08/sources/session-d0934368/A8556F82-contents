library(readr) 

# Importing IPR005143+IPR000792 TSV
ahl_sbd <- read_tsv("Data/1st Objective Data - Diversity & Distribution/1 - UniProtKB Raw Input/AHL_type_LuxR_UniProt.tsv")
#16,582 entries

# Import IPR001782+IPR000792 TSV
tcs_sbd<-read_tsv("Data/1st Objective Data - Diversity & Distribution/1 - UniProtKB Raw Input/TCS_type_LuxR_UniProt.tsv")
#275,392 entries

# Retain only entries with +/- 20AA from consensus 250AA of LuxRs
# Filter for entries with length between 230 and 270
filtered_ahl_sbd <- subset(ahl_sbd, Length >= 230 & Length <= 270)
#get 13,888 entries

filtered_tcs_sbd <- subset(tcs_sbd, Length >= 230 & Length <= 270)
#get 36,212 entries 
#######################################################################################################

#Python script executed to merge AHL + TCS type LuxRs
#Python script to extract Class & Genus column from taxonomic lineage & add that new column to TSV

#######################################################################################################
# Loading required packages
library(stringr)
library(ggplot2)
library(dplyr)

# Importing IPR005143+IPR000792 TSV - i.e. the AHL LuxRs
ahl_size_class <- read_tsv("Data/1st Objective Data - Diversity & Distribution/4 - Class and Genus Size Filtered TSV/size_filtered_ahl_sbd_with_class_genus.tsv")
#13,888 entries w/ 10 columns

# Importing proteomes TSV
ahl_proteomes <- read_tsv("Data/1st Objective Data - Diversity & Distribution/5 - Proteome Number Tables/ahl_proteome_class_count.tsv")

# Calculating the ratio and store it in a new column 'ratio'
ahl_proteomes <- ahl_proteomes %>%
  mutate(ratio = count / uniprotkb_proteomes)

# Sorting the data by the ratio in descending order and taking the top 10 classes
top_classes <- ahl_proteomes %>%
  arrange(desc(ratio)) %>%
  head(10)

# Checking top classes
top_classes$top_classes_ahl

# Creating a color palette for the top 10 classes
class_palette <- c("Alphaproteobacteria" = "skyblue", "Methylacidiphilae" = "lightgreen", "Oligoflexia" = "orange",
                   "Betaproteobacteria" = "pink", "Gammaproteobacteria" = "purple", "Nitrospira" = "red",
                   "Acidithiobacillia" = "yellow", "Hydrogenophilia" = "brown", "Deltaproteobacteria" = "blue", "Actinomycetes" = "green")

# Defining the legend
legend_labels <- paste(top_classes$count, "/", top_classes$uniprotkb_proteomes)

# Creating the bar chart with different colors for each bar + annotated colors in the legend 
#(WRONG COLORS FOR THOSE LABELS --> PHOTOSHOP COLOR CORRECTION)
ggplot(top_classes, aes(x = reorder(top_classes_ahl, -ratio), y = ratio, fill = top_classes_ahl)) +
  geom_bar(stat = "identity") +
  labs(x = "Class", y = "Proteome Number Corrected LuxR Count", 
       title = "Distribution of Top 10 Classes of AHL type LuxRs, Normalised Against Number of Proteomes") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 12, face = "bold"),  
        axis.text.y = element_text(size = 12, face = "bold"),                        
        axis.title = element_text(size = 14, face = "bold")) +                        
  scale_fill_manual(values = class_palette, labels = legend_labels, name = "LuxR Count / Proteome Count")

#######################################################################################################
# Importing merged TSV
merged_size_class <- read_tsv("Data/1st Objective Data - Diversity & Distribution/2 - Merged AHL TCS/merged_ahl_tcs_annot.tsv")
#49,568 entries filtered by size + w/ class annot

# NORMALIZED AGAINST PROTEOME VALUES (MERGED)
# Importing proteomes TSV
merged_proteomes <- read_tsv("Data/1st Objective Data - Diversity & Distribution/5 - Proteome Number Tables/merged_proteome_class_count.tsv")

# Calculating the ratio and storing in new column 'ratio'
merged_proteomes <- merged_proteomes %>%
  mutate(ratio = count_merged / uniprotkb)

# Sorting the data by the ratio in descending order and taking the top 10 classes
top_classes_merged <- merged_proteomes %>%
  arrange(desc(ratio)) %>%
  head(10)

## ADDING LEGEND STUFF

# Creating a color palette for the top 10 classes
class_palette_merged <- c("Alphaproteobacteria" = "skyblue", "Anaerolineae" = "aquamarine", "Nitrospira" = "darkgoldenrod2",
                          "Betaproteobacteria" = "pink", "Gammaproteobacteria" = "purple", "Planctomycetia" = "azure3",
                          "Bacilli" = "yellow2", "Acidobacteriia" = "coral1", "Deltaproteobacteria" = "blue", "Actinomycetes" = "green")

## adding count/proteome in legend

# Customizing the legend
legend_labels_merged <- paste(top_classes_merged$count_merged, "/", top_classes_merged$uniprotkb)

# Creating the bar chart with different colors for each bar and annotated colors in the legend 
# (WRONG COLORS FOR THOSE LABELS - PHOTOSHOP CORRECTION)
ggplot(top_classes_merged, aes(x = reorder(taxa_distrib_merged, -ratio), y = ratio, fill = taxa_distrib_merged)) +
  geom_bar(stat = "identity") +
  labs(x = "Class", y = "Proteome Number Corrected LuxR Count", 
       title = "Distribution of Top 10 Classes of AHL+TCS type LuxRs, Normalised Against Number of Proteomes") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 12, face = "bold"),  
        axis.text.y = element_text(size = 12, face = "bold"),                        
        axis.title = element_text(size = 14, face = "bold")) +                        
  scale_fill_manual(values = class_palette_merged, labels = legend_labels_merged, name = "LuxR Count / Proteome Count")

#####################################################################################################
##############################  GENUS LVL TAXO DISTRIB ANALYSIS #####################################
# NORMALIZED AGAINST PROTEOME VALUES (AHL)
# Importing proteomes TSV
ahl_genera_proteomes <- read_tsv("Data/1st Objective Data - Diversity & Distribution/5 - Proteome Number Tables/ahl_proteome_genera_count.tsv")

# Calculating the ratio and storing it into the new column 'ratio'
ahl_genera_proteomes <- ahl_genera_proteomes %>%
  mutate(ratio = count_merged / uniprotkb)

# Sorting the data by the ratio in descending order and take the top 10 genera
top_genera_ahl <- ahl_genera_proteomes %>%
  arrange(desc(ratio)) %>%
  head(10)

# Creating the bar chart with colored bars and no text labels above bars
ggplot(top_genera_ahl, aes(x = reorder(taxa_distrib_merged, -ratio), y = ratio, fill = class)) +
  geom_bar(stat = "identity") +
  labs(x = "Genus", y = "Proteome Number Corrected LuxR Count", 
       title = "Distribution of Top 10 Genera of AHL type LuxRs, Normalised Against Number of Proteomes") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        axis.text = element_text(size = 12, face = "bold"),  # Increase font size and make it bold
        axis.title = element_text(size = 14, face = "bold")) +  # Increase font size and make it bold
  scale_fill_manual(values = class_palette)

#################GENUS LVL FOR MERGED 

### NORMALIZED AGAINST PROTEOME VALUES (MERGED)
# Importing proteomes TSV
merged_genera_proteomes <- read_tsv("Data/1st Objective Data - Diversity & Distribution/5 - Proteome Number Tables/merged_proteome_genera_count.tsv")

# Calculating the ratio and storing it column 'ratio'
merged_genera_proteomes <- merged_genera_proteomes %>%
  mutate(ratio = count_merged / uniprotkb)

# Sorting the data by the ratio in descending order and take the top 10 classes
top_genera_merged <- merged_genera_proteomes %>%
  arrange(desc(ratio)) %>%
  head(10)

# Coloring according to class
# Creating the bar chart with colored bars and no text labels above bars
ggplot(top_genera_merged, aes(x = reorder(taxa_distrib_merged, -ratio), y = ratio, fill = class)) +
  geom_bar(stat = "identity") +
  labs(x = "Genus", y = "Proteome Number Corrected LuxR Count", 
       title = "Distribution of Top 10 Genera of AHL+TCS type LuxRs, Normalised Against Number of Proteomes") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1),
        axis.text = element_text(size = 12, face = "bold"),  # Increase font size and make it bold
        axis.title = element_text(size = 14, face = "bold")) +  # Increase font size and make it bold
  scale_fill_manual(values = class_palette_merged)

#####################################################################################################
#### MAKING SUPPLMENTAL TABLES FOR PROTEOME VALUES

# Loading the required libraries
library(gt)

## AHL CLASS table
# Choosing the desired columns from ahl_proteomes
selected_columns <- c("top_classes_ahl", "count", "uniprotkb_proteomes", "ratio")

## Arranging the data by ratio in decreasing order
sorted_ahl_proteomes <- ahl_proteomes[selected_columns] %>%
  arrange(desc(ratio))

# Creating a styled table using the gt package
table <- sorted_ahl_proteomes[selected_columns] %>%
  gt() %>%
  tab_header(title = "Proteome Number Corrected AHL-type LuxR Count (Class Level)") %>%
  cols_label(
    top_classes_ahl = "Class Name",
    count = "Absolute LuxR Count",
    uniprotkb_proteomes = "Proteome Number",
    ratio = "Proteome Normalized Count"
  )

# Displaying the styled table
print(table)

## AHL GENUS PROTEOME table
# Selecting the desired columns
selected_columns <- c("taxa_distrib_merged", "count_merged", "class", "uniprotkb", "ratio")
# Arranging the data by ratio in decreasing order
sorted_ahl_Gproteomes <- ahl_genera_proteomes[selected_columns] %>%
  arrange(desc(ratio))

# Create a styled table using the gt package
table <- sorted_ahl_Gproteomes[selected_columns] %>%
  gt() %>%
  tab_header(title = "Proteome Number Corrected AHL-type LuxR Count (Genus Level)") %>%
  cols_label(
    taxa_distrib_merged = "Genus Name",
    class = "Class Belonging",
    count_merged = "Absolute LuxR Count",
    uniprotkb = "Proteome Number",
    ratio = "Proteome Normalized Count"
  )

# Display the styled table
print(table)

### MERGED Class table
# Select the desired columns
selected_columns <- c("taxa_distrib_merged", "count_merged", "uniprotkb", "ratio")
## Arrange the data by ratio in decreasing order
sorted_merged_proteomes <- merged_proteomes[selected_columns] %>%
  arrange(desc(ratio))

# Create a styled table using the gt package
table <- sorted_merged_proteomes[selected_columns] %>%
  gt() %>%
  tab_header(title = "Proteome Number Corrected LuxR Count (AHL & TCS type LuxRs on Class Level)") %>%
  cols_label(
    taxa_distrib_merged = "Class Name",
    count_merged = "Absolute LuxR Count",
    uniprotkb = "Proteome Number",
    ratio = "Proteome Normalized Count"
  )

# Displaying the styled table
print(table)

## merged GENUS proteome table
# Selecting the desired columns
selected_columns <- c("taxa_distrib_merged", "count_merged", "class", "uniprotkb", "ratio")
# Arranging the data by ratio in decreasing order
sorted_merged_Gproteomes <- merged_genera_proteomes[selected_columns] %>%
  arrange(desc(ratio))

# Creating a styled table using the gt package
table <- sorted_merged_Gproteomes[selected_columns] %>%
  gt() %>%
  tab_header(title = "Proteome Number Corrected AHL & TCS-type LuxR Count (Genus Level)") %>%
  cols_label(
    taxa_distrib_merged = "Genus Name",
    class = "Class Belonging",
    count_merged = "Absolute LuxR Count",
    uniprotkb = "Proteome Number",
    ratio = "Proteome Normalized Count"
  )

# Display the styled table
print(table)
