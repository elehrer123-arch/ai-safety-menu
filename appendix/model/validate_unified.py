"""Behavioral checks for the national lead estimand, not snapshots of desired prices."""
import json
from pathlib import Path
import numpy as np
from country_dynamics import propagate,endpoint_summary,common_diffusion
from production_model import integrate_resource_effect

checks=[]
def check(name,condition,detail=''):
    if not bool(condition):raise AssertionError(name+':'+str(detail))
    checks.append(dict(check=name,passed=True,detail=detail))

def run():
    n=64;ts=np.linspace(0,3,157);z=np.zeros((n,len(ts)));gt=np.full(n,3.)
    d=common_diffusion(n);d={k:np.zeros(n) if 'spillover' in k else np.full(n,60.) for k in d}
    out=propagate(ts,z,z,np.zeros(n),gt,d)
    check('Zero intervention has exactly zero effect',np.all(out['us']==0) and np.all(out['china']==0))
    u=-.5*gt[:,None]*ts[None,:]
    out=propagate(ts,u,z,np.zeros(n),gt,d);net=endpoint_summary(out,gt,ts)['mean_days']
    check('Half-speed US with no diffusion closes exactly half a year',abs(net-365.25/2)<1e-9,net)
    out=propagate(ts,z,u,np.zeros(n),gt,d);net=endpoint_summary(out,gt,ts)['mean_days']
    check('Symmetric ruler: half-speed China widens by half a year',abs(net+365.25/2)<1e-9,net)
    out=propagate(ts,u,u,np.zeros(n),gt,d)
    check('Equal direct country shocks cancel without spillovers',abs(endpoint_summary(out,gt,ts)['mean_days'])<1e-9)
    out=propagate(ts,z,z,np.full(n,30.),gt,d)
    check('Public delay does nothing with zero reliance',abs(endpoint_summary(out,gt,ts)['mean_days'])<1e-12)
    d['teacher_spillover']=np.full(n,.1)
    out=propagate(ts,z,z,np.full(n,30.),gt,d);net=endpoint_summary(out,gt,ts)['mean_days']
    check('Public-only delay with teacher reliance widens US lead',net<0,net)
    check('Public-only delay never mechanically delays internal US frontier',np.all(out['us']==0))
    d['teacher_spillover']=np.full(n,.2)
    out2=propagate(ts,z,z,np.full(n,30.),gt,d);net2=endpoint_summary(out2,gt,ts)['mean_days']
    check('Teacher effect linear in marginal reliance with no feedback',abs(net2-2*net)<1e-10)
    d['teacher_spillover']=np.full(n,.1)
    out=propagate(ts,u,z,np.zeros(n),gt,d)
    check('China dependency reduces unilateral-US restriction gap closure',0<endpoint_summary(out,gt,ts)['mean_days']<365.25/2)
    s=dict(g_A=np.full(n,1.2),lambda_R=np.full(n,.7),beta=np.full(n,.65),eta=np.zeros(n))
    rr=np.ones_like(z)
    a=integrate_resource_effect(s,ts,rr)
    check('Unchanged research inputs preserve the baseline',np.max(abs(a))<1e-12)
    rr[:]=.8;a=integrate_resource_effect(s,ts,rr)
    check('Research resource reduction causes negative algorithmic effect',np.all(a[:,1:]<0))
    # Analytical steady state for eta=0: a*=lambda/beta*ln(resource ratio).
    equilibrium=.7/.65*np.log(.8)
    check('Diminishing returns prevents constant resource loss from unbounded linear accumulation',np.all(a[:,-1]>equilibrium) and np.all(a[:,-1]<0),equilibrium)
    Path(__file__).with_name('unified-validation.json').write_text(json.dumps(dict(checks=checks),indent=2)+'\n')
    print(f'{len(checks)} behavioral checks passed')
if __name__=='__main__':run()
