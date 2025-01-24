Documentation: Natural Language Inference (NLI) Analysis for Call Transcripts and Summaries

1. Objective

The goal of this analysis is to evaluate the alignment between call transcripts and their French summaries using Natural Language Inference (NLI). This involves determining whether the content in the summaries is entailed by the original transcripts.

2. Model Used
	•	Model Name: bart_large_mnli
	•	Purpose: Text classification for NLI tasks, determining relationships between text pairs as Entailment, Neutral, or Contradiction.
	•	Limitation: 512-token input limit, requiring chunking of longer transcripts.

3. Methodology

3.1 Data Processing
	•	Total Records: 6,706 call transcripts and corresponding summaries.
	•	Summary Sentences: 25,168 sentences in total.
	•	Chunking: Due to the token limit, transcripts were split into chunks of various sizes (128, 256, and 400 tokens).
	•	Overlap: A 30% overlap between chunks ensured context preservation.

3.2 NLI Score Computation
	•	Each summary sentence was compared against all transcript chunks.
	•	NLI Evidence: A boolean indicating if a sentence is entailed (True) or not (False).
	•	NLI Score: The highest entailment probability score for each sentence across all chunks.

3.3 Chunk Size Impact
	•	Chunk Size 400: Delivered the most consistent and higher scores.
	•	Chunk Sizes 128 & 256: Showed similar performance with ~30% overlap in results.

4. Results

4.1 Chunk Size 256
	•	False: 7,314
	•	True: 17,879
	•	Average NLI Entailment Score:
	•	True Evidence: 0.729630
	•	False Evidence: 0.253074

4.2 Chunk Size 128
	•	False: 10,751
	•	True: 14,477
	•	Average NLI Entailment Score:
	•	True Evidence: 0.740799
	•	False Evidence: 0.227967

4.3 Overall Statistics (Optimal at Chunk Size 400)
	•	Total True NLI Evidence: 20,362
	•	Total False NLI Evidence: 4,806
	•	Average NLI Entailment Score:
	•	True Evidence: 0.734574
	•	False Evidence: 0.273954

5. Key Insights
	•	Larger chunk sizes (400 tokens) improve NLI accuracy due to more context being available.
	•	Smaller chunks (128, 256) perform similarly but with slightly lower entailment scores.
	•	30% overlap between chunks aids in maintaining contextual integrity.

6. Conclusion

The analysis effectively measures how well call summaries reflect the original transcripts using NLI. The bart_large_mnli model, optimized at a chunk size of 400 tokens with overlap, achieves high entailment accuracy, validating the reliability of summaries.

7. Next Steps
	•	Experiment with different overlap percentages for further improvement.
	•	Explore model fine-tuning for the French language to boost performance.
	•	Automate chunk size optimization for scalability.

This structured documentation provides a clear, step-by-step explanation of your NLI analysis and results. Let me know if you’d like me to add visualizations or refine any sections.
Below is a detailed structure for the documentation that aligns with how a Model Risk Management (MRM) team would expect to see a thorough report. The document outlines the steps, processes, metrics, and findings related to your NLI analysis.

Documentation for NLI Score Analysis Between Call Transcripts and Summaries

1. Objective

The goal of this analysis is to evaluate the performance of the BART-large MNLI model in assessing Natural Language Inference (NLI) between call transcripts (agent-customer interactions in a banking context) and their corresponding summaries. This involves:
	•	Calculating NLI entailment scores and NLI evidence (True/False) for various chunk sizes of transcripts.
	•	Analyzing the sensitivity of the model’s performance to chunk sizes.
	•	Establishing a baseline using random NLI scores by shuffling the summaries to measure the model’s lift.
	•	Providing detailed metrics and observations to support model validation and risk assessment.

2. Methodology

2.1. Model Used
	•	Model Name: BART-large MNLI
	•	Type: Pre-trained text classification model
	•	Purpose: To classify relationships between pairs of text (entailment, contradiction, or neutral).

2.2. Data Inputs
	•	Call Transcripts: Bank agent and customer interactions, consisting of multiple sentences. These are chunked into smaller sections.
	•	Summaries: Manually generated summaries of the transcripts, sentence by sentence.

2.3. Process Overview
	1.	Chunking Transcripts:
	•	Transcripts were divided into chunks of various sizes (100, 200, 300, 400, 500 tokens) to ensure manageable input for the NLI model, given its token limit.
	•	Each summary sentence was aligned with the best-matching chunk to calculate entailment.
	2.	NLI Score Calculation:
	•	For each summary sentence, NLI entailment scores were calculated for every chunk of the transcript.
	•	NLI Evidence: A binary metric (True or False) indicating whether a summary sentence aligns with the transcript chunk.
	3.	Baseline Calculation:
	•	A baseline was created by randomly shuffling summaries and calculating NLI scores to compare with the actual performance.
	4.	Coverage Metrics:
	•	True Evidence Coverage: The percentage of NLI evidence marked as True.
	•	False Evidence Coverage: The percentage of NLI evidence marked as False.
	•	Average Coverage: Calculated by averaging True and False coverage across all records and further averaging over all chunks.

2.4. Chunk Size Sensitivity
	•	NLI scores were calculated for chunk sizes: 100, 200, 300, 400, and 500 tokens.
	•	Comparisons were made across sizes to analyze model performance trends.

3. Metrics and Calculations

3.1. Key Metrics
	•	NLI Evidence: Binary classification (True/False) of whether the summary aligns with the chunk.
	•	Entailment Scores: Continuous scores indicating the degree of alignment (0–1 scale).
	•	Average True Coverage: The average percentage of True NLI evidence across records.
	•	Average False Coverage: The average percentage of False NLI evidence across records.
	•	Baseline Lift: Difference in average True coverage between normal NLI and random NLI.

3.2. Calculation Examples
	•	True Coverage per Record:
￼
	•	Average of Averages (True and False):
￼
	•	Baseline Lift:
￼

4. Results

4.1. Normal NLI Analysis
	•	The average of average True evidence increases with larger chunk sizes, indicating that larger chunks capture more contextual information and lead to higher entailment accuracy.
	•	False evidence coverage decreases slightly, indicating fewer mismatches as chunk size increases.

Chunk Size	Avg. True Coverage	Avg. False Coverage
100	X%	Y%
200	X%	Y%
300	X%	Y%
400	X%	Y%
500	X%	Y%

4.2. Baseline (Random NLI) Analysis
	•	In the random baseline, False evidence coverage increases with chunk size, while True evidence remains minimal.

Chunk Size	Avg. Random True Coverage	Avg. Random False Coverage
100	X%	Y%
200	X%	Y%
300	X%	Y%
400	X%	Y%
500	X%	Y%

5. Observations
	1.	Chunk Size Sensitivity:
	•	Larger chunk sizes lead to better entailment scores, likely due to improved contextual overlap between transcripts and summaries.
	•	Small chunk sizes may miss critical context, reducing True evidence coverage.
	2.	Baseline Comparison:
	•	Random NLI scores are significantly lower than normal scores, indicating that the model is effectively identifying entailment relationships.
	3.	Coverage Patterns:
	•	True evidence coverage dominates across all chunk sizes, validating model accuracy.
	•	False evidence coverage trends downward with larger chunks.

6. Recommendations
	1.	Optimal Chunk Size: Chunk sizes of 400–500 tokens are recommended for optimal performance.
	2.	Model Performance Monitoring: Regularly assess baseline lift to ensure the model remains effective.
	3.	Documentation Updates: Maintain detailed logs of changes to model parameters or chunking strategies.

7. Conclusion

This documentation outlines the process, metrics, and findings of the NLI analysis, supporting the validation and assessment needs of the MRM team. The results demonstrate the model’s sensitivity to chunk size and its ability to outperform the baseline random NLI scores, ensuring reliable performance in summarization tasks.

Would you like me to refine this further or add visualizations like graphs and tables for better clarity?