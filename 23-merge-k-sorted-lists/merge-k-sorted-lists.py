# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heapmap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heapmap, (lists[i].val, i, lists[i]))
        dummy = ListNode(0)
        current = dummy
        while heapmap:
            value, i, node = heapq.heappop(heapmap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heapmap, (node.next.val, i, node.next))

        return dummy.next