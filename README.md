This repository contain ".gitignore" so the following rules will apply.


1. All files and directories which are contained in a hidden directory ".terraform" will be ignored. ".terraform" can be located in any folder.

2. All files with file extension ".tfstate" in any directories will be ignored.

3. All files which contain ".tfstate." in the name of file and any number of character after it (even 0) in any directories will be ignored.

4. The file "crash.log" will be ignored in any directories.

5. All files with file extension ".tfvars" will be ignored in any directories.

6. Files "override.tf" and "override.tf.json" will be ignored in any directories.

7. In any directories will be ignored files which contain "_override.tf" and any number of characters before it in the file name(even 0). But files "example_override.tf" wil not be ignored.

8. In any directories will be ignored files which contain "_override.tf.json" and any number of characters  before it in the file name.

9. The file ".terraformrc" will be ignored  in any directories.

10.The file "terraform.rc" will be ignored in any directories.
 
