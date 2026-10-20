# VirtualOps Assist - Skip desktops in maintenance

desktops = [
    {
        'name': 'vdi-01',
        'maintenance_mode': False,
        'is_agent_reachable': True
    },
    {
        'name': 'vdi-02',
        'maintenance_mode': True,
        'is_agent_reachable': False
    },
    {
        'name': 'vdi-03',
        'maintenance_mode': False,
        'is_agent_reachable': False
    }
]

for desktop in desktops:
    if desktop['maintenance_mode']:
        print(f"Skipping maintenance desktop: {desktop['name']}")
        continue
    
    
    print(f"Checking Desktop: {desktop['name']}")
    if desktop['is_agent_reachable']:
        print("Agent is reachable")
    else:
        print("Agent communication needs investigation")

print("All desktop checks finished")