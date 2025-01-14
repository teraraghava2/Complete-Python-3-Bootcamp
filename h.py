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