# Product Idea  
<br>
![HITCHD](/Images/HITCHED3.png)  
<br>

## Vision
HITCHD is a mobile carpooling platform that connects drivers with available seats to passengers travelling in the same direction. Its vision is to make everyday journeys more affordable, convenient and efficient by helping people share rides and contribute toward travel costs.

- **Brand Name**: HITCHD
- **Tagline**: Hitch a ride. Save your stride.
- **Supporting Brand Line**: Your journey just got smarter.

HITCHD aims to encourage shared journeys, reduce reliance on solo car travel and improve the use of available vehicle capacity. The brand personality is bold, urban, community-oriented and practical - making carpooling feel accessible and appealing to everyday travellers.

The initial product will be a focused Minimum Viable Product (MVP) for a mobile application. The objective of this part of the project is to define a viable, technically buildable product and document its requirements, user stories, acceptance criteria architecture, APIs and data models.

## Users
- **Drivers**: People travelling to work, university or other destinations who have spare seats in their vehicles. They want to publish journeys, specify available seats and departure times, request a contribution toward shared travel costs, manage passenger booking requests and receive payments for confirmed shared journeys.
- **Passengers**: People looking for affordable and convenient transport to work, university or other destinations. They want to search for available rides, compare journey details and cost contributions, request seats, manage bookings and pay their agreed contribution through the application.
- **General Community**: People outside the traditional commuter and university student groups who want to share journeys with others travelling in the same direction. They need an accessible way to find suitable rides and coordinate shared travel.
- **Shared User Needs**: Users need clear journey information, reliable booking status updates, transparent cost contributions, secure account access, and a straightforward way to manage bookings and payments. Basic trust and safety measures, including access to relevant user profiles and a mechanism for reporting inappropriate behaviour are also important.

## Key Features

- **User Registration and Profiles**: Allow users to create accounts, authenticate themselves, and maintain basic profile information.
- **Ride Listings**: Allow drivers to publish and manage journeys with an origin, destination, departure time, available seats and requested contribution toward shared travel costs.
- **Ride Search**: Allow passengers to search for available journeys using journey details and departure preferences.
- **Booking Management**: Allow passengers to request seats and drivers to accept or decline requests. Users can view booking statuses and manage eligible cancellations.
- **In-App Payments**: Integrate a third-party payment provider so passengers can pay agreed journey contributions through the application. Associate payment records with bookings and display relevant payment statuses. Payment failures, cancellations, refunds and payment confirmations will be addressed in the technical specification.
- **Booking and Payment Status**: Display relevant booking states, such as pending, confirmed, declined, or cancelled, and payment states, such as pending, successful, failed or refunded where applicable.
- **Basic Trust and Safety**: Provide relevant user and journey information and a mechanism for reporting inappropriate behaviour. Detailed identity verification, driver eligibility and vehicle verification requirements remain to be defined.

## Key Differentiators
- Combine shared-journey discovery, booking management, and integrated cost contributions in one mobile experience. Use a bold, urban brand identity to appeal to commuters, university students, and the wider community.
## Intended Benefits
- Help passengers access more affordable travel, help drivers offset some journey expenses, encourage better use of available vehicle seats, and potentially reduce solo car journeys. These are intended benefits that have not yet been measured or validated.

## MVP Scope
- Prioritise account creation, ride publishing, ride search, booking requests, booking management, in-app payments, and booking and payment status visibility. Keep the first release focused on the essential carpooling journey rather than adding non-essential functionality.

## Future Releases
- Consider ratings and reviews, live GPS location sharing, advanced route matching, push notifications and journey reminders, environmental impact estimates, enhanced identity verification, and expanded booking and payment options. These features are candidates for future prioritisation, not commitments for the initial release.

## Technical and Product Considerations
- The application is intended to use a mobile client, a backend service, and persistent data storage. A third-party payment provider is proposed so the application does not need to store raw payment card details. The supported mobile platforms, launch regions, currencies, payment and payout arrangements, cancellation and refund rules, privacy requirements, and detailed trust and safety requirements remain open questions for subsequent specification work.

## Project Deliverables
- Develop a structured documentation package containing product requirements, user stories, acceptance criteria, functional and non-functional requirements, system architecture, API specifications, data models, and a reflection on the effectiveness of AI in specification writing. Building and deploying the application are outside the scope of this documentation-focused assignment unless separately required. 