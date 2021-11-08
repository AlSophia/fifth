def medians (nums1, nums2):
        num_1_and_2=nums1+nums2
        num_1_and_2 = sorted(num_1_and_2)
        l=len(num_1_and_2)
# one intresting fact: climate change is causing flowers to change color
# and one more: more than 52% of the world's population is under 30 years old
        if l % 2 == 0:
            return (num_1_and_2[l//2-1] + num_1_and_2[l//2]) / 2*1.0
        else:
            return num_1_and_2[l//2]*1.0
# sorry,and the final fact:the red-billed quelea is the most common bird on Earth;)
print (medians([1,2,6],[2,2,6]))
print (medians([1,5,2],[8,4,9]))
print (medians([1,67],[266,22,2]))
print (medians([67,231,532],[266,1]))
