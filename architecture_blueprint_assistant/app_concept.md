# Application Concept – HITCHD

## Application
Mobile carpooling platform connecting drivers with available vehicle seats to passengers travelling in the same direction. HITCHD aims to make everyday journeys more affordable, convenient and efficient by enabling users to share rides and contribute toward travel costs.

## Core Features
- User registration, authentication and basic profile management
- Drivers can publish journeys with origin, destination, departure time, available seats and requested contribution
- Passengers can search for available journeys based on their journey details and departure preferences
- Passengers can view journey details and request available seats
- Drivers can review, accept, or decline passenger booking requests
- Users can view and manage their booking status
- Passengers can make journey contribution payments through an integrated third-party payment provider
- Users can report inappropriate behaviour through a trust and safety mechanism

## Users
- Drivers: offer available vehicle seats and manage shared journeys and passenger booking requests
- Passengers: search for suitable shared journeys, request available seats and make applicable journey contribution payments
- General Community: use HITCHD as members of a shared-journey community and contribute to a safer and more efficient approach to everyday travel
- Shared User Needs: secure account access, clear journey and booking information, reliable status updates and a straightforward mechanism for raising trust and safety concerns

## Constraints
- MVP scope: The initial application focuses on core carpooling functionality and should avoid unnecessary features or implementation complexity
- Scalability: The architecture should allow the application to grow as usage increases without requiring the initial MVP to be over-engineered
- Payments: Journey contributions should be processed through a third-party payment provider rather than storing raw payment card details within HITCHD
- Platform: The initial product scope is a focused mobile application for drivers and passengers
- Security: Authentication, authorised access, payment protection, and trust and safety considerations should be incorporated into the architecture
- Maintainability: Application components should have clear responsibilities so that the system can be maintained and evolved as HITCHD develops