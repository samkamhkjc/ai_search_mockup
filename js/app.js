/**
 * Shared: load demo-results.json
 * Expects to run in a page served over HTTP so fetch works (no file:// CORS).
 */
function loadDemoData() {
  return fetch('data/demo-results.json').then(function (r) {
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return r.json();
  });
}
