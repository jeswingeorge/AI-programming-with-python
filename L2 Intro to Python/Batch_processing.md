## Batch Processing
Now that you have completed coding check_images.py, you are ready to run it on all 3 models. One way to do this is to call the program from the terminal window for one of the models, wait until it completes running, record its results, and then repeat for the other two models.

An easier way to handle this task is with batch processing using a shell script. For this exercise, you will find the bash program __run_models_batch.sh__ in the workspace. Open that file and you will notice comments use # just like python and the rest look the same as the commands you type into the terminal window to run your program (see code below).

```
#  Code from run_models_batch.sh 
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt
     > resnet_pet-images.txt
python check_images.py --dir pet_images/ --arch alexnet  --dogfile dognames.txt  
     > alexnet_pet-images.txt
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt 
     > vgg_pet-images.txt
```

You will also notice that each file ends with `> filename.txt`.  
The `>` is a pipe and it pipes the output from the console into a file. The file contains the filename of the model being used. This way after each run, the results are automatically stored in your workspace.

To run file __run_models_batch.sh__ in the workspace, open a terminal window (in Unix/Linux/OSX/Lab Workspace) and type the following:

```
sh run_models_batch.sh
```

[If you want to batch process the program on a Windows computer you will need to follow the instructions found here](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#running-batch-files-on-windows-os-locally).

