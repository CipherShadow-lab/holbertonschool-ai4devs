// Code snippet contains a Logical Error due to a boolean condition.

function canAccessCourse(age, hasPermission) {
    if (age >= 18 || hasPermission === false) {
        return true;
    }

    return false;
}

const studentAge = 16;
const studentHasPermission = false;

const accessGranted = canAccessCourse(
    studentAge,
    studentHasPermission
);

console.log("Course access:", accessGranted);
