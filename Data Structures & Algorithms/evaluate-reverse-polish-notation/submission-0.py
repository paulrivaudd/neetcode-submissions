class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=('+','*','-','/')
        stack=[]
        for c in tokens:
            if c not in operators:
                stack.append(int(c))
            else:
                if c=='+':
                    b = stack.pop()   
                    a = stack.pop()  
                    res=a + b 
                    stack.append(res)
                if c=='-':
                    b = stack.pop()   
                    a = stack.pop() 
                    res=a-b
                    stack.append(res)
                if c=='*':
                    b = stack.pop()   
                    a = stack.pop()
                    res= a*b
                    stack.append(res)
                if c=='/':
                    b = stack.pop()   
                    a = stack.pop() 
                    res= int(a/b)
                    stack.append(res)
        return stack[0]
                

                
               
