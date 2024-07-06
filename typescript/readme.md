In langchain , which retrevier search type is usd to balance between relevancy and diversity ? - similarity
What does a dedicated RDMA cluster network do during model fine tuning and inference? - It enables the depolyment of multiple fine tuned models with in a single cluster 
Which role does a "model endpoint" serve in the inference workflow of the OCI Generative AI service ? - Hosts the training data for fine tuning custom models 
Which is distinguished feature of "Parameter efficient fine tuning(PEFT)" as opposed to classic "Fine-tuning" in LLM training ?- PEFT involves only a few or new parameters and uses labeled , task specific data 
How does RAG token technique differ from RAG sequence when generating a models response? - RAG token retrieves relevant documents for each part of the response and constructs the answer incrementally 
Which component of RAG evaluates and proritizes the information retreieved by the retrieval system ? - Ranker
Which statement describes the differences between "Top k" and "Top p" in selecting the next token in the OCI generative AI generation model ? - Top K considers the sum of probablites of the top tokens , where as Top p selects from the Top K tokens sorted by probability 
Which statement is true about the Top p parameter of the OCI generative AI generation models ? - Top P limits token selection based on the sum of their probabilities
What is the primary function of the temperature parameter in the OCI generative AI generation models? - Controls the randomness of the models output affecting its creativity 
What distiniguishes the coherence emnbed v3 model from its predecessor in the OCI genrative AI service ? - Improved retrivals for RAG systems

What is the purpose of the stop sequence parameter in the OCI generative AI generation model ? - It specifies a string that tells the model to stop generating more contents 
What does a higher number assigned to a token signify in the show likelishoods feature of the language model toekn generation ? - The token is more likely to follow the current token
Coverating image memeory is not built in memory type in langchain
chain = prompt | 11m --> LECL is declarative and preferred way to compoose chains together 
translation models is not a category of pretrained foundational models available in the OCI generative AI service 
How are fine tuned customer models stored to enable strong data privacy and security in the OCI generative AI service ? - Stored in Object storage encrypted by default 
Why is normalization of vectores important before indexing in ahybrid search system ? - It standardixes vector lengths for meaningful comparison using metrics such as cosine similarity
How does the archeitecture of dedicated Ai clusters contribute to minimizing GPU memory ovehead for T-few fine tuned model infeence ? - By sharing base model weights across multipole fine tuned models on the same group of GPUs



Dot product - measures the magnitude and direction of vectors, whereas cosine distance focuses on the orientatio regardless of magnitude
