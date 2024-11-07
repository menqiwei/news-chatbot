from openai import OpenAI
from os import listdir
from os.path import isfile, join
import summaries

directoryToSummarize = join("BBC News Summary","News Articles","politics")

directoryOfSummaries = join("BBC News Summary", "Summaries", "politics")

onlyfiles = [f for f in listdir(directoryToSummarize) if isfile(join(directoryToSummarize, f))]

onlySummaries = [f for f in listdir(directoryOfSummaries) if isfile(join(directoryOfSummaries, f))]

contentList = []

summaryList = []


for filePath in onlyfiles:
    with open(join(directoryToSummarize,filePath), 'r') as file:
        contentList.append(file.read())

for filePath in onlySummaries:
    with open(join(directoryOfSummaries,filePath), 'r') as file:
        summaryList.append(file.read())



AIsummaries = []

AIsummaries.append(summaries.summarizeANDBias(contentList[0], len(summaryList[0].split(" "))))

print(len(summaryList[0].split(" ")))


for suma in AIsummaries:
    print(suma)
    print(len(suma.split(" ")))

"""
TODO:
-Compare human summaries to ChatGPT summaries
-Automate and save the three tasks: Summarize, Get Bias, and Get Bias and then summarize

-Possible Comparison methods: BERT, rouge, some from class



"""