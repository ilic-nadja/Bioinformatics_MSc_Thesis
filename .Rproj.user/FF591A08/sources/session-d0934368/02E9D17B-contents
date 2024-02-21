library("rio")
library("stringr")
library('ggtree')
library('ggplot2')
library('treeio')
library('dplyr')

######################################################################################################
# MERGED40 - AHL_TCS based on tip shape

## USING 50,100 entry file where Python script merged the AHL and TCS tsv + extracted Class
merged40_df <- import("Data/2nd Objective Data - Clustering Trees/merged40 tree additional data/merged_ahl_tcs_for_merged40tree.tsv")

#merged40_tree
merged40_tree <- ape::read.tree("Data/2nd Objective Data - Clustering Trees/4 - mega/1 - merged40/newick_merged40.txt")
merged40_tree
#has 3408 tips (samples) + 3406 nodes 

# Extracting the pattern from the "tree" object
pattern <- "(tr|sp)\\|([^|]+)\\|"

# Finding matches in the "Entry" column
matches_merged40 <- str_match(merged40_tree$tip.label, pattern)[, 3]

# Filtering the data frame based on the matches
filtered_merged40_df <- merged40_df[merged40_df$Entry %in% matches_merged40, ]
#3408

# Python script used to add cluster belonging to each LuxR entry

##ADDING CLUSTER ANNOTATION COLUMN TO MERGED TSV 
merged40_clstr <- import("Data/2nd Objective Data - Clustering Trees/5 - cluster_metadata_extraction/merged40_clstr.tsv")

# Finding matches in the "Entry" column
matches_merged40_clstr <- str_match(merged40_tree$tip.label, pattern)[, 3]

# Extracting the pattern from the "Entry" column
merged40_clstr$Entry <- str_extract(merged40_clstr$Entry, "(?<=\\|)[^|]+")

# adding the seq_count column to this AHL
merged40_clstr_df <- merge(filtered_merged40_df, merged40_clstr[c("Entry", "Seq_count")], by = "Entry", all.x = TRUE)

# Getting the names from the "tree" object
merged40tree_names <- merged40_tree$tip.label

# Assigning tree_names as labels for the "Entry" column in filtered_df
merged40_clstr_df$Entry <- merged40tree_names[match(merged40_clstr_df$Entry, matches_merged40)]

# check
merged40_clstr_df$Entry %in% merged40_tree$tip.label #doesnt show false?
merged40_tree$tip.label %in% merged40_clstr_df$Entry 

# showing any sample IDs that are not on the tree
merged40_clstr_df$Entry[!merged40_tree$tip.label %in% merged40_clstr_df$Entry]
##character(0)

# adding NAs to blank Class entries
# Replacing blank entries with NA in the "Class" column
merged40_clstr_df$Class <- ifelse(merged40_clstr_df$Class == "", NA, merged40_clstr_df$Class)

#####################################################################################################
# Process of adding AHL_TCS column to be able to differentiate AHL vs TCS type LuxRs
write.table(merged40_clstr_df, file = "merged40_clstr_df", sep = "\t", quote = FALSE, row.names = FALSE)

tcs_merged <- import("Data/2nd Objective Data - Clustering Trees/merged40 tree additional data/size_filt_tcs.tsv")
#36,212
ahl_merged <- import("Data/2nd Objective Data - Clustering Trees/merged40 tree additional data/size_filt_ahl.tsv")
#13,888

# Filtering the data frame based on the matches
filt_tcs_merged <- tcs_merged[tcs_merged$Entry %in% matches_merged40, ]
#get 2478 entries..
filt_ahl_merged <- ahl_merged[ahl_merged$Entry %in% matches_merged40, ]
#930 entries
#3408 entries total which is same as filtered_merged40_df together

# Assigning tree_names as labels for the "Entry" column in filt_tcs and ahl dfs
filt_tcs_merged$Entry <- merged40tree_names[match(filt_tcs_merged$Entry, matches_merged40)]
filt_ahl_merged$Entry <- merged40tree_names[match(filt_ahl_merged$Entry, matches_merged40)]

# now writing i.e. saving them and matching them via Python script:
write.table(filt_tcs_merged, file = "filt_tcs_merged.tsv", sep = "\t", quote = FALSE, row.names = FALSE)
write.table(filt_ahl_merged, file = "filt_ahl_merged.tsv", sep = "\t", quote = FALSE, row.names = FALSE)

# Checking for matches with filt_tcs_merged and assign "tcs"
merged40_clstr_df$ahl_tcs <- ifelse(merged40_clstr_df$Entry %in% filt_tcs_merged$Entry, "tcs", "")

# Checking for matches with filt_ahl_merged and assign "ahl"
merged40_clstr_df$ahl_tcs <- ifelse(merged40_clstr_df$Entry %in% filt_ahl_merged$Entry, "ahl", merged40_clstr_df$ahl_tcs)
head(merged40_clstr_df)

write.table(merged40_clstr_df, file = "merged40_clstr_df", sep = "\t", quote = FALSE, row.names = FALSE)

#####################################################################################################
# coloring the tree by ahl vs tcs
# Clustering tree where customisation of FONT, BOLD, LEGEND enabled
ggtree(merged40_tree, layout = 'circular', branch.length = 'none') %<+% merged40_clstr_df + 
  aes(color = ahl_tcs) +
  
  # Customization for font size and legend bar text bold
  theme(legend.text = element_text(size = 12, face = "bold"),    
        legend.title = element_text(size = 14, face = "bold")) +  
  
  # Adding a title to the legend bar
  labs(color = "AHL or TCS type LuxR")

#####################################################################################################
# Creating clustering tree with cluster size and class annotations
ggtree(merged40_tree, layout = 'circular', branch.length = 'none') %<+% merged40_clstr_df + 
  aes(color = Class) + 
  geom_tippoint(aes(size = Seq_count), alpha = .6) +
  scale_size_continuous(breaks = c(50, 100, 200, 400, 1000), 
                        limits = c(0, 6500),
                        range = c(2, 10)) +
  
  # Customization for font size and legend bar text bold
  theme(legend.text = element_text(size = 10, face = "plain"),   # Sets the font to 12 
        legend.title = element_text(size = 12, face = "bold")) + # Sets the font size to 14 and makes it bold
  
  # Adding a custom title to the legend bar
  labs(size = "Cluster Size (# Sequnces)")

######################################################################################################
####AHL40 TREE

## USING the 13,888 AHL entries file
ahl40_df <- import("Data/1st Objective Data - Diversity & Distribution/4 - Class and Genus Size Filtered TSV/size_filtered_ahl_sbd_with_class_genus.tsv")

# ahl40_tree object
ahl40_tree <- ape::read.tree("Data/2nd Objective Data - Clustering Trees/4 - mega/2 - ahl40/ahl40_tree.txt")
ahl40_tree
#has 930 tips (samples) + 928 nodes // same as dbd, sbd...

# Extracting the pattern from the "tree" object
pattern <- "(tr|sp)\\|([^|]+)\\|"

# Finding matches in the "Entry" column
matches_ahl40 <- str_match(ahl40_tree$tip.label, pattern)[, 3]

# Filtering the data frame based on the matches
filtered_ahl40_df <- ahl40_df[ahl40_df$Entry %in% matches_ahl40, ]
#930

# Python script used to add cluster belonging to each LuxR entry

# ADDING CLUSTER ANNOTATION COLUMN TO AHL TSV
ahl40_clstr <- import("Data/2nd Objective Data - Clustering Trees/5 - cluster_metadata_extraction/ahl40_cluster_extraction.tsv")

# Finding matches in the "Entry" column
matches_ahl40_clstr <- str_match(ahl40_tree$tip.label, pattern)[, 3]
head(matches_ahl40_clstr) #checking

# Extracting the pattern from the "Entry" column
ahl40_clstr$Entry <- str_extract(ahl40_clstr$Entry, "(?<=\\|)[^|]+")

# adding the seq_count column to this OG AHL
merged_ahl_40df <- merge(filtered_ahl40_df, ahl40_clstr[c("Entry", "Seq_count")], by = "Entry", all.x = TRUE)

# Get the names from the "tree" object
ahl40tree_names <- ahl40_tree$tip.label
head(ahl40tree_names) #checking

# Assign tree_names as labels for the "Entry" column in filtered_df
merged_ahl_40df$Entry <- ahl40tree_names[match(merged_ahl_40df$Entry, matches_ahl40)]
#some sp's and tr's have 'sp whereas others no '

#checking
merged_ahl_40df$Entry %in% ahl40_tree$tip.label #doesnt show false
ahl40_tree$tip.label %in% merged_ahl_40df$Entry 

#show any sample IDs that are not on the tree
merged_ahl_40df$Entry[!ahl40_tree$tip.label %in% merged_ahl_40df$Entry]
##character(0)

## adding NAs to blank Class entries
# Replacing blank entries with NA in the "Class" column
merged_ahl_40df$Class <- ifelse(merged_ahl_40df$Class == "", NA, merged_ahl_40df$Class)

# want to know count of each class:
# Use the table() function to count the occurrences of each value in the "Class" column
class_counts <- table(merged_ahl_40df$Class)
# Displaying the counts
sort(class_counts)

# saving the merged ahl40 df
write.table(merged_ahl_40df, file = "merged_ahl_40df", sep = "\t", quote = FALSE, row.names = FALSE)

# Clustering tree where customisation of FONT, BOLD, LEGEND enabled
ggtree(ahl40_tree, layout = 'circular', branch.length = 'none') %<+% merged_ahl_40df + 
  aes(color = Class) + 
  geom_tippoint(aes(size = Seq_count), alpha = .6) +
  scale_size_continuous(breaks = c(50, 150, 300, 450, 600), 
                        limits = c(0, 800),
                        range = c(2, 10)) +
  
  # Customization for font size and legend bar text bold
  theme(legend.text = element_text(size = 12, face = "plain"),   
        legend.title = element_text(size = 14, face = "bold")) +
  
  # Adding a custom title to the legend bar
  labs(size = "Cluster Size (# Sequnces)")

######################################################################################################
###AHL70
## USING the 13,888 AHL entries file
ahl70_df <- import("Data/1st Objective Data - Diversity & Distribution/4 - Class and Genus Size Filtered TSV/size_filtered_ahl_sbd_with_class_genus.tsv")

# ahl70_tree object
ahl70_tree <- ape::read.tree("Data/2nd Objective Data - Clustering Trees/4 - mega/4 - ahl70/newick_tree.txt")
ahl70_tree
#has 3359 tips (samples) + 3357 nodes

# Extracting the pattern from the "tree" object
pattern <- "(tr|sp)\\|([^|]+)\\|"

# Finding matches in the "Entry" column
matches_ahl70 <- str_match(ahl70_tree$tip.label, pattern)[, 3]

# Filtering the data frame based on the matches
filtered_ahl70_df <- ahl70_df[ahl70_df$Entry %in% matches_ahl70, ]
#3359

# Python script used to add cluster belonging to each LuxR entry

# ADDING CLUSTER ANNOTATION COLUMN TO the AHL TSV
ahl70_clstr <- import("Data/2nd Objective Data - Clustering Trees/5 - cluster_metadata_extraction/ahl70_clstr_extraction.tsv")

# Extracting the pattern from the "tree" object
pattern_clstr <- "(tr|sp)\\|([^|]+)\\|"

# Finding matches in the "Entry" column
matches_ahl70_clstr <- str_match(ahl70_tree$tip.label, pattern)[, 3]

# Extracting the pattern from the "Entry" column
ahl70_clstr$Entry <- str_extract(ahl70_clstr$Entry, "(?<=\\|)[^|]+")

# adding the seq_count column to this AHL
merged_ahl_70df <- merge(filtered_ahl70_df, ahl70_clstr[c("Entry", "Seq_count")], by = "Entry", all.x = TRUE)

# Getting the names from the "tree" object
ahl70tree_names <- ahl70_tree$tip.label
head(ahl70tree_names) #checking

# Assigning tree_names as labels for the "Entry" column in filtered_df
merged_ahl_70df$Entry <- ahl70tree_names[match(merged_ahl_70df$Entry, matches_ahl70)]

#check
merged_ahl_70df$Entry %in% ahl70_tree$tip.label #doesnt show false
ahl70_tree$tip.label %in% merged_ahl_70df$Entry 

#shows any sample IDs that are not on the tree
merged_ahl_70df$Entry[!ahl70_tree$tip.label %in% merged_ahl_70df$Entry]
##character(0)

# adds NAs to blank Class entries
# Replacing blank entries with NA in the "Class" column
merged_ahl_70df$Class <- ifelse(merged_ahl_70df$Class == "", NA, merged_ahl_70df$Class)

# CLustering tree where customisation of FONT, BOLD, LEGEND enabled
ggtree(ahl70_tree, layout = 'circular', branch.length = 'none') %<+% merged_ahl_70df + 
  aes(color = Class) + 
  geom_tippoint(aes(size = Seq_count), alpha = .6) +
  scale_size_continuous(breaks = c(50, 150, 300, 450, 600), 
                        limits = c(0, 800),
                        range = c(2, 10)) +
  
  # Customization for font size and legend bar text bold
  theme(legend.text = element_text(size = 12, face = "plain"),   
        legend.title = element_text(size = 14, face = "bold")) + 
  
  # Adding a custom title to the legend bar
  labs(size = "Cluster Size (# Sequences)")

####################################################################################

## Adding labels for entries which were reviewed in UniProt
# reviewd_luxrs_list.xlsx file from path 
# "Data/2nd Objective Data - Clustering Trees/4 - ahl70_reviewed luxrs in clade"
# was uploaded to iTOL alongside the ahl70 nwk file
# the final output was a clustering tree with tip labelling the reviwed LuxR entries
# that image was layered onto the gg tree created above to produce the graph from the Output folder

############## ############## ############## ############## ############## ############## ############
#DOING AN AHL70 REVIEWeD TABLE
reviewed_data<- import("Data/2nd Objective Data - Clustering Trees/6 - reviewed UniProt entries/reviewed UniProt entries.tsv")

# Loading the required library
library(gt)

# Selecting the desired columns
selected_columns_reviewed <- c("short_name", "Class", "clade")

# Creating a gt styled table 
table <- reviewed_data[selected_columns_reviewed] %>%
  gt() %>%
  tab_header(title = "Reviewed AHL-binding LuxRs") %>%
  fmt_number(columns = clade, decimals = 0) %>%
  cols_label(
    short_name = "Entry Name",
    Class = "Class",
    clade = "Clade",
  )

# Showing the styled table
print(table)

############## ############## ############## ############## ############## ############## ############
# DBD SBD CLADE ANNOTATIONS 
ahl40_clades <- import("Data/2nd Objective Data - Clustering Trees/merged_ahl_40df_with_clades.tsv")

ahl40_clades$clades[ahl40_clades$clades == ""] <- NA

# Defining a custom color scheme for clades
custom_colors <- c("clade_1" = "red", "clade_3" = "blue", "clade_2" = "green", "clade_4" = "magenta", "clade_5"= "yellow", "clade_6" = "turquoise2")

# Defining new identifiers for the legend
new_legend_names <- c("clade_1" = "Clade 1", "clade_2" = "Clade 2", "clade_3" = "Clade 3", "clade_4" = "Clade 4", "clade_5" = "Clade 5", "clade_6" = "Clade 6")

sbd40_tree <- ape::read.tree("Data/2nd Objective Data - Clustering Trees/4 - mega/3 - sbd40/sbd40_tree.txt")
sbd40_tree
#has 930 tips (samples) + 928 nodes 

# SBD40 Clustering tree where customisation of FONT, BOLD, LEGEND enabled
ggtree(sbd40_tree, layout = 'circular', branch.length = 'none') %<+% ahl40_clades + 
  aes(color = clades) + 
  geom_tippoint(aes(size = Seq_count), alpha = .6) +
  scale_size_continuous(breaks = c(50, 150, 300, 450, 600), 
                        limits = c(0, 800),
                        range = c(2, 10)) +
  
  theme(legend.text = element_text(size = 12, face = "plain"),
        legend.title = element_text(size = 14, face = "bold")) +
  
  labs(size = "Cluster Size (# Sequences)") +
  
  # Manually specify the color scheme and rename the legend values
  scale_color_manual(values = custom_colors, breaks = names(new_legend_names), labels = new_legend_names)

# Full AHL40 Clustering tree where customisation of FONT, BOLD, LEGEND enabled
ggtree(ahl40_tree, layout = 'circular', branch.length = 'none') %<+% ahl40_clades + 
  aes(color = clades) + 
  geom_tippoint(aes(size = Seq_count), alpha = .6) +
  scale_size_continuous(breaks = c(50, 150, 300, 450, 600), 
                        limits = c(0, 800),
                        range = c(2, 10)) +
  
  theme(legend.text = element_text(size = 12, face = "plain"),
        legend.title = element_text(size = 14, face = "bold")) +
  
  labs(size = "Cluster Size (# Sequences)") +
  
  # Manually specify the color scheme and rename the legend values
  scale_color_manual(values = custom_colors, breaks = names(new_legend_names), labels = new_legend_names)

## FOR DBD CLADE ASSIGNMENTS
dbd40_tree <- ape::read.tree("Data/2nd Objective Data - Clustering Trees/4 - mega/3 - dbd40/dbd40.txt")
dbd40_tree
#has 930 tips (samples) + 928 nodes 

# DBD40 Clustering tree where customisation of FONT, BOLD, LEGEND enabled
ggtree(dbd40_tree, layout = 'circular', branch.length = 'none') %<+% ahl40_clades + 
  aes(color = clades) + 
  geom_tippoint(aes(size = Seq_count), alpha = .6) +
  scale_size_continuous(breaks = c(50, 150, 300, 450, 600), 
                        limits = c(0, 800),
                        range = c(2, 10)) +
  
  theme(legend.text = element_text(size = 12, face = "plain"),
        legend.title = element_text(size = 14, face = "bold")) +
  
  labs(size = "Cluster Size (# Sequences)") +
  
  # Manually specify the color scheme and rename the legend values
  scale_color_manual(values = custom_colors, breaks = names(new_legend_names), labels = new_legend_names)



