import argparse
import os
import shutil


def option_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", "--dir_name", required=True, type=str, help="Directory name.")
    args = arg_parser.parse_args()

    return args.dir_name


if __name__ == "__main__":
    dir_name = option_parser()
    beamer_dir_path = os.path.dirname(__file__) or "."
    new_dir_path = f"{beamer_dir_path}/paper/{dir_name}"

    os.mkdir(new_dir_path)
    os.mkdir(f"{new_dir_path}/figure")
    shutil.copy(f"{beamer_dir_path}/template.tex", new_dir_path)
    os.rename(f"{new_dir_path}/template.tex", f"{new_dir_path}/main.tex")
    shutil.copy(f"{beamer_dir_path}/symbols_terms.tex", new_dir_path)
    shutil.copy(f"{beamer_dir_path}/supplementary_figure.pptm", f"{new_dir_path}/figure")
