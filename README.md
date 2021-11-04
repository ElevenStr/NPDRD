# NPDRD

## About

A non-phylogeny-dependent reassortment detection method for influenza A viruses.

## Usage

### data

The sequences of each segment of the viruses used for reassortment detection are given in FASTA format.

### doc

We also give the accession number of each sequence in XLSX format.

### figure

The figures used in the paper.

### src

Source code used in the experiment. All source code files are executable scripts, which can be run directly in the python interpreter. The total input of the program is: 

* isolateHostClassLocationRankedByTimeHostDetail-6ForAsia.txt: Epidemiological information of the virus, including genomeID, host, location, subtype, year and date.
* seg_Asia.fasta: Sequences of each segment, FASTA format

Reassortment detection can be done by running the following code accordingly. The function of each code is:

* 0_3_SubtypeHostNum.py: Count the host distribution of virus by subtype.
* 0_4_HostNum.py: Count the host distribution of all viruses.
* 0_5_locNum.py: Count the location distribution of all viruses.
* 1_1_CalculateDMk.py: Convert sequence to feature vector.
* 1_2_CalculateDistanceMatrix.py: Calculate eigenvector distance matrix.
* 1_3_DistanceMatrixMSTnetwork.py: Construct a similarity network between individual segment sequences.
* 1_4_CalculateDMkForAllSegment.py: Synthesize the feature vectors of 8 segments of the viral genome into one.
* 1_5_CalculateDistanceMatrixForAllSegment.py: Calculate eigenvector distance matrix for genome.
* 1_6_DistanceMatrixMSTnetworkForAllSegment.py: Construct a similarity network between genome.
* 2_clusteringAgrithom.py: Use SOM to cluster each segment.
* 2_clusteringAgrithomShowResult.py: Use SOM to cluster each segment and display the clustering results of HA and NA segments.
* 3_2_AnalyzeClusteringResultSubtype.py: Analyze whether HA and NA segments classified into the same type are of the same subtype.
* 3_3_AnalyzeSegmentClusterSubtype.py: Count the number of types divided into HA and NA subtypes.
* 4_analyze_clusters.py: Combine cluster classification information with epidemiological information.
* 5_isolatetCombinationsname.py: Add the name of the virus.
* 6_analyze_recombinations.py: Analyze the source of reasssortment for each segment of a specific virus.
* 7_analyzeTypeNetworkReassortment.py: Detect reassortment for each virus in the data set.
* 7_2_SubtypeNum.py: Count the number of genotypes.
* 8_reassortmenttonetwork.py: Form reassortment events into a network.
* 10_MSTnetwork.py: Use genotypes as nodes to construct a reassortment network
* 12_SpecificSubtypeReassortment.py: Analyze the reassortmnet patterns of each subtype in reassortment events

### utils

This folder shows part of the results of our experiment.

* DMk_seg_Asia.txt：The result of feature extraction of seg segment.

* ClusterResultForAsia_seg.txt：The result of clustering seg segment.

* isolatesCombinationsWithNameHostDetail-6ForAsia.xlsx：The epidemiological information and genotype of all viruses.

* reassortmentHistroy3HostDetailForAsia.txt：All detected reassortment events. Each reassortment event starts with '>'. The first line includes the genotype number of the reassortant virus, the number of parental viruses, and the reassortment cost. The second line is the information about the reassortment virus, and the next few lines are the information about the parent virus.

### validation

Traditionally, reassortments are tested based on the nucleotide similarity between the sequence of each segment of the virus. In order to verify the effectiveness of our method, we compared the nucleotide similarity between the sequences in the clustering results. 

* ClusterResultForAsia_MP.txt: The result of clustering MP segment.

* CompareClusterResultWithSimilarity.py: Compare the nucleotide similarity between the sequences in the clustering results.

* MP_Asia.mafft.fasta: The result of multiple sequence alignment of MP segments using MAFFT v7.037.

* TypeSimilarity.txt: Including cluster_type, intra_type_similarity, inter_type_minSimilarity, inter_type_maxSimilarity, inter_type_meanSimilarity and if_inter>intra+0.01. intra_type_similarity is the similarity between sequences within the type. inter_type_minSimilarity is the minimum value of inter-type similarity, inter_type_maxSimilarity is the maximum value of inter-type similarity, if the maximum value of inter-type similarity is 0.01 higher than the intra-class similarity, then if_inter>intra+0.01 is set to True, otherwise it is set to False. 

For MP segment sequences, our method divides them into 402 types, where the intra-type similarity of each type is between 93%-100%. Among them, the intra-type similarity of 326 types is higher than all the inter-type similarities. For the other 76 types, although some of the inter-type similarity exceeds the intra-type similarity, it is basically the same as the intra-type similarity, and the difference in similarity is within 1%. Therefore, our method can group the sequences with high nucleotide similarity together, and further subdivide the sequences with high nucleotide similarity.