/** Demo-only profile rendering using safe text insertion. */
function renderProfile(name, outputElement) {
  if (typeof name !== "string") {
    throw new TypeError("Name must be a string");
  }
  const paragraph = outputElement.ownerDocument.createElement("p");
  paragraph.textContent = `Welcome, ${name}`;
  outputElement.replaceChildren(paragraph);
  return outputElement.innerHTML;
}

if (typeof document !== "undefined") {
  const target = document.getElementById("profile");
  if (target) renderProfile("Alex", target);
}
if (typeof module !== "undefined") module.exports = { renderProfile };
