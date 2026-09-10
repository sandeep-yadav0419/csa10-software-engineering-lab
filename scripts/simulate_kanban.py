"""Produce an explicitly local Kanban workflow simulation."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
def simulate(board):
    board=json.loads(json.dumps(board))
    history=[]
    for task in board['tasks']:
        for status in ['In Progress','Done']:
            history.append({'task':task['id'],'from':task['status'],'to':status})
            task['status']=status
    return {'kind':'local simulation, not Jira or Trello execution','board':board,'transitions':history}

if __name__=='__main__':
    result=simulate(json.loads((ROOT/'experiments/01-kanban-board/board.json').read_text()))
    output=ROOT/'evidence/runtime';output.mkdir(parents=True,exist_ok=True)
    (output/'kanban-simulation.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Three tasks moved through To Do, In Progress and Done in a local simulation.')
