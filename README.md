# Blast_mismatch_search
A early model of blast mismatch search engine using python script
General usage:
Designed by Timothy Ting-Leung NG, The Hong Kong Polytechnic University, Hong Kong Special Administrative Region, China

Downloading the python script
Download and save the python in a folder of your interest. Create a folder called pocket in the same folder where the python script is located.

Downloading the BLAST xml file after the BLAST alignment
After mapping the consensus genomes to the reference genome (NC_045512.2), download the xml file. Open the xml file and locate all the Hsp child elements (there may be more than one) under the Hit element (Hit/Hsps_Hit). The text information in Hsp_Hit-from, Hsp_Hit-to, Hsp_qseq, Hsp_hseq, and Hsp_midline can be found in each Hsp element. To avoid confusion, creating a text file with a recommended file name format SampleID_(Hsp_Hit-from.text)_(Hsp_Hit-to.text).txt, for example, Sample123456_55_29835.txt). Copy the text to the text file in the following format, remember to exclude the tags nesting the text information.

55
29836
ATCGATTC......
ATCGAGTC......
||||| ||......

Please note that only one Hsp child element is allowed in one text file. If there is more than one Hsp child element in each sample ID, please input the information into separated text files.

Searching the variants with the python script
Put the text files into the pocket folder. Run the following commandline in command prompt:
python blast_mismatch_search.py
