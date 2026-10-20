![HITCHTECH](/Images/HITCHDTECH.png)  
<br>

# Technical Specification

## System Components
- **Mobile Application**: Provides the user interface for drivers and passengers to register, manage profiles, publish and search for rides, manage bookings, view statuses, make payments and report inappropriate behaviour.
- **Authentication Service**: Handles user registration, authentication, account access and basic profile information.
- **Ride Service**: Allows drivers to create and manage ride listings containing origin, destination, departure time, available seats and requested contribution.
- **Booking Service**: Manages passenger booking requests, driver acceptance or decline decisions, booking status and eligible cancellations.
- **Payment Service**: Integrates with a third-party payment provider to process journey contributions and associate payment status with the relevant booking.
- **Trust and Safety Service**: Supports access to relevant user and journey information and provides a mechanism for users to report inappropriate behaviour.
- **Persistent Data Storage**: Stores user, ride, booking and relevant payment status information required by the application.
- **API Gateway**: Provides a central interface between the mobile application and backend services and routes requests to the appropriate service.

## Data Models
- **User**: id, name, email, role, profile_information
- **Ride**: id, driver_id, origin, destination, departure_time, available_seats, requested_contribution, status
- **Booking**: id, ride_id, passenger_id, status, payment_status, payment_reference

## API Endpoints
- **POST /auth/register**: Creates a user account. Parameters: name, email, password, role.
- **POST /auth/login**: Authenticates a registered user. Parameters: email, password.
- **POST /rides**: Creates a new ride listing. Parameters: origin, destination, departure_time, available_seats, requested_contribution.
- **POST /rides/search**: Searches for available rides. Parameters: origin, destination, departure_preferences.
- **GET /rides/{ride_id}**: Retrieves the details of a specific ride. Parameters: ride_id.
- **POST /rides/{ride_id}/bookings**: Creates a passenger booking request for a ride. Parameters: ride_id, passenger_id.
- **PATCH /bookings/{booking_id}**: Updates a booking status, including driver acceptance, decline, or an eligible cancellation. Parameters: booking_id, status.
- **POST /bookings/{booking_id}/payment**: Initiates payment for an applicable booking through the third-party payment provider. Parameters: booking_id, payment_method.
- **GET /bookings/{booking_id}**: Retrieves booking and associated payment status. Parameters: booking_id.
- **POST /reports**: Submits a report concerning inappropriate behaviour. Parameters: reported_user_id, ride_id, description.