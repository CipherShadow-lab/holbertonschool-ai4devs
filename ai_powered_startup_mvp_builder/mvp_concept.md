# BLOOM — MVP Concept

## Problem Statement
People who want to discover flowering trees and plants in their area often lack a simple way to find recent, location-specific sightings. General maps and plant-identification resources do not necessarily show where a particular species has been spotted. BLOOM aims to make local botanical discovery easier through a community-maintained map of plant sightings.

## Target Users
- Local residents and nature enthusiasts looking for flowering plants nearby.
- Walkers and photographers seeking particular species or seasonal blooms.
- Community contributors who want to share verified-by-location observations (not expert-verified identifications).

## Core Features
1. **Browse plant species:** View a searchable list of supported species and open concise plant detail pages.
2. **Explore sightings on a map:** View geolocated sightings and filter map markers by species to reduce clutter.
3. **Submit a sighting:** Add a species, location, observation date and optional photo with basic input validation.
4. **View sighting details:** Open a marker to see the species, date, photo when available and contributor notes.
5. **Review sightings:** Add a short community comment to an existing sighting to share observations or flag uncertainty.

## Constraints
- MVP supports a limited curated set of species, initially Magnolia, Jacaranda, Wattle and Bottlebrush.
- A responsive web implementation is acceptable for the MVP; the existing mobile UI designs guide its appearance.
- No automated species identification, pollen forecasting, advanced moderation or payment features in the initial release.
- Sighting locations are user-submitted and may be inaccurate; display observation dates and avoid claiming real-time bloom status.
- Photos are optional. Limit file size and accepted formats; avoid retaining unnecessary image metadata where feasible.
- Basic contributor identification may use a simple display name or session identity; full account management is deferred.
- Deployment, database and mapping choices will be confirmed during implementation, prioritising a small, testable stack.

## MVP Success Criteria
A user can find a supported species, filter the map to that species, inspect a sighting and submit a new sighting that persists and becomes visible on the map. Core flows are covered by automated tests.
