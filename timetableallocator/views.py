from django.shortcuts import render
from django.http import HttpResponse
import datetime
from timetableallocator.forms import TimeTableForm
import pandas as pd

def Timetable(request):
   Class="Please input a class"
   if request.method == "POST":
      #Get the posted form
      Form = TimeTableForm(request.POST)
      if Form.is_valid():
         Class = Form.cleaned_data['Class']
   else:
      Form = TimeTableForm()

   class Table:
      def __init__(self,root,list):
         # code for creating table
         for i in range(total_rows):
            for j in range(total_columns):
               self.e = Entry(root, width=20, fg='blue', font=('Arial',16,'bold'))
               self.e.grid(row=i, column=j)
               self.e.insert(END, list[i][j])
   class Timetable:
      def __init__(self,root,list):
         countrow=0
         countcolumn=0
         for i in list:
            countcolumn=0
            for tab in i:
               self.e = Entry(root, width=20, fg='blue', font=('Arial',16,'bold'))
               self.e.grid(row=countrow, column=countcolumn)
               self.e.insert(END, tab)
               countcolumn+=1
            countrow+=1
   # A class to represent a graph object
   class Graph:
      # Constructor
      def __init__(self, edges, N):
         self.adj = [[] for _ in range(N)]
         # add edges to the undirected graph
         for (src, dest) in edges:
               self.adj[src].append(dest)
               self.adj[dest].append(src)

   # Function to assign colors to vertices of a graph
   def colorGraph(graph):
      # keep track of the color assigned to each vertex
      result = {}
      # assign a color to vertex one by one
      for u in range(node_count):
         # check colors of adjacent vertices of `u` and store them in a set
         assigned = set([result.get(i) for i in graph.adj[u] if i in result])
         # check for the first free color
         color = 1
         for c in assigned:
               if color != c:
                  break
               color = color + 1
         # assign vertex `u` the first available color
         result[u] = color

      for v in range(node_count):
      #    print("Color assigned to vertex", v, "is", colors[result[v]])
         key = colors[result[v]+1]
         dict3.setdefault(key, [])
         for key1, value in nodes.items():
               if dict1[v][0] == value:
                  string=key1
         for key1, value in nodes.items():
               if dict1[v][1] == value:
                  string1=key1
         dict3[key].append(string+","+string1)
   def equal_cells(list):
      max=0
      for i in list:
         if len(i)>max:
            max=len(i)
      for i in list:
         for k in range(max-len(i)):
            i.append("-")

   even_sem=pd.read_csv('even_sem.csv').to_dict() # import csv file
   #print(even_sem)
   teachers=pd.read_csv('teachers.csv').to_dict() # import csv file
   #print(teachers)
   # assign data to nodes
   nodes={}
   # assign course to nodes
   for courses in even_sem.values():
      for course in courses.values():
         nodes[course]=len(nodes)
   # assign teachers to nodes
   for teacher in teachers.keys():
         nodes[teacher]=len(nodes)
   #print(nodes)
   # bipartite graph
   bipartite_graph=[]
   tuple1=()
   for teacher,courses in teachers.items():
      for course in courses.values():
         if not isinstance(course, float):
               del tuple1
               tuple1=(nodes[teacher],nodes[course])
               bipartite_graph.append(tuple1)
   #print(bipartite_graph) # bipartite graph
   node_count=len(bipartite_graph) # node count
   #print("Node Count :",node_count)
      # assign numbers to each line
   dict1={}
   for i,j in enumerate(bipartite_graph):
      dict1[i]=j
   #print(dict1)
   # dict with adjacent lines
   dict2={}
   for key,value in dict1.items():
      for key1,value1 in dict1.items():
         if value1[0]==value[0]:
               dict2.setdefault(key, [])
               dict2[key].append(key1)
         if value1[1]==value[1]:
               dict2.setdefault(key, [])
               dict2[key].append(key1)
   # remove duplicates in dict
   for key,value in dict2.items():
      dict2[key]=list(set(value))
   # remove own line number
   for key,value in dict2.items():
      if key in value:
         value.remove(key)
   #print(dict2)
   # convert bipartite graph to line graph(make adjacent lines as a graph)
   line_graph=[]
   del tuple1
   for key,value in dict2.items():
      for i in value:
         tuple1=(key,i)
         line_graph.append(tuple1)
   #print(line_graph)
   # Add more colors for graphs with many more vertices
   colors = ["", "BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK", "BLACK", "BROWN", "WHITE", "PURPLE", "VOILET","GREY"]
   # build a graph from the given edges
   graph = Graph(line_graph,node_count)
   # color graph using the greedy algorithm
   dict3={}
   colorGraph(graph)
   #print(dict3)
   # take the data
   list1=[]
   table_list=[]
   # find maximum value in dict
   max=0
   for i,j in dict3.items():
      if len(j)>max:
         max=len(j)
   # assign - to empty values
   for i,j in dict3.items():
      for k in range(max-len(j)):
         j.append("-")
   #print("\n\n",dict3)
   # order dict to generate as table
   for i in range(max):
      list1.clear()
      for j in dict3.values():
         list1.append(j[i])
      tuple1=tuple(list1)
      #print(tuple1)
      table_list.append(tuple1)
   #print("\n\n",table_list)

   days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
   # print("\n\n\n")
   # # print("ss timetable")

   teachertt={}
   for teacher in teachers.keys():
      teachertt[teacher]={}

   list2s=[]
   list4s=[]
   list6s=[]
   s2_p=0
   s4_p=0
   s6_p=0
   ss2_periods=[]
   ss4_periods=[]
   ss6_periods=[]
   for j in range(0,len(table_list[0])):
      k=0
      while k < len(table_list):
         i=table_list[k]
         if i[j] == '-':
               break
         teacher,cid=i[j].split(",")
         if cid.startswith("20XW2"):
               if str(len(ss2_periods))+','+str(s2_p) in teachertt[teacher].keys():
                  ss2_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(ss2_periods))+','+str(s2_p)]=cid
                  ss2_periods.append(i[j])
               if (len(ss2_periods)==5):
                  list2s.append(ss2_periods)
                  ss2_periods=[]
                  s2_p=s2_p+1

         elif cid.startswith("18XW4"):
               if str(len(ss4_periods))+','+str(s4_p) in teachertt[teacher].keys():
                  ss4_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(ss4_periods))+','+str(s4_p)]=cid
                  ss4_periods.append(i[j])
               if (len(ss4_periods)==5):
                  list4s.append(ss4_periods)
                  ss4_periods=[]
                  s4_p+=1

         elif cid.startswith("18XW6"):
               if str(len(ss6_periods))+','+str(s6_p) in teachertt[teacher].keys():
                  ss6_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(ss6_periods))+','+str(s6_p)]=cid
                  ss6_periods.append(i[j])
               if (len(ss6_periods)==5):
                  list6s.append(ss6_periods)
                  ss6_periods=[]
                  s6_p+=1
         k=k+1

   list2s.append(ss2_periods)
   list4s.append(ss4_periods)
   list6s.append(ss6_periods)

   list2ss=[]
   list4ss=[]
   list6ss=[]

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list2s:
         if i<=len(j)-1:
               x.append(j[i])
      list2ss.append(x)

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list4s:
         if i<=len(j)-1:
               x.append(j[i])
      list4ss.append(x)

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list6s:
         if i<=len(j)-1:
               x.append(j[i])
      list6ss.append(x)
   list2ss.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list2ss[0]))])
   list4ss.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list4ss[0]))])
   list6ss.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list6ss[0]))])

   equal_cells(list2ss)
   equal_cells(list4ss)
   equal_cells(list6ss)
   #print(list2ss)
   #print(list4ss)
   #print(list6ss)

   #print("DS timetable")
   list2d=[]
   list4d=[]
   list6d=[]
   d2_p=0
   d4_p=0
   d6_p=0
   ds2_periods=[]
   ds4_periods=[]
   ds6_periods=[]
   for j in range(0,len(table_list[0])):
      k=0
      while k < len(table_list):
         i=table_list[k]
         if i[j] == '-':
               break
         teacher,cid=i[j].split(",")
         if cid.startswith("20XD2"):
               if str(len(ds2_periods))+','+str(d2_p) in teachertt[teacher].keys():
                  ds2_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(ds2_periods))+','+str(d2_p)]=cid
                  ds2_periods.append(i[j])
               if (len(ds2_periods)==5):
                  list2d.append(ds2_periods)
                  ds2_periods=[]
                  d2_p=d2_p+1

         elif cid.startswith("18XD4"):
               if str(len(ds4_periods))+','+str(d4_p) in teachertt[teacher].keys():
                  ds4_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(ds4_periods))+','+str(d4_p)]=cid
                  ds4_periods.append(i[j])
               if (len(ds4_periods)==5):
                  list4d.append(ds4_periods)
                  ds4_periods=[]
                  d4_p+=1

         elif cid.startswith("18XD6"):
               if str(len(ds6_periods))+','+str(d6_p) in teachertt[teacher].keys():
                  ds6_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(ds6_periods))+','+str(d6_p)]=cid
                  ds6_periods.append(i[j])
               if (len(ds6_periods)==5):
                  list6d.append(ds6_periods)
                  ds6_periods=[]
                  d6_p+=1
         k=k+1

   list2d.append(ds2_periods)
   list4d.append(ds4_periods)
   list6d.append(ds6_periods)

   list2ds=[]
   list4ds=[]
   list6ds=[]

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list2d:
         if i<=len(j)-1:
               x.append(j[i])
      list2ds.append(x)

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list4d:
         if i<=len(j)-1:
               x.append(j[i])
      list4ds.append(x)

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list6d:
         if i<=len(j)-1:
               x.append(j[i])
      list6ds.append(x)
   list2ds.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list2ds[0]))])
   list4ds.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list4ds[0]))])
   list6ds.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list6ds[0]))])

   equal_cells(list2ds)
   equal_cells(list4ds)
   equal_cells(list6ds)
   #print(list2ds)
   #print(list4ds)
   #print(list6ds)

   #print("TCS timetable")
   list2tcs=[]
   list4tcs=[]
   list6tcs=[]
   t2_p=0
   t4_p=0
   t6_p=0
   t2_periods=[]
   t4_periods=[]
   t6_periods=[]
   for j in range(0,len(table_list[0])):
      k=0
      while k < len(table_list):
         i=table_list[k]
         if i[j] == '-':
               break
         teacher,cid=i[j].split(",")
         if cid.startswith("20XT2"):
               if str(len(t2_periods))+','+str(t2_p) in teachertt[teacher].keys():
                  t2_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(t2_periods))+','+str(t2_p)]=cid
                  t2_periods.append(i[j])
               if (len(t2_periods)==5):
                  list2tcs.append(t2_periods)
                  t2_periods=[]
                  t2_p=t2_p+1

         elif cid.startswith("18XT4"):
               if str(len(t4_periods))+','+str(t4_p) in teachertt[teacher].keys():
                  t4_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(t4_periods))+','+str(t4_p)]=cid
                  t4_periods.append(i[j])
               if (len(t4_periods)==5):
                  list4tcs.append(t4_periods)
                  t4_periods=[]
                  t4_p+=1

         elif cid.startswith("18XT6"):
               if str(len(t6_periods))+','+str(s6_p) in teachertt[teacher].keys():
                  t6_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(t6_periods))+','+str(t6_p)]=cid
                  t6_periods.append(i[j])
               if (len(t6_periods)==5):
                  list6tcs.append(t6_periods)
                  t6_periods=[]
                  t6_p+=1
         k=k+1

   list2tcs.append(t2_periods)
   list4tcs.append(t4_periods)
   list6tcs.append(t6_periods)

   list2t=[]
   list4t=[]
   list6t=[]

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list2tcs:
         if i<=len(j)-1:
               x.append(j[i])
      list2t.append(x)

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list4tcs:
         if i<=len(j)-1:
               x.append(j[i])
      list4t.append(x)

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list6tcs:
         if i<=len(j)-1:
               x.append(j[i])
      list6t.append(x)
   list2t.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list2t[0]))])
   list4t.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list4t[0]))])
   list6t.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list6t[0]))])
   equal_cells(list2t)
   equal_cells(list4t)
   equal_cells(list6t)

   #print("cs timetable")
   list2cs=[]
   c2_p=0
   c2_periods=[]
   for j in range(0,len(table_list[0])):
      k=0
      while k < len(table_list):
         i=table_list[k]
         if i[j] == '-':
               break
         teacher,cid=i[j].split(",")
         if cid.startswith("20XC2"):
               if str(len(c2_periods))+','+str(c2_p) in teachertt[teacher].keys():
                  c2_periods.append('-')
                  k=k-1
               else:
                  teachertt[teacher][str(len(c2_periods))+','+str(c2_p)]=cid
                  c2_periods.append(i[j])
               if (len(c2_periods)==5):
                  list2cs.append(c2_periods)
                  c2_periods=[]
                  c2_p=c2_p+1

         k=k+1

   list2cs.append(c2_periods)
   list2c=[]

   for i in range(0,5):
      x=[]
      x.append(days[i])
      for j in list2cs:
         if i<=len(j)-1:
               x.append(j[i])
      list2c.append(x)

   list2c.insert(0,['Days']+["Period "+str(i) for i in range(1,len(list2t[0]))])
   #print(list2t)
   #print(list4t)
   #print(list6t)
   if Class=="2s":
      timetable=list2ss
   elif Class=="4s":
      timetable=list4ss
   elif Class=="6s":
      timetable=list6ss
   elif Class=="2d":
      timetable=list2ds
   elif Class=="4d":
      timetable=list4ds
   elif Class=="6d":
      timetable=list6ds
   elif Class=="2t":
      timetable=list2t
   elif Class=="4t":
      timetable=list4t
   elif Class=="6t":
      timetable=list6t
   elif Class=="2c":
     timetable=list2c
   elif Class in teachertt.keys():
      ll=[]
      for i in range(0,5):
         l=[days[i]]
         for j in range(0,5):
            if str(i)+','+str(j) in teachertt[Class].keys():
               l.append(teachertt[Class][str(i)+','+str(j)])
            else:
               l.append('-')
         ll.append(l)
      ll.insert(0,['Days']+["Period "+str(i) for i in range(1,6)])
      equal_cells(ll)
      timetable=ll
   else:
      timetable="Not Found"
   return render(request, 'timetable.html', {"timetable" : timetable})
