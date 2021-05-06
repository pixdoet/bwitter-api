#aternos api for testing only
#first new module in some time


from aternosapi import AternosAPI

headers_cookie = "ATERNOS_SEC_b3roddvcalm00000=d390tpdhhqd00000; _gid=GA1.2.1712722002.1615869219; ATERNOS_SESSION=q0Z7j9W4Bgb5gctyaTf54bkTrDgGQ14XlvwoUx3l8isldKOmTB2fMS7BZUKZn3BOucuvGVLh5caIUotDieIE6DthQ8xITAKPIuJd; ATERNOS_SERVER=Z7ABLy0xIe3oNJ5C; _gat=1; ATERNOS_LANGUAGE=en; cto_bidid=ZmcnOV9TbDh5VnlzNWVQUmV4UTltTm45ZlNUc3gxb2JpTllYY29wN1JiaEdtMXBpOUYlMkYyT1BMYyUyQjZWMzkwT0ppNm1uOTRIWmNXM2dxJTJCUlg2b2J6ejJvbFZjWkdJcnl4anFnRVBFcU13YmFVanQ5SSUzRA; cto_bundle=tF-s319vN1pjVmtaZiUyQlY4V3VJSDNhekpWdlRvSWpMZW1RSTh2ZUQwcWNNbE93MVNBVU5jcmp6NUFKR0lGJTJCamswUEM3WUlMJTJCSG1lQ1hiNW92JTJCOXJwaG9VJTJGVU5NMTR3JTJGR2MzSjRlODgydXd4QiUyRmFISElDSWtFODltQnlOVWhWSjN6azUwWXdtZTlncVY3bnhHRnZaRFRwSWJUckROM1RPazViYTk4ZFUlMkZNQyUyQjhxbTAlM0Q; cto_test_cookie=; __cfduid=d832ef3cb1446a4ef35d4b4988d400bcc1614868834; __gads=ID=682cfbc1fe68af60-2292d6753cc600ac:T=1614869038:RT=1616633056:S=ALNI_MZiUTOPX735aqneKctkhKx6sE3cjQ; _ga=GA1.2.1155401417.1614868859; cto_bundle=6lnoo19vN1pjVmtaZiUyQlY4V3VJSDNhekpWdlc1WmJubkYxRjYyNElJaDBjYW9WWmZTaUVHd1JUeU8yREJkdnNiMzYxVW1sdUY5bUlUSDJ0NVYzZlpYJTJCN0dEV2tZMTN5ZTJSNDNjenB0V1pUWXpOM0xmbHdMRGslMkZueTE4WUdwTWk4bzJVODZPa3ZNQWJBaVEwV0o4M3N6QmpNTWphYmg5amUxQ1NjMjZSeEZ0eGFRSTAlM0Q; ATERNOS_STYLE=default; cnx_userId=9a6d794b6eef4961baf4069f970e6eeb; id5id.1st_364_nb=1"
TOKEN = "b3roddvcalm00000=d390tpdhhqd00000"
server = AternosAPI(headers_cookie, TOKEN)

def cmd(cmd):
	if cmd == "start":
		return(server.StartServer())
	if cmd == "stop":
		return(server.StopServer())
	if cmd == "status":
		return(server.GetStatus())
	if cmd == "info":
		return(server.GetServerInfo())

# backup if api fails(which it most probably will)
# https://aternos.org/panel/ajax/start.php?SEC=xxlgqemjmfb00000%3A7dov2endun000000&TOKEN=1PlqDwFE1EMrfs7crKAK
# https://aternos.org/panel/ajax/stop.php?SEC=xxlgqemjmfb00000%3A7dov2endun000000&TOKEN=1PlqDwFE1EMrfs7crKAK
