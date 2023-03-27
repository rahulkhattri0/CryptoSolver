"""
complexity of this algo O(10^length of unique string)
for example: In the case of Send,More and Money
The Unique string will be SENDMORY,its length is 8,so the complexity is O(10^8)
"""
class cryp:
    def __init__(self) -> None:
        self.flag = False
        self.resList = []
    def makenum(self,map:dict,str:str):
        s = ""
        for i in str:
            s = s + map[i].__str__()
        return int(s)
    def checkForInitialZeroes(self,words:list,map:dict):
        for word in words:
            if(map[word[0]]==0):
                return True
        return False
    def helper(self,map:dict,unique:str,used:list,words:list,result:str,target:int)->None:
        # base case
        if(target==len(unique)):
            if(map[result[0]]==0 or self.checkForInitialZeroes(words,map)):
                return
            sum=0
            for i in words:
                sum = sum + self.makenum(map,i)
            res = self.makenum(map,result)
            if(sum==res):
                self.flag = True
                ans=[]
                for i in map:
                    ans.append(i + ": " +map[i].__str__())
                self.resList.append(ans)
            return
        ch = unique[target]
        for i in range(0,10):
            if(used[i]==False):
                map[ch] = i
                used[i] = True
                self.helper(map,unique,used,words,result,target+1)
                used[i] = False
    def isSolvable(self,words:list,result:str)->bool:
        map = {}
        unique = ""
        for i in words:
            for j in i:
                if((j in map)==False):
                    map[j] = -1
                    unique = unique+j
        for i in result:
            if((i in map)==False):
                map[i] = -1
                unique =unique + i
        print(unique)
        if(len(unique)>10):
            return False
        used=[]
        for i in range(0,10):
            used.append(False)
        self.helper(map,unique,used,words,result,target=0)
        print(len(map))
        return self.flag
if __name__=='__main__':
    words = ["ABCD","EF"]
    res = "ABCG"
    ob = cryp()
    print(ob.isSolvable(words,res))
    print(ob.resList)
    print(len(ob.resList))
        
                        