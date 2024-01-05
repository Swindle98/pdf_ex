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
 ### Orange highlight by Sam Windle on page k:

>TEXT: 
> keystone species whose removal can cause a dramatic shift in microbiome 
structure and functioning. Yet, an efficient method to systematically ident

>COMMENT:
> 

### Orange highlight by Sam Windle on page  :

>TEXT: 
>  keystone species identification (DKI) framework 

>COMMENT:
> 

### Orange highlight by SJW on page t:

>TEXT: 
> this habitat. The well-trained deep-learning model enables us to quantify 
the community-specific keystoneness of each species in any microbiome 
sample from this habitat by conducting a thought experiment on species 
removal. We systematically validated this DKI framework using synthetic 

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> community specificity. The presented DKI framework demonstrates the 
power of machine learning in tackling a fundamental problem in community 
ecology, paving the way for the data-driven management of complex 
microbial communities.

>COMMENT:
> 

### Orange highlight by SJW on page k:

>TEXT: 
> keystone species has its roots in food web ecology

>COMMENT:
> 

### Orange highlight by SJW on page t:

>TEXT: 
> that is, a keystone species is a species that has a disproportionately large 
effect on the stability of the community relative to its abundance1,2.

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> can be classified into two approaches: experimental manipulations
and statistical comparisons4.

>COMMENT:
> 

### Orange highlight by SJW on page k:

>TEXT: 
> keystone species5–9. Yet, the keystone species identification approaches 
developed for macro ecosystems are challenging to apply to large,
complex microbial communities5–9. For experimental manipulations, 

>COMMENT:
> 

### Orange highlight by SJW on page c:

>TEXT: 
> complex microbial communities5–9. For experimental manipulations, 
targeted removal of each species in a complex community is impos-
sible with current antimicrobial techniques, not to mention the corre-

>COMMENT:
> 

### Orange highlight by SJW on page s:

>TEXT: 
> such as the human gut microbiome. As for statistical comparisons, 
finding two communities that differ by just one species is challeng-
ing, especially for complex host-associated microbial communities 

>COMMENT:
> 

### Orange highlight by Sam Windle on page o:

>TEXT: 
> one may consider directly inferring a population dynamics model to 
predict the temporal behaviour of microbial communities and then
identify keystone species through numerical simulations of targeted 
species removal. Yet, model misspecification and the requirement for

>COMMENT:
> 

### Orange highlight by Sam Windle on page h:

>TEXT: 
> high-quality absolute abundance data13–15 

>COMMENT:
> 

### Orange highlight by Sam Windle on page m:

>TEXT: 
> methods limit their application for identifying keystone species in
large, complex microbial communities.

>COMMENT:
> 

### Orange highlight by Sam Windle on page A:

>TEXT: 
> A recent numerical study16 claimed that those highly con-
nected (that is, ‘hubs’) and high-betweenness-centrality species in 
the microbial correlation network are keystone species of microbial 
communities6,17. Despite the popularity and interpretability of the 

>COMMENT:
> 

### Orange highlight by Sam Windle on page a:

>TEXT: 
> at least two reasons. First, edges in microbial correlation networks
do not represent direct ecological interactions but just statistically 
significant co-occurrences or mutual exclusions of species. Second, 

>COMMENT:
> 

### Orange highlight by Sam Windle on page t:

>TEXT: 
> the impact of a species’ removal naturally depends on the resident
community. This underscores a fundamental challenge in keystone

>COMMENT:
> 

### Orange highlight by Sam Windle on page s:

>TEXT: 
> species identification—the community specificity, that is, a spe-
cies may be a keystone in one community but not necessarily a key-
stone in another community, which is completely ignored based on

>COMMENT:
> This is very important


### Red highlight by Sam Windle on page S:

>TEXT: 
> So far, very few microbial species have been experimentally con-
firmed as keystones5,18–20. An efficient method to systematically identify

>COMMENT:
> 

### Orange highlight by Sam Windle on page b:

>TEXT: 
> be a keystone. In this Article, we first proposed an operational definition 
of keystoneness for microbial species on the basis of commonly availa-
ble relative abundance data. Then, we proposed a data-driven keystone

>COMMENT:
> 

### Orange highlight by Sam Windle on page b:

>TEXT: 
> ble relative abundance data. Then, we proposed a data-driven keystone 
species identification (DKI) framework to compute the keystoneness. 

>COMMENT:
> 

### Orange highlight by Sam Windle on page t:

>TEXT: 
> the species assemblage of the community s is represented by a binary 
vector z ∈ {0, 1}
N whose ith entry zi is 1 (or 0) if species i is present in 
(or absent from) s. The microbial composition or taxonomic profile of 
 

>COMMENT:
>  This is a mutldimensional vector that only has to options 1 or 0. N would be the number of species and i is a random niumber, and it’s presece in that community.


### Orange highlight by Sam Windle on page W:

>TEXT: 
> We emphasize that the structural (or functional) keystoneness
defined here is community-specific, which is fundamentally differ-
ent from those topological indices used in the food web and other 
ecological systems26.

>COMMENT:
> 

### Orange highlight by Sam Windle on page s:

>TEXT: 
> s ∈ 𝒮𝒮
munity of the habitat. We assume that the collected samples roughly 
represent the steady states of the local communities so that they can
be used to learn the assembly rules of those communities.

>COMMENT:
> 

