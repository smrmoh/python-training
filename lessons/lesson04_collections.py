
desktop_names = ["vdi-01", "vdi-02", "vdi-03"]
print(desktop_names[1])

desktop_names.append("vdi-04")
print(len(desktop_names))

desktop = {
    "name": "vdi-04",
    "power_state": "running",
    "is_agent_reachable": True,
    "maintenance_mode": False,
    "cpu_usage": 65,
    "response_time": 1.5,
    "logged_on_user": None
}

print(f"Second Desktop: {desktop['name']}")
print(f"CPU Usage: {desktop['cpu_usage']}%")
print(f"Response time: {desktop['response_time']}s")

desktop["cpu_usage"] = 85

if desktop["cpu_usage"] >= 80:
    print("performance needs investigation")
else:
    print("Performance check passed")



      