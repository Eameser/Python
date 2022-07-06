import os
import pickle
import datetime
import time
import pathlib

class Commit:
    def __init__(self, comment, game, l_c):
        self.move = game[0]
        self.player = game[1]
        self.enemies = game[2:]
        self.comment = comment
        self.date = datetime.datetime.now()
        self.l_c = l_c
    def show_comment(self):
        return self.comment
    def show_date(self):
        return self.date
    def get_game(self):
        return [self.move, self.player] + self.enemies

class Branch:

    def __init__(self, name):
        self.name = name
        self.commits = []
        f = open(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle", 'ab+')
        f.close()
        if os.path.getsize(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle") > 0:
            fl = open(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle", 'rb')
            self.commits = pickle.load(fl)
            fl.close()
        print("New branch {} created.".format(name))

    def add_commit(self, game):
        commit = input("Commit: ")
        if len(self.commits) == 0:
            self.commits.append(Commit(comment=commit, game=game, l_c="first"))
        else:
            xx = self.commits[-1]
            ll = []
            ll = self.commits[0].get_game()
            for x in range(1, len(self.commits)):
                ll[0] = ll[0] + self.commits[x].move
                ll[1] = self.commits[x].player
                for p in range(0, len(self.commits[x].enemies)):
                    ll[p+2] = self.commits[x].enemies[p]
            #ii = len(ll[0])
            xxx = []
            xxx.append(game[0][len(ll[0]):])
            for j in range(1, len(game)):
                xxx.append(game[j])
            self.commits.append(Commit(comment=commit, game=xxx, l_c=xx))
        f = open(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle", 'wb')
        pickle.dump(self.commits, f)
        f.close()
        fl = open(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle", 'rb')
        self.commits = pickle.load(fl)
        fl.close()
        print("Commit added.")

    def show_branch(self):
        os.system("cls")
        print(self.name)
        for i in range(0, len(self.commits)):
            print("{0} \t| {1} \t| {2} \t| {3} \t| {4}".format(i+1, self.commits[i].show_comment(), self.commits[i].show_date(), self.commits[i].move, self.commits[i].l_c))
        print("_" * 25)

    def remove_commit(self):
        self.show_branch()
        idx = int(input("Choose commit to remove: "))
        #self.commits.pop(idx-1)
        self.commits = self.commits[:idx-1]
        f = open(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle", 'wb')
        pickle.dump(self.commits, f)
        f.close()
        fl = open(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle", 'rb')
        self.commits = pickle.load(fl)
        fl.close()
        print("Commit removed.")

    def get_name(self):
        return self.name

    def load_commit(self):
        self.show_branch()
        idx = int(input("Choose commit to load: "))
        ll = []
        ll = self.commits[0].get_game()
        for x in range(1, idx):
            ll[0] = ll[0] + self.commits[x].move
            ll[1] = self.commits[x].player
            for p in range(0, len(self.commits[x].enemies)):
                ll[p+2] = self.commits[x].enemies[p]

        #self.commits = self.commits[:idx]
        f = open(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle", 'wb')
        pickle.dump(self.commits, f)
        f.close()
        fl = open(str(pathlib.Path().resolve())+"/git/"+self.name+".pickle", 'rb')
        self.commits = pickle.load(fl)
        fl.close()
        return ll


class Git:

    def __init__(self):
        self.branches = []
        self.branches.append(Branch("master"))
        for file in os.listdir(str(pathlib.Path().resolve())+"/git/"):
            if file != "master.pickle":
                self.branches.append(Branch(file.replace(".pickle", "")))
        self.curr_branch = self.branches[0]

    def create_branch(self):
        name = input("New branch: ")
        self.branches.append(Branch(name))

    def show_branches(self):
        os.system("cls")
        for i in range(0, len(self.branches)):
            if self.branches[i] == self.curr_branch:
                print("{0}. {1} (you are here)".format(i+1, self.branches[i].get_name()))
            else:
                print("{0}. {1}".format(i+1, self.branches[i].get_name()))
        print("_" * 25)

    def remove_branch(self):
        self.show_branches()
        idx = int(input("Choose branch to remove: "))
        r_name = self.branches[idx-1].get_name()
        if self.branches[idx-1] == self.curr_branch:
            print("You can't remove current branch! Change the branch and then remove.")
        else:
            os.remove(str(pathlib.Path().resolve())+"/git/"+self.branches[idx-1].name + ".pickle")
            self.branches.pop(idx-1)
            print("Branch {0} removed.".format(r_name))

    def move_branch(self):
        self.show_branches()
        i = int(input("Choose the branch: "))
        self.curr_branch = self.branches[i-1]

    def get_curr(self):
        return self.curr_branch

    def git_menu(self):
        print("\nGIT MENU:")
        print("\n1 - Show existing branches")
        print("2 - Show all commits on current branch")
        print("3 - Change current branch")
        print("4 - Create new branch")
        print("5 - Delete branch")
        print("6 - Add new commit")
        print("7 - Delete commit")
        print("8 - Load commit")
        print("9 - Apply&Continue")
        print("0 - Exit\n")

    def git_command(self, i):
        return {1: self.show_branches,
                2: self.curr_branch.show_branch,
                3: self.move_branch,
                4: self.create_branch,
                5: self.remove_branch,
                6: self.curr_branch.add_commit,
                7: self.curr_branch.remove_commit,
                8: self.curr_branch.load_commit,
                0: exit}.get(i, "Error!")
