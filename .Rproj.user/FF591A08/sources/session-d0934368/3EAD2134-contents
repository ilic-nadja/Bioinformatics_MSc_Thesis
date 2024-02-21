library("ggplot2")
library("rio")
library("stringr")

luxr_data<- import("Data/3rd Objective Data - Species Level Analysis/species_lvl_cdhit_distrib.tsv")

# MAKING A 95-100% GRAPH
# Defining the necesary order of CD-HIT settings
cd_hit_order <- c("100%", "99%", "98%", "97%", "96%", "95%")

# Reordering the levels of CD_HIT_setting
luxr_data$CD_HIT_setting <- factor(luxr_data$CD_HIT_setting, levels = cd_hit_order)

# Making the plot
plot <- ggplot(luxr_data, aes(x = CD_HIT_setting, y = Number_of_Clusters, color = LuxR_type)) +
  geom_point(size = 3, alpha = 0.8) +
  geom_line(aes(group = LuxR_type), size = 1, alpha = 0.6) +
  facet_wrap(~Species, scales = "free_y", ncol = 2) +
  labs(x = "CD-HIT Setting (%)", y = "Number of Clusters", title = "Number of Clusters for Different CD-HIT Settings") +
  theme_minimal() +
  theme(
    text = element_text(size = 14, face = "bold"),         # Adjust font size and boldness
    axis.title = element_text(face = "bold"),              # Bold axis titles
    plot.title = element_text(face = "bold", size = 16),   # Bold and larger plot title
    strip.text = element_text(face = "bold")               # Bold facet labels
  ) +
  labs(color = "LuxR Type")  # Change the title of the legend bar

# Showing the plot
print(plot)

# ADDING LOG FOLD CHANGE - scatter plot version
luxr_data$log_fold_change <- log2(luxr_data$Number_of_Clusters / luxr_data$Seqs_before_CD_HIT)

# Creating the plot
plot <- ggplot(luxr_data, aes(x = CD_HIT_setting, y = log_fold_change, color = LuxR_type)) +
  geom_point(size = 3, alpha = 0.8) +
  geom_line(aes(group = LuxR_type), size = 1, alpha = 0.6) +
  facet_wrap(~Species, scales = "free_y", ncol = 2) +
  labs(x = "CD-HIT Setting(%)", y = "Log Fold Change", title = "Log Fold Change - Total Sequence Count ÷ Number of Clusters") +
  theme_minimal() +
  theme(
    text = element_text(size = 14, face = "bold"),         # Adjust font size and boldness
    axis.title = element_text(face = "bold"),              # Bold axis titles
    plot.title = element_text(face = "bold", size = 16),   # Bold and larger plot title
    strip.text = element_text(face = "bold")               # Bold facet labels
  ) +
  labs(color = "LuxR Type")  # Change the title of the legend bar

# Showing the plot
print(plot)

#######################################################################################################
# Making tables of certain luxr_data columns:
# gt package APPROACH 
library(gt)

# Picking the necesary columns
selected_columns <- c("Species", "LuxR_type", "Seqs_before_CD_HIT", "CD_HIT_setting", "Number_of_Clusters")

# Define colors for LuxR types
luxr_colors <- c("BglJ" = "#F8766D", "CsgD" = "#CF9400", "DtcR" = "#7CAE00","EpcR" = "#00BE6C", "GadE" = "#00BFC4", "RcsA" = "#00A5FF", "SdiA" = "#C77CFF", "VpsT" = "#F763E0")

# Creating a ft styled table
table <- luxr_data[selected_columns] %>%
  gt() %>%
  tab_header(title = "Varying CD-HIT Settings Impact on Cluster Size") %>%
  fmt_number(columns = c(Seqs_before_CD_HIT, Number_of_Clusters), decimals = 0) %>%
  cols_label(
    Species = "Species",
    LuxR_type = "LuxR Type",
    Seqs_before_CD_HIT = "Total Count",
    CD_HIT_setting = "CD-HIT Setting",
    Number_of_Clusters = "Number of Clusters"
  )

# Showing it
print(table)

# Saving the table through writexl library 
library("writexl")

write_xlsx(luxr_data, "Output/3- species lvl")

####################################################################################
