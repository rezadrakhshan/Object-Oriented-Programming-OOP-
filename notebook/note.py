
class note:
    def __init__(self,memo:str,tag:str = ""):
        self.memo = memo
        self.tag = tag


    def search(self,exmemo) -> bool:
        if exmemo in self.memo or self.tag:
            return True
        return False

   

  


