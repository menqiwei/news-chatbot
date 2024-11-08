from openai import OpenAI
from os import listdir
from os.path import isfile, join
import os
import summaries


topic = "politics"

#Path to our data
directoryToSummarize = join("BBC News Summary","News Articles", topic)
#Path to our 'label'
directoryOfSummaries = join("BBC News Summary", "Summaries", topic)

#A list of the files in the data directory
onlyfiles = [f for f in listdir(directoryToSummarize) if isfile(join(directoryToSummarize, f))]

#A list of the files in the 'label' directory
onlySummaries = [f for f in listdir(directoryOfSummaries) if isfile(join(directoryOfSummaries, f))]

#Stores the data content in a list
contentList = []

#Store the summary content from labels
summaryList = []

#Read in our content
for filePath in onlyfiles:
    with open(join(directoryToSummarize,filePath), 'r') as file:
        contentList.append(file.read())
#Read in our summaries
for filePath in onlySummaries:
    with open(join(directoryOfSummaries,filePath), 'r') as file:
        summaryList.append(file.read())


#Predicted Summaries List
AIsummaries = []

#Call ChatGPT to summarize
AIsummaries.append(summaries.bias(contentList[0]))  #, len(summaryList[0].split(" "))))


for i,suma in enumerate(AIsummaries):
    with open("GeneratedSummaries" + os.sep + "Detected Bias" + os.sep  + topic + "{:0>3}.txt".format(i), 'w') as file:
        file.write(suma)
        file.close()





"""
TODO:
-Compare human summaries to ChatGPT summaries
-Automate and save the three tasks: Summarize, Get Bias, and Get Bias and then summarize

-Possible Comparison methods: BERT, rouge, some from class



"""