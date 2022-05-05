# Contents <!-- omit in toc -->

- [1. Patents and Publications](#1-patents-and-publications)
  - [1.1. Patent: Methods and systems for multi-label classification of text data - 2020](#11-patent-methods-and-systems-for-multi-label-classification-of-text-data---2020)
  - [1.2. Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding - 2019](#12-enhancing-pio-element-detection-in-medical-text-using-contextualized-embedding---2019)
  - [1.3. A review of standard text classification practices for multi-label toxicity identification of online content - 2018](#13-a-review-of-standard-text-classification-practices-for-multi-label-toxicity-identification-of-online-content---2018)
  - [1.4. Detection of Abusive Online Behaviour Using Multi-Label Classification - 2018](#14-detection-of-abusive-online-behaviour-using-multi-label-classification---2018)
  - [1.5. Principal component analysis-based occupancy detection with ultra wideband radar 2017](#15-principal-component-analysis-based-occupancy-detection-with-ultra-wideband-radar-2017)
- [2. Projects](#2-projects)
  - [2.1. Speech to speech translation](#21-speech-to-speech-translation)
  - [2.2. Portable speech transcription models](#22-portable-speech-transcription-models)
  - [2.3. UWB Radar based breathing rate detection](#23-uwb-radar-based-breathing-rate-detection)
  - [2.4. Toxic comment classification engine](#24-toxic-comment-classification-engine)
  - [2.5. Autonomous inventory robot](#25-autonomous-inventory-robot)
  - [2.6. Telepresence robot](#26-telepresence-robot)
  - [2.7. Ultra low power display driver for bi-stable displays](#27-ultra-low-power-display-driver-for-bi-stable-displays)
  - [2.8. FPGA based image enhancement and object detection system.](#28-fpga-based-image-enhancement-and-object-detection-system)
  - [2.9. FPGA based HDMI transmitter and receiver module.](#29-fpga-based-hdmi-transmitter-and-receiver-module)

# 1. Patents and Publications

## 1.1. Patent: Methods and systems for multi-label classification of text data - 2020
	
**[US11163947B2](https://patents.google.com/patent/US11163947B2/en)**

Led the team that developed a novel multi-label classification method that utilizes soft labelling and stacking of multiple models to improve text classification performance

## 1.2. Enhancing PIO Element Detection in Medical Text Using Contextualized Embedding - 2019
**[Published](https://aclanthology.org/W19-5023.pdf) in [BioNLP 2019 : 18th ACL Workshop on Biomedical Natural Language Processing](https://www.aclweb.org/portal/content/18th-sigbiomed-workshop-biomedical-natural-language-processing) in Florence, Italy**

A new approach to Population, Intervention and Outcome (PIO) element detection for Evidence Based Medicine and a new dataset created by applying multiple rule based labelling functions to unlabelled data and reweighing and combining their outputs into a single, confidence-weighted training label per data point. Obtained an ROC-AUC score of 0.9998



## 1.3. A review of standard text classification practices for multi-label toxicity identification of online content - 2018
**[Published](https://drive.google.com/file/d/1Ea9QuE1g5oBfBg7ik-UM9wIjnSvzaAkL/view) in the [ALW2](https://sites.google.com/view/alw2018/program/accepted-papers) workshop at [2018 conference on Empirical Methods in Natural Language Processing (EMNLP 2018)](https://aclweb.org/portal/content/2nd-workshop-abusive-language-online) in Brussels, Belgium**

As the available data for toxicity classification is heavily unbalanced (in most web-crawl datasets the amount of toxic sentences are usually far fewer than neutral/positive sentences), developed novel methods to augment the data and use multiple ML models together to improve accuracy and achieved an ROC-AUC score of 0.9862

	

## 1.4. Detection of Abusive Online Behaviour Using Multi-Label Classification - 2018

**[Montreal AI Symposium](https://montrealaisymposium.wordpress.com/accepted-papers-montreal-ai-symposium-2018/) in Montreal, Canada**

Poster presentation about a comparison of conventional SVM vs a GRU DNN model for text classification with different text representation methods.

## 1.5. Principal component analysis-based occupancy detection with ultra wideband radar 2017

**[Published](https://ieeexplore.ieee.org/document/8053237) in the [60th International Midwest Symposium on Circuits and Systems (MWSCAS)](https://ieee-cas.org/conference/2017-ieee-60th-international-midwest-symposium-circuits-and-systems-mwscas) in Medford, MA, US**

Developed a novel method for occupancy detection using Ultra Wide-band (UWB) radar. The developed algorithm is able to distinguish two people separated by only 0.8m with 86% accuracy while also being able to detect binary occupancy 100\% of the time


# 2. Projects

## 2.1. Speech to speech translation

Led a team of 9 engineers to successfully deliver Android applications for **offline speech to speech translation** on 5 different languages. Achieved speech to text Word Error Rates between 7%
to 12% and translation BLEU scores above 52 for all languages.

As the application required to be run offline without any network access, all the models used for speech transcription, text to text translation and text to speech needed to be stored on device and loaded to memory when the application is used. Therefore, models trained using high performance NVIDIA GPUs had to be compressed without severely affecting performance in order to be able to fit them in the storage and RAM of a mobile phone and also allow fast loading times. All models were compressed and optimized to reduce loading time to sub-seconds and execution time to near real time once the models are loaded.

Each language required speech to text, text to text translation and text to speech models to be trained. Some of the languages for this application involved regional dialects and low resource languages with limited training data. In case of regional dialects, models were trained using more commonly used parent languages and optimized for regional dialects by fine tuning using a smaller dialect dataset.


## 2.2. Portable speech transcription models

Successfully delivered speech transcription models trained using unclassified data that can be run on unseen, classified data. The purpose of this project is to be able to train transcription models using public datasets that match a general criteria derived from classified data. This project allowed engineers to train and fine tune models that need to be run on classified data that cannot be accessed without special clearances. The models were made portable so that an analyst with proper clearance can run the trained models on classified data without requiring specialized knowledge about machine learning. 

## 2.3. UWB Radar based breathing rate detection

## 2.4. Toxic comment classification engine

## 2.5. Autonomous inventory robot

Developed a robot capable of of autonomously navigating inside a retail store environment while avoiding obstacles and taking inventory of RFID tagged merchandise for a fortune 500 retailer. This robot also won the following awards:
- Winner in the Research and Development category and the winner of the overall gold award in the National Best Quality ICT Awards Sri Lanka, 2015 organized by the British Computer Society (BCS).
- Winner of the Asia Pacific ICT Alliance Awards 2015 (APICTA 2015 Awards) in the Research and Development category. The Asia Pacific ICT Alliance is an alliance between 16 member countries in the Asia Pacific region and the autonomous inventory robot won the gold award competing with 11 teams from Australia, China, Hong Kong, Malaysia, Thailand, Taiwan and Indonesia.

The robot used wheel encoders for position estimation and a 2D LIDAR sensor for position correction using a particle filter algorithm. The 2D lidar and multiple 3D point cloud and sonar sensors were used for obstacle detection. The path planning was done using A* algorithm for global path planning and Dijkstra's algorithm for local path planning. 

## 2.6. Telepresence robot

A telepresence robot with two way video+audio+control connectivity along with the ability to avoid obstacles and navigate autonomously was developed. The autonomous navigation was developed by using wheel encoders for position estimation, 3D point cloud, sonar and infrared sensors for obstacle detection.

## 2.7. Ultra low power display driver for bi-stable displays

Built an ultra low power display driver capable of showing 12 gray levels on bi-stable displays. As the name suggests, bi-stable displays are usually only stable on two levels, black and white. An algorithm was developed using C and ARM assembly to run on an STM32F4 microcontroller in order to quickly change between the two stable levels in the display per pixel to be able to stabilize the display in intermediate levels between the two stable conditions. 

As the voltage in each pixel needs to be changed within a few nanoseconds in order to stabilize the display in intermediate levels, an optimized algorithm for converting an image into pixel level voltages was developed and a decompressed version of each image is saved in a dedicated NAND flash chip before sending the image to the display. After the decompression and voltage calculation is done for each image, a heavily optimized program written in ARM assembly reads the decompressed data and drives the display to stabilize it in the intermediate state for each pixel. 

## 2.8. FPGA based image enhancement and object detection system.

A system capable of receiving new images from a computer and processing them with various filters
on an Altera Cyclone II FPGA was developed. An Altera NIOS II soft processor was used in conjunction with the hardware modules to handle image transmission, storage and display. Dedicated hardware modules were developed on FPGA using Verilog to process the receieved images parallely making the image processing significantly faster than processing them using general purpose microprocesssors.

## 2.9. FPGA based HDMI transmitter and receiver module.

An HDMI transmitter module on a Xilinx Virtex 7 FPGA and a receiver module on a Xilinx SPARTAN
6 FPGA was developed.