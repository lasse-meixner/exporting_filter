1) Make sure you have anaconda or miniconda installed (https://docs.conda.io/en/latest/miniconda.html).
To verify: Open your terminal and type:

> conda --version

2) Place the UpStraight App export, which should be called "export.csv", into this folder. Do not change the filename, otherwise this wont work.

3) Place the Apple Health export, which should be called "export.xml", into this folder. Do not change the filename, otherwise this wont work.

4) Open a terminal session, and paste these lines one by one (These will first create an isolated environment with all the needed packages to run this code (so that you can delete it afterwards), 
and then do some work on the export files to make sure we get only what we need):

> conda create -n upstraight_data_processing -y -c conda-forge python pandas

> conda activate upstraight_data_processing

> python apple_health_xml_convert.py

> python export_filter.py

_____
You're done!

You should now have a new file called "health_filtered.csv" in the folder.
Send me "health_filtered.csv" and "export.csv"

