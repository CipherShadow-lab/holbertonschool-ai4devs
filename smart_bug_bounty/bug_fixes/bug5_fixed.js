/** Demo-only in-memory per-email rolling-window rate limiter. */
function createResetHandler() {
  const queuedRequests = [];
  const acceptedByEmail = new Map();
  const WINDOW_MS = 60000;
  const LIMIT = 3;

  function requestReset(email, nowMs) {
    if (typeof email !== "string" || !email.includes("@")) {
      return { status: 400, message: "Invalid email" };
    }
    if (!Number.isFinite(nowMs)) {
      return { status: 400, message: "Invalid timestamp" };
    }
    const key = email.trim().toLowerCase();
    const recent = (acceptedByEmail.get(key) || []).filter(
      timestamp => timestamp <= nowMs && nowMs - timestamp < WINDOW_MS
    );
    if (recent.length >= LIMIT) {
      acceptedByEmail.set(key, recent);
      return { status: 429, message: "Too many requests" };
    }
    recent.push(nowMs);
    acceptedByEmail.set(key, recent);
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
