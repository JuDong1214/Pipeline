# **Tool for Annotation and Classification of Genes and Variants (TAGC-Var)**
Our developed pipeline (TACG-Var) efficiently annotates large numbers of variants files and helps estimate specific tissue enrichment over the association of miRNA.

# **Overview**
![pasted image 0](https://user-images.githubusercontent.com/80075365/123517696-76a2e400-d670-11eb-917d-bb1560d1e560.png)

# **Publication and Citation**

Song et al., Identification of functionally important miRNA targeted genes associated with child obesity trait in genome-wide association studies
, In revison at BMC Medical Genomics

# **Requirements**
* python 3.X
* intertools
* subprocess
* shelx
* glob
* pandas


# **Usage**
## **Step 1: Annovar Annotaion**
### **Input**
This part of the pipeline is used to create an ANNOVAR formatted output file so that the 3' UTR Prevalenece Script can use it as an input file. One of the many input files we used was the PBC trait SNP list (for easy processing). A shortened version follows,
```rs1775421
rs1775420
rs1818038
rs770685
rs12116874
rs707583
rs707582
rs770718
rs11260662
rs9439587
rs9329417
rs10157819
rs9439605
rs12143743
```

but the input file should be in the format of .sumstats.add.txt. An example follows;
```[kaiwang@biocluster ~/]$ cat example/ex1.avinput
1 948921 948921 T C comments: rs15842, a SNP in 5' UTR of ISG15
1 1404001 1404001 G T comments: rs149123833, a SNP in 3' UTR of ATAD3C
1 5935162 5935162 A T comments: rs1287637, a splice site variant in NPHP4
1 162736463 162736463 C T comments: rs1000050, a SNP in Illumina SNP arrays
1 84875173 84875173 C T comments: rs6576700 or SNP_A-1780419, a SNP in Affymetrix SNP arrays
1 13211293 13211294 TC - comments: rs59770105, a 2-bp deletion
1 11403596 11403596 - AT comments: rs35561142, a 2-bp insertion
1 105492231 105492231 A ATAAA comments: rs10552169, a block substitution
1 67705958 67705958 G A comments: rs11209026 (R381Q), a SNP in IL23R associated with Crohn's disease
2 234183368 234183368 A G comments: rs2241880 (T300A), a SNP in the ATG16L1 associated with Crohn's disease
16 50745926 50745926 C T comments: rs2066844 (R702W), a non-synonymous SNP in NOD2
16 50756540 50756540 G C comments: rs2066845 (G908R), a non-synonymous SNP in NOD2
16 50763778 50763778 - C comments: rs2066847 (c.3016_3017insC), a frameshift SNP in NOD2
13 20763686 20763686 G - comments: rs1801002 (del35G), a frameshift mutation in GJB2, associated with hearing loss
13 20797176 21105944 0 - comments: a 342kb deletion encompassing GJB6, associated with hearing loss
```
Citation: Kai Wang, e. (2021). Prepare Input Files - ANNOVAR Documentation. Annovar.openbioinformatics.org. Retrieved 26 June 2021, from https://annovar.openbioinformatics.org/en/latest/user-guide/input/.

### **Output**
The ANNOVAR output result is as follows;
![PBC](https://user-images.githubusercontent.com/80075365/123524019-aca68f00-d695-11eb-96e3-8dfb2cdd8df0.png)

## **Step 2: 3' UTR Variant Prevalence**
### **Input**
To get the number of each region (Intergenic, Intronice, 3'UTR, etc...) like in row F of the ANNOVAR annotated output files, we have generated a python script to count the number of each regions in the variants of each trait. The input files would be the 31 traits located in the VariantsList folder. The input files would look like the picture below, and the python script would list the number of each region in column 7.
![3'utr](https://user-images.githubusercontent.com/80075365/123525530-60604c80-d69f-11eb-8b5f-f44780ef657c.png)

### **Output**
The output would look similar to this

![3' utr putty](https://user-images.githubusercontent.com/80075365/123525444-a963d100-d69e-11eb-824a-1b99c55df787.png)

## **Step 3: Common Genes**
### **Input**
This common genes python script takes in Genelists for two individual traits files and compares them to find the number of common genes and the gene names. The input files would be the two genelists, each representing a different trait, from the GeneList folder. A shortened version of ONE of the input file will look like the list below. Note that you need two of these input files to compare
```CCL22
ESM1
KCNV1
MMP19
RPRD2
TMTC1
ZNF263
CD40
DAGLA
FAM171B
PPP1R1B
TUSC1
KCNA7
GOLGB1
NEK1
RAB5B
THAP6
```
### **Output**
The output would be printed in terminal, and it will include the number of common genes between the two traits in the first line and the names of those genes in the second line:
```5
ZNF263 CD40 DAGLA FAM171B PPP1R1B
```

## **Step 4: Common Variants**
This common genes python script takes in ANNOVAR formatted csv or excel files with variants info for two individual traits and compares them to find the number of common variants and the variant locations. A shortened version of ONE of the the input file will look like the list below. Note that you need two of these input files to compare, and the inputs must be csv or excel files. 
```	Chr	Start	End	Ref	Alt	Func.refGene	Gene.refGene
25939	chr1	149931541	149931541	G	A	intronic	OTUD7B
25940	chr1	149938898	149938898	T	C	intronic	OTUD7B
25941	chr1	149943784	149943784	T	C	intronic	OTUD7B
25942	chr1	149955163	149955163	G	A	intronic	OTUD7B
25943	chr1	149968717	149968717	A	G	intronic	OTUD7B
25944	chr1	149989434	149989434	T	C	intergenic	OTUD7B;VPS45
25945	chr1	149991147	149991147	C	T	intergenic	OTUD7B;VPS45
25946	chr1	149995979	149995979	A	C	intergenic	OTUD7B;VPS45
25947	chr1	150000165	150000165	A	G	intergenic	OTUD7B;VPS45
25948	chr1	150001721	150001721	T	G	intergenic	OTUD7B;VPS45
25949	chr1	150001899	150001899	A	G	intergenic	OTUD7B;VPS45
25950	chr1	150008790	150008790	T	C	intergenic	OTUD7B;VPS45
25951	chr1	150019580	150019580	G	A	intergenic	OTUD7B;VPS45
```
### **Output**
The output would be printed in terminal, and it will include the number of common variants between the two traits in the first line and the location of the variants in the following lines:
```3
chr1	149931541
chr1	149938898
chr1	149968717
```
## **Step 5: Integrated Bash Script**
We have developed a Bash script to run all the python scripts all together. You are able to put all input files into one directory and this unix code will call all the python codes and run it through the input files.

The output should look like the following images:

![bashputtypic](https://user-images.githubusercontent.com/80075365/123982796-538a7400-d991-11eb-837e-c97d3118f09a.png)
![bashputtypic2](https://user-images.githubusercontent.com/80075365/123982996-83d21280-d991-11eb-8bd9-0202a1037bf1.png)

**Note: The number of common genes and variants will be outputted, but the list of the genes and variants will not be! If the list of common genes and variants is needed, please use the python scripts individially.**

## **Acknowledgements** 
The Tool for Annotation and Classification of Genes and Variants (TAGC-Var) recognizes these works:
  * [Pinpointing miRNA and genes enrichment over trait-relevant tissue network in Genome-Wide Association Studies](https://link.springer.com/article/10.1186/s12920-020-00830-w)
  * [GTEx]
