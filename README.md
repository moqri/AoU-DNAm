f=1123364

gsutil -u $GOOGLE_PROJECT -m cp gs://fc-aou-datasets-controlled/pooled/longreads/v8_delta/UW/revio/bam/$f/GRCh38/$f.bam .
gsutil -u $GOOGLE_PROJECT -m cp gs://fc-aou-datasets-controlled/pooled/longreads/v8_delta/UW/revio/bam/$f/GRCh38/$f.bam.bai .

./pb-CpG-tools-v3.0.0-x86_64-unknown-linux-gnu/bin/aligned_bam_to_cpg_scores --bam bam/$f.bam --output-prefix meth/$f --threads 96

wget https://github.com/smithlabcode/dnmtools/releases/download/v1.5.0/dnmtools-1.5.0.tar.gz
tar -zxvf dnmtools-1.5.0.tar.gz
cd dnmtools-1.5.0
mkdir build && cd build
../configure --prefix=~/

~/htslib$ make install prefix=$HOME/local

dnmtools merge -t -radmeth \
     1123364.meth 1019230.meth 1017202.meth \
     1062200.meth 1037492.meth 1118525.meth > proportion-table.txt



base	case
1123364.meth	1	0
1019230.meth	1	0
1017202.meth	1	0
1062200.meth	1	1
1037492.meth	1	1
1118525.meth	1	1
