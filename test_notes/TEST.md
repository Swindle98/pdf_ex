---
title: {{title}}
authors: {{authorString}}
year: {{year}}
DOI: {{DOI}}
---
## Abstract
{{abstract}}

## Notes

## citations to follow up on.

## PDF Annotations
 ### Orange highlight by SJW on page p:

>TEXT: 
> performance of different assembly approaches, including genomic-, metagenomic- and
20 
transcriptomic-specialized assemblers. We quantified recovery and accuracy rates of each 
21 

>COMMENT:
> 

### Orange highlight by SJW on page T:

>TEXT: 
> The results revealed that none of the investigated tools can accurately capture genomic 
27 
contexts present in samples of high complexity. The transcriptomic assembler Trinity showed 
28 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> analysis of sewage from different parts of the world has revealed that the same ARGs are
52 
found in different genomic backgrounds globally, proving the need to not only identify the 
53 

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  what genomic context they are present. 

>COMMENT:
> 

### Orange highlight by SJW on page T:

>TEXT: 
> The genomic background of an ARG determines co-resistance patterns and mobilization 
55 
potential, both of which can affect the choice of intervention strategies locally and globally
56 
(Munk et al. 2022). For this reason, metagenomic sequencing has been suggested as a 
57 

>COMMENT:
> 

### Orange highlight by SJW on page (:

>TEXT: 
> (Munk et al. 2022). For this reason, metagenomic sequencing has been suggested as a
57 
possible means for surveillance of AMR not only in sewage (Hendriksen et al. 2019; 
58 
Pruden et al. 2021), but also in the environment in general (Bengtsson-Palme et al. 
59 
2023). Current high-throughput sequencing platforms produce hundreds of millions of rea
60 

>COMMENT:
> 

### Orange highlight by SJW on page r:

>TEXT: 
> reconstructed into longer stretches called contigs, 

>COMMENT:
> 

### Red highlight by SJW on page (:

>TEXT: 
> (Vollmers et al. 2017; Meyer et al. 2022). 

>COMMENT:
> These might be useful papers for contig/ genome assembly

### Red highlight by SJW on page  :

>TEXT: 
>  de Bruijn graph approach

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  based on reconstructing graphs to represent k-mers present in a set of reads

>COMMENT:
> 

### Orange highlight by SJW on page f:

>TEXT: 
> followed by traversing these graphs and identifying the most probable path representing a
73 
contig. Converting a graph path into a contig is not a trivial task. Metagenomic samples 
74 

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  Converting a graph path into a contig is not a trivial task

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> contig. Converting a graph path into a contig is not a trivial task. Metagenomic samples
74 
typically contain an unknown number of species with unknown abundance distributions.
75 

>COMMENT:
> 

### Orange highlight by SJW on page t:

>TEXT: 
> the case of related species, sequences can carry similar sets of k-mers resulting in complex
76 
assembly graphs. This is further complicated by conserved repetitive regions (such as ARGs
77 

>COMMENT:
> 

### Orange highlight by SJW on page g:

>TEXT: 
> genomic contexts typically results in highly complex branched assembly graphs

>COMMENT:
> 

### Orange highlight by SJW on page g:

>TEXT: 
> graph into multiple short contigs (Bengtsson-Palme et al. 2017). For metagenomic 
81 
analysis targeting ARGs, this means that sometimes all contextual information regarding the
82 
taxonomic origin or mobility of a gene will be lost, which can potentially lead to 
83 
misinterpretation of the results. 
84 

>COMMENT:
> 

### Orange highlight by SJW on page T:

>TEXT: 
> There are several studies benchmarking metagenomic assembly tools, such as the “Critical 
86 
Assessment of Metagenome Interpretation” (CAMI) challenge (Wang et al. 2019; Meyer et 
87 
al. 2022). The focus of these studies has largely been on the ability of assemblers to 
88 

>COMMENT:
> 

### Orange highlight by SJW on page d:

>TEXT: 
> distinguish evolutionary related organisms in complex microbial samples. There is also a 
89 
study by Brown et al. (2021) assessing different assemblers for contextualization of ARGs
90 
using co-occurrence of ARGs and mobile genetic elements (MGEs) on assembled contigs 
91 
as a proxy. However, a critical evaluation of currently available short-read assemblers on 
92 

>COMMENT:
> 

### Orange highlight by SJW on page i:

>TEXT: 
> in metagenomic assemblies, as they are often present in multiple contexts, can be
95 
surrounded by various forms of repeat regions, and can be present on plasmids wi
96 

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> surrounded by various forms of repeat regions, and can be present on plasmids with varying 
96 
degrees of copy numbers. A specific investigation of how assemblers handle these genes is 
97 

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  ARGs in the correct genomic context from metagenomic data

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> assembled the test datasets and evaluated performance of several tools (Velvet, SPAdes, 
107 
metaSPAdes, MEGAHIT, Trinity, Ray) with respect to their accuracy of recovering the 
108 

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> samples. Furthermore, they call into question some of the practices currently used for
113 
quantification of ARGs based on metagenomic sequencing. 
114 

>COMMENT:
> 

### Orange highlight by SJW on page E:

>TEXT: 
> Evaluation using simulated reads

>COMMENT:
> They took metagnemoes from Sara and added the arg plasmid to the reads.
only used high matechted.    For each arg 5 plasmids of differi7ng sizes was selected.
Insilicoseq was then used to gerate in simulated reads.


### Orange highlight by SJW on page W:

>TEXT: 
> We also performed the same analyses in a simplified scenario with only two plasmids for
208 
each of two resistance genes (blaNDM-1 and aph(3’’)-Ib), to test whether the reduced 
209 
complexity would improve the assembly performance. We performed this test with 
210 

>COMMENT:
> 

### Orange highlight by SJW on page T:

>TEXT: 
> Trinity (Table 2, Figure S1). Trinity outperformed all the tools for the total assembled length
262 
and the number of reconstructed contigs at all coverages. In contrast, metaSPAdes 
263 

>COMMENT:
> 

### Orange highlight by SJW on page T:

>TEXT: 
> The results showed that MEGAHIT, metaSPAdes and Trinity managed to capture almost all
307 
ARGs at all coverages. However, the MEGAHIT contigs containing ARGs were on average 
308 

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> contrast, Trinity performed consistently better at all coverages, with more than 50% of 
310 
contigs containing the full length ARG sequences (Figure 3). Among the genome 
311 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> ay had the best performance in terms of reconstructing full ARGs

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> assemblers, Ray had the best performance in terms of reconstructing full ARGs, while Velvet 
312 
reconstructed only one full ARG out of 3724 assembled ARG-containing contigs, with the 
313 

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  we investigated the number and length of correctly assembled contexts

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  3B shows that Trinity performed better in comparison

>COMMENT:
> 

### Orange highlight by SJW on page p:

>TEXT: 
> performance across the coverages. Notably, the performance of Ray was rather similar to
329 
that of metaSPAdes. In some cases, Ray produced even longer correct contigs despite 
330 

>COMMENT:
> 

### Orange highlight by SJW on page M:

>TEXT: 
> MEGAHIT produced only two correct contigs at lower coverages

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> surprising is that from a total number of 5 different genomic contexts per resistance gene 
333 
present in the sample on average only three original contexts (12%) were correctly captured
334 
by any of the assembler. These contexts corresponded to plasmids of different sizes 
335 

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> suggesting that the total length of plasmids did not determine assembly success, but rather
336 
features surrounding the particular genes (Figure S2). 
337 

>COMMENT:
> 

### Red highlight by SJW on page  :

>TEXT: 
>  TriMetAss

>COMMENT:
> What is this?
An extension for trinity -it essentiallyre-runs trinity until certain conditions are met..

Why us spades not trinity.

### Orange highlight by SJW on page r:

>TEXT: 
> revealed that in general TriMetAss output a few more correctly assembled contigs containing 
341 
full ARGs. Importantly, these contigs were on average 2000 bp longer than initial SPAdes 
342 

>COMMENT:
> 

### Orange highlight by SJW on page f:

>TEXT: 
> full ARGs. Importantly, these contigs were on average 2000 bp longer than initial SPAdes
342 
contigs. As a drawback, TriMetAss also produced more misassembled contigs in 
343 

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> contigs. As a drawback, TriMetAss also produced more misassembled contigs in
343 
comparison to SPAdes output (Figure 3A). 
344 

>COMMENT:
> 

### Orange highlight by SJW on page A:

>TEXT: 
> All assemblers reconstructed large contigs spanning in some cases half of the plasmid
363 
sequence (as shown on the example of AP023079 plasmid; Figure 4), but broke exactl
364 

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> sequence (as shown on the example of AP023079 plasmid; Figure 4), but broke exactly at 
364 
the beginning of ARG sequence. The complexity of assembly graphs also increased with 
365 

>COMMENT:
> 

### Orange highlight by SJW on page t:

>TEXT: 
> the beginning of ARG sequence. The complexity of assembly graphs also increased with 
365 
more coverage, but for some tools, such as SPAdes and metaSPAdes, additional coverage
366 
helped to resolve ambiguous branching and reconstruct longer contigs, while for MEGAHIT 
367 

>COMMENT:
> 

### Orange highlight by SJW on page h:

>TEXT: 
> helped to resolve ambiguous branching and reconstruct longer contigs, while for MEGAHIT
367 
increased coverage resulted in profound fragmentation. The assembly graphs also made it 
368 

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> clear that Trinity, as a transcriptomic assembler, utilizes a different approach in comparison
369 
to the other tools, resulting in very characteristic assembly graph patterns. 
370 

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  validate the findings from the simulated metagenome data, 

>COMMENT:
> 

### Orange highlight by SJW on page w:

>TEXT: 
> with a real dataset. For this, we used PacBio reads containing full ARGs as a reference for
389 
the contigs assembled from a corresponding short-read data set derived from the same 
390 

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> samples

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> samples (see Materials and Methods for details). In this dataset, we annotated ARGs on the
391 
PacBio reads, which resulted in 18 unique ARGs (98% identity and 100% coverage) found 
392 
on 125 PacBio reads (32 reads carried more than one ARG). This set of PacBio reads was 
393 

>COMMENT:
> 

### Orange highlight by SJW on page r:

>TEXT: 
> reads to assess the correctness of genomic context. In this comparison, Trinity had the
397 
highest number of correct contigs matching the reference PacBio reads, and these cont
398 

>COMMENT:
> 

### Orange highlight by SJW on page S:

>TEXT: 
> S1). In contrast, MEGAHIT, metaSPAdes and SPAdes assembled half as many contigs with
400 
on average shorter length than Trinity. To check if another approach using TriMetAss could 
401 

>COMMENT:
> 

### Orange highlight by SJW on page A:

>TEXT: 
> All together, 55 unique ARGs were identified from all the assembled contigs by all the short-
415 
read tools and PacBio reads, with only 6 ARGs common between all of them (Figure 6B). 
416 

>COMMENT:
> 

### Orange highlight by SJW on page I:

>TEXT: 
> Interestingly, Trinity, SPAdes and metaSPAdes recovered several additional ARGs (full or
417 
truncated) not present on PacBio reads. Importantly, annotation of short reads alone 
418 

>COMMENT:
> 

### Orange highlight by SJW on page t:

>TEXT: 
> truncated) not present on PacBio reads. Importantly, annotation of short reads alone
418 
resulted in 85 matches (80% coverage and 98% identity). 
419 

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  short-reads to assembled contigs

>COMMENT:
> 

### Orange highlight by SJW on page R:

>TEXT: 
> ResFinder database to quantify ARG abundances directly from the reads. 

>COMMENT:
> 

### Orange highlight by SJW on page d:

>TEXT: 
> direct comparison between the two prevailing approaches to quantify ARGs in metagenomic
424 
data (Bengtsson-Palme et al. 2017). This analysis revealed that for some ARGs, results are 
425 

>COMMENT:
> Check this paper out.

### Orange highlight by SJW on page d:

>TEXT: 
> data (Bengtsson-Palme et al. 2017). This analysis revealed that for some ARGs, results are
425 
very similar between approaches, such as for several tetracycline genes (e.g., tetQ and 
426 
tetW), as well as the erythromycin resistance gene ermB and aminoglycoside resistance 
427 
gene aph(3’)-III (Figure 6C). However, several ARGs were detected only by mapping reads 
428 

>COMMENT:
> 

### Orange highlight by SJW on page g:

>TEXT: 
> gene aph(3’)-III (Figure 6C). However, several ARGs were detected only by mapping reads
428 
directly to the ResFinder database and were missing completely from the assembly-based 
429 
approach (e.g., tetB, blaTEM-104 and ermT). 
430 

>COMMENT:
> 

### Orange highlight by SJW on page e:

>TEXT: 
> e (Su et al. 2017; Lee et al. 2021

>COMMENT:
> Look into these papers that are addressing metagenommic sequencing 

### Orange highlight by SJW on page r:

>TEXT: 
> reconstructed genomes. A few studies have looked into the benefits of using long-reads for 
444 
improving metagenomic assemblies (Bertrand et al. 2019; Latorre-Pérez et al. 2020; Xie
445 
et al. 2020). Within the framework of the CAMI challenge, Sczyrba et al. (2017) and 
446 

>COMMENT:
> 

### Orange highlight by SJW on page e:

>TEXT: 
> et al. 2020). Within the framework of the CAMI challenge, Sczyrba et al. (2017) and
446 
Meyer et al. (2022) evaluated assembly performance, but largely for the purpose of 
447 
taxonomic profiling. However, only a few studies have looked into the implications of 
448 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> assembler choice for the inference of gene contexts and gene abundances from
449 
metagenomic assemblies. Brown et al. (2021) used resistome risk score based
450 

>COMMENT:
> 

### Orange highlight by SJW on page m:

>TEXT: 
> metagenomic assemblies. Brown et al. (2021) used resistome risk score based on co-
450 
occurrences of ARGs, MGEs and pathogen gene markers on the same contig to evaluate
451 
convergence of biological output produced by different assemblers. Another paper by 
452 

>COMMENT:
> Add to reading list.

### Orange highlight by SJW on page G:

>TEXT: 
> Galata et al. (2021) sho

>COMMENT:
> Read.

### Orange highlight by SJW on page Y:

>TEXT: 
> Yorki et al. (2023) fo

>COMMENT:
> Read,

### Orange highlight by SJW on page U:

>TEXT: 
> Unfortunately, the results of these studies are often contradictory, 

>COMMENT:
> 

### Orange highlight by SJW on page i:

>TEXT: 
> importantly, despite being mentioned by several studies, the impact of assembler choice on
459 
the biological interpretability has not been well explored. 
460 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> ability to correctly reconstruct the genomic contexts surrounding these ARGs. Metagenomic
464 
assemblers are optimized to deal with sequence data from samples containing multiple 
465 
species in different abundances, and therefore their performance was of primary interest. In 
466 

>COMMENT:
> 

### Orange highlight by SJW on page t:

>TEXT: 
> the simulated scenario, metaSPAdes considerably outperformed MEGAHIT in terms of 
467 
number of contigs containing full ARG sequences, with MEGAHIT predominantly produ
468 

>COMMENT:
> 

### Orange highlight by SJW on page n:

>TEXT: 
> number of contigs containing full ARG sequences, with MEGAHIT predominantly producing 
468 
short contigs (on average 284 bp long) with truncated ARGs. This could have severe 
469 

>COMMENT:
> 

### Orange highlight by SJW on page 2:

>TEXT: 
> 2020; Chen et al. 2022; Yi et al. 2022; Ke et al. 2023). Even if we were to apply the most 
473 
allowing cut-off of 300 bp to the MEGAHIT results, 99% of contigs containing ARGs would 
474 
be filtered out, resulting in a considerable underestimation of the resistome in the sample. 
475 

>COMMENT:
> 

### Orange highlight by SJW on page d:

>TEXT: 
> dataset. For a real dataset, there is no way to know the true complete repertoire of ARGs. 
480 
Therefore, we used PacBio reads containing full ARGs as a reference for the contigs 
481 

>COMMENT:
> 

### Orange highlight by SJW on page 6:

>TEXT: 
> 6B). The number of unique ARGs captured by the different assemblers varied greatly, from
484 
44 identified by Trinity to 20 captured by metaSPAdes. Similarly to the assemblies from the
485 

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> simulated data, 52% of the MEGAHIT contigs containing ARGs would have been filtered out 
486 
using a 300 bp length cut-off, showing that this undesired effect is not simply a matter of our 
487 

>COMMENT:
> 

### Orange highlight by SJW on page m:

>TEXT: 
> methodological choices for simulating data. Interestingly, Trinity, SPAdes and metaSPAdes
488 
recovered several additional ARGs not present on the PacBio reads. In this particular case, 
489 
the short read dataset was sequenced three times deeper than the PacBio dataset, 
490 
suggesting that the long read dataset did not have sufficient depth to pick up all the ARGs. 
491 

>COMMENT:
> 

### Orange highlight by SJW on page T:

>TEXT: 
> That said, the two approaches would probably perform similarly well at comparable
492 
sequencing depth, but the costs of long read sequencing would – at present – be 
493 
considerably higher. 
494 

>COMMENT:
> 

### Orange highlight by SJW on page W:

>TEXT: 
> Worryingly, only six ARGs were commonly identified by all tools, including two
496 
aminoglycoside, two tetracycline and two erythromycin resistance genes. Cons
497 

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  blaOXA, 

>COMMENT:
> Missing in all short read tools.

### Orange highlight by SJW on page t:

>TEXT: 
> those were rare genes that did not get sufficient coverage to be assembled by the short-read
501 
sequencing effort and therefore are missing from the resulting assembly. An alternative 
502 

>COMMENT:
> 

### Orange highlight by SJW on page h:

>TEXT: 
> hich resulted in identification of 85 unique ARGs. 

>COMMENT:
> 

### Orange highlight by SJW on page f:

>TEXT: 
> far surpassed the total number of ARGs identified by mapping reads to the assembled
507 
contigs, as well as on PacBio reads alone. Reads are typically much shorter than conti
508 

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> contigs, as well as on PacBio reads alone. Reads are typically much shorter than contigs
508 
and might map spuriously to several different targets causing false positives. At the same
509 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> approach does not require coverage of the entire ARG in order to detect it, which

>COMMENT:
> 

### Orange highlight by SJW on page m:

>TEXT: 
> may be crucial for the detection of rare ARGs. As many clinically relevant ARGs to last resort 
511 
antibiotics are typically rare in most microbiomes, the increase of detection ability is highly 
512 

>COMMENT:
> 

### Orange highlight by SJW on page i:

>TEXT: 
> important for e.g. monitoring of high-risk ARGs (Abramova et al. 2023; Bengtsson-Palme
513 
et al. 2023). This finding also highlights the importance of not basing gene catalogs only on 
514 

>COMMENT:
> Citations for short read alignments might be worth a look.

### Orange highlight by SJW on page d:

>TEXT: 
> drastically different. It is important to mention though that the number of correctly assembled
519 
full-length ARGs on its own is not always a good measure of assembler performance, if the 
520 

>COMMENT:
> 

### Orange highlight by SJW on page e:

>TEXT: 
> est of the output contigs contain misassembled sequences. 

>COMMENT:
> 

### Orange highlight by SJW on page u:

>TEXT: 
> underscoring the importance of assembly tools achieving a good ability to stitch reads 
523 
together while still maintaining strict precision in terms of obtaining the correct assembled
524 
contexts.  
525 

>COMMENT:
> 

### Orange highlight by SJW on page O:

>TEXT: 
> Obtaining a correctly assembled full or even truncated ARG might be enough for certain 
528 
applications, for example when estimating the ARG diversity in a sample. However, for the 
529 
purpose of host taxonomic inference or mobility assessment of a given ARG, it is necessary
530 
to look into the genomic context around it. After assembling short-reads data we compared 
531 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> assembled genomic contexts. In this comparison, Trinity had the highest number of correct 
534 
contigs matching the reference in both cases, and the Trinity contigs were on average longer
535 
than the ones reconstructed by the other tools (Figure 3B and Table S1). Trinity is a 
536 

>COMMENT:
> 

### Orange highlight by SJW on page t:

>TEXT: 
> transcriptome assembler, specifically designed to assemble transcript variants resulting from
537 
alternative splicing or gene duplication (Grabherr et al. 2011). Instead of trying to 
538 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> alternative splicing or gene duplication (Grabherr et al. 2011). Instead of trying to 
538 
reconstruct the full graph, it starts with assembling disjoint transcription loci which are further
539 
converted into de Brujin graphs and pruned based on read support. The difference to the 
540 

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> contigs are represented by nodes of more even coverage and less complexity in comparison
542 
to graphs resulting from metaSPAdes and MEGAHIT assemblies. The original MEGAHIT 
543 

>COMMENT:
> 

### Orange highlight by SJW on page  :

>TEXT: 
>  MEGAHIT

>COMMENT:
> 

### Orange highlight by SJW on page p:

>TEXT: 
> publication (Li et al. 2015) showed that its performance becomes better with increased
544 
coverage (from 10x to 100x) in terms of N50 value, largest alignment length and number
545 

>COMMENT:
> 

### Orange highlight by SJW on page m:

>TEXT: 
> misassemblies. However, we observed that in our simulated data scenario MEGAHIT
546 
performed best at lower coverages (0.5x and 1x; Figure 2 and 3), showing extensive 
547 

>COMMENT:
> 

### Orange highlight by SJW on page p:

>TEXT: 
> performed best at lower coverages (0.5x and 1x; Figure 2 and 3), showing extensive 
547 
fragmentation at the higher coverages as revealed by the highly branching graph (Figure 4). 
548 

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> said, due to the rather short length of the MEGAHIT and metaSPAdes contigs they match to
553 
several different PacBio reads (different genomic contexts) implying that their length is not 
554 
sufficient to unambiguously decipher the taxonomic origin of the ARGs they carry. Taking 
555 

>COMMENT:
> 

### Orange highlight by SJW on page d:

>TEXT: 
> different approaches. It was surprising to observe that quantification by mapping reads back
567 
to the ResFinder database revealed in general lower abundance levels than when 
568 
calculating abundance by mapping to the assembled contigs (Figure 5A). The ResFinder 
569 

>COMMENT:
> 

### Orange highlight by SJW on page (:

>TEXT: 
> (e.g. blaNDM-1, tet(M)-6). We hypothesized that the observed results is a consequence of 
572 
variant ”spill-over” effect when the lengths of the reads were insufficient to differentiate 
573 
between the variants. 
574 

>COMMENT:
> 

### Orange highlight by SJW on page A:

>TEXT: 
> A possible solution often used to reduce the impact of this variant ”spill-over” effect is to 
575 
cluster all the similar variants and retain only a single representative sequence. We did this
576 
in an additional test using the ResFinder database clustered to 90% identity (Figure 5B). 
577 

>COMMENT:
> 

### Orange highlight by SJW on page v:

>TEXT: 
> variants instead of a particular variant. Despite the somewhat lower resolution, using a 
579 
clustered database yielded abundance estimates for all the spiked-in genes comparable to
580 
those estimated based on the mapping to assembled contigs.  
581 

>COMMENT:
> 

### Orange highlight by SJW on page I:

>TEXT: 
> In the real-case scenario, the results revealed that several ARGs were quantified only by 
583 
mapping short reads directly to the ResFinder database and were missing completely from
584 
the assembly-based approach (Figure 6C). Some of those are clinically relevant genes suc
585 

>COMMENT:
> 

### Orange highlight by SJW on page l:

>TEXT: 
> low-abundant gene that did not have enough coverage to be assembled by short-read
590 
assemblers and was not picked-up by long-read sequencing. 
591 

>COMMENT:
> 

### Orange highlight by SJW on page A:

>TEXT: 
> ARG diversity and abundance. Assembled contigs provide a good resolution in terms of 
594 
identification and quantification of specific ARG variants as well as their genomic context, but 
595 
at the same time this approach misses rare ARGs due to insufficient coverage. In contrast, 
596 

>COMMENT:
> 

### Orange highlight by SJW on page d:

>TEXT: 
> direct mapping of short reads spuriously aligns them to different ARG variants, leading to an
597 
overestimation of the resistome diversity in a sample. There are several studies suggesting 
598 

>COMMENT:
> 

### Orange highlight by SJW on page i:

>TEXT: 
> interventions (Zhang et al. 2021; Munk et al. 2022). Therefore, using read-based 
601 
quantification alone to determine ARG abundance in a sample can result in a misleading 
602 
interpretation regarding which particular variant is present and abundant in a sample. Thi
603 

>COMMENT:
> 

### Orange highlight by SJW on page I:

>TEXT: 
> Interestingly, not all of the ARGs were equally easy to assemble (Figure 2), with aph(3’’)-lb
610 
being the most difficult gene to fully assemble among the ones spiked-in. This is a good 
611 

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> contexts with differential coverage in the same sample. On the original plasmids, the 
613 
aminoglycoside resistance gene aph(3’’)-lb was surrounded by insertion sequences, several
614 
other ARGs and recombinases, all contributing to making it difficult to assemble the region 
615 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> around the gene correctly. Not surprisingly, the assembly graphs showed that this problem
616 
becomes more pronounced with increasing coverage (Figure 4, the brush-like structures 
617 

>COMMENT:
> 

### Orange highlight by SJW on page g:

>TEXT: 
> genomic contexts present in a sample. The transcriptomic assembler Trinity, despite being 
637 
designed for a different purpose, is an interesting alternative as it showed better 
638 
performance in reconstructing longer and fewer contigs matching unique genomic contexts, 
639 
which can be beneficial for deciphering the taxonomic origin of ARGs. Therefore, for 
640 

>COMMENT:
> 

### Orange highlight by SJW on page F:

>TEXT: 
> Finally, we have made one very important observation: our results show that using a length
654 
filtering threshold for the assembled contigs can contribute to a dramatic loss of ARG-
655 
containing contigs. This is due to that ARGs seem to be over-represented among 
656 

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> sample. We suggest, therefore, to annotate ARGs on contigs before filtering on the length, to
660 
have an idea of what is being filtered out. When it comes to ARG abundance quantification, 
661 

>COMMENT:
> 

### Orange highlight by SJW on page a:

>TEXT: 
> ability, but risks increasing false positive detections. One alternative approach is to cluster 
663 
the reference database to reduce the number of ARG variants. This will lead to a lower 
664 
resolution at the ARG variant level, but will on the other hand reduce the risks for biasing the
665 
picture of ARG prevalence. Another way could be to assign a threshold for the minimal 
666 

>COMMENT:
> Consider this !

### Orange highlight by SJW on page I:

>TEXT: 
> In conclusion, as researchers we should not blindly trust the output of our bioinformatics
670 
tools. If tools corroborate each other, one can put more trust into their output. If not, one
671 

>COMMENT:
> 

