from lib import itchat
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


class ScheduleMsgSender(object):

    def __init__(self, userNick='', context=''):
        self.userNick = userNick
        self.context = context
        #itchat.auto_login(hotReload=True, loginCallback=self.loginCallback, exitCallback=self.exitCallback)
        friends = itchat.get_friends()
        for f in friends:
            if f.NickName == self.userNick:
                print(f)
                self.user = f.UserName
        self.schedulerForSender()

    def sendMsg(self, user, context):
        if user:
            sendtime = datetime.now().strftime('%m-%d-%Y %H:%M:%S,%A')
            msg = context + "  Sending in " + sendtime
            print("send msg to %s, name %s", user, self.userNick)
            itchat.send_msg(msg=msg, toUserName=user)

    def loginCallback(self):
        print("Successfully logged in.")

    def exitCallback(self):
        print("Successfully logged out.")

    def sendMsgToUser(self):
        self.sendMsg(self.user, self.context)

    def schedulerForSender(self):
        if self.user:
            scheduler = BackgroundScheduler()
            scheduler.add_job(self.sendMsgToUser, 'interval', seconds=300)
            scheduler.start()


if __name__ == '__main__':
    context = "hi"
    ScheduleMsgSender(userNick='雾蒙蒙', context=context)
