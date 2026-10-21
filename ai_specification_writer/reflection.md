![HITCHDREFLECT](/Images/HITCHDREFLECT.png)  
<br>

# Reflection on AI-Assisted Specification Writing

## Introduction

This project explored how AI can assist with transforming a product idea into a structured specification package. HITCHD was developed as a shared-journey application connecting drivers with available seats and passengers seeking suitable rides. AI was used to generate and refine user stories, technical specifications, APIs, and supporting documentation. The experience demonstrated that AI can accelerate specification writing, but the quality of its output depends heavily on the quality of the prompt, the context provided, and human verification.

## AI Strengths

AI handled structured and clearly defined tasks particularly well. Prompts that provided the product context, required format, constraints, and expected output produced useful results quickly. Generating user stories and converting established requirements into technical components and API examples were relatively straightforward because these tasks had clear patterns and boundaries.

More open-ended tasks were harder. Asking AI to “improve” an entire specification initially encouraged over-refinement, with changes being suggested even where the original content was already clear. This demonstrated that broader prompts can produce plausible but unnecessary output, while focused prompts with explicit constraints are more effective.

Prompt structure also influenced the quality of the results. Providing a role, such as asking AI to approach a problem from a product or technical perspective, helped establish an appropriate mindset. Specifying the desired tone, level of technical detail, and document format reduced ambiguity. Placeholders and explicit context were also useful when information was intentionally unknown, because they prevented assumptions from being presented as confirmed requirements.

## AI Weaknesses

A significant weakness was AI's tendency to add technically plausible detail that was not necessarily required. During refinement, AI initially treated improvement as an opportunity to modify almost every specification item. Without explicit instructions to preserve scope, this could have introduced unnecessary features or implementation decisions.

One successful prompting adjustment was to explicitly instruct AI to preserve the existing MVP and only make changes that provided a measurable benefit. This produced a much stronger refinement process. Conversely, a less constrained approach produced unnecessary elaboration. This demonstrated that prompt wording directly affects whether AI behaves as a useful reviewer or simply generates more content.

## Human Role

Human refinement was critical for verifying AI output against the original HITCHD product concept and previously established user groups. Proposed changes were assessed for clarity, consistency, security, and scope rather than being accepted automatically.

The strongest example was the refinement of the booking API. Instead of continuing with a client-provided `passenger_id`, the specification was refined so that the request was associated with the authenticated passenger. This improved the security and technical clarity of the specification without introducing a new feature.

Security considerations were also applied selectively to payment processing. The use of a third-party payment provider was clarified without expanding the project into a full security architecture.

## Lessons Learned

The project demonstrated that effective AI-assisted specification writing depends on **prompt quality, structured context, and critical human review**. Easier prompt types were those with a defined format and clear source requirements, while harder prompts were broad requests such as “refine this specification” because they required judgement about what should and should not change.

A strong prompt should establish the **role, context, objective, constraints, tone, expected structure, and relevant placeholders or known limitations**. These elements influence how AI interprets the task and help prevent unsupported assumptions.

The most important lesson is that AI should be treated as a **collaborative specification assistant rather than an unquestioned author**. A practical process is:

**Define → Prompt → Review → Verify → Refine → Challenge → Finalise**

AI can suggest what could be changed, but the product developer must decide whether it should be changed. The goal is therefore not to produce the most detailed specification possible, but the **clearest, most consistent, useful, and appropriately scoped specification possible**.