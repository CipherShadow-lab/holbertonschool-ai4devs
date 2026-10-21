![HITCHDREADME](/Images/HITCHDREADME2.png)  
<br>

# AI-Assisted Specification Refinement

I decided to include a README for this part of the project, for I felt it was important to explain the purpose of the refinement stage and detail my reasonings.  

## Purpose

The purpose of this refinement stage is not to rewrite every specification item. Instead, AI-generated specifications are reviewed critically to identify areas where improvements can provide genuine value through clearer language, greater consistency, improved technical precision, or appropriate security considerations.

## Approach to AI-Assisted Refinement

AI was used as a collaborative tool to review the existing HITCHD specifications and identify opportunities for improvement.

The refinement process followed these principles:

- **Verify first**: Proposed changes were checked against the original HITCHD product concept and previously approved user stories.
- **Refine with purpose**: A specification was only changed when the refinement provided a clear benefit.
- **Preserve scope**: Refinements were not used to introduce new MVP features or unsupported technical requirements.
- **Maintain consistency**: Terminology and responsibilities were reviewed across user stories, system components, data models, and APIs.
- **Challenge AI output**: AI suggestions were critically reviewed rather than accepted automatically.
- **Consider security**: Security improvements were included where they directly supported existing product requirements without creating a separate security specification.
- **Prefer clarity over complexity**: Refinement was not treated as an instruction to make specifications longer or more technical.

## Examples of Meaningful Refinement

### User Stories

An original user story stated:

> As a driver, I want to publish a journey with available seats and a requested contribution so that passengers travelling in the same direction can request to share my journey.

The refined version makes the required journey information explicit:

> As a driver, I want to publish a journey with an origin, destination, departure time, available seats, and requested contribution so that passengers travelling in the same direction can find and request my shared journey.

This refinement adds value because the information required to publish a journey is already established by the HITCHD product concept. The refinement therefore improves precision without introducing a new feature.

### API Design

The original booking endpoint was:

> POST /rides/{ride_id}/bookings { passenger_id }

The refined version is:

> POST /rides/{ride_id}/bookings — creates a booking request for the authenticated passenger.

This avoids unnecessarily trusting a client-provided passenger identity and makes the relationship between authentication and booking clearer. It also avoids prematurely specifying an implementation such as JWT or OAuth.

### Payment Security

The original Payment Service stated that it would use a third-party payment provider.

The refined specification makes an important security implication explicit:

> Payment Service: Processes journey contributions through the integrated third-party payment provider without storing raw payment card details and associates the resulting payment status with the relevant booking.

This does not introduce a new payment feature. It clarifies an existing design direction and reduces unnecessary handling of sensitive payment information.

## When AI Suggestions Were Not Used

Not every specification required refinement.

For example, the original Ride data model was already sufficiently clear:

> Ride: id, driver_id, origin, destination, departure_time, available_seats, requested_contribution, status

Changing this simply for the sake of demonstrating refinement would not provide a meaningful benefit.

Similarly, an API such as:

> GET /rides/{ride_id}

is already concise and understandable. Adding unnecessary wording or parameters would make the specification less useful rather than more precise.

This demonstrates an important principle of AI-assisted documentation:

> **Refinement does not mean changing everything.**

A human reviewer must determine whether an AI-proposed change actually improves the specification.

## Security and Scope Considerations

Security was considered during refinement, but only where it was directly relevant to the existing HITCHD MVP.

Examples include:

- **Authentication**: API operations should operate within an authenticated user context where appropriate.
- **Authorisation**: Booking changes should only be performed by an authorised user.
- **Payment protection**: Raw payment card details should not be stored by HITCHD when using the proposed third-party payment provider.
- **User identity**: Sensitive identity information should not be unnecessarily supplied by clients when it can be determined from the authenticated request.

More advanced security mechanisms were deliberately not specified because they would require additional architectural decisions that are outside the current project scope.

## Human Verification and Critical Thinking

AI can produce technically plausible specifications, but plausibility does not guarantee correctness.

The refined HITCHD specification was therefore reviewed against the previous project outputs to ensure that:

- The product concept remained unchanged.
- User stories remained consistent with the identified user groups.
- Technical components supported the approved MVP capabilities.
- APIs corresponded to the documented user interactions.
- Data models supported the required functionality.
- Security considerations did not introduce unnecessary scope.
- New requirements were not invented simply because they were technically possible.

This review highlighted that AI can sometimes favour additional detail when a shorter specification would be clearer. Human judgement was therefore used to distinguish **useful precision from unnecessary elaboration**.

## Key Learning

The refinement process demonstrated that AI is most effective when used as a **collaborative specification assistant rather than an unquestioned author**.

AI can quickly identify ambiguities, suggest alternative wording, detect inconsistencies, and propose technical improvements. However, the resulting suggestions still require human verification against the original product requirements and project scope.

For HITCHD, the most valuable refinement was therefore not adding the greatest amount of detail. It was identifying **which details mattered** and which proposed changes should be rejected.

The overall approach can be summarised as:

**Generate → Review → Verify → Refine → Challenge → Finalise**

This approach helps ensure that AI-assisted specifications remain clear, consistent, technically useful, and aligned with the intended product.