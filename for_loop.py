#OOP
class RemoteControl:


    def change_channel(self,channel):
        return f"Change channel to {channel}"

    if __name__ ==  "__main__":
        remote = RemoteControl()
        print(remote.change_channel("Tv 4"))

        print("------------")


