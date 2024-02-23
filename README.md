## Project Title:

"Mapping the microevolution of LuxR transcriptional regulation in the ecosphere"

## Research Rationale:

- Limited survey of the LuxR protein family across all domains of life inclusive of different signal-binding domains.

- Incomplete reconstruction of evolutionary history & domain diversification.

- Insufficiency in assessing the extent of sequence variance on per species-level.

## Main Objectives:

1. Explore distribution of AHL and TCS LuxR proteins.

2. Build clustering trees to study taxonomic fidelity and drivers of sequence flexibility.

3. Investigate within species LuxR sequence variance to better understand cell-cell communication chemical diversity.

#### 1. Creating Bar Plot to Survey Distribution & Diversity of LuxRs

- UniProtKB for LuxR search based on domain identity
- Got TSV files
- Size filtered (to an acceptable range given that ~250AA is consensus)
- Continuing in R, extracted classes and genera with highest absolute LuxR count
- Then corrected values by number of proteomes – got fairer comparison which taxa relatively high or low representation

![[FIGURE 1 | Building taxonomic distribution plots]](README Media/Picture 1.png)

#### 2. Building Clustering Trees to Reconstruct Evolutionary History & Domain Diversification

- FASTA files from UniProtKB
- CD-HIT to cluster sequences of pre-processed entries
- MUSCLE to align homologous regions
- MEGA/X to infer phylogenetic tree via ML method.
- R to visualize the Newick file trees

![[Pasted image 20240130110956.png]]

#### 2. DBD & SBD Coordinate Extraction

- An added component to the tree building was to create:
- New FASTA files corresponding to each domain - UniProtKB included all AHL-type LuxRs, whilst InterPro had the metadata on domain positions. These files were matched
- Exposed to tree building algorithms (MUSCLE, MEGA, R)

![[Pasted image 20240130111040.png]]


#### 3. Within Species Diversification of LuxR Proteins
- KEGG Brite – species selection and sequence repository to extract all distinct LuxRs annotated in the LuxR family
- BLASTp – retrieve from the nr database in BLAST all sequence homologous to each distict LuxR found in KEGG
- CD-HIT – sequence variance assessment --> decreased CD-HIT setting by 1% each run.

![[Pasted image 20240130111356.png]]

## Results:

#### [](https://github.com/ConorGilesDoran/MSc_Thesis_Transcriptomics/blob/main/README.md#batch-analysis)1st Objective Output - Diversity & Distribution:

- Results generated from the distribution_diveristy_bar_plots.R script and Python scripts in the Scripts/1st Objective Scripts - Diversity & Distribution.

- Achieved unbiased complete survey across all taxa.

- Bar plots of proteome number adjusted LuxR counts to show extent certain classes enriched by LuxR-type proteins.

- Compare and contrast analyses helped determine prevailing signal transduction mechanism on class and genus level.

- Greater count of LuxRs --> greater complexity of regulatory networks --> higher possibility for interkingdom, interspecies and intraspecies communication.

#### 2nd Objective Output - Clustering Trees:

- Gained Information on homology between different LuxRs, and how each standalone domain contributed to family diversification.

- Congruency between 16s rRNA and LuxR protein tree suggests ancient origin.
- Homologs from different taxa that clustered together belonged to same niche - Interjections allude to ability of organisms to acquire new LuxRs to better adapt to new niche.

###### LuxR-type Protein Family Supertree
- Clustering tree for combined AHL & TCS LuxR-type protein collection.
- Distinct separation of AHL from TCS type LuxRs.
- Interjections from one subfamily within uniform segment of the other.

###### AHL-type LuxR Clustering Tree
- Sufficient characterisation of AHL domain allowed evolutionary history exploration for AHL-type LuxRs.
- Separation according to taxonomic belonging.
- Occurrence of interjections.

###### Diversification from Domain Perspective
- Involvement of each domain in influencing evolutionary trajectory - Input for SBD included bigger segment of full-length sequences vs. DBD portion had higher conservation.

#### 3rd Objective Output - Species Level Analysis:

- Log-fold change accounted for different total counts prior to CD-HIT.

- Established the extent of distinct LuxR sequence variance for select species.

- Test for 100% sequence identity had a great number of variants, whereas lower thresholds showed significant reduction - this is seen with proteins that have a role in signalling and control of virulence.

- Genomes possessing multiple homologues for same signal regulate different genes --> growth dependant regulation or fine-tuning.

## Final Remarks 

- Researching the LuxR protein family contributes to the understanding of the “Interaction – Regulation – Outcome” principle at the foundation of microbial behaviour. Additionally, it contributes to fairly sparse documentation of gene expression regulation that results from cell-cell signalling.

- Organisms recognise and constantly adjust to changing situations by sensing environmental and self-produced signals, altering gene expression accordingly. Therefore, success in nature depends upon an ability to perceive and adapt to the surrounding environment, which ultimately highlights the importance of such research.
