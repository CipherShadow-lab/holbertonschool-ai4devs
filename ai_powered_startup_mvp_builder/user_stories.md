# BLOOM — MVP User Stories

## Story 1 — Browse supported species
**As a** visitor, **I want** to browse a list of supported plants **so that** I can discover what BLOOM tracks.
- **Acceptance criteria:** The list shows each supported species with its name and a link to details.

## Story 2 — Search the species list
**As a** visitor, **I want** to search species by name **so that** I can find a plant quickly.
- **Acceptance criteria:** A partial, case-insensitive name returns matching species; an unmatched query shows an empty state.

## Story 3 — Read species details
**As a** visitor, **I want** to view a species detail page **so that** I can recognise the plant before looking for sightings.
- **Acceptance criteria:** The page displays the common name, description and reference image when available.

## Story 4 — View local sightings
**As a** visitor, **I want** to see reported sightings on a map **so that** I can explore flowering plants by location.
- **Acceptance criteria:** Each valid geolocated sighting has a map marker that opens its details.

## Story 5 — Filter sightings by species
**As a** visitor, **I want** to select a species filter **so that** the map shows only relevant sightings.
- **Acceptance criteria:** Selecting Magnolia shows only Magnolia sightings; clearing the filter restores all supported sightings.

## Story 6 — Inspect sighting details
**As a** visitor, **I want** to open a sighting **so that** I can check when and where it was reported.
- **Acceptance criteria:** Details show species, observation date, location and optional notes or photo; missing optional fields do not break the view.

## Story 7 — Submit a sighting
**As a** contributor, **I want** to report a plant sighting **so that** others can discover it.
- **Acceptance criteria:** A valid submission includes a supported species, coordinates and observation date; the saved sighting appears on the map.

## Story 8 — Receive submission feedback
**As a** contributor, **I want** clear validation messages **so that** I can correct incomplete or invalid reports.
- **Acceptance criteria:** Missing species, invalid coordinates and invalid dates are rejected with understandable messages; no invalid record is stored.

## Story 9 — Add a sighting photo
**As a** contributor, **I want** to attach an optional photo **so that** other users can better recognise the plant.
- **Acceptance criteria:** Supported image formats within the configured size limit are accepted; an unsupported or oversized upload is rejected; photo omission is allowed.

## Story 10 — Comment on a sighting
**As a** visitor, **I want** to leave a short comment on a sighting **so that** I can share observations or uncertainty about it.
- **Acceptance criteria:** A non-empty comment within the length limit is stored against the correct sighting and displayed in chronological order.

## Scope Note
These stories describe the BLOOM MVP, not all previously designed screens. Authentication, hayfever alerts and automatic plant identification remain potential later features.
