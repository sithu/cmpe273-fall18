import os
import hashlib

class MarkleTree:
    def __init__(self, rootDir):
        self._rootDir = rootDir
        self._transactions = {}
        self._hashlist = {}
        self._roothash = ''
        self.__build__()

    def __build__(self):
        self.HashList(self._rootDir)
        self.build_merkle_tree()
        print("Merkle Tree for directory: %s" % self._rootDir)
        self.print_tree(self._roothash)
        print(30*'-')

    def build_merkle_tree(self):
        for node, hash in self._hashlist.items():
            items = self.scan_files(node)
            value = []
            value.append(node)
            list = {}
            for item in items:
                if node == self._rootDir:
                    list[self._hashlist[item]] = item
                else: 
                    list[self._hashlist[os.path.join(node, item)]] = os.path.join(node, item)
            value.append(list)
            self._transactions[hash] = value
        self._roothash = self._hashlist[self._rootDir]

    def md5_hash_file(self, data):
        m = hashlib.md5()
        fn = os.path.join(self._rootDir, data)
        if os.path.isfile(fn):
            with open(fn, 'rb') as f:
                for line in f:
                    m.update(line)
        else:
            m.update(data.encode('utf-8'))
        return m.hexdigest()

    def scan_files(self, directory):
        filelist = []
        if directory != self._rootDir:
            directory = os.path.join(self._rootDir, directory)
        if os.path.isdir(directory):
            files = os.listdir(directory)
            for f in files:
                filelist.append(f)
            filelist.sort()
        return filelist
    
    def HashList(self, rootdir):
        self.HashListChild(rootdir)
        files = self.scan_files(rootdir)
        if not files:
            self._hashlist[rootdir] = ''
            return
        s = ''
        for f in files:
            s = s + self._hashlist[f]
        self._hashlist[rootdir] = self.md5_hash_file(s)

    def HashListChild(self, rootdir):
        items = self.scan_files(rootdir)
        if not items:
            self._hashlist[rootdir] = ''
            return
        for item in items:
            itemname = os.path.join(rootdir, item)
            if os.path.isdir(itemname):
                self.HashListChild(item)
                subitems = self.scan_files(item)
                s = ''
                for subitem in subitems:
                    s = s + self._hashlist[os.path.join(item, subitem)]
                if rootdir == self._rootDir:
                    self._hashlist[item] = self.md5_hash_file(s)
                else:
                    self._hashlist[itemname] = self.md5_hash_file(s)
            else:
                if rootdir == self._rootDir:
                    self._hashlist[item] = self.md5_hash_file(item)
                else:
                    self._hashlist[itemname] = self.md5_hash_file(itemname)
 
    def print_tree(self, hash):
        value = self._transactions[hash]
        # TODO


def find_diff(merkle_tree_a, a_roothash, merkle_tree_b, b_roothash):
    if a_roothash == b_roothash:
        print("Top hash is equal for %s and %s" % (merkle_tree_a._rootDir, merkle_tree_b._rootDir))
    else:
        a_value = merkle_tree_a._transactions[a_roothash] 
        a_child = a_value[1]    # retrieve the child list for merkle tree a
        b_value = merkle_tree_b._transactions[b_roothash] 
        b_child = b_value[1]    # retrieve the child list for merkle tree b

        # TODO
                
if __name__ == "__main__":
    merkle_tree_a = MarkleTree('A')
    merkle_tree_b = MarkleTree('B')
    find_diff(merkle_tree_a, merkle_tree_a._roothash, merkle_tree_b, merkle_tree_b._roothash)


