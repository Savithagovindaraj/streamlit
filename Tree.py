# # # # # # # # # import streamlit as st

# # # # # # # # # # Custom component to render multi-select tree checkbox
# # # # # # # # # def render_tree_checkbox(options):
# # # # # # # # #     selected_options = st.empty()

# # # # # # # # #     selected_items = set()

# # # # # # # # #     for parent, children in options.items():
# # # # # # # # #         parent_checked = st.checkbox(parent)
# # # # # # # # #         if parent_checked:
# # # # # # # # #             selected_items.add(parent)
# # # # # # # # #             for child in children:
# # # # # # # # #                 child_checked = st.checkbox(f"{' ' * 4}{child}")
# # # # # # # # #                 if child_checked:
# # # # # # # # #                     selected_items.add(child)

# # # # # # # # #     selected_options.markdown(f"Selected Items: {', '.join(selected_items)}")

# # # # # # # # # def main():
# # # # # # # # #     st.title("Multi-Select Tree Checkbox in Streamlit")

# # # # # # # # #     options = {
# # # # # # # # #         "Fruits": ["Apple", "Banana", "Orange"],
# # # # # # # # #         "Vegetables": ["Carrot", "Spinach", "Tomato"],
# # # # # # # # #         "Drinks": ["Water", "Juice", "Soda"],
# # # # # # # # #     }

# # # # # # # # #     render_tree_checkbox(options)

# # # # # # # # # if __name__ == "__main__":
# # # # # # # # #     main()



# # # # # # # # # # import streamlit as st

# # # # # # # # # # col1,col2 = st.columns(2)

# # # # # # # # # # with col1:
# # # # # # # # # #     a = st.checkbox("Bulk")
# # # # # # # # # #     if a:
# # # # # # # # # #         na = st.checkbox("Nonsterile")
# # # # # # # # # #         if na:
# # # # # # # # # #             na1 = st.checkbox("Liduide")
# # # # # # # # # #             if na1:
# # # # # # # # # #                 l1 = st.checkbox("Bottles")
# # # # # # # # # #                 l2 = st.checkbox("Drops")
# # # # # # # # # #                 l3 = st.checkbox("Other*")
# # # # # # # # # #                 l4 = st.checkbox("Sache")
# # # # # # # # # #                 l5 = st.checkbox("Spray")
# # # # # # # # # #                 l6 = st.checkbox("Syrup")

# # # # # # # # # #             nb1 = st.checkbox("Semi-Solid")
# # # # # # # # # #             if nb1:
# # # # # # # # # #                 s1 = st.checkbox("Cream")
# # # # # # # # # #                 s2 = st.checkbox("Gels")
# # # # # # # # # #                 s3 = st.checkbox("Ointment")
# # # # # # # # # #                 s4 = st.checkbox("Other")
# # # # # # # # # #                 s5 = st.checkbox("Soft Capsules")
# # # # # # # # # #                 s6 = st.checkbox("Suppositories")
                
# # # # # # # # # #             nc1 = st.checkbox("Solid")
# # # # # # # # # #             if nc1:
# # # # # # # # # #                 pass
# # # # # # # # # #         s = st.checkbox("Nonsterile")
# # # # # # # # # #         if s:
# # # # # # # # # #             li = st.checkbox("Sterile")
# # # # # # # # # #             if li:
# # # # # # # # # #                 b = st.checkbox("Sterile")
# # # # # # # # # #                 c = st.checkbox("Ampouls")
# # # # # # # # # #                 d = st.checkbox("Bottles")
# # # # # # # # # #                 e = st.checkbox("Drops")
# # # # # # # # # #                 f = st.checkbox("Ophthalmic Ointments")
# # # # # # # # # #                 g = st.checkbox("Other**")
# # # # # # # # # #                 h = st.checkbox("Single dose")
# # # # # # # # # #                 i = st.checkbox("Spray")
# # # # # # # # # #                 j = st.checkbox("Syrings")
# # # # # # # # # #                 k = st.checkbox("Vials")              

# # # # # # # # # #             ly = st.checkbox("Ampouls")
# # # # # # # # # #             if ly:
# # # # # # # # # #                 ly1 = st.checkbox("Ampouls")
# # # # # # # # # #                 ly2 = st.checkbox("Bottles")
# # # # # # # # # #                 ly3 = st.checkbox("Other*")
# # # # # # # # # #                 ly4 = st.checkbox("Vials") 
                
# # # # # # # # import tkinter as tk
# # # # # # # # from tkinter import ttk

# # # # # # # # def check_children(item):
# # # # # # # #     # Recursively check all children
# # # # # # # #     children = tree.get_children(item)
# # # # # # # #     for child in children:
# # # # # # # #         tree.item(child, values=(1,))
# # # # # # # #         check_children(child)

# # # # # # # # def uncheck_children(item):
# # # # # # # #     # Recursively uncheck all children
# # # # # # # #     children = tree.get_children(item)
# # # # # # # #     for child in children:
# # # # # # # #         tree.item(child, values=(0,))
# # # # # # # #         uncheck_children(child)

# # # # # # # # def on_check(item):
# # # # # # # #     # Handle checkbox checking
# # # # # # # #     checked = tree.item(item, 'values')[0]
# # # # # # # #     if checked == 1:
# # # # # # # #         check_children(item)
# # # # # # # #     elif checked == 0:
# # # # # # # #         uncheck_children(item)

# # # # # # # # root = tk.Tk()
# # # # # # # # root.title("Tree with Checkboxes")

# # # # # # # # tree = ttk.Treeview(root, columns=("Check", "Data"), show="tree")
# # # # # # # # tree.heading("#0", text="Items", anchor='w')
# # # # # # # # tree.heading("Check", text="Check")
# # # # # # # # tree.heading("Data", text="Data")

# # # # # # # # # Inserting data
# # # # # # # # tree.insert("", "end", "item1", text="Item 1")
# # # # # # # # tree.insert("item1", "end", text="Sub-item 1.1")
# # # # # # # # tree.insert("item1", "end", text="Sub-item 1.2")
# # # # # # # # tree.insert("", "end", "item2", text="Item 2")
# # # # # # # # tree.insert("item2", "end", text="Sub-item 2.1")
# # # # # # # # tree.insert("item2", "end", text="Sub-item 2.2")

# # # # # # # # # Adding checkboxes
# # # # # # # # for item in tree.get_children():
# # # # # # # #     tree.item(item, values=(0,))  # 0 is unchecked

# # # # # # # # tree.bind("<Button-1>", lambda event: on_check(tree.selection()[0]))

# # # # # # # # tree.pack(expand=True, fill="both")
# # # # # # # # root.mainloop()


# # # # # # # import streamlit as st


# # # # # # # def makecollapsibletree(df):
# # # # # # #     return _makeTree("Collapsible-tree",df)

# # # # # # # def make(df):
# # # # # # #     return _makeTree("Linear-de")



# # # # # # # with st.sid


# # # # # # import streamlit as st

# # # # # # class HierarchicalCheckbox:
# # # # # #     def __init__(self, text, children=None):
# # # # # #         self.text = text
# # # # # #         self.children = children if children else []

# # # # # #     def add_child(self, child):
# # # # # #         self.children.append(child)

# # # # # #     def __repr__(self):
# # # # # #         return f"{'[X]' if self.checked else '[ ]'} {self.text}"

# # # # # #     def display(self, depth=0):
# # # # # #         indent = '  ' * depth
# # # # # #         print(indent + repr(self))
# # # # # #         for child in self.children:
# # # # # #             child.display(depth + 1)

# # # # # #     def toggle(self):
# # # # # #         self.checked = not self.checked
# # # # # #         for child in self.children:
# # # # # #             child.toggle()

# # # # # # # Example usage:
# # # # # # if __name__ == "__main__":
# # # # # #     st.title("Heading")
# # # # # #     root = HierarchicalCheckbox("Root")
# # # # # #     child1 = HierarchicalCheckbox("Child 1")
# # # # # #     child2 = HierarchicalCheckbox("Child 2")
# # # # # #     grandchild1 = HierarchicalCheckbox("Grandchild 1")
# # # # # #     grandchild2 = HierarchicalCheckbox("Grandchild 2")
# # # # # #     child1.add_child(grandchild1)
# # # # # #     child2.add_child(grandchild2)
# # # # # #     root.add_child(child1)
# # # # # #     root.add_child(child2)

# # # # # #     root.display()

# # # # # #     grandchild1.toggle()
# # # # # #     print("\nAfter toggling Grandchild 1:")
# # # # # #     root.display()


# # # import tkinter as tk

# # # class HierarchicalCheckbox(tk.Frame):
# # #     def __init__(self, master=None, items=None):
# # #         super().__init__(master)
# # #         self.pack()
# # #         self.items = items if items else {}
# # #         self.create_widgets()

# # #     def create_widgets(self):
# # #         for item, children in self.items.items():
# # #             self.add_checkbox(item, children)

# # #     def add_checkbox(self, text, children):
# # #         var = tk.IntVar()
# # #         checkbox = tk.Checkbutton(self, text=text, variable=var, command=lambda: self.update_children(var.get(), children))
# # #         checkbox.pack(anchor='w')
# # #         if children:
# # #             sub_frame = tk.Frame(self)
# # #             sub_frame.pack(padx=20, anchor='w')
# # #             self.add_children_checkboxes(sub_frame, children, var)

# #     # def add_children_checkboxes(self, parent, children, parent_var):
# #     #     for child, grandchildren in children.items():
# #     #         var = tk.IntVar()
# #     #         checkbox = tk.Checkbutton(parent, text=child, variable=var, command=lambda: self.update_children(var.get(), grandchildren))
# #     #         checkbox.pack(anchor='w')
# #     #         if grandchildren:
# #     #             sub_frame = tk.Frame(parent)
# #     #             sub_frame.pack(padx=20, anchor='w')
# #     #             self.add_children_checkboxes(sub_frame, grandchildren, var)

# #     # def update_children(self, value, children):
# #     #     for child, grandchildren in children.items():
# #     #         child_var = child.winfo_children()[0].cget('variable')
# #     #         child_var.set(value)
# #     #         if grandchildren:
# # #     #             self.update_children(value, grandchildren)

# # # # Example usage:
# # # if __name__ == "__main__":
# # #     items = {
# # #         'Parent 1': {
# # #             'Child 1.1': {},
# # #             'Child 1.2': {},
# # #             'Child 1.3': {
# # #                 'Grandchild 1.3.1': {},
# # #                 'Grandchild 1.3.2': {},
# # #             }
# # #         },
# # #         'Parent 2': {
# # #             'Child 2.1': {},
# # #             'Child 2.2': {},
# # #         }
# # #     }

# # #     root = tk.Tk()
# # #     root.title("Hierarchical Checkbox")
# # #     app = HierarchicalCheckbox(master=root, items=items)
# # #     app.mainloop()



# # import streamlit as st

# # class HierarchicalCheckbox:
# #     def __init__(self, text, children=None, checked=False):
# #         self.text = text
# #         self.checked = checked
# #         self.children = children if children else []

# #     def add_child(self, child):
# #         self.children.append(child)

# #     def toggle(self):
# #         self.checked = not self.checked
# #         for child in self.children:
# #             child.toggle()

# # def display_checkbox(checkbox, depth=0):
# #     if st.checkbox(checkbox.text, value=checkbox.checked):
# #         for child in checkbox.children:
# #             display_checkbox(child, depth + 1)

# # def main():
# #     root = HierarchicalCheckbox("Root")
# #     child1 = HierarchicalCheckbox("Child 1")
# #     child2 = HierarchicalCheckbox("Child 2")
# #     grandc = HierarchicalCheckbox("Grandchild 1")
# #     grandc1 = HierarchicalCheckbox("Grandchild 2")
# #     child1.add_child(grandc)
# #     child1.add_child(grandc1)
# #     root.add_child(child1)
# #     root.add_child(child2)

# #     st.title("Hierarchical Checkbox")
# #     st.write("Select checkboxes:")

# #     display_checkbox(root)

# # if __name__ == "__main__":
# #     main()



# # # import tkinter as tk

# # # class CheckboxTree(tk.Frame):
# # #     def __init__(self, master, items):
# # #         super().__init__(master)

# # #         self.items = items
# # #         self.checkboxes = {}

# # #         for item in self.items:
# # #             checkbox = tk.Checkbutton(self, text=item)
# # #             checkbox.pack()

# # #             self.checkboxes[item] = checkbox

# # #     def get_checked_items(self):
# # #         checked_items = []

# # #         for item, checkbox in self.checkboxes.items():
# # #             if checkbox.var.get():
# # #                 checked_items.append(item)

# # #         return checked_items

# # # if __name__ == '__main__':
# # #     root = tk.Tk()

# # #     items = ['Item 1', 'Item 2', 'Item 3']

# # #     tree = CheckboxTree(root, items)
# # #     tree.pack()

# # #     button = tk.Button(root, text='Get checked items', command=lambda: print(tree.get_checked_items()))
# # #     button.pack()

# # #     root.mainloop()



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
    
    
    
    
    
    
#   #  a = st.checkbox("Bulk")
# # # # # # # # # #     if a:
# # # # # # # # # #         na = st.checkbox("Nonsterile")
# # # # # # # # # #         if na:
# # # # # # # # # #             na1 = st.checkbox("Liduide")
# # # # # # # # # #             if na1:
# # # # # # # # # #                 l1 = st.checkbox("Bottles")
# # # # # # # # # #                 l2 = st.checkbox("Drops")
# # # # # # # # # #                 l3 = st.checkbox("Other*")
# # # # # # # # # #                 l4 = st.checkbox("Sache")
# # # # # # # # # #                 l5 = st.checkbox("Spray")
# # # # # # # # # #                 l6 = st.checkbox("Syrup")

# # # # # # # # # #             nb1 = st.checkbox("Semi-Solid")
# # # # # # # # # #             if nb1:
# # # # # # # # # #                 s1 = st.checkbox("Cream")
# # # # # # # # # #                 s2 = st.checkbox("Gels")
# # # # # # # # # #                 s3 = st.checkbox("Ointment")
# # # # # # # # # #                 s4 = st.checkbox("Other")
# # # # # # # # # #                 s5 = st.checkbox("Soft Capsules")
# # # # # # # # # #                 s6 = st.checkbox("Suppositories")
                
# # # # # # # # # #             nc1 = st.checkbox("Solid")
# # # # # # # # # #             if nc1:
# # # # # # # # # #                 pass
# # # # # # # # # #         s = st.checkbox("Nonsterile")
# # # # # # # # # #         if s:
# # # # # # # # # #             li = st.checkbox("Sterile")
# # # # # # # # # #             if li:
# # # # # # # # # #                 b = st.checkbox("Sterile")
# # # # # # # # # #                 c = st.checkbox("Ampouls")
# # # # # # # # # #                 d = st.checkbox("Bottles")
# # # # # # # # # #                 e = st.checkbox("Drops")
# # # # # # # # # #                 f = st.checkbox("Ophthalmic Ointments")
# # # # # # # # # #                 g = st.checkbox("Other**")
# # # # # # # # # #                 h = st.checkbox("Single dose")
# # # # # # # # # #                 i = st.checkbox("Spray")
# # # # # # # # # #                 j = st.checkbox("Syrings")
# # # # # # # # # #                 k = st.checkbox("Vials")              

# # # # # # # # # #             ly = st.checkbox("Ampouls")
# # # # # # # # # #             if ly:
# # # # # # # # # #                 ly1 = st.checkbox("Ampouls")
# # # # # # # # # #                 ly2 = st.checkbox("Bottles")
# # # # # # # # # #                 ly3 = st.checkbox("Other*")
# # # # # # # # # #                 ly4 = st.checkbox("Vials")



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
