# chat gpt
#  tahgigh uml
class note:
    def __init__(self,memo:str,tag:str = ""):
        self.memo = memo
        self.tag = tag


    def search(self,exmemo) -> bool:
        if exmemo in self.memo or self.tag:
            return True
        return False

   

    # def __str__(self) -> str:
    #     return self.memo


