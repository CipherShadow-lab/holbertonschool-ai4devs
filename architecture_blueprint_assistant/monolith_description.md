![HITCHARCH](/Images/HITCHDARCH.png)  
<br>

# Monolithic Architecture

- **Mobile App**: Provides the interface used by drivers and passengers to access HITCHD functionality.
- **HITCHD Backend Monolith**: Contains the application's core business logic and internal modules required to operate the platform. These modules are deployed as part of a single backend application.
- **Authentication Module**: Manages user authentication and access to HITCHD.
- **Ride Management Module**: Allows drivers to publish and manage journeys and provides the logic required for passengers to find suitable journeys.
- **Booking Module**: Manages passenger booking requests and associated booking status.
- **Payment Module**: Manages journey contribution payments through the integrated third-party payment provider without storing raw payment card details.
- **Trust & Safety Module**: Supports the existing trust and safety functionality, including mechanisms for users to report inappropriate behaviour.
- **HITCHD Database**: Centrally stores the application data required by the backend modules, including user, journey, booking and payment-related information.  