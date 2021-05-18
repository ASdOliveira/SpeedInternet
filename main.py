import speedtest


st = speedtest.Speedtest()
closest_servers = st.get_closest_servers()
for key, value in closest_servers[1].items():
    print(key, ' : ', value)

print(st.download())

print(st.upload())

print(st.results.ping)

