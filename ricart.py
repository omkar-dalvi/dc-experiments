import random
def cust_sort(kv):
	value_list=kv.values()
	temp=[]
	for i in sorted(value_list):
		value=[key  for (key, value) in kv.items() if value == i][0]
		temp.append(value)
	return temp
import random
def selecting_process(n):
	request_processes = random.randrange(1,n+1)
	# Allocating timestamp to the processes
	ts=[]
	for i in range(request_processes):
		temp=random.randrange(1,100)
		if temp in ts:
			while temp not in ts:
				temp=random.randrange(1,100)
		ts.append(temp)
	print()
	print("=====================REQUEST=====================")
	for i in range(request_processes):
		for j in range(n):
			if i!=j:
				print("Process "+str(i+1)+" Sending REQUEST ("+str(i+1)+","+str(ts[i])+")"+" to Process "+str(j+1))
	req_array=[]
	for i in range(1,request_processes+1):
		req_array.append(i)
	kv={}
	for i in range(request_processes):
		kv[i+1]=ts[i]
	request_queue=sorted(req_array,key=cust_sort(kv).index)
	print("Request queue (sorted in ascending order of timestamp):",request_queue)
	return ts,request_queue

def sending_reply_cs(pid,no_of_processes):
	print()
	print("=====================REPLY=====================")
	# for i in range(no_of_processes):
	# 	if i!=pid:
	# 		print("Process "+str(i+1)+" sending REPLY to "+"Process "+str(pid+1))
	for i in range(no_of_processes):
		for j in range(no_of_processes):
			if i!=j:
				if i+1!=pid:
					print("Process "+str(i+1)+" sending REPLY to "+"Process "+str(j+1))
def csprocess_reply(pid,request_queue):
	for i in request_queue:
		print("Process "+str(pid+1)+" sending REPLY to Process "+str(i))
flag=0
rq=[]
no_of_processes = int(input("Enter the number of processes:"))
ts,rq=selecting_process(no_of_processes)
sending_reply_cs(rq[0],no_of_processes)
for i in range(len(rq)):
	pid=rq[i]-1
	print()
	print("===================Process "+str(pid+1)+" ENTERING CS===================")
	print("Process "+str(pid+1)+" entered CS")
	print()
	print("===================Process "+str(pid+1)+" EXITING CS===================")
	if len(rq[i+1:])!=0:
		csprocess_reply(pid,rq[i+1:])
	else:
		print("All processes have successfully executed CS!")







