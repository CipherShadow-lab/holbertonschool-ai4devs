![HITCHTECH](/Images/HITCHDREFINED.png)  
<br>

# Refined Specification

## User Stories

- **Original**: As a driver, I want to publish a journey with available seats and a requested contribution so that passengers travelling in the same direction can request to share my journey.
- **Refined**: As a driver, I want to publish a journey with an origin, destination, departure time, available seats, and requested contribution so that passengers travelling in the same direction can find and request my shared journey.

- **Original**: As a passenger, I want to search for available journeys using my journey details and departure preferences so that I can find a suitable shared ride.
- **Refined**: As a passenger, I want to search for available journeys using my origin, destination, and departure preferences so that I can find a suitable shared ride.

- **Original**: As a passenger, I want to request a seat on an available journey so that I can arrange a shared ride to my destination.
- **Refined**: As a passenger, I want to request an available seat on a listed journey so that I can arrange a shared ride and track whether my booking request is pending, confirmed, or declined.

- **Original**: As a driver, I want to manage passenger booking requests so that I can decide which passengers can share my journey.
- **Refined**: As a driver, I want to review, accept, or decline passenger booking requests for my published journeys so that I can manage who shares my available seats.

- **Original**: As a passenger, I want to pay my agreed contribution through the application so that I can complete payment for a confirmed shared journey.
- **Refined**: As a passenger, I want to pay my agreed journey contribution through the application using the integrated third-party payment provider so that the payment is associated with my confirmed booking.

- **Original**: As a HITCHD user, I want to report inappropriate behaviour so that I can raise a trust or safety concern.
- **Refined**: As a HITCHD user, I want to report inappropriate behaviour associated with a user or journey so that I have a clear mechanism for raising a trust or safety concern.

## System Components

- **Original**: Authentication Service: Handles user registration, authentication, account access, and basic profile information.
- **Refined**: Authentication Service: Handles user registration and authentication and provides authenticated account access for HITCHD users.

- **Original**: Ride Service: Allows drivers to create and manage ride listings containing origin, destination, departure time, available seats, and requested contribution.
- **Refined**: Ride Service: Creates and manages ride listings containing origin, destination, departure time, available seats, requested contribution, and ride status, and supports passenger ride searches.

- **Original**: Booking Service: Manages passenger booking requests, driver acceptance or decline decisions, booking status, and eligible cancellations.
- **Refined**: Booking Service: Manages passenger seat requests, driver acceptance or decline decisions, booking status transitions, and eligible booking cancellations.

- **Original**: Payment Service: Integrates with a third-party payment provider to process journey contributions and associate payment status with the relevant booking.
- **Refined**: Payment Service: Processes journey contributions through the integrated third-party payment provider without storing raw payment card details and associates the resulting payment status with the relevant booking.

## Data Models

- **Original**: User: id, name, email, role, profile_information
- **Refined**: User: id, name, email, role, profile_information, authentication_status

- **Original**: Booking: id, ride_id, passenger_id, status, payment_status, payment_reference
- **Refined**: Booking: id, ride_id, passenger_id, status, payment_status, payment_reference

## API Endpoints

- **Original**: POST /auth/register
- **Refined**: POST /auth/register { name, email, password, role }

- **Original**: POST /auth/login
- **Refined**: POST /auth/login { email, password } — authenticates the user and establishes authenticated access.

- **Original**: POST /rides/{ride_id}/bookings
- **Refined**: POST /rides/{ride_id}/bookings — creates a booking request for the authenticated passenger.

- **Original**: PATCH /bookings/{booking_id}
- **Refined**: PATCH /bookings/{booking_id} { status } — updates the booking status for an authorised user according to the applicable booking action.

- **Original**: POST /bookings/{booking_id}/payment
- **Refined**: POST /bookings/{booking_id}/payment { payment_method } — initiates payment through the third-party payment provider and records the resulting payment status against the booking.

- **Original**: POST /reports
- **Refined**: POST /reports { reported_user_id, ride_id, description } — submits a trust and safety report from the authenticated user concerning a relevant user or journey.