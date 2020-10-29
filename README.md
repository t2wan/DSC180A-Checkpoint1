Background

The purpose of phrase mining is to extract high-quality phrases from a large amount of text corpus. It identifies the phrases instead of an unigram word, which provides a much more understanding of the text.  In this study, we apply AutoPhrase method into two different datasets and compare the decreasing quality ranked list of phrase ranked list in multi-words and single word. Our datasets are from the abstract of Scientific papers in English with the English knowledge base from Wikipedia. Through this project, we will be able to understand the advantages of the AutoPhrase method and how to implement Autophrase in two datasets by identifying different outcomes it produces. 

Purpose of the Code

For CheckPoint 1, our code would do the data ingestion proportion only, to pull either DBLP.txt or DBLP.5k.txt as the input corpus for future use from the cloud and save it at data/EN/ depository depending on the hyper-parameter.

Code Content

The code basically includes Python Script that generates a Bash File and calls that Bash to pull data from the cloud.
	
How to Run the Code

Assuming you are using a Mac computer and have brew installed already, this should be runnable with either

python run.py DBLP.txt

Or

python run.py DBLP.5k.txt

depending on which corpus you would like to use as the input file. You will see the file at data/En when the ingestion is done.



Work Cited

Professor Jingbo Shang’s Github: https://github.com/shangjingbo1226/AutoPhrase
Jingbo Shang, Jialu Liu, Meng Jiang, Xiang Ren, Clare R Voss, Jiawei Han, "Automated Phrase Mining from Massive Text Corpora", accepted by IEEE Transactions on Knowledge and Data Engineering, Feb. 2018.


### Responsibilities

We discussed the general idea of the replication project and outlined the steps of the process together.
Tiange Wan: majority of code portion, reviewed the report portion and did the modification on the report.
Yicen Ma: majority of report portion, review the code portion and involved in the readme file.





