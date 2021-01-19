import os.path
import shutil


def augmented_move(
        target_folder, *filenames, verbose=False, **specific
):
    """Move all filenames into the target_folder, allowing
    specific treatment of certain files."""

    def print_verbose(message, filename):
        """print the message only if verbose is enabled"""
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == "ignore":
                print_verbose("Ignoring {0}", filename)
            elif specific[filename] == "copy":
                print_verbose("Copying {0}", filename)
                shutil.copyfile(filename, target_path)
        else:
            print_verbose("Moving {0}", filename)
            shutil.move(filename, target_path)


augmented_move(
    "/Users/nguyendangtuan/Documents/Project/montypython/ebook/Chapter07/target_move", "filemove1.txt",
    "filemove2.txt", "filemove3", verbose=True, filemove3="ignore"
)
