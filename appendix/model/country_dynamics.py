"""Two-country lagged spillovers on a shared log-effective-compute ruler.

This is a structural response model with disclosed analyst priors, not a fitted
causal estimate. Direct policy effects are inputs from the production, regulatory,
and access/security modules. No old menu prices enter the computation.
"""
from __future__ import annotations
import hashlib
import numpy as np

def triangular(name, low, mode, high, n, seed=20260925):
    """Name-stable common random numbers, so a shared parameter is shared."""
    if low == high:
        return np.full(n, float(low))
    tag=int.from_bytes(hashlib.sha256(name.encode()).digest()[:8], 'little')
    rng=np.random.default_rng(np.random.SeedSequence([int(seed),tag]))
    return rng.triangular(low, mode, high, n)

def common_diffusion(n,seed=20260925):
    return {
        'research_spillover':triangular('research_spillover',0,.15,.40,n,seed),
        'teacher_spillover':triangular('teacher_spillover',0,.10,.35,n,seed),
        'absorption_days':triangular('absorption_days',21,60,150,n,seed),
        'knowledge_lag_days':triangular('knowledge_lag_days',14,45,120,n,seed),
        'reverse_spillover':triangular('reverse_spillover',0,.025,.10,n,seed),
    }

def lag_at(array, t, lag_years, times):
    """Per-draw linear interpolation, with zero pre-implementation shock."""
    at=t-lag_years
    dt=times[1]-times[0]
    ix=np.floor(np.maximum(at,0)/dt).astype(int)
    ix=np.minimum(ix,len(times)-2)
    frac=np.clip((at-times[ix])/dt,0,1)
    r=np.arange(array.shape[0])
    return np.where(at>0,array[r,ix]*(1-frac)+array[r,ix+1]*frac,0.)

def propagate(times, us_direct, china_direct, release_delay_days, g_total,
              diffusion=None, seed=20260925):
    """Return total shocks and channel contributions, all N x time arrays.

    A public release delay changes teacher availability; it never directly sets
    the originating lab's internal capability back. Delay ramps from zero and
    is not multiplied by the number of model releases. China-to-US spillovers
    provide an explicit small reverse channel. g_total is the SAME per-draw
    ruler used by the direct production modules.
    """
    n,T=us_direct.shape
    assert china_direct.shape==(n,T) and len(times)==T
    d=common_diffusion(n,seed) if diffusion is None else diffusion
    D=np.asarray(release_delay_days)
    if D.ndim==1:
        D=np.minimum(D[:,None],365.25*np.asarray(times)[None,:])
    assert D.shape==(n,T)
    u=us_direct.copy(); c=china_direct.copy()
    yc=np.zeros(n); yu=np.zeros(n)
    induced_c=np.zeros((n,T)); induced_u=np.zeros((n,T))
    lag=d['knowledge_lag_days']/365.25
    tau=d['absorption_days']/365.25
    teacher=d['teacher_spillover']; research=d['research_spillover']
    reverse=d['reverse_spillover']
    for j in range(1,T):
        t=times[j]; dt=t-times[j-1]
        delayed_u=lag_at(u,t,lag,times)
        delayed_c=lag_at(c,t,lag,times)
        # Older teachers remain usable; D is the marginal quality/time shift.
        delayed_release=lag_at(D,t,lag,times)
        target_c=(research+teacher)*delayed_u-teacher*g_total*delayed_release/365.25
        target_u=reverse*delayed_c
        w=-np.expm1(-dt/tau)
        yc += w*(target_c-yc)
        yu += w*(target_u-yu)
        induced_c[:,j]=yc; induced_u[:,j]=yu
        u[:,j]=us_direct[:,j]+yu; c[:,j]=china_direct[:,j]+yc
    return {'us':u,'china':c,'china_spillover':induced_c,'us_reverse_spillover':induced_u,'diffusion':d}

def endpoint_summary(result,g_total,times,horizon=1.):
    j=int(np.argmin(abs(np.asarray(times)-horizon)))
    assert abs(times[j]-horizon)<1e-8
    us=-result['us'][:,j]/g_total*365.25
    cn=-result['china'][:,j]/g_total*365.25
    net=us-cn
    return {'mean_days':float(net.mean()),'median_days':float(np.median(net)),
            'p05_days':float(np.quantile(net,.05)),'p95_days':float(np.quantile(net,.95)),
            'probability_closes':float(np.mean(net>0)),
            'us_delay_days':float(us.mean()),'china_delay_days':float(cn.mean()),
            'mc_standard_error_days':float(net.std(ddof=1)/np.sqrt(len(net))),
            'draws':net}
