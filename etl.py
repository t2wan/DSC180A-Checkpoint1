'''
etl.py contains to download data
'''
import subprocess
#import os
def get_data(input_file):
    '''
    download and save data to 
    '''
    #if os.path.exists("auto_phrase.sh"):
        #os.remove("auto_phrase.sh")
    if input_file == 'DBLP.5k.txt':
        with open ('auto_phrase.sh', 'w') as rsh:
            rsh.write('''\
#!/bin/bash
# In effect, the commands below check to see if we're running in a Docker container--in that case, the (default) 
# "data" and "models" directories will have been renamed, in order to avoid conflicts with mounted directories 
# with the same names.
#
# DATA_DIR is the default directory for reading data files.  Because this directory contains not only the default
# dataset, but also language-specific files and "BAD_POS_TAGS.TXT", in most cases it's a bad idea to change it.
# However, when this script is run from a Docker container, it's perfectly fine for the user to mount an external
# directory called "data" and read the corpus from there, since the directory holding the language-specific files
# and "BAD_POS_TAGS.txt" will have been renamed to "default_data".
if [ -d "default_data" ]; then
    DATA_DIR=${DATA_DIR:- default_data}
else
    DATA_DIR=${DATA_DIR:- data}
fi
# MODEL is the directory in which the resulting model will be saved.
if [ -d "models" ]; then
    MODELS_DIR=${MODELS_DIR:- models}
else
    MODELS_DIR=${MODELS_DIR:- default_models}
fi
MODEL=${MODEL:- ${MODELS_DIR}/DBLP}
# RAW_TRAIN is the input of AutoPhrase, where each line is a single document.
DEFAULT_TRAIN=${DATA_DIR}/EN/DBLP.5k.txt
RAW_TRAIN=${RAW_TRAIN:- $DEFAULT_TRAIN}
# When FIRST_RUN is set to 1, AutoPhrase will run all preprocessing. 
# Otherwise, AutoPhrase directly starts from the current preprocessed data in the tmp/ folder.
FIRST_RUN=${FIRST_RUN:- 1}
# When ENABLE_POS_TAGGING is set to 1, AutoPhrase will utilize the POS tagging in the phrase mining. 
# Otherwise, a simple length penalty mode as the same as SegPhrase will be used.
ENABLE_POS_TAGGING=${ENABLE_POS_TAGGING:- 1}
    # A hard threshold of raw frequency is specified for frequent phrase mining, which will generate a candidate set.
MIN_SUP=${MIN_SUP:- 10}
# You can also specify how many threads can be used for AutoPhrase
THREAD=${THREAD:- 10}
COMPILE=${COMPILE:- 1}
### Begin: Suggested Parameters ###
MAX_POSITIVES=-1
LABEL_METHOD=DPDN
RAW_LABEL_FILE=${RAW_LABEL_FILE:-""}
### End: Suggested Parameters ###

green=`tput setaf 2`
reset=`tput sgr0`

if [ $COMPILE -eq 1 ]; then
    echo ${green}===Compilation===${reset}
    bash compile.sh
fi

mkdir -p tmp
mkdir -p ${MODEL}

if [ $RAW_TRAIN == $DEFAULT_TRAIN ] && [ ! -e $DEFAULT_TRAIN ]; then
    echo ${green}===Downloading Toy Dataset===${reset}
    curl http://dmserv2.cs.illinois.edu/data/DBLP.txt.gz --output ${DEFAULT_TRAIN}.gz
    gzip -d ${DEFAULT_TRAIN}.gz -f
fi

### END Compilation###

''')
    else:
        with open ('auto_phrase.sh', 'w') as rsh:
            rsh.write('''\
#!/bin/bash
# In effect, the commands below check to see if we're running in a Docker container--in that case, the (default) 
# "data" and "models" directories will have been renamed, in order to avoid conflicts with mounted directories 
# with the same names.
#
# DATA_DIR is the default directory for reading data files.  Because this directory contains not only the default
# dataset, but also language-specific files and "BAD_POS_TAGS.TXT", in most cases it's a bad idea to change it.
# However, when this script is run from a Docker container, it's perfectly fine for the user to mount an external
# directory called "data" and read the corpus from there, since the directory holding the language-specific files
# and "BAD_POS_TAGS.txt" will have been renamed to "default_data".
if [ -d "default_data" ]; then
    DATA_DIR=${DATA_DIR:- default_data}
else
    DATA_DIR=${DATA_DIR:- data}
fi
# MODEL is the directory in which the resulting model will be saved.
if [ -d "models" ]; then
    MODELS_DIR=${MODELS_DIR:- models}
else
    MODELS_DIR=${MODELS_DIR:- default_models}
fi
MODEL=${MODEL:- ${MODELS_DIR}/DBLP}
# RAW_TRAIN is the input of AutoPhrase, where each line is a single document.
DEFAULT_TRAIN=${DATA_DIR}/EN/DBLP.txt
RAW_TRAIN=${RAW_TRAIN:- $DEFAULT_TRAIN}
# When FIRST_RUN is set to 1, AutoPhrase will run all preprocessing. 
# Otherwise, AutoPhrase directly starts from the current preprocessed data in the tmp/ folder.
FIRST_RUN=${FIRST_RUN:- 1}
# When ENABLE_POS_TAGGING is set to 1, AutoPhrase will utilize the POS tagging in the phrase mining. 
# Otherwise, a simple length penalty mode as the same as SegPhrase will be used.
ENABLE_POS_TAGGING=${ENABLE_POS_TAGGING:- 1}
# A hard threshold of raw frequency is specified for frequent phrase mining, which will generate a candidate set.
MIN_SUP=${MIN_SUP:- 10}
# You can also specify how many threads can be used for AutoPhrase
THREAD=${THREAD:- 10}
COMPILE=${COMPILE:- 1}
### Begin: Suggested Parameters ###
MAX_POSITIVES=-1
LABEL_METHOD=DPDN
RAW_LABEL_FILE=${RAW_LABEL_FILE:-""}
### End: Suggested Parameters ###

green=`tput setaf 2`
reset=`tput sgr0`

if [ $COMPILE -eq 1 ]; then
    echo ${green}===Compilation===${reset}
    bash compile.sh
fi

mkdir -p tmp
mkdir -p ${MODEL}

if [ $RAW_TRAIN == $DEFAULT_TRAIN ] && [ ! -e $DEFAULT_TRAIN ]; then
    echo ${green}===Downloading Toy Dataset===${reset}
    curl http://dmserv2.cs.illinois.edu/data/DBLP.txt.gz --output ${DEFAULT_TRAIN}.gz
    gzip -d ${DEFAULT_TRAIN}.gz -f
fi

### END Compilation###
        
        ''')
    subprocess.run(['brew','install','gcc6'])
    subprocess.run(['brew','update'])
    subprocess.run(['chmod','+x','auto_phrase.sh'])
    subprocess.run(['./auto_phrase.sh'])


    return