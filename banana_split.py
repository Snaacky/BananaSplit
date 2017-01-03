from steam import SteamClient
from steam.enums import EResult, EPersonaStateFlag, EPersonaState

client = SteamClient()


@client.on("logged_on")
def handle_after_logon():
    print("Logged on as: {0}".format(client.user.name))
    client.change_status(persona_state=EPersonaState.Online, player_name=client.user.name, persona_state_flags=EPersonaStateFlag.HasGoldenProfile)
    print("Press ^C to exit")


try:
    result = client.cli_login()

    if result != EResult.OK:
        print("Failed to login: {0}".format(repr(result)))
        raise SystemExit

    client.run_forever()
except KeyboardInterrupt:
    if client.connected:
        client.logout()
