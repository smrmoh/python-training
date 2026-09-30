vdi_name= "vdi-02"
cpu_usage = 72
response_time = 1.8
registered = True
maint_mode = False
logged_on_user = ""
projected_cpu_usage = cpu_usage + 10

print(f"VDI Name: {vdi_name} | Type: {type(vdi_name)}")
print(f"CPU Usage: {cpu_usage} | Type: {type(cpu_usage)}")
print(f"Response Time: {response_time} | Type: {type(response_time)}")
print(f"Registered: {registered} | Type: {type(registered)}")
print(f"Maintenance Mode: {maint_mode} | Type: {type(maint_mode)}")
print(f"Logged On user: {logged_on_user} | Type: {type(logged_on_user)}")
print(f"Projected CPU Usage: {projected_cpu_usage}")
