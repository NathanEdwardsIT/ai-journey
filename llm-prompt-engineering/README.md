Prompt Engineering Experiment: Explaining LLM Tokens
Experiment date: October 18, 2026
Task: Ask a language model to explain what a token is in the context of large language models (LLMs).
Study type: Small, exploratory, single-response comparison (not a statistically powered experiment).
Research question
How do four prompting approaches affect the quality of a beginner-friendly explanation of LLM tokens compared with the ambiguous baseline, explain what a token is?
Conditions
ID	Condition	Prompting approach	Key change
A	Baseline	Minimal instruction	"explain what a token is"
B	Clear instructions	Specificity and constraints	Specifies LLM context, beginner audience, key topics, and length
C	Context / motivation	Explain the learning goal	Frames the answer as preparation for studying ML and LLMs
D	XML structure	Tagged sections	Separates task, audience, requirements, output format, and constraints
E	Few-shot	Demonstration example	Shows an example explanation of embeddings to model style and depth


Important design limitation: The enhanced prompts change multiple things at once. B, C, D, and E differ in wording, requirements, and format, not just the named technique. These results compare the specific prompts tested; they do not isolate the causal effect of each technique.
Scoring rubric
Each response was evaluated against six predeclared, observable criteria, scored 0–2 points each, for a maximum of 12 points. The rubric is applied to the response text, not to the intended prompt technique.
Criterion	0 points	1 point	2 points
LLM-topic relevance	Explains an unrelated meaning of token	Partly about LLM tokens	Clearly about tokens used by LLMs
Definition accuracy	No applicable or substantially incorrect definition	Basically correct but imprecise/oversimplified	Correctly describes tokens as units from a model's tokenizer (which may be words, subwords, punctuation, etc.)
Tokenization process	Missing/incorrect	Mentions splitting text but with notable omissions or misleading claims	Correctly describes converting text into token units for model processing
Concrete example	None	Illustrative but vague or presented as universally exact when tokenizer-dependent	Clear example with an appropriate tokenizer-dependent caveat or unambiguous illustration
Practical significance	Absent/irrelevant	General or somewhat misleading	Accurately explains how tokens relate to input/output, limits, costs, or generation
Clarity and organization	Hard to follow	Readable but poorly structured or incomplete	Clear and accessible for a beginner


The rubric is a transparent manual assessment, not an objective ground-truth metric. Another evaluator might assign different points, especially for borderline examples.
Results
Condition	Relevance	Definition	Process	Example	Significance	Clarity	Total / 12
A · Baseline	0	0	0	0	0	2	2
B · Clear instructions	2	2	2	1	2	2	11
C · Context / motivation	2	1	2	1	2	2	10
D · XML structure	2	1	2	1	2	1	9
E · Few-shot	2	1	1	1	2	2	9


Observed ranking for these five outputs: B (11) > C (10) > D = E (9) > A (2).
Normalized rubric scores: B 91.7%, C 83.3%, D/E 75.0%, A 16.7%. These percentages are rubric points, not factual accuracy rates or probabilities.
Response-by-response assessment
A — Baseline: 2/12
- What worked: Fluent, understandable prose.
- Main problem: Interpreted token as a blockchain/digital-asset token instead of an LLM text token. Consequently it does not answer the intended question.
- Interpretation: An underspecified prompt permits a different, legitimate meaning of a polysemous word. This demonstrates an ambiguity failure, not poor writing ability.
B — Clear instructions: 11/12
- What worked: Directly defines text tokens, describes tokenization, gives examples of possible token types, and explains token-by-token generation.
- Caveat: The examples are categories of possible tokens, not a real, tokenizer-specific segmentation of one input. "Understand the meaning" also anthropomorphizes the underlying process a little.
- Interpretation: Best response under this rubric, mainly due to coverage and specificity.
C — Context / motivation: 10/12
- What worked: Strong intuitive account of why models break text into smaller units; connects tokenization to pattern recognition and prediction.
- Caveat: Starts with why tokenization is necessary rather than a direct definition, and uses an analogy instead of a concrete tokenized example. Statements such as "understand the meaning of each word" are simplified beyond what tokenization itself accomplishes.
- Interpretation: Helpful educational context, slightly weaker as a stand-alone definition.
D — XML structure: 9/12
- What worked: Explains splitting text into units and why that supports model processing. Includes examples of potential subdivisions.
- Caveat: The exact segmentations of I love playing football and unhappiness depend on the tokenizer and were not verified. Its output also begins without the requested first sections and jumps to headings "3" and "4". Claims about directly capturing nuance from tokenization alone are overstated.
- Interpretation: Structured input did not guarantee complete adherence to the requested output structure in this run.
E — Few-shot: 9/12
- What worked: Clear beginner-friendly explanation, logical progression, and a strong account of why tokens matter for text generation.
- Caveat: It implies that each whole word in the example sentence is a token, although real tokenizers may split words or encode spaces differently. It also omits the important possibility of subword tokens.
- Interpretation: Good presentation; technical precision was weaker than B.
Key findings
1. Disambiguation mattered most here. The baseline answered an entirely different meaning of token. All enhanced prompts identified the LLM domain.
2. Clear instructions received the highest rubric score (11/12) for these particular outputs.
3. More prompt structure did not automatically mean a better answer. The XML version contained unverified segmentation examples and missing expected sections.
4. An example can influence style without guaranteeing precision. The few-shot answer was readable but oversimplified how tokenizers divide words.
Limitations
- One generation per condition: No estimate of run-to-run variation, confidence intervals, or statistical significance.
- One question: Findings may not generalize to other topics, models, or questions.
- Subjective manual scoring: Criteria are explicit, but scores depend on reviewer judgment; there was no independent second rater.
- Confounded treatments: The enhanced prompts differ on several dimensions, so comparisons do not isolate one prompting technique.
- Unknown inference settings: Model name/version, temperature, seed, and other generation settings were not supplied and cannot be claimed controlled.
- No verified tokenizer output: Illustrative token segmentations should not be treated as exact unless tested with a named tokenizer.
- A single rubric score is not an accuracy statistic. For instance, 11/12 is 91.7% of available rubric points, not 91.7% objectively correct facts.
How to improve the experiment
1. Use one fixed model and settings, logging model/version, temperature, and timestamps.
2. Create a shared base prompt and vary only one feature at a time (e.g. adding XML tags without altering requirements).
3. Test more questions with known expected concepts, including ambiguous words such as attention, embedding, context window, and parameter.
4. Run at least 10–20 generations per prompt per question to estimate variability. Randomize testing order.
5. Separate objective checks from ratings: Check whether the response mentions subword pieces and tokenizer dependence, whether it stays under 200 words, and whether output sections are present. Have multiple independent reviewers rate clarity.
6. Report per-criterion averages and dispersion, and use paired comparisons on the same questions rather than relying on a single ranking.
7. Verify examples with a real tokenizer (specific model and tokenizer version) before treating splits as correct.
Reproducibility
The scores are based only on the five response texts supplied for this experiment. The corresponding prompts were the original baseline and four crafted variants; the model and generation configuration were not reported. Save full prompts, raw outputs, and future scoring runs alongside this README before drawing stronger conclusions.
Reference
Anthropic, Claude Prompting Best Practices.