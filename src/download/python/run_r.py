import subprocess
import os


ROOT = "C:\\Users\\Vojta\\Desktop\\diploma"
#ROOT = "/home/usp/pro0255/diploma"

name_of_r_file = "download_gutenberg_with_config.R"
path_to_r = os.path.sep.join([ROOT, "src", "download", "r", name_of_r_file])
subprocess_str =  f"Rscript {path_to_r}"

subprocess.call(subprocess_str)


