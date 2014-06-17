*********************************************************************
** INTRUCTIONS FOR "DATA CLEANING AND STANDARDIZING IN PYTHON" JOB **
*********************************************************************
The job: I have three large datasets containing string (text) variables which need to be cleaned, standardized and merged using Python.


*****STEP ONE:

SAMPLE OF wORKER'S EDUCATION DATASET:
raw_education1.txt
raw_education2.txt
raw_education3.txt


ABOUT THE MAIN DATASET:
1) Each dataset contains information from members of a professional networking website (these are just samples of the data).
2) These datasets contain self-reported information about 100,000 workers’ education all around the world. 
3) The variables of interest are 
	1) e_name = name of university/school attended
	2) e_degree = degree name 
	3) e_major = major/course name
4) Main problems with the dataset:
	o Information typed by worker (not dropdown menu), so there are many misspellings.
  	o The name of the same university is written in many different ways such as UNIVERSITY OF CAMBRIDGE, CAMBRIDGE UNIVERSITY, CAMBRIDGE, CAMBRIDGE UNI.
   	o Some workers typed information that should be in the major/course column  or another column such as CAMBRIDGE UNIVERSITY MASTER PROGRAM or cAMBRIDGE ENGINEERING PROGRAM.
	o University names, degrees and majors could be in English or Local language.

TO-DO
1) Write a script to clean and standardize all three variables (e_name, e_degree, e_major) in Python through tokenizing, removing punctuation, cleaning text of stopwords, stemming and lemmatizing, and any other helpful functions.
2) More specifically, write the script to create a second variable for all three variables (e_name_clean, e_degree_clean, e_major_clean) to hold the standardized value (In English). 
3) For example,

e_name 					e_major				e_name_clean				e_major_clean
UNIVERSITY OF CAMBRIDGE			MATHS				UNIVERSITY OF CAMBRIDGE			MATHEMATICS
CAMBRIDGE UNIVERSITY			MATHEMATICS			UNIVERSITY OF CAMBRIDGE			MATHEMATICS
CAMBRIGE UNIVERSITY			BUSINESS			UNIVERSITY OF CAMBRIDGE			BUSINESS	
CAMBRIDGE UNI								UNIVERSITY OF CAMBRIDGE			
JESUS COLLEGE CAMBRIDGE			ZOOLOGY				UNIVERSITY OF CAMBRIDGE			ZOOLOGY
CAMBRIDGE BUSINESS SCHOOL						UNIVERSITY OF CAMBRIDGE			BUSINESS

(not including e_degree in this example, but this should be included in the dataset as well as indicated above).

*****STEP TWO:

WORLD UNIVERSITY DATASET:
whed_restricted.csv
name_variants.csv

ABOUT SECOND DATASET (whed_restricted):
1) This dataset contains 18,000+ names of universities and university ids.
2) The variables in these dataset are the following:
	o Country = country of location
	o OrgName = name of School/University/Organization in the Local Language
	o InstNameEnglish = name of School/University/Organization in English if Local Language is not English
	o OrgGUID = unique identifier for School/University/Organization
	

PS: name_variants.csv = this dataset simply contain name variants of schools/universities found in academic journals. 
There is no need to use/merge this dataset, however, it might be a useful dataset to have when cleaning/standardizing the names of the universities.


UNIVERSITY RANKINGS DATASET:
rankings_urap.csv
rankings_qs.csv

ABOUT THIRD DATASETS
2) These datasets contain 3000+ names of universities and university ids from two different university rankings.

TO-DO:
1) Use the same script as in STEP ONE to clean and standardize these datasets (that is, using the same format as the previous dataset).
2) Merge all datasets using exact and nearest match functions with university names. 
3) For example, the final product should look like this:

e_name 					e_major				e_name_clean			e_major_clean		OrgGUID		urap_id 	qs_id
UNIVERSITY OF CAMBRIDGE			MATHS				UNIVERSITY OF CAMBRIDGE		MATHEMATICS		34567		1		8
CAMBRIDGE UNIVERSITY			MATHEMATICS			UNIVERSITY OF CAMBRIDGE		MATHEMATICS		34567		1		8
CAMBRIGE UNIVERSITY			BUSINESS			UNIVERSITY OF CAMBRIDGE		BUSINESS		34567		1		8
CAMBRIDGE UNI								UNIVERSITY OF CAMBRIDGE					34567		1		8
JESUS COLLEGE CAMBRIDGE			ZOOLOGY				UNIVERSITY OF CAMBRIDGE		ZOOLOGY			34567		1		8
CAMBRIDGE BUSINESS SCHOOL						UNIVERSITY OF CAMBRIDGE		BUSINESS		34567		1		8
UNIVERSITY OF HARVARD			MATHS				UNIVERSITY OF HARVARD 		MATHEMATICS		18736		2		3
HARVARD UNIVERSITY			MATHEMATICS			UNIVERSITY OF HARVARD 		MATHEMATICS		18736		2		3


(not including e_degree in this example, but this should be included in the dataset as well as indicated above).

***Important: I need to be able to run the python code and replicate this standardization process in the entire WORKER'S EDUCATION DATASET.***

PLEASE LET ME KNOW IF YOU HAVE ANY QUESTIONS!

THANKS, 

RENATA