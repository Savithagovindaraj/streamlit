import tkinter.tix as Tix
import streamlit as st

class View(object):
    def __init__(self, root):
        self.root = root
        self.makeCheckList()

    def makeCheckList(self):
        self.cl = Tix.CheckList(self.root,height=2000,width=400)
        self.cl.pack()
        self.cl.hlist.add("C", text="Bulk")
        
        
        self.cl.hlist.add("C.CL1", text="Nonsterile")
        self.cl.hlist.add("C.CL1.It1", text="Liquide")
        self.cl.hlist.add("C.CL1.It1.I1", text="Bottles")
        self.cl.hlist.add("C.CL1.It1.I2", text="Drops")
        self.cl.hlist.add("C.CL1.It1.I3", text="Sache")
        self.cl.hlist.add("C.CL1.It1.I4", text="Spray")
        self.cl.hlist.add("C.CL1.It1.I5", text="Syrup")
        
        self.cl.hlist.add("C.CL1.Item2", text="Semi-Solid")
        self.cl.hlist.add("C.CL1.Item2.m1", text="Cream")
        self.cl.hlist.add("C.CL1.Item2.m2", text="Gels")
        self.cl.hlist.add("C.CL1.Item2.m3", text="Ointment")
        self.cl.hlist.add("C.CL1.Item2.m4", text="Other")
        self.cl.hlist.add("C.CL1.Item2.m5", text="Soft Capsules")
        self.cl.hlist.add("C.CL1.Item2.m6", text="Suppositories")
        
        self.cl.hlist.add("C.CL1.Item3", text="Solid")
        self.cl.hlist.add("C.CL1.Item3.a1", text="Cream")
        self.cl.hlist.add("C.CL1.Item3.a2", text="Gels")
        self.cl.hlist.add("C.CL1.Item3.a3", text="Ointment")
        self.cl.hlist.add("C.CL1.Item3.a4", text="Other")
        self.cl.hlist.add("C.CL1.Item3.a5", text="Soft Capsules")
        self.cl.hlist.add("C.CL1.Item3.a6", text="Suppositories")
        
        
        
        self.cl.hlist.add("C.CL2", text="Sterile")
        self.cl.hlist.add("C.CL2.t1", text="Ampouls")
        self.cl.hlist.add("C.CL2.t2", text="Bottles")
        self.cl.hlist.add("C.CL2.t3", text="Drops")
        self.cl.hlist.add("C.CL2.t4", text="Ophthalmic Ointments")
        self.cl.hlist.add("C.CL2.t5", text="Other**")
        self.cl.hlist.add("C.CL2.t6", text="Single dose")
        self.cl.hlist.add("C.CL2.t7", text="Spray")
        self.cl.hlist.add("C.CL2.t8", text="Syrings")
        self.cl.hlist.add("C.CL2.t9", text="Vials")
        
        self.b = self.cl.setstatus("C", "off")
        
        self.cl.setstatus("C.CL1", "off")
        self.cl.setstatus("C.CL1.It1", "off")
        self.cl.setstatus("C.CL1.It1.I1", "off")
        self.cl.setstatus("C.CL1.It1.I2", "off")
        self.cl.setstatus("C.CL1.It1.I3", "off")
        self.cl.setstatus("C.CL1.It1.I4", "off")
        self.cl.setstatus("C.CL1.It1.I5", "off")
        
        self.cl.setstatus("C.CL1.Item2", "off")
        self.cl.setstatus("C.CL1.Item2.m1", "off")
        self.cl.setstatus("C.CL1.Item2.m2","off")
        self.cl.setstatus("C.CL1.Item2.m3", "off")
        self.cl.setstatus("C.CL1.Item2.m4", "off")
        self.cl.setstatus("C.CL1.Item2.m5", "off")
        self.cl.setstatus("C.CL1.Item2.m6", "off")
        
        self.cl.setstatus("C.CL1.Item3", "off")
        self.cl.setstatus("C.CL1.Item3.a1", "off")
        self.cl.setstatus("C.CL1.Item3.a2", "off")
        self.cl.setstatus("C.CL1.Item3.a3", "off")
        self.cl.setstatus("C.CL1.Item3.a4", "off")
        self.cl.setstatus("C.CL1.Item3.a5", "off")
        self.cl.setstatus("C.CL1.Item3.a6", "off")

        self.cl.setstatus("C.CL2","off")
        self.cl.setstatus("C.CL2.t1", "off")
        self.cl.setstatus("C.CL2.t2","off")
        self.cl.setstatus("C.CL2.t3","off")
        self.cl.setstatus("C.CL2.t4", "off")
        self.cl.setstatus("C.CL2.t5", "off")
        self.cl.setstatus("C.CL2.t6", "off")
        self.cl.setstatus("C.CL2.t7", "off")
        self.cl.setstatus("C.CL2.t8", "off")
        self.cl.setstatus("C.CL2.t9", "off")
        
        status = self.cl.setstatus('C')
        if self.b=="off":
            st.write(f"Item {'C'} status: {self.b}")
        
        self.cl.autosetmode()

def main():
    root = Tix.Tk()
    view = View(root)
    root.update()
    root.mainloop()

if __name__ == '__main__':
    main()
    
    
    
    
    
    
#    a = st.checkbox("Bulk")
#     if a:
#         na = st.checkbox("Nonsterile")
#         if na:
#             na1 = st.checkbox("Liduide")
#             if na1:
#                 l1 = st.checkbox("Bottles")
#                 l2 = st.checkbox("Drops")
#                 l3 = st.checkbox("Other*")
#                 l4 = st.checkbox("Sache")
#                 l5 = st.checkbox("Spray")
#                 l6 = st.checkbox("Syrup")

#             nb1 = st.checkbox("Semi-Solid")
#             if nb1:
#                 s1 = st.checkbox("Cream")
#                 s2 = st.checkbox("Gels")
#                 s3 = st.checkbox("Ointment")
#                 s4 = st.checkbox("Other")
#                 s5 = st.checkbox("Soft Capsules")
#                 s6 = st.checkbox("Suppositories")
                
#             nc1 = st.checkbox("Solid")
#             if nc1:
#                 pass
#         s = st.checkbox("Nonsterile")
#         if s:
#             li = st.checkbox("Sterile")
#             if li:
#                 b = st.checkbox("Sterile")
#                 c = st.checkbox("Ampouls")
#                 d = st.checkbox("Bottles")
#                 e = st.checkbox("Drops")
#                 f = st.checkbox("Ophthalmic Ointments")
#                 g = st.checkbox("Other**")
#                 h = st.checkbox("Single dose")
#                 i = st.checkbox("Spray")
#                 j = st.checkbox("Syrings")
#                 k = st.checkbox("Vials")              

#             ly = st.checkbox("Ampouls")
#             if ly:
#                 ly1 = st.checkbox("Ampouls")
#                 ly2 = st.checkbox("Bottles")
#                 ly3 = st.checkbox("Other*")
#                 ly4 = st.checkbox("Vials")



# import tkinter.tix as Tix
# import streamlit as st

# def print_item_status(item_id):
#     status = checklist.setstatus(item_id)
#     st.write(f"Item {item_id} status: {status}")

# root = Tix.Tk()

# # Create a CheckList widget
# checklist = Tix.CheckList(root)
# checklist.pack()

# # Add items to the checklist
# checklist.hlist.add("C", text="Item 1")
# checklist.hlist.add("C.Item1", text="Subitem 1")
# checklist.hlist.add("C.Item1.Subitem1", text="Subsubitem 1")
# checklist.autosetmode()
# root.mainloop()
# checklist.autosetmode()

# # Check status of "C.Item1"
# print_item_status("C.Item1")
