
# BWSAT(BEST WORST SCALING ANNOTAION TOOL)

Given a lexicon along with their meanings and comparison pairs generated from Best Worst Scaling Algorithm, the tool provides a UI for annotators to generate comparison results which can later be used to create a rating scale.

Note : This tool was part of research project done as an Intern at MIDAS Lab, IIITD.

[Hindi Sentiment Lexicon GuideLine](https://docs.google.com/document/d/1ipGS2ZQqSzGXZbQT5F6E6PgNWlXUnhYmshc6BB0WvFQ/edit?usp=sharing)

## Best Worst Scaling

* Download the perl scripts and generate the annotaion tuples like /data/part5.csv (generate-BWS-tuples.pl)
* Run the get-scores-from-BWS-annotations-counting.pl to get scores.
* [Reference scripts](https://saifmohammad.com/WebPages/bwsVrs.html)


## Tool Features

* Tool provides user functionality.
* You can divide the total annoation in 5 buckets (part 1-5).
* The annotation for each user are tracked separately and tool continues from the last annotated point.
* The pickle file in data folder contains a dictonary [word, meaning].
* If there are multiple meanings of the word, #Number is used to make the dictionary.
* Usename.txt file contains the final annotation for a particular part.
* Mainly used for sentiment analysis in the example, can be extened for other tasks as shown in screenshots.

##  Result Description

### Input

* मजा#10	राक्षस#9	नारा#15	हथेली#3
* खूबसूरत#3	प्रणाली#3	शर्म#4	शुक्ला#8
* सपना#5	वासी#2	कलाई#1	उत्तरार्ध#1
* सरल#7	मुहिम#5	न्यायोचित#1	हर्ष#8
* हक#22	पेट#20	आशंका#6	मस्तिष्क#4

### Output 
* (row number, choice 1 (most positive), choice 2(least positive))
* 0,0,1
* 1,0,2
* 2,0,1
* 3,3,2
* 4,3,2

In first example 0th row, user has selected मजा#10 for most positive and राक्षस#9 least positive

## Reference

Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation. Kiritchenko, S. and Mohammad, S. In Proceedings of the Annual Meeting of the Association for Computational Linguistics (ACL-2017), Vancouver, Canada, 2017.

## Tool Screenshots

### 1. Starting Screen for User Input

![ScreenShot](/images/main.png)

### 2. Sample Hindi Sentiment Annotation

![ScreenShot](/images/sample.png)
![ScreenShot](/images/complete.png)

### 3. Tool extension for other problems

![ScreenShot](/images/extend.png)



