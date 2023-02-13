# OrgaTuring-Accelerating Organoid Discovery with visual AI
OrgaTuring is a novel deep-learning approach to investigating organoids and designing a real-time accurate medical device. The CNN-based interpretable deep-learning model facilitates the real-time location, quantification, tracking, and classification of organoids from 2D and 3D images. This research will serve as a stepping stone to creating smart point-of-care devices equipped with mobile healthcare.


## Folder Structure

```
OrgaTuring-AI-Deciphers-Organoids-towards-Futurizing-Healthcare
│   .ipynb_checkpoints
└───results
└───src
│   │   code_class_weight.ipynb
|   |   code_oversample.ipynb
|   └───finetuning_dataugmentation.ipynb
└───LICENCE     
└───README.md  
└───tools.yml      


```

## Prerequisites
The dependencies are listed under requirements.txt and are all purely python based. To install them simply run
```
conda env update --file tools.yml
```

## Dataset
The dataset is private. Since there are no publicly available datasets for our model training, we created a unique dataset comprising approximately 400 organoid images (350 healthy and 50 inflamed organoids). To culture healthy- and Crohn's Disease- (CD) patient-derived organoids (PDOs), patients were enrolled for colonoscopies as a part of their routine care for the management of their diseases by the University of California, San Diego IBD-Center, following research protocols compliant with the Human Research Protection Program (HRPP) and approved by the Institutional Review Board (IRB) (Project ID# 1132632: PI Boland and Sandborn).

## Running
For a local installation, make sure you have pip installed and run: 
```
pip install notebook
```
For running jupyter
```
jupyter notebook
```

  
![](/results/1.png)

![](/results/2.png)

## What is Organoid?
![](/results/3.png)

## Potential
![](/results/4.png)

## OrgaTuring
![](/results/5.png)

![](/results/6.png)

![](/results/7.png)
![](/API/static/images/bg/Presentation1.gif)

## Inflamed Images
![](/results/Inflamed.png)
## NonInflamed Images
![](/results/NonInflamed.png)

