# Microservices Architecture

- **API Gateway**: Provides a single entry point for requests from the mobile application and routes requests to the appropriate backend service.
- **Authentication Service**: Manages user authentication and access to HITCHD.
- **User Profile Service**: Manages basic user profile information required by the application.
- **Ride Service**: Manages driver journeys, including publishing and managing available rides and supporting ride searches.
- **Booking Service**: Manages passenger booking requests and booking status. It interacts with the Ride Service to work with available journeys and the Payment Service when a journey contribution payment is required.
- **Payment Service**: Manages journey contribution payments through the integrated third-party payment provider without storing raw payment card details.
- **Trust & Safety Service**: Manages trust and safety functionality, including mechanisms for users to report inappropriate behaviour. It can interact with user and booking information when required to process a report.
- **Service Data Stores**: Each service owns its application data separately, reducing direct dependency on a shared database between services.