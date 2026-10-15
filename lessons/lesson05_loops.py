# VirtualOps Assist - Check multiple desktop agents

desktops = [
    {
        "name": "vdi-01",
        "is_agent_reachable": True,
        "cpu_usage": 25
    },
    {
        "name": "vdi-02",
        "is_agent_reachable": False,
        "cpu_usage": 40
    },
    {
        "name": "vdi-03",
        "is_agent_reachable": True,
        "cpu_usage": 90
    }
]

for desktop in desktops:
    print(f"checking Desktop: {desktop['name']}")
    if desktop['is_agent_reachable'] == False:
        print('Agent communication needs investigation')
    elif desktop['cpu_usage'] >= 80:
        print('Agent is reachable, but CPU usage is high')
    else:
        print('Basic health checks passed')

print('All desktop checks finished')