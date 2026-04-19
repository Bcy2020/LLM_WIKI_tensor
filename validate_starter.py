from pathlib import Path

required = [
    '.claude/settings.json',
    '.mcp.json',
    'raw/.manifest.json',
    'wiki/wiki-index.md',
    'wiki/log.md',
    'wiki/hot.md',
    'wiki/overview.md',
    'wiki/sources/_index.md',
    'wiki/concepts/_index.md',
    'wiki/entities/_index.md',
    'wiki/questions/_index.md',
    'wiki/learning/_index.md',
    'wiki/maintenance/_index.md',
    'wiki/maintenance/trash/_index.md',
    '.claude/skills/wiki-assess-mastery/SKILL.md',
    '.claude/skills/wiki-teach/SKILL.md',
    '.claude/skills/wiki-set-mastery/SKILL.md',
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    raise SystemExit('Missing required files:\n' + '\n'.join(missing))
print('Starter structure looks valid.')
