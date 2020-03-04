        ph = 0
        while l1 or l2:
            A = (l1.val if l1 else 0)
            B = (l2.val if l2 else 0)

            val = A + B + ph
            # print ("val is "+str(val))
            ph = 0

        
            if val >= 10:
                ph = 1
                val = val - 10
                
                print("First Loop")
                result_tail.next = ListNode(val)
                print(result_tail)
                result_tail = result
                
                
                # result_tail = ListNode(val)
                
                # print(result_tail)
                # result_tail = result_tail.next
                

                
            else:
                # result_tail = ListNode(val)
               
                print("Second Loop")
                result_tail.next = ListNode(val)
                
                print(result_tail)
                result_tail = result_tail.next
                # print(result_tail)
                # print(result_tail)
                # print(result_tail)
                # result_tail = result_tail.next
                
            # print(RL)
            l1 = (l1.next if l1 else 0)
            l2 = (l2.next if l2 else 0)
            
        return(result.next)