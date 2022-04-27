import os
import subprocess

"""Python script with which can be downloaded data from Gutenberg Project. Please edit ROOT variable. This varibles shoud be edited in config and .R script also. Script should be optimalized in future.

Also if user wants to call with .py script .r scirpt. Then should be Rscript.exe added to path.
"""


# User should overwrite ROOT where project is situated. In my case was used local computer and remote school computer which provided more power for experiments.
ROOT = "C:\\Users\\Vojta\\Desktop\\diploma"
# ROOT = "/home/usp/pro0255/diploma"

# Name of r script which downloads libs and starts to download all books from Gutenberg Project. It can be configured by r_config.csv.
name_of_r_file = "download_gutenberg_with_config.R"


# Path where r scripts for download are situated.
path_to_r = os.path.sep.join([ROOT, "src", "download", "r", name_of_r_file])


# If user wants to run python script with subprocess of r script. Then r is needed to be installed on user computer. Auhors of project had to add Rscript.exe to path variables. These instructions should be described in project README.md.
subprocess_str = f"Rscript {path_to_r}"

# If all conditions are followed subprocess should work well.
subprocess.call(subprocess_str)
