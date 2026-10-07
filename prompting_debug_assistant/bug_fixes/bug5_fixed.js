// Code is fixed by ensuring both conditions are true - using && rather than ||.
// Note: const studentHasPermission was required to be 'true', which is an additional change that ChatGPT failed to inform the user/dev.
// Note: This meant the code remained broken until the value for studentHasPermission was changed from 'false' to 'true'. 

function canAccessCourse(age, hasPermission) {
    return age >= 18 && hasPermission
}

const studentAge = 18;
const studentHasPermission = true;

const accessGranted = canAccessCourse(
    studentAge,
    studentHasPermission
);

console.log("Course access:", accessGranted);
