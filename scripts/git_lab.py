"""Execute real Git operations in disposable local repositories.

The fork remote and second worktree are local stand-ins. No GitHub fork, PR,
human reviewer, or collaborator is fabricated by this script.
"""
from pathlib import Path
import json
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]

def main():
    work=Path(tempfile.mkdtemp(prefix='csa10-git-lab-'))
    log=[]
    def git(*args,cwd=work,allow_failure=False):
        result=subprocess.run(['git',*args],cwd=cwd,text=True,capture_output=True)
        log.append('$ git '+' '.join(args)+'\n'+result.stdout+result.stderr)
        if result.returncode and not allow_failure:
            raise RuntimeError(log[-1])
        return result
    def identity(path):
        git('config','user.name','Software Engineering Lab',cwd=path)
        git('config','user.email','lab@example.invalid',cwd=path)
    def commit(path,message):
        git('add','.',cwd=path);git('commit','-m',message,cwd=path)

    git('init','--bare','--initial-branch=main','origin.git')
    git('clone',str(work/'origin.git'),'primary')
    primary=work/'primary';identity(primary)
    (primary/'README.md').write_text('# Local version control exercise\nmode=base\n')
    commit(primary,'Initialize repository and project description')
    git('push','-u','origin','main',cwd=primary)

    git('clone',str(work/'origin.git'),'second-workstation')
    second=work/'second-workstation';identity(second)
    (second/'README.md').write_text('# Local version control exercise\nmode=base\nUpdate from second local checkout.\n')
    commit(second,'Add update in second local checkout')
    git('push','origin','main',cwd=second)
    git('pull','--ff-only','origin','main',cwd=primary)
    assert 'second local checkout' in (primary/'README.md').read_text()

    git('checkout','-b','feature-branch',cwd=primary)
    (primary/'README.md').write_text('# Local version control exercise\nmode=feature\n')
    commit(primary,'Change mode on feature branch')
    git('push','-u','origin','feature-branch',cwd=primary)
    git('checkout','main',cwd=primary)
    (primary/'README.md').write_text('# Local version control exercise\nmode=main\n')
    commit(primary,'Change the same line on main')
    conflict=git('merge','feature-branch',cwd=primary,allow_failure=True)
    assert conflict.returncode!=0
    conflicted=(primary/'README.md').read_text()
    assert '<<<<<<<' in conflicted and '=======' in conflicted and '>>>>>>>' in conflicted
    (primary/'README.md').write_text('# Local version control exercise\nmode=main-and-feature\n')
    commit(primary,'Resolve merge conflict preserving both intentions')
    assert not git('ls-files','-u',cwd=primary).stdout.strip()
    git('push','origin','main',cwd=primary)

    for branch,filename,contents in [
        ('module1','catalogue.py','def search_books(titles, query):\n    return [t for t in titles if query.casefold() in t.casefold()]\n'),
        ('module2','loans.py','def is_overdue(due_date, today):\n    return today > due_date\n'),
        ('feature-login','login.py',(ROOT/'experiments/24-feature-login/login.py').read_text()),
    ]:
        git('checkout','-b',branch,cwd=primary)
        (primary/filename).write_text(contents)
        commit(primary,'Implement '+branch)
        git('push','-u','origin',branch,cwd=primary)
        git('checkout','main',cwd=primary)
        git('merge','--no-ff',branch,'-m','Integrate '+branch+' after local inspection',cwd=primary)
    git('push','origin','main',cwd=primary)

    # Separate local bare repository demonstrates the remote structure of a fork.
    git('clone','--bare',str(work/'origin.git'),'fork.git')
    git('clone',str(work/'fork.git'),'fork-worktree')
    fork=work/'fork-worktree';identity(fork)
    git('remote','add','upstream',str(work/'origin.git'),cwd=fork)
    git('checkout','-b','feature-new',cwd=fork)
    shutil.copyfile(ROOT/'experiments/25-fork-feature/feature.py',fork/'feature.py')
    commit(fork,'Add completion percentage feature')
    git('push','-u','origin','feature-new',cwd=fork)
    git('remote','add','contributor',str(work/'fork.git'),cwd=primary)
    git('fetch','contributor','feature-new',cwd=primary)
    git('diff','main...contributor/feature-new',cwd=primary)
    git('merge','--no-ff','contributor/feature-new','-m','Integrate local fork feature',cwd=primary)
    git('push','origin','main',cwd=primary)
    git('log','--graph','--all','--oneline','--decorate',cwd=primary)
    assert not git('status','--porcelain',cwd=primary).stdout.strip()
    output=ROOT/'evidence/runtime';output.mkdir(parents=True,exist_ok=True)
    (output/'git-workflow.log').write_text('\n'.join(log))
    (output/'git-summary.json').write_text(json.dumps({
        'executed_at':datetime.now(timezone.utc).isoformat(),
        'environment':'disposable local Git repositories',
        'verified':['init','clone','modify','commit','push','pull','module branches','feature-login','conflict detection','conflict resolution','non-fast-forward merges','local fork feature'],
        'not_performed':['GitHub fork','GitHub pull request','human peer review'],
        'conflict_observed':True,'working_tree_clean':True,
        'head':git('rev-parse','HEAD',cwd=primary).stdout.strip(),
        'workspace':str(work)},indent=2)+'\n')
    print('Git exercises passed: clone, commit, push, pull, branches, real conflict resolution, and local fork integration.')
    print('Evidence: evidence/runtime/git-workflow.log')
    print('These are local operations; GitHub PR and human review are separate requirements.')
    return work

if __name__=='__main__':
    main()
