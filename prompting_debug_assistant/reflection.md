# Reflection on AI-Assisted Debugging

## Introduction
This project involved creating five small code snippets containing different bugs:

- Syntax error (bug1.py)
- Logic error (bug2.py)
- Type error (bug3.py)
- Off-by-one error (bug4.js)
- Logical Operator bug (bug5.js)

Each code was passed through Claude, ChatGPT and Gemini using the same prompt:

*"This code throws an error / doesn't behave as expected. Can you identify and explain the issue and how to fix it?"*

The models were compared based on how accurately they identified the bugs, the detail and clarity of their explanations, the conciseness of their suggested fixes, whether they identified unforeseen issues and whether they suggested test cases or best coding practices.

The project aimed to assess AI's effectiveness in debugging, the level of trust placed in suggested fixes and whether human judgement was needed to investigate those suggestions.

## AI Strengths
All three models correctly identified the bugs and provided reasoning and suggested fixes. However, their responses varied with some models being better suited to particular aspects of debugging.

Gemini consistently identified and labelled the type of bug before explaining why it caused an issue and how to fix it. Claude was the only model to identify an additional unforeseen bug in `bug4.js`, which the other models missed. Claude and Gemini also provided clear and concise responses without unnecessary detail.

## AI Weaknesses
Although ChatGPT correctly identified all bugs, it suggested a fix in `bug5.js` that indirectly changed the intended logic.

The original issue involved the Boolean condition `hasPermission === false`. ChatGPT suggested changing this to `hasPermission === true` **AND** changing the rule to `if (age >= 18 && hasPermission === true)` instead of keeping `if (age >= 18 || hasPermission === true)`.

This demonstrated that AI can not only make mistakes but can also unintentionally steer developers towards changing their code's logic while attempting to fix a bug.

## Human Role
No significant manual intervention was required however, `bug4.js` demonstrated that some issues can have multiple valid solutions.

The `for` loop could be corrected by:
- adding `=` so it included `itemIndex <= lastIndex`
- OR removing `lastIndex` and using `itemIndex < shoppingList.length`

This led to further research and prompting AI to determine the best approach from a code cleanliness and optimisation perspective.

## Conclusion
In summary, this project demonstrated that AI can be useful for identifying and resolving coding issues. AI can save developers time by helping detect, interpret and fix bugs more efficiently.

However, AI can also suggest fixes that unintentionally change existing logic. Therefore, AI-assisted debugging should be approached critically rather than relying on the model's initial response. Human judgement remains important, particularly when debugging under tight time constraints.