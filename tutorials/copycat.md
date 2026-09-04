---
title: CopyCat
source: Article
url: https://learn.foundry.com/nuke/content/reference_guide/air_nodes/copycat.html
author: learn.foundry.com
ingested: 2026-09-04
app: "[PENDING]"
version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/copycat/
frame_count: 0
frame_status: skipped
uncertainty_frames: []
---

# CopyCat

**Source:** [Article](https://learn.foundry.com/nuke/content/reference_guide/air_nodes/copycat.html)
**Author:** learn.foundry.com
**Duration:** unknown | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frame capture was skipped for this ingest (--skip-video). Text-only extraction.


### Full Content [0:00]
**Transcript:** CopyCat CopyCat Inputs and Controls Step-by-Step Guides CopyCat ( NukeX and Nuke Studio only) copies sequence-specific effects, such as garbage matting, beauty repairs, or deblurring, from a small number of frames in a sequence and then trains a network to replicate this effect on the full sequence. CopyCat outputs a trained network in a .cat file ready for the Inference node to apply your effect. See also Inference . Inputs and Controls Connection Type Connection Name Function Input Input The image sequence before any effects have been applied. Ground Truth The image sequence after the required effects have been applied. This input describes what the network is attempting to learn. Preview An optional sample image overlay. This input is used to view how the model will work when applied to a frame that is not part of the data set you're using to the train the model. As the training progresses, the Preview image should move toward the ideal result defined by the Ground Truth . Note: This input is only visible when the Input and Ground Truth are connected. Control (UI) Knob (Scripting) Default Value Function CopyCat Tab Local GPU gpuName N/A Displays the GPU used for rendering when Use GPU if available is enabled. Local GPU displays Not available when: • Use CPU is selected as the default blink device in the Preferences . • no suitable GPU was found on your system. • it was not possible to create a context for processing on the selected GPU, such as when there is not enough free memory available on the GPU. You can select a different GPU, if available, by navigating to the Preferences and selecting an alternative from the default blink device dropdown. Selecting a different GPU requires you to restart Nuke before the change takes effect. Use GPU if available useGPUIfAvailable on When enabled, rendering occurs on the Local GPU specified, if available, rather than the CPU. Note: Enabling this option with no local GPU allows the script to run on the GPU whenever the script is opened on a machine that does have a GPU available. You should also select this if you wish to render from the command line with the --gpu option. See Nuke 17 Release Notes for more information on the GPUs Nuke supports. Data Directory dataDirectory N/A Sets the location to which CopyCat writes contact sheets and .cat files for use with an Inference node. Epochs epochs 10000 Sets the number of times CopyCat processes the entire data set during training. Higher values generally produce better trained networks, but at the cost of longer processing time. Channels trainingInfo none Read-only information about the current training model: • Channels - the channels to process from the Input and Ground Truth respectively. • Batch Size - the Advanced Batch Size dropdown controls this field. • Total Steps - the number of steps required to complete the specified number of Epochs . At each step, CopyCat trains the network using random crop pairs from the Input and Ground Truth images divided by the Batch Size . Total Steps = Epochs * (Data Set) / (Batch Size) The Data Set is the number of Input and Ground Truth image pairs connected to CopyCat. Batch Size 0 (Auto) Total Steps N/A Start Training startTraining N/A Click to start training the network using the current settings. Resume Training resumeTraining N/A Click to resume training from a checkpoint recorded in the Data Directory . Create Inference createInference N/A Click to add an Inference node to the Node Graph with the Model File control automatically referencing the correct .cat file for this CopyCat node. Advanced Initial Weights initialWeights None Sets whether training begins from scratch or from weighting defined by a previous model: • None - the training begins from scratch with no weighting applied. • Checkpoint - the training uses weighting from a previously trained .cat file, which is saved to the Data Directory every 1000 steps by default. Tip: You can change how often checkpoints are created using the Checkpoint Interval control. • Deblur - the training starts with a model weighted towards deblur effects, which can improve the training results for similar operations. • Upscale - the training starts with a model weighted towards upscaling, which can improve the training results for similar operations. • Human Matting - the training starts with a model weighted towards rotoscoping humanoid shapes, which can improve the training results for similar operations. This checkpoint is available in large , medium and small model sizes (see Model Size). Checkpoint File checkpointFile N/A When Initial Weights is set to Checkpoint , enter the location of the .cat file to use as the weighting when training resumes. Model Size modelSize Medium Allows you to trade off speed and memory use against potentially better results. Small models are faster to train and use the least GPU memory, but Large models may produce better results on complex tasks such as beauty work or when attempting to generalize for multiple shots. Batch Size batchSizeType Auto Sets the number of image pairs to train the network with at each Epoch and is used to calculate the Total Steps required to complete the training run. Total Steps = Epochs * (Data Set Size) / (Batch Size) The Batch Size is calculated automatically using the available GPU memory by default. batchSize N/A When Batch Size is set to Manual , enter the batch size to use. Smaller Batch Size values may cause the training to be inefficient, but larger values can cause your GPU to run out of memory. Values between 4 and 16 were found to be suitable in most scripts, depending on the data set. Note: The Batch Size must be less than or equal to the number of image pairs in your data set. Crop Size cropSize 256 Defines the size of the random crops taken from the data set image pairs. Larger values generally produce more accurate results, but at the expense of processing time and memory, and smaller values may require more iterations to produce a good result. If you find that training takes a long time or uses too much memory, try reducing the Crop Size control. In our tests, the default 256 was suitable for most scripts, but data sets of larger images may require a larger Crop Size to train effectively. Checkpoint Interval checkpointInterval 1000 Sets the number of steps between each checkpoint .cat file saved to the Data Directory . You can load .cat files into Inference nodes to check the progress of the training at each checkpoint on the full sequence. Contact Sheet Interval imageInterval 100 Sets the number of steps between each contact sheet .png file saved to the Data Directory . You can examine the contact sheets to judge whether the training is progressing as expected. Use Multi-Resolution Training useMultiResolutionTraining on Enabling multi-resolution training can speed up your training by up to two times. It does so by splitting the training into three stages - low, medium, and high resolution. During the low and medium-resolution stages, the input and ground truth images are downsized to 1/4 and 1/2 resolution respectively, allowing for fast training. In the final high-resolution stage, the model is trained on full-resolution input and ground truth images as regular CopyCat does, allowing the model to learn from the fine details and achieve optimal results. It is recommended that you disable multi-resolution training when using a large dataset of input and ground truth images (more than 100). Note: Stopping training prematurely may prevent the model training on full resolution images. Progress Tab Runs [Run Table] runTable N/A Displays run data for all training in the specified Data Directory . Live Updates off When on, live training data is polled from the distributed training network so that you can check training progress. Live Updates is off by default to avoid unnecessary data fetching from the network. Note: This control has no effect when you're training on your local machine. Graph Log Scale logScale off When on, the graph y axis is converted from linear to log, which displays more detail at lower values as the training progresses. Smoothness smoothness 0.6 Controls the overall smoothness of the loss curve. Lower values allow you to see more accurate data points, but the overall trend can be harder to read. Show Original Curve showOriginal on When on, the original graph before applying any smoothing is displayed as well as the smoothed graph. [graph] N/A N/A Displays Step/Loss data for all training in the specified Data Directory . You can use the curve to monitor training in real-time using the zoom controls above the graph. Runs runTable N/A Displays run data for all training in the specified Data Directory . You can enable and disable curves for run individually using the checkbox on the left of each entry. You can also rename the files in the Data Directory by double-clicking on the Name field and entering your own string. Python Tab (These controls are for Python callbacks and can be used to have Python functions automatically called when various events happen in Nuke .) before render beforeRender none These functions run prior to starting rendering in execute(). If they throw an exception, the render aborts. before each frame beforeFrameRender none These functions run prior to starting rendering of each individual frame. If they throw an exception, the render aborts. after each frame afterFrameRender none These functions run after each frame is finished rendering. They are not called if the render aborts. If they throw an exception, the render aborts. after render afterRender none These functions run after rendering of all frames is finished. If they throw an error, the render aborts. render progress renderProgress none These functions run during rendering to determine progress or failure. Step-by-Step Guides Train Neural Networks to Replicate Effects Using Machine Learning Can't find what you're looking for? Use our feedback widget on the right to request more information.



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### Nodes / Tools / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### Foundry App & Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Tutorials
[PENDING EXTRACTION]
