import channels, interfaces

# In production, the credentials will be obtained using load_dotenv
creds = interfaces.Credentials("192.168.1.1:1111", "username", "password")
rest_interface = (interfaces.RestInterface(creds))


def get_channel():
    channel_id: str = "123456"
    channel = channels.Channel(rest_interface, channel_id)
    r = channel.get()
    print(r.text)


def main():
    get_channel()


if __name__ == "__main__":
    main()
