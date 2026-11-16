/** Demo-only password-reset request handler; no messages are sent. */
function createResetHandler() {
  const queuedRequests = [];

  function requestReset(email, nowMs) {
    if (typeof email !== "string" || !email.includes("@")) {
      return { status: 400, message: "Invalid email" };
    }
    if (!Number.isFinite(nowMs)) {
      return { status: 400, message: "Invalid timestamp" };
    }

    // BUG: unlimited requests are accepted for the same account.
    queuedRequests.push({ email, requestedAt: nowMs });
    return { status: 202, message: "Request accepted" };
  }

  return { requestReset, queuedRequests };
}

if (require.main === module) {
  const handler = createResetHandler();
  console.log(handler.requestReset("alex@example.test", 1000));
  console.log(handler.requestReset("alex@example.test", 1001));
}

module.exports = { createResetHandler };
