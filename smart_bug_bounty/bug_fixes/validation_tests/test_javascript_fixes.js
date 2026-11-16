const assert = require("assert");
const {renderProfile} = require("../bug_fixes/bug2_fixed");
const {createResetHandler} = require("../bug_fixes/bug5_fixed");
function target() {
  const obj = { children: [], ownerDocument: {createElement: () => ({textContent: ""})},
    replaceChildren(...children) {this.children = children;},
    get innerHTML() {return this.children.map(c=>"<p>"+c.textContent.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")+"</p>").join("");}};
  return obj;
}
let t=target();assert.strictEqual(renderProfile("Alex",t),"<p>Welcome, Alex</p>");
t=target();assert.ok(renderProfile("<img src=x onerror=alert(1)>",t).includes("&lt;img"));
t=target();assert.throws(()=>renderProfile(1,t),TypeError);
t=target();t.replaceChildren({textContent:"old"});renderProfile("New",t);assert.strictEqual(t.children.length,1);
let h=createResetHandler();for(let i=0;i<3;i++)assert.strictEqual(h.requestReset("a@test.com",i).status,202);
assert.strictEqual(h.requestReset("a@test.com",3).status,429);assert.strictEqual(h.queuedRequests.length,3);
assert.strictEqual(h.requestReset("a@test.com",60000).status,202);
h=createResetHandler();assert.strictEqual(h.requestReset("b@test.com",1).status,202);
assert.strictEqual(h.requestReset("c@test.com",1).status,202);
h=createResetHandler();for(let i=0;i<3;i++)h.requestReset("A@Test.com",i);
assert.strictEqual(h.requestReset("a@test.com",3).status,429);
h=createResetHandler();assert.strictEqual(h.requestReset("invalid",1).status,400);
assert.strictEqual(h.requestReset("a@test.com",NaN).status,400);
console.log("9 JavaScript tests passed");
