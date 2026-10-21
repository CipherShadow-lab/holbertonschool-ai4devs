![HITCHDREFLECT](/Images/HITCHDREFLECT.png)  
<br>

# Reflection on AI-Assisted Specification Writing

## Introduction

This project explored how AI can assist with transforming a product idea into a structured specification package. HITCHD was developed as a shared-journey application connecting drivers with available seats and passengers seeking suitable rides. AI was used throughout the process to help produce user stories, acceptance criteria, technical specifications, API definitions, and refinement documentation. The experience demonstrated that AI can significantly accelerate specification writing, but effective results still depend on human verification, product knowledge, and critical thinking.

## AI Strengths

AI was particularly effective at quickly transforming high-level product ideas into structured documentation. It was able to generate user stories in a consistent format and translate those stories into acceptance criteria that could be understood by both product and technical audiences.

AI also performed well when producing the initial technical specification. It identified logical system components such as authentication, rides, bookings, payments, and trust and safety, and connected these components to appropriate data models and API endpoints. This created a useful starting point for thinking about how the product could be structured technically without requiring implementation decisions.

Another strength was maintaining consistency across related documentation. Once the product requirements and user stories had been established, AI could use them as a foundation for developing subsequent specifications and identifying relationships between features, components, models, and APIs.

## AI Weaknesses

The most significant weakness was a tendency toward over-specification. During refinement, AI initially attempted to improve almost every part of the documentation, even when some sections were already sufficiently clear. This demonstrated that refinement does not automatically mean adding more detail.

AI can also introduce technically plausible requirements that were not actually part of the original product concept. For example, it would have been easy to introduce technologies, advanced security mechanisms, GPS functionality, ratings, or other features simply because they could be relevant to a real application. While these suggestions may be technically reasonable, including them would have expanded the HITCHD MVP beyond its defined scope.

This highlighted an important limitation: AI can produce convincing content without necessarily understanding which requirements are appropriate for the specific project unless the human reviewer provides and enforces clear boundaries.

## Human Role

Human refinement was critical throughout the project. The product concept and identified user groups were treated as the source of truth, ensuring that later specifications remained traceable to the original requirements.

The refinement stage was particularly valuable. Rather than accepting every AI-generated improvement, proposed changes were questioned based on whether they provided a genuine benefit. Some specifications were deliberately left unchanged because they were already clear. Other changes improved precision, terminology, consistency, or security without introducing new functionality.

Security was also considered through human review. For example, the booking API was refined so that the authenticated passenger's identity could be associated with the request rather than unnecessarily trusting a client-provided passenger ID. Payment processing was also clarified to reinforce the use of a third-party provider without storing raw payment card details.

## Lessons Learned

The main lesson from this project is that AI works best as a **collaborative specification assistant rather than an unquestioned author**. It is highly effective at generating alternatives, identifying structures, and accelerating the initial documentation process, but human judgement remains essential for determining whether an output is correct, useful, secure, and within scope.

A practical approach for real-world specification writing is:

**Generate → Review → Verify → Refine → Challenge → Finalise**

AI can suggest what could be changed, but the product developer must decide whether it should be changed. The most valuable use of AI is therefore not simply producing more documentation, but helping humans produce **clearer, more consistent, and more useful documentation while retaining control over product decisions and scope**.