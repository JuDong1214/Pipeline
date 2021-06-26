# **Tool for Annotation and Classification of Genes and Variants (TAGCVar)**
Our developed pipeline (TACGVar) efficiently annotates large numbers of variants files and helps estimate specific tissue enrichment over the association of miRNA.

# **Overview**
![pasted image 0](https://user-images.githubusercontent.com/80075365/123517696-76a2e400-d670-11eb-917d-bb1560d1e560.png)

# **Publication and Citation**
Paper still in progress

# **Usage**
**_Step 1: Annovar Annotaion_**
**Input**
This part of the pipeline is used to create an ANNOVAR formatted output file so that the 3' UTR Prevalenece Script can use it as an input file. The input file we used was a SNP list for easy processing. A shortened version follows,
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

but the input file should be in the format of .sumstats.add.txt and looks as follows;
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
**Output**
The ANNOVAR output result is as follows; [image]

The
