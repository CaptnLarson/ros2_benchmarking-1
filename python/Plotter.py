import subprocess

class Plotter:
    def compareTimes(self, tid, cmd, title):
        params = [ "title='{}'".format(title) ]
        params.append("input1='data/{}-{}-pub.dat'".format(tid, cmd))
        params.append("input2='data/{}-{}-rec.dat'".format(tid, cmd))
        params.append("output='graphs/{}-{}.png'".format(tid, cmd))
        self.call('compare-times.plt', params)

    def lostPackets(self, tid, cmd, title):
        params = [ "title='{}'".format(title) ]
        params.append("input='data/{}-{}-lost-packets.dat'".format(tid, cmd))
        params.append("output='graphs/{}-{}-lost-packets.png'".format(tid, cmd))
        self.call('lost-packets.plt', params)

    def lostPacketsEstablished(self, tid, title):
        params = [ "title='{}'".format(title) ]
        params.append("input='data/{}-lost-packets-established.dat'".format(tid))
        params.append("output='graphs/{}-lost-packets-established.png'".format(tid))
        self.call('lost-packets-established.plt', params)

    def publishedHistogram(self, tid, cmd, title):
        params = [ "title='{}'".format(title) ]
        params.append("input='data/{}-{}-pub.dat'".format(tid, cmd))
        params.append("output='graphs/{}-{}-pub.png'".format(tid, cmd))
        params.append("label='Packets published'")
        params.append("legend='Packets published by console'")
        self.call('histogram.plt', params)

    def receivedHistogram(self, tid, cmd, title):
        params = [ "title='{}'".format(title) ]
        params.append("input='data/{}-{}-rec.dat'".format(tid, cmd))
        params.append("output='graphs/{}-{}-rec.png'".format(tid, cmd))
        params.append("label='Packets received'")
        params.append("legend='Packets received by robot'")
        self.call('histogram.plt', params)

    def firstReceived(self, tid, cmd, title):
        params = [ "title='{}'".format(title) ]
        params.append("input='data/{}-{}-first-received.dat'".format(tid, cmd))
        params.append("output='graphs/{}-{}-first-received.png'".format(tid, cmd))
        self.call('first-received.plt', params)

    def call(self, script, params):
        command = 'gnuplot -e "{}" gnuplot/{}'.format("; ".join(params), script)
        fh = open('graphs/replot.sh', "a")
        fh.write(command + "\n")
        subprocess.call(command, shell = True)

