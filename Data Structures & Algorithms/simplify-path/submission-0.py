class Solution:
    def simplifyPath(self, path: str) -> str:
        res = path.split('/')
        stock = []
        for top in res:
            
            if top == '' or top =='.':
                continue
            elif top == '..':
                if stock:
                    stock.pop()
            else:
                stock.append(top)
        return '/' + '/'.join(stock)