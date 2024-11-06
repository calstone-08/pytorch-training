import torch
from torch.nn import Module

class ExerciseModel(Module):

    def __init__(self, mytensor, elem_add: int, elem_multiply: int):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply
    
    def forward(self,x):
        prob2 = x + self.mytensor
        prob3 = prob2 + self.elem_add
        prob4 =  prob3 * self.elem_multiply
        return prob2, prob3, prob4

if __name__=="__main__":
    mymodel = ExerciseModel(torch.ones((3, 3)), 4, 6)

    p2out, p3out, p4out = mymodel(torch.full((3, 3), 2))

    print("===== problem 2 =====")
    print(repr(p2out))
    print("===== problem 3 =====")
    print(repr(p3out))
    print("===== problem 4 =====")
    print(repr(p4out))