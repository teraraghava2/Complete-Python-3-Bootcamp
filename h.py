Below is a detailed documentation for your Cosine Similarity Score Analysis between call transcripts and summaries, structured to meet the requirements of a Model Risk Management (MRM) team. The document ensures completeness, clarity, and transparency in methodology, metrics, findings, and conclusions.

Cosine Similarity Score Analysis Between Call Transcripts and Summaries

1. Objective

The purpose of this analysis is to evaluate the semantic similarity between call transcripts (conversations between bank agents and customers) and model-generated summaries using cosine similarity scores. The objective includes:
	•	Measuring similarity at different chunk sizes (ranging from 25 to 500 tokens) to determine sensitivity to chunk size.
	•	Comparing actual summary similarity with a random baseline (summaries shuffled across transcripts) to quantify the model’s performance.
	•	Assessing model effectiveness in capturing meaningful relationships between transcripts and summaries.
	•	Providing a structured risk assessment for model evaluation and validation.

2. Methodology

2.1. Model and Metric Used
	•	Model: Pre-trained text similarity model (Cosine Similarity computation).
	•	Metric: Cosine Similarity Score (range: 0 to 1).
	•	Higher values indicate stronger semantic similarity.
	•	Lower values indicate weaker similarity.

2.2. Data Inputs
	•	Call Transcripts: Bank agent-customer conversations (variable-length text).
	•	Model-Generated Summaries: AI-generated summaries intended to concisely represent transcripts.

2.3. Chunking Strategy
	•	Chunking transcripts into sizes of 25, 50, 60, 70, 100, 200, 280, 300, 330, 360, 380, 400, 500 tokens.
	•	Each summary sentence compared to its best-matching transcript chunk for similarity measurement.

2.4. Cosine Similarity Computation
	1.	Regular Cosine Similarity: Measures similarity between transcript and corresponding summary.
	2.	Random Baseline Similarity: Measures similarity by randomly shuffling summaries across transcripts to estimate a baseline score.

3. Results and Observations

3.1. Cosine Similarity Scores Across Chunk Sizes

Regular Summary Similarity Scores (cs_mean)
	•	Highest cosine similarity observed for small chunk sizes (25–70 tokens), gradually declining with increasing chunk size.
	•	Scores stabilize from 100 tokens onward, with minor fluctuations.

Chunk Size	Mean Cosine Similarity (cs_mean)
25	0.567007
50	0.565699
60	0.563123
70	0.561658
100	0.555293
200	0.546926
280	0.542680
300	0.541662
330	0.540351
360	0.538696
380	0.537719
400	0.536660
500	0.531839

Random Baseline Similarity Scores (cs_Random_mean)
	•	Lower cosine similarity across all chunk sizes, confirming that the model-generated summaries contain meaningful information from the transcripts.
	•	Random baseline scores decrease slightly as chunk size increases, similar to the regular summary trend.

Chunk Size	Mean Random Cosine Similarity (cs_Random_mean)
25	0.427952
50	0.421624
60	0.418562
70	0.415739
100	0.410040
200	0.409189
280	0.407064
300	0.407757
330	0.408403
360	0.407641
380	0.407056
400	0.406399
500	0.405288

4. Analysis and Findings

4.1. Model Performance vs. Random Baseline
	•	Regular cosine similarity scores are consistently higher than random baseline scores, validating the effectiveness of the model-generated summaries.
	•	Gap between regular and random similarity indicates a meaningful alignment between summaries and transcripts.

4.2. Impact of Chunk Size
	•	Smaller chunk sizes (25–70 tokens) yield the highest similarity scores, indicating better alignment of summaries with smaller transcript sections.
	•	Larger chunk sizes (100+ tokens) show a decline in similarity scores, likely due to increased noise and dilution of relevant content.
	•	Stability is observed from chunk size 300 onwards, suggesting a balance between contextual coverage and information dilution.

4.3. Key Observations
	1.	Regular similarity consistently outperforms random baseline, proving that model-generated summaries capture meaningful transcript content.
	2.	Cosine similarity scores gradually decline with larger chunk sizes, suggesting that summarization accuracy decreases as chunk size increases.
	3.	Gap between regular and random similarity remains stable across all chunk sizes, demonstrating robustness in summary quality.

5. Recommendations

5.1. Optimal Chunk Size for Evaluation
	•	For maximum similarity, chunk sizes between 25 and 100 tokens are recommended as they yield the highest cosine similarity scores.
	•	Chunk sizes above 300 tokens are less sensitive to further increases, making them viable for efficient processing without major loss in similarity.

5.2. Model Performance Monitoring
	•	Regularly monitor cosine similarity trends to ensure model-generated summaries remain informative.
	•	Compare against updated random baselines periodically to validate ongoing model effectiveness.

5.3. Suggested Enhancements
	•	Incorporate additional similarity metrics (e.g., Jaccard Similarity, BLEU scores) to cross-validate findings.
	•	Experiment with dynamic chunking (adaptive chunk sizes based on summary length) to optimize summary alignment.

6. Conclusion

This documentation presents a comprehensive analysis of cosine similarity scores between bank call transcripts and model-generated summaries, evaluated across 6707 records with varying chunk sizes.
	•	Smaller chunk sizes yield higher similarity, confirming better summary alignment.
	•	Model-generated summaries outperform the random baseline, validating their semantic accuracy.
	•	Stability in scores beyond chunk size 300 suggests a balance between context coverage and dilution.

This evaluation ensures a transparent and structured approach for model risk assessment, demonstrating reliable summary performance while highlighting areas for improvement.