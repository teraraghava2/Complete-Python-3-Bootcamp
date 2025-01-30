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

Significance of Using All-MiniLM-L6-v2 for Cosine Similarity Calculation

1. Introduction to the Model

For this analysis, you have used the all-mpnet-base-v2 model to compute cosine similarity scores between call transcripts and model-generated summaries. This model is a part of the Sentence Transformers (SBERT) family, optimized for semantic similarity and dense vector embeddings.

The all-mpnet-base-v2 model is a transformer-based sentence embedding model trained using a contrastive learning approach. It is pre-trained on millions of sentence pairs, making it highly effective for capturing the semantic meaning of text.

2. Why All-MPNet-Base-V2 for Cosine Similarity?

The model is designed specifically for dense vector representations of sentences, making it ideal for tasks like semantic search, paraphrase detection, and text similarity calculations. Key reasons for choosing this model are:
	1.	Superior Semantic Understanding
	•	Unlike traditional TF-IDF or BOW (Bag-of-Words) models, all-mpnet-base-v2 captures contextual meaning rather than just keyword overlap.
	•	It generates dense embeddings where similar sentences cluster closely in vector space.
	2.	Robust Contextual Embeddings
	•	The model maps sentences with similar meanings to closer points in vector space, ensuring that semantically related transcripts and summaries yield high cosine similarity scores.
	•	It reduces reliance on exact word matches, which is crucial for paraphrased summaries.
	3.	Optimized for Short and Long Texts
	•	The model performs well on both short summaries and longer transcript chunks, making it ideal for chunk-wise cosine similarity evaluations.
	4.	Efficient and Scalable
	•	It has a smaller footprint compared to larger models like BERT-large, making it more efficient for large-scale computations across 6707 records.
	•	Inference is faster, allowing for seamless evaluation across different chunk sizes.

3. How Cosine Similarity Works with MPNet Embeddings

The cosine similarity metric measures how similar two vectors are in high-dimensional space. The all-mpnet-base-v2 model transforms text into dense 768-dimensional embeddings, where:
	•	Highly similar summaries and transcript chunks have embeddings with a smaller angular distance, leading to higher cosine similarity scores (closer to 1.0).
	•	Unrelated or randomly assigned summaries have embeddings with a larger angular distance, resulting in lower cosine similarity scores (closer to 0.0).

4. Impact of Chunk Size on Cosine Similarity Scores

Because the all-mpnet-base-v2 model is context-sensitive, the way transcript chunks are constructed directly impacts similarity scores:
	1.	Smaller Chunks (25-70 Tokens) → Higher Similarity
	•	Since the chunk contains a more focused context, it aligns better with the summary, leading to higher cosine similarity scores.
	•	MPNet’s embeddings can efficiently capture meaning in short contexts without dilution.
	2.	Larger Chunks (100+ Tokens) → Slightly Lower Similarity
	•	As chunks get larger, more irrelevant content gets mixed in, causing a gradual decline in cosine similarity.
	•	The model finds it harder to match the summary to a specific part of the transcript, reducing similarity scores.
	3.	Cosine Similarity vs. Random Baseline
	•	The random baseline scores are consistently lower, proving that MPNet embeddings preserve semantic relationships between summaries and transcripts.
	•	Without contextual alignment (random summaries), MPNet assigns lower similarity scores, demonstrating the model’s ability to differentiate meaningful summaries from random text.

5. Advantages Over Other Models

Compared to other similarity models, all-mpnet-base-v2 offers:

Feature	All-MPNet-Base-V2	BERT (Vanilla)	TF-IDF / BoW
Semantic Awareness	✅ Strong	✅ Moderate	❌ Weak
Contextual Understanding	✅ Deep	✅ Partial	❌ None
Handles Paraphrased Text	✅ Yes	✅ Partial	❌ No
Scalability for Large Datasets	✅ High	❌ Slow	✅ High
Performance on Short and Long Text	✅ Optimized	❌ Degrades on long text	✅ Works, but lacks meaning
Computational Efficiency	✅ Fast	❌ Slower	✅ Fast
Resistant to Exact Word Matching Bias	✅ Yes	❌ No	❌ No

This highlights why all-mpnet-base-v2 is ideal for evaluating semantic similarity in your use case.

6. Conclusion

The all-mpnet-base-v2 model plays a crucial role in computing cosine similarity scores for transcript-summary pairs.
	•	It ensures meaningful alignment between summaries and their corresponding transcript sections.
	•	It captures deeper contextual meaning, making it more reliable than traditional keyword-based similarity metrics.
	•	It is robust against paraphrasing, making it well-suited for NLP applications like summarization validation.
	•	Chunk size impacts similarity scores, and smaller chunks generally yield higher similarity.

Using all-mpnet-base-v2 for cosine similarity provides a strong foundation for evaluating model-generated summaries in a model risk management framework.
