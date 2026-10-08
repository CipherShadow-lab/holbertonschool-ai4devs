# Reflection on AI-Assisted Debugging

## Introduction
This project was approached by first creating 5 small codes / code snippets that included bugs such as:  

- Syntax error (bug1.py)
- Logic error (bug2.py)
- Type error (bug3.py)
- Off-by-one error (bug4.js)
- Logical Operator bug (bug5.js)

All codes were passed through three AI models (Claude, ChatGPT and Gemini) with the same prompt:  

*"This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?"*  

As LLMs will always generate a different response (both by the same model and across different models), three models were used to assess and compare each response in relation to:

- How well they were able to identify the bugs  
- The level of detail provided as to why the bugs caused issues in the code  
- How concise the responses were in relation to explaining the issue and the suggested fixes 
- Whether they were able to identify other/unforeseen issues in the code; and  
- If further suggestions were made relating to test cases and/or best coding practices.  

This approach also revealed how much each of the responses varied and highlighted any potential issues/mistakes made by the model(s) when identifying the bugs. 

**Note**: It needs to be noted that the codes submitted to the models were **not** overly complex; as the goal of this project was to assess AI's capabilities in identifying bugs, the level of trust formed when reviewing the suggested fixes and determining whether human intuition was required to further investigate the proposed fixes.  

Ultimately, the objective of the project is to provide further insights into AI's role when it comes to real-world debugging.  


## AI Strengths
Across the three models, all bugs were correctly identified, along with sufficient reasoning and suggested fixes for each code.  

As expected, the responses varied across all three models however, throughout the process, it became apparent that certain models were better suited to debugging compared to others.  

For example:
Gemini was found to consistently label the type of bug that was present in the code (e.g. Logic error, TypeError, etc.) before providing an explanation of what the bug type meant, why this caused issues in the code and what the suggested fix(es) were. 
Yet Claude was the only model to identify an additional unforeseen bug in `bug4.js`, which the other two models completely missed. 
Additionally, Claude's and Gemini's responses were both clear and concise, without providing extensive details (unless requested). 

## AI Weaknesses
Despite ChatGPT being able to correctly identify the bugs in all of the codes, there was one instance where it suggested a fix that indirectly changed the logic as well. 

For example, in `bug5.js` the issue was specifically related to a Boolean condition `hasPermission === false` (defined in the `if` statement). 
Here, ChatGPT proposed changing `hasPermission === false` to `hasPermission === true` **AND** changing the intended rule to `if (age >= 18 && hasPermission === true)` - instead of keeping `if (age >=18 || hasPermission === true)`.

This highlighted that AI not only has the potential to make mistakes, it also has the potential to steer developers down the path of making unintended changes to their code logic when debugging. 

## Human Role
Throughout this project, there were no significant concerns or issues where manual intervention was required. However, there was a case where the issue in the code could be addressed in more than one way.

For example, in `bug4.js` the `for` loop was able to be corrected by:

- simply adding an `=` so that it included `itemIndex <= lastIndex`
- OR dropping `lastIndex` entirely, where the loop would include: `itemIndex < shoppingList.length` 

This led to checking on Google as well as further prompting AI for clarification on what the best practice / approach would be - from a 'cleaner' code and optimisation perspective.

## Conclusion
In summary, all models demonstrated how AI can be useful and effective when it comes to identifying bugs in code and software. It is evident that AI can save developers time by helping to detect, interpret and resolve coding issues more efficiently.  
However, as mentioned above, there is also great potential for AI to indirectly lead developers down a path where the logic in their code is changed - resulting from applying a suggested fix. This highlights that using AI (as a tool) in debugging should be approached with a critical mindset and without defaulting to trusting the model's initial response. This is especially true in situations where code is required to be delivered under tight time constraints.