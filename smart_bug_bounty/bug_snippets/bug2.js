/** Demo-only profile rendering with intentionally unsafe DOM insertion. */
function renderProfile(name, outputElement) {
  if (typeof name !== "string") {
    throw new TypeError("Name must be a string");
  }

  // BUG: browser interprets untrusted name as HTML markup.
  outputElement.innerHTML = `<p>Welcome, ${name}</p>`;
  return outputElement.innerHTML;
}

// Local browser example: create a <div id="profile"></div> first.
if (typeof document !== "undefined") {
  const target = document.getElementById("profile");
  if (target) {
    renderProfile("Alex", target);
  }
}

if (typeof module !== "undefined") {
  module.exports = { renderProfile };
}
