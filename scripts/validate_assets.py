"""Check lab file coverage, prototype links and infrastructure configuration."""
from pathlib import Path
import json
import subprocess
import yaml

ROOT=Path(__file__).resolve().parents[1]
def main():
    experiments=json.loads((ROOT/'experiments.json').read_text())
    assert [x['number'] for x in experiments]==list(range(1,26))
    for exp in experiments:
        path=ROOT/exp['path'];assert path.is_dir()
        assert (path/'README.md').is_file(), f'Missing instructions: {path}'
    for n in [2,3]:
        directory=ROOT/experiments[n-1]['path']
        screens=json.loads((directory/'screens.json').read_text())
        ids={s['id'] for s in screens};assert len(ids)==len(screens)
        for screen in screens:
            assert (directory/'screens'/f'{screen["id"]}.svg').is_file()
            for item in screen['items']:
                if item['type']=='button':assert item['to'] in ids
                if item['type']!='text':
                    assert item['x']+item['w']<=390 and item['y']+item['h']<=844
        starts=['home'] if n==2 else ['a-home','b-home']
        for start in starts:
            reachable={start}
            for _ in screens:
                reachable.update(item['to'] for s in screens if s['id'] in reachable for item in s['items'] if item['type']=='button')
            expected={x for x in ids if x.startswith(start[:2])} if n==3 else ids
            assert reachable==expected
    docs=[]
    for path in ROOT.rglob('*.yaml'):
        docs.extend(x for x in yaml.safe_load_all(path.read_text()) if x)
    for obj in docs:
        if obj.get('kind')=='Deployment':
            spec=obj['spec'];labels=spec['template']['metadata']['labels']
            assert all(labels[k]==v for k,v in spec['selector']['matchLabels'].items())
            for c in spec['template']['spec']['containers']:
                assert 'yourusername' not in c['image']
                assert c.get('ports') and c.get('resources')
    for directory in [ROOT/'experiments/12-flask-kubernetes',ROOT/'experiments/18-multi-container-kubernetes']:
        items=[obj for path in directory.glob('*.yaml') for obj in yaml.safe_load_all(path.read_text()) if obj]
        deployments=[x for x in items if x.get('kind')=='Deployment']
        for s in (x for x in items if x.get('kind')=='Service'):
            matches=[d for d in deployments if all(d['spec']['template']['metadata']['labels'].get(k)==v for k,v in s['spec']['selector'].items())]
            assert matches, s['metadata']['name']
            available={p['containerPort'] for d in matches for c in d['spec']['template']['spec']['containers'] for p in c['ports']}
            assert all(p['targetPort'] in available for p in s['spec']['ports'])
    for path in (ROOT/'.github/workflows').glob('*.yml'):
        workflow=yaml.safe_load(path.read_text())
        assert ('on' in workflow or True in workflow) and workflow.get('jobs')
        for job in workflow['jobs'].values():
            assert job.get('runs-on')
    for path in ROOT.rglob('*.sh'):
        subprocess.run(['bash','-n',str(path)],check=True)
    print('25 experiments checked; prototype links, Kubernetes selectors and ports, YAML and shell syntax passed.')
    print('Configuration checks do not assert that external services or containers have run.')

if __name__=='__main__':main()
