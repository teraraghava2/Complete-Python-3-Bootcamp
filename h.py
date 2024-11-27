bRole: You are an evaluator tasked with assessing the quality and relevance of customer support call summaries against the original call transcripts. Your evaluation should align closely with typical human judgment, acknowledging practical imperfections and realistic variations in standards.

Evaluation Criteria and Scoring Guide:
	1.	Input Quality (1-5): Evaluate the clarity, completeness, and organization of the original call transcript.
	•	1: Transcript is highly disorganized, incomplete, and very difficult to follow.
	•	2: Transcript has notable clarity issues and missing key parts.
	•	3: Transcript is somewhat clear, with moderate disorganization or minor missing parts.
	•	4: Transcript is mostly clear and complete, with minor organizational issues.
	•	5: Transcript is fully clear, complete, well-organized, and easy to follow.
	2.	Summary Quality (1-5): Assess the accuracy of the summary in representing the main points, tone, and flow of the conversation, while allowing for minor imperfections as humans often do.
	•	1: Summary is inaccurate, missing major details, or contains significant errors.
	•	2: Summary captures some key details but omits notable parts or contains moderate inaccuracies.
	•	3: Summary covers most important points but has some less critical errors.
	•	4: Summary represents main points well, with only minor inaccuracies.
	•	5: Summary is highly accurate and aligns closely with the conversation.
	3.	Summary Coherence (1-5): Evaluate the coherence, grammar, and readability of the summary.
	•	1: Summary is highly disjointed, with severe grammatical issues, and very difficult to understand.
	•	2: Summary has notable coherence issues with multiple grammatical errors.
	•	3: Summary is somewhat coherent but may contain minor grammatical issues.
	•	4: Summary is mostly coherent, with good grammar and minor readability issues.
	•	5: Summary is well-structured, grammatically correct, and easy to understand.
	4.	Resolution Capture (1-5): Assess whether the summary accurately captures the resolution or conclusion of the call.
	•	1: Resolution is completely missing or misrepresented.
	•	2: Resolution is partially captured but misses key details.
	•	3: Resolution is somewhat captured, but some details are incomplete.
	•	4: Resolution is mostly accurate, with only minor omissions.
	•	5: Resolution is fully captured and accurately summarized.
	5.	Informative Content (1-5): Rate how well the summary captures essential details and informative content from the call.
	•	1: Summary lacks informative content and omits critical details.
	•	2: Summary has minimal informative content, with several key details missing.
	•	3: Summary includes sufficient content but has some gaps in minor areas.
	•	4: Summary is mostly comprehensive, with few omissions.
	•	5: Summary is fully comprehensive, capturing all essential details.
	6.	Truthfulness (1-5): Evaluate the factual accuracy of the summary relative to the transcript.
	•	1: Summary contains major inaccuracies or misrepresents key aspects.
	•	2: Summary has several inaccuracies that could mislead understanding.
	•	3: Summary is somewhat accurate, with minor factual errors.
	•	4: Summary is mostly accurate, with only small factual errors.
	•	5: Summary is entirely accurate, with no factual errors.
	7.	Absence of Hallucinations (1-5): Assess whether the summary avoids introducing information not present in the transcript.
	•	1: Summary includes significant hallucinations (false or invented information).
	•	2: Summary contains multiple details not in the transcript.
	•	3: Summary has some minor hallucinated details but mostly stays on track.
	•	4: Summary has very few hallucinated details, sticking closely to the transcript.
	•	5: Summary introduces no information not found in the transcript.

Additional Instructions:
	•	Use these criteria as guidelines to ensure a realistic and human-like judgment of transcript and summary quality.
	•	Prioritize balance and consistency in your ratings, avoiding over-perfectionism or undue harshness.
	•	Consider contextual nuances and practical limits in human evaluations, recognizing that not all aspects of a summary or transcript will always align perfectly.

This prompt reduces over-stringency by explicitly allowing room for small errors or imperfections, thus increasing alignment with human evaluation tendencies. It sets a realistic standard for scoring and reflects the variability in human judgment.


Here is a well-structured prompt optimized for calculating Resolution Capture, Informative Content, Truthfulness (for the summary), and Transcript Quality (for the call transcript). It includes a one-shot negative example to guide the model and specifies the desired JSON output format for clarity and usability.

Instruction:
You are an evaluator assessing customer support call summaries against the original call transcript. Your goal is to evaluate the following metrics:
	1.	Transcript Quality (1-5): Assess the clarity, completeness, and organization of the original call transcript.
	2.	Resolution Capture (1-5): Evaluate how well the summary captures the resolution or conclusion of the call.
	3.	Informative Content (1-5): Assess the extent to which the summary captures essential and critical details from the call.
	4.	Truthfulness (1-5): Evaluate the factual accuracy of the summary relative to the transcript.

Use the scoring criteria below for your evaluation:

Scoring Guidelines (1-5):
	•	Transcript Quality (Original Call Transcript)
1: Transcript is highly disorganized, incomplete, and very difficult to follow.
2: Transcript has significant clarity issues or is missing key parts.
3: Transcript is somewhat clear but has moderate disorganization or minor missing parts.
4: Transcript is mostly clear, complete, and well-organized with only minor issues.
5: Transcript is fully clear, complete, well-organized, and easy to follow.
	•	Resolution Capture (Summary)
1: Summary completely misses or misrepresents the resolution or conclusion of the call.
2: Summary captures some aspects of the resolution but omits important details.
3: Summary partially captures the resolution, though some details are incomplete.
4: Summary captures the resolution well, with only minor omissions.
5: Summary fully captures and accurately summarizes the resolution.
	•	Informative Content (Summary)
1: Summary lacks informative content and omits critical details.
2: Summary includes minimal content, with several key points missing.
3: Summary includes sufficient content but has gaps in minor details.
4: Summary is mostly comprehensive, with only minor omissions.
5: Summary is fully comprehensive, capturing all critical details.
	•	Truthfulness (Summary)
1: Summary contains significant factual inaccuracies or misrepresents key aspects.
2: Summary has several inaccuracies that could mislead understanding.
3: Summary is somewhat truthful but contains minor factual errors.
4: Summary is mostly truthful, with small inaccuracies.
5: Summary is entirely truthful, with no factual inaccuracies.

One-shot Example (Negative):
Call Transcript:

	Customer: I want to close my savings account.
Agent: I can assist you with that. Please confirm your account number.
Customer: 123456.
Agent: Your request has been submitted. The account will close within 3-5 business days.

Summary Provided:

	The customer wanted help with an account issue. The agent provided some information, but the resolution is unclear.

Evaluation:
	•	Transcript Quality: 4 (Mostly clear, but formatting could be better.)
	•	Resolution Capture: 1 (The resolution is entirely missing in the summary.)
	•	Informative Content: 2 (Minimal details; no mention of account closure or timeline.)
	•	Truthfulness: 3 (Somewhat truthful but misleads by omitting resolution details.)

Output Format (JSON):

{
  "transcript_quality": <1-5>,
  "resolution_capture": <1-5>,
  "informative_content": <1-5>,
  "truthfulness": <1-5>
}

Task:
Evaluate the provided call transcript and summary based on the criteria and scoring guidelines above. Return the results in the specified JSON format. Response key: "evaluation_result"
Here’s a structured approach to creating an effective slide deck to explain your evaluation methodology and potential improvements. I’ll outline the key slides and their content:

Title Slide

	•	Title: “Evaluation of Transcript and Summary Quality for Bank Customer Conversations”
	•	Subtitle: A detailed approach to scoring and improving AI-generated summaries
	•	Your Name and Date

Slide 1: Introduction

	•	Title: “Why Evaluate Transcript and Summary Quality?”
	•	Content:
	•	Explain the importance of evaluating bank customer service interactions.
	•	Highlight goals:
	•	Ensure AI-generated summaries accurately reflect conversations.
	•	Maintain confidentiality and data integrity.
	•	Use case: Enhancing customer support outcomes with AI.

Slide 2: Approach Overview

	•	Title: “The Evaluation Workflow”
	•	Content:
	•	Show a flowchart or steps:
	1.	Input: Call transcript and model-generated summary.
	2.	Human evaluation using scoring criteria.
	3.	Output: JSON structure with scores, justifications, and evidence.
	•	Emphasize evidence-based, strict adherence to provided data.

Slide 3: Scoring Criteria

	•	Title: “Key Evaluation Criteria”
	•	Content:
	•	List and briefly describe:
	1.	Transcript Quality (Low, Medium, High)
	2.	Summary Quality (Low, Medium, High)
	3.	Summary Coherence (Good, Neutral, Bad)
	4.	Resolution Capture (Yes, No)
	5.	Informative Content (Low, Medium, High)
	6.	Truthfulness and Absence of Hallucinations (Yes, No)
	7.	Presence of Toxic Language (Yes, No)
	•	Mention evidence-backed scoring.

Slide 4: JSON Output Format

	•	Title: “Standardized Output Format”
	•	Content:
	•	Show a visual example of the JSON structure.
	•	Highlight fields: Score, Justification, Evidence.
	•	Explain why this format is effective for machine learning models and analysis.

Slide 5: Guardrails for Evaluation

	•	Title: “Ensuring Confidentiality and Accuracy”
	•	Content:
	•	Key guardrails:
	•	Confidentiality: Data is sensitive, and no assumptions are allowed.
	•	Strict adherence to provided information.
	•	Evidence-based scoring with no fabrication.
	•	How these guardrails maintain reliability and integrity.

Slide 6: One-Shot Prompting Approach

	•	Title: “Using One-Shot Prompting for Evaluation”
	•	Content:
	•	Describe the one-shot prompt format.
	•	Explain how including sample input and output improves LLM responses.
	•	Visual example of one-shot prompt and expected JSON output.

Slide 7: Areas for Improvement

	•	Title: “Opportunities for Refinement”
	•	Content:
	•	Accuracy: Enhance prompts for better clarity and alignment.
	•	Scalability: Automate parts of the scoring process.
	•	Granularity: Add more detailed scoring criteria (e.g., empathy detection).
	•	Feedback Loop: Incorporate evaluator feedback to improve models.

Slide 8: Challenges

	•	Title: “Challenges in Evaluation”
	•	Content:
	•	Reliance on human interpretation for evidence-based scoring.
	•	Handling edge cases where transcript data is unclear or incomplete.
	•	Balancing scoring granularity with practicality.

Slide 9: Potential Enhancements

	•	Title: “Next Steps for Improvement”
	•	Content:
	•	Introduce multi-turn conversation context for holistic scoring.
	•	Explore advanced metrics (e.g., empathy, tone analysis).
	•	Train models using human-evaluated examples to refine AI outputs.
	•	Leverage visualization tools to analyze evaluation data trends.

Slide 10: Conclusion

	•	Title: “Key Takeaways”
	•	Content:
	•	Evidence-based evaluation ensures high-quality AI summaries.
	•	Guardrails are crucial for confidentiality and reliability.
	•	Opportunities for iterative improvements in the process.
	•	Future potential: Scalable and automated quality evaluation.

Slide 11: Questions

	•	Title: “Questions and Discussion”
	•	Content:
	•	Open the floor for questions.
	•	Include a contact slide if necessary.

Visuals and Design Tips:

	•	Use charts or visuals to explain processes (e.g., flowcharts for evaluation workflow, JSON examples).
	•	Keep text concise and highlight key points.
	•	Use icons for categories (e.g., thumbs up/down for Yes/No questions).
	•	Choose a professional color scheme (e.g., blue and white for corporate themes).

This slide deck will effectively explain your approach while leaving room for discussing potential enhancements and next steps.