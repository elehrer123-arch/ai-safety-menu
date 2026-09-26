/* The AI Safety Menu: shared p(doom) arithmetic, used by the page, the build and the preview images.
   Each rule removes a share of the remaining risk (risk.central, a fraction; negative adds risk).
   Rules in the same group overlap: together they can remove at most the group's cap.
   Bills count as their parts. */
(function (root) {
  function list(D) { return D.policies.concat(D.combos); }
  function expand(ids, D) {
    const all = list(D), by = id => all.find(p => p.id === id), out = [];
    ids.forEach(id => { const p = by(id); if (!p) return; (p.components || [id]).forEach(c => { const q = by(c); if (q && q.risk && out.indexOf(q) < 0) out.push(q); }); });
    return out;
  }
  // Share of p(doom) removed by a set of rules. k: 'low' | 'central' | 'high'.
  // ov (optional): { id: share } replaces a rule's own estimate with a player's number.
  // adj (optional): { id: scale } multiplies a rule's estimate after the player changes its assumptions; overlap caps still apply.
  function cut(ids, D, k, ov, adj) {
    k = k || 'central'; const G = (D.risk && D.risk.groups) || {}, groups = {}; let keep = 1;
    // A player's own number counts as they set it, outside the overlap caps.
    expand(ids, D).forEach(p => { const mine = ov && ov[p.id] != null, r = mine ? ov[p.id] : p.risk[k] * (adj && adj[p.id] != null ? adj[p.id] : 1), g = p.risk.group;
      if (g && G[g] && r > 0 && !mine) (groups[g] = groups[g] || []).push(r); else keep *= (1 - r); });
    Object.keys(groups).forEach(g => { const cap = G[g].cap;
      keep *= 1 - cap * (1 - groups[g].reduce((a, r) => a * (1 - Math.min(r, cap) / cap), 1)); });
    return 1 - keep;
  }
  const one = (p, D, k, ov, adj) => cut([p.id], D, k, ov, adj);
  const BANDS = [
    { min: 0.10, pips: 4, label: 'Large' }, { min: 0.04, pips: 3, label: 'Medium' },
    { min: 0.015, pips: 2, label: 'Small' }, { min: 0.0005, pips: 1, label: 'Tiny' }];
  function band(r) {
    if (r <= -0.0005) { const a = -r; return { adds: true, pips: a >= 0.04 ? 3 : a >= 0.015 ? 2 : 1, label: a >= 0.015 ? 'Adds risk' : 'Adds a little risk' }; }
    for (const b of BANDS) if (r >= b.min) return { pips: b.pips, label: b.label };
    return { pips: 0, label: 'None' };
  }
  // Starting p(doom): one of the sourced estimates, or 'c<basis points>' for a player's own value (c250 = 2.5%).
  function baseline(D, id) { const bs = D.risk.baselines;
    if (/^c\d{1,4}$/.test(id || '')) { const p = parseInt(id.slice(1), 10) / 10000; if (p > 0 && p < 0.95) return { id, p, short: fmtP(p), label: 'Your own estimate', who: 'A starting p(doom) you set yourself.' }; }
    return bs.find(b => b.id === id) || bs.find(b => b.id === D.risk.default_baseline) || bs[0]; }
  // "4.95%", "0.376%", "19.8%"
  function fmtP(p) { const v = p * 100; if (v <= 0) return '0%'; return (v >= 10 ? String(Number(v.toFixed(1))) : Number(v.toPrecision(3)).toString()) + '%'; }
  const pct = r => { const v = Math.abs(r) * 100; return (v < 1 ? Number(v.toPrecision(1)) : Math.round(v)) + '%'; };
  // Best risk cut we can find for a budget (in days): knapsack on each rule's own cut, then swaps that respect overlaps.
  function best(pool, budget, cost, D, ov) {
    const r1 = p => one(p, D, 'central', ov), base = pool.filter(p => cost(p) <= 1e-9 && r1(p) >= 0).map(p => p.id), rest = pool.filter(p => cost(p) > 1e-9 && r1(p) > 0);
    const U = 0.05, B = Math.floor(budget / U + 1e-9), w = p => Math.ceil(cost(p) / U - 1e-9), dp = new Float64Array(B + 1), keep = rest.map(() => new Uint8Array(B + 1));
    rest.forEach((p, i) => { const v = -Math.log(1 - r1(p)); for (let b = B; b >= w(p); b--) if (dp[b - w(p)] + v > dp[b]) { dp[b] = dp[b - w(p)] + v; keep[i][b] = 1; } });
    let cur = base.slice(), b = B; for (let i = rest.length - 1; i >= 0; i--) if (keep[i][b]) { cur.push(rest[i].id); b -= w(rest[i]); }
    const byId = id => pool.find(p => p.id === id), spent = ids => ids.reduce((a, id) => a + cost(byId(id)), 0);
    for (let more = true; more;) { more = false; const v0 = cut(cur, D, 'central', ov);
      for (const p of rest) { if (cur.indexOf(p.id) >= 0) continue; for (const out of [null].concat(cur)) { const t = cur.filter(x => x !== out).concat(p.id); if (spent(t) <= budget + 1e-9 && cut(t, D, 'central', ov) > v0 + 1e-9) { cur = t; more = true; break; } } if (more) break; } }
    return { cut: cut(cur, D, 'central', ov), ids: cur };
  }
  root.MENU_RISK = { cut, one, expand, band, baseline, fmtP, pct, best };
})(typeof window !== 'undefined' ? window : globalThis);
