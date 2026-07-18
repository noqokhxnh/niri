#!/usr/bin/env python3
"""Generate 120-day Coding Interview University roadmap into calendar notes JSON."""
import json, os
from datetime import datetime, timedelta

START_DATE = datetime(2026, 7, 17)
NOTES_FILE = os.path.expanduser("~/.local/state/quickshell/calendar/notes.json")

days = {}

# Phase 1: Big-O & Data Structures (Days 1-14)
days[1] = (
    "🧠 Phase 1: Nền tảng — Ngày 1/120\n"
    "📚 Độ phức tạp thuật toán / Big-O\n\n"
    "🎯 Mục tiêu: Hiểu cách phân tích độ phức tạp thuật toán\n\n"
    "📹 Video cần xem:\n"
    "- [ ] Harvard CS50 - Asymptotic Notation\n"
    "  → https://www.youtube.com/watch?v=iOq5kSKqeR4\n"
    "- [ ] Big O Notations (quick tutorial)\n"
    "  → https://www.youtube.com/watch?v=V6mKVRU1evU\n"
    "- [ ] Big O Notation - best mathematical explanation\n"
    "  → https://www.youtube.com/watch?v=ei-A_wy5Yxw\n\n"
    "📖 Đọc:\n"
    "- [ ] Big O Cheat Sheet → http://bigocheatsheet.com/\n\n"
    "💻 Thực hành:\n"
    "- [ ] Xác định Big-O của các đoạn code đơn giản\n"
    "- [ ] Phân biệt O(1), O(n), O(n²), O(log n), O(2^n)"
)

days[2] = (
    "🧠 Phase 1: Nền tảng — Ngày 2/120\n"
    "📚 Độ phức tạp thuật toán (tiếp)\n\n"
    "📹 Video:\n"
    "- [ ] Skiena: Algorithm Analysis\n"
    "  → https://www.youtube.com/watch?v=z1mkCe3kVUA\n"
    "- [ ] UC Berkeley Big O\n"
    "  → https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98\n"
    "- [ ] Amortized Analysis\n"
    "  → https://www.youtube.com/watch?v=B3SpQZaAZP4\n"
    "- [ ] Review: Analyzing Algorithms (18 min)\n"
    "  → https://www.youtube.com/playlist?list=PL9xmBV_5YoZMxejjIyFHWa-4nKg6sdoIv\n\n"
    "💻 Thực hành:\n"
    "- [ ] Đọc TopCoder: Computational Complexity phần 1 & 2\n"
    "- [ ] Làm bài quiz ở cuối chương Cracking the Coding Interview về Big-O\n"
    "- [ ] Ôn lại Master Theorem"
)

days[3] = (
    "🧠 Phase 1: Nền tảng — Ngày 3/120\n"
    "📚 Cấu trúc dữ liệu: Arrays\n\n"
    "🎯 Mục tiêu: Hiểu và implement Array & Dynamic Array\n\n"
    "📹 Video:\n"
    "- [ ] Arrays - CS50 Harvard → https://www.youtube.com/watch?v=tI_tIZFyKBw&t=3009s\n"
    "- [ ] Arrays (Coursera) → https://www.coursera.org/lecture/data-structures/arrays-OsBSF\n"
    "- [ ] Dynamic Arrays → https://www.coursera.org/lecture/data-structures/dynamic-arrays-EwbnV\n\n"
    "💻 Implement:\n"
    "- [ ] Tạo mảng: insert, delete, search\n"
    "- [ ] Dynamic Array (tự động resize)\n"
    "- [ ] Phân tích Big-O từng thao tác\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Two Sum → https://leetcode.com/problems/two-sum/\n"
    "- [ ] Best Time to Buy and Sell Stock → https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"
)

days[4] = (
    "🧠 Phase 1: Nền tảng — Ngày 4/120\n"
    "📚 Cấu trúc dữ liệu: Arrays (tiếp)\n\n"
    "📹 Video:\n"
    "- [ ] UC Berkeley CS61B Linear Arrays → https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE\n"
    "- [ ] Resizable Arrays → https://www.coursera.org/lecture/data-structures/resizable-arrays-UmF7h\n\n"
    "💻 Thực hành: xử lý mảng đa chiều\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Product of Array Except Self → https://leetcode.com/problems/product-of-array-except-self/\n"
    "- [ ] Maximum Subarray → https://leetcode.com/problems/maximum-subarray/\n"
    "- [ ] Contains Duplicate → https://leetcode.com/problems/contains-duplicate/"
)

days[5] = (
    "🧠 Phase 1: Nền tảng — Ngày 5/120\n"
    "📚 Cấu trúc dữ liệu: Linked Lists\n\n"
    "📹 Video:\n"
    "- [ ] Singly Linked Lists → https://www.coursera.org/lecture/data-structures/singly-linked-lists-tR1Gz\n"
    "- [ ] CS61B Linked Lists → https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0\n"
    "- [ ] Doubly Linked Lists → https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpG3e\n\n"
    "💻 Implement:\n"
    "- [ ] SinglyLinkedList: insert, delete, search, traverse\n"
    "- [ ] DoublyLinkedList: insert, delete\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Reverse Linked List → https://leetcode.com/problems/reverse-linked-list/\n"
    "- [ ] Middle of the Linked List → https://leetcode.com/problems/middle-of-the-linked-list/"
)

days[6] = (
    "🧠 Phase 1: Nền tảng — Ngày 6/120\n"
    "📚 Linked Lists (tiếp)\n\n"
    "📹 Video:\n"
    "- [ ] CS61B Linked Lists (tt) → https://archive.org/details/ucberkeley_webcast_cNBtDstfa5Q\n"
    "- [ ] Review: Linked Lists in 4min → https://youtu.be/F8AbOfQwl1c\n\n"
    "💻 Thực hành:\n"
    "- [ ] Detect cycle trong linked list\n"
    "- [ ] Merge two sorted lists\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Linked List Cycle → https://leetcode.com/problems/linked-list-cycle/\n"
    "- [ ] Merge Two Sorted Lists → https://leetcode.com/problems/merge-two-sorted-lists/\n"
    "- [ ] Remove Nth Node From End → https://leetcode.com/problems/remove-nth-node-from-end-of-list/\n"
    "- [ ] Add Two Numbers → https://leetcode.com/problems/add-two-numbers/"
)

days[7] = (
    "🧠 Phase 1: Nền tảng — Ngày 7/120\n"
    "📚 Cấu trúc dữ liệu: Stack\n\n"
    "📹 Video:\n"
    "- [ ] Stack → https://www.coursera.org/lecture/data-structures/stacks-UdKzQ\n"
    "- [ ] Review: Stack in 3min → https://youtu.be/KcT3aVgrrpU\n\n"
    "💻 Implement:\n"
    "- [ ] Stack dùng array\n"
    "- [ ] Stack dùng linked list\n"
    "- [ ] push, pop, peek, isEmpty, size\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Valid Parentheses → https://leetcode.com/problems/valid-parentheses/\n"
    "- [ ] Min Stack → https://leetcode.com/problems/min-stack/\n"
    "- [ ] Evaluate Reverse Polish Notation → https://leetcode.com/problems/evaluate-reverse-polish-notation/"
)

days[8] = (
    "🧠 Phase 1: Nền tảng — Ngày 8/120\n"
    "📚 Cấu trúc dữ liệu: Queue\n\n"
    "📹 Video:\n"
    "- [ ] Queue → https://www.coursera.org/lecture/data-structures/queues-2sXpK\n"
    "- [ ] Circular Buffer → https://en.wikipedia.org/wiki/Circular_buffer\n"
    "- [ ] Review: Queue in 3min → https://youtu.be/D6gu-_tmEpQ\n\n"
    "💻 Implement:\n"
    "- [ ] Queue dùng array (circular buffer)\n"
    "- [ ] Queue dùng linked list\n"
    "- [ ] Deque (double-ended queue)\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Implement Queue using Stacks → https://leetcode.com/problems/implement-queue-using-stacks/\n"
    "- [ ] Sliding Window Maximum → https://leetcode.com/problems/sliding-window-maximum/\n"
    "- [ ] Task Scheduler → https://leetcode.com/problems/task-scheduler/"
)

days[9] = (
    "🧠 Phase 1: Nền tảng — Ngày 9/120\n"
    "📚 Cấu trúc dữ liệu: Hash Table\n\n"
    "📹 Video:\n"
    "- [ ] Hashing with Chaining → https://www.youtube.com/watch?v=0M_kIqhwbFo\n"
    "- [ ] Table Doubling → https://www.youtube.com/watch?v=BRO7mVIFt08\n"
    "- [ ] Open Addressing → https://www.youtube.com/watch?v=rvdJDijO2Ro\n\n"
    "💻 Implement:\n"
    "- [ ] Hash Table với chaining (linked list)\n"
    "- [ ] Hash function cơ bản"
)

days[10] = (
    "🧠 Phase 1: Nền tảng — Ngày 10/120\n"
    "📚 Hash Table (tiếp)\n\n"
    "📹 Video:\n"
    "- [ ] PyCon 2010: The Mighty Dictionary → https://www.youtube.com/watch?v=C4Kc8xzcA68\n"
    "- [ ] Review: Hash tables in 4min → https://youtu.be/knV86FlSXJ8\n"
    "- [ ] Core Hash Tables → https://www.coursera.org/lecture/data-structures-optimizing-performance/core-hash-tables-m7UuP\n\n"
    "💻 Implement:\n"
    "- [ ] Hash Table với open addressing (linear probing)\n"
    "- [ ] add, get, exists, remove, hash(k,m)\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Two Sum → https://leetcode.com/problems/two-sum/\n"
    "- [ ] Group Anagrams → https://leetcode.com/problems/group-anagrams/\n"
    "- [ ] Top K Frequent Elements → https://leetcode.com/problems/top-k-frequent-elements/"
)

days[11] = (
    "🧠 Phase 1: Nền tảng — Ngày 11/120\n"
    "📚 Binary Search\n\n"
    "📹 Video:\n"
    "- [ ] Binary Search → https://www.youtube.com/watch?v=D5SrAga1pno\n"
    "- [ ] Khan Academy → https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search\n"
    "- [ ] Review in 4min → https://youtu.be/fDKIpRe8GW4\n\n"
    "💻 Implement:\n"
    "- [ ] Binary search trên mảng đã sort\n"
    "- [ ] Binary search đệ quy\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Binary Search → https://leetcode.com/problems/binary-search/\n"
    "- [ ] Search Insert Position → https://leetcode.com/problems/search-insert-position/"
)

days[12] = (
    "🧠 Phase 1: Nền tảng — Ngày 12/120\n"
    "📚 Binary Search (tiếp)\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Find First and Last Position → https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/\n"
    "- [ ] Search in Rotated Sorted Array → https://leetcode.com/problems/search-in-rotated-sorted-array/\n"
    "- [ ] Find Minimum in Rotated Sorted Array → https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/\n\n"
    "📖 Ôn: so sánh linear vs binary search"
)

days[13] = (
    "🧠 Phase 1: Nền tảng — Ngày 13/120\n"
    "📚 Toán tử trên bit (Bitwise Operations)\n\n"
    "📖 Thuộc lòng luỹ thừa 2 (2^1 đến 2^16, 2^32)\n\n"
    "📹 Video:\n"
    "- [ ] Bit Manipulation → https://www.youtube.com/watch?v=7jkIUgLC29I\n"
    "- [ ] Bitwise Operators → https://www.youtube.com/watch?v=d0AwjSpNXR0\n\n"
    "💻 Implement:\n"
    "- [ ] Đếm bit 1 (popcount), kiểm tra bit thứ k\n"
    "- [ ] Set/Clear/Toggle bit\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Number of 1 Bits → https://leetcode.com/problems/number-of-1-bits/\n"
    "- [ ] Single Number → https://leetcode.com/problems/single-number/"
)

days[14] = (
    "🧠 Phase 1: Nền tảng — Ngày 14/120\n"
    "📚 ÔN TẬP CUỐI PHASE 1\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Counting Bits → https://leetcode.com/problems/counting-bits/\n"
    "- [ ] Reverse Bits → https://leetcode.com/problems/reverse-bits/\n"
    "- [ ] Missing Number → https://leetcode.com/problems/missing-number/\n\n"
    "📝 Ôn tập:\n"
    "- [ ] Big-O cheat sheet → http://bigocheatsheet.com/\n"
    "- [ ] Review tất cả cấu trúc dữ liệu đã học\n"
    "- [ ] Làm ít nhất 1 bài LeetCode mỗi dạng"
)

# Phase 2: Trees & Sorting (Days 15-28)
days[15] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 15/120\n"
    "📚 Trees: Giới thiệu & Binary Trees\n\n"
    "📹 Video:\n"
    "- [ ] Trees - Harvard → https://www.youtube.com/watch?v=oSWTXtMglNU\n"
    "- [ ] Tree Traversal → https://www.youtube.com/watch?v=9RHO6jU--GU\n\n"
    "💻 Implement:\n"
    "- [ ] Class Node với left, right, value\n"
    "- [ ] Binary Tree cơ bản"
)

days[16] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 16/120\n"
    "📚 Binary Search Tree (BST)\n\n"
    "📹 Video:\n"
    "- [ ] BST - Harvard → https://www.youtube.com/watch?v=76dhtgZt38A\n"
    "- [ ] BST - CS61B → https://archive.org/details/ucberkeley_webcast_gxV26e7q8FY\n"
    "- [ ] Insert → https://www.youtube.com/watch?v=wcIRPqTR3Kc\n"
    "- [ ] Delete → https://www.youtube.com/watch?v=gcULXE7ViZw\n"
    "- [ ] Review: BST in 4min → https://youtu.be/pSjxV6L2tCQ\n\n"
    "💻 Implement: BST insert, search, delete, findMin, findMax"
)

days[17] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 17/120\n"
    "📚 BST Practice\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Validate BST → https://leetcode.com/problems/validate-binary-search-tree/\n"
    "- [ ] LCA of BST → https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/\n"
    "- [ ] Kth Smallest in BST → https://leetcode.com/problems/kth-smallest-element-in-a-bst/"
)

days[18] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 18/120\n"
    "📚 Heap / Priority Queue\n\n"
    "📹 Video:\n"
    "- [ ] Heap → https://www.coursera.org/lecture/data-structures/heaps-bwQGB\n"
    "- [ ] Heap CS61B → https://archive.org/details/ucberkeley_webcast_3otGq7V9a5o\n"
    "- [ ] Priority Queue → https://www.coursera.org/lecture/data-structures/priority-queues-Ci8Qd\n\n"
    "💻 Implement:\n"
    "- [ ] Binary Heap: insert, extractMin, heapify\n"
    "- [ ] Priority Queue dùng heap"
)

days[19] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 19/120\n"
    "📚 Heap Practice\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Kth Largest Element → https://leetcode.com/problems/kth-largest-element-in-an-array/\n"
    "- [ ] Top K Frequent → https://leetcode.com/problems/top-k-frequent-elements/\n"
    "- [ ] Find Median from Data Stream → https://leetcode.com/problems/find-median-from-data-stream/\n\n"
    "💻 Implement Heap Sort"
)

days[20] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 20/120\n"
    "📚 Balanced Trees\n\n"
    "📖 Đọc:\n"
    "- [ ] AVL Trees → https://en.wikipedia.org/wiki/AVL_tree\n"
    "- [ ] Red-Black Trees → https://en.wikipedia.org/wiki/Red-black_tree\n\n"
    "📹 Video:\n"
    "- [ ] AVL → https://www.youtube.com/watch?v=FNeL18KsWPc\n"
    "- [ ] Red-Black → https://www.youtube.com/watch?v=qvZGUFHWChY\n\n"
    "⚠️ Chỉ hiểu khái niệm, không cần implement"
)

days[21] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 21/120\n"
    "📚 Tree Traversal\n\n"
    "📹 Video:\n"
    "- [ ] Binary Tree Traversals → https://www.youtube.com/watch?v=9RHO6jU--GU\n"
    "- [ ] CS61B Traversal → https://archive.org/details/ucberkeley_webcast_5cU1ILGy6dM\n"
    "- [ ] BFS & DFS Tree → https://www.youtube.com/watch?v=uWL6FJhq5fM\n\n"
    "💻 Implement:\n"
    "- [ ] Pre-order (đệ quy + iterative)\n"
    "- [ ] In-order, Post-order\n"
    "- [ ] Level-order (BFS dùng queue)"
)

days[22] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 22/120\n"
    "📚 Tree Traversal Practice\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Binary Tree Inorder → https://leetcode.com/problems/binary-tree-inorder-traversal/\n"
    "- [ ] Level Order → https://leetcode.com/problems/binary-tree-level-order-traversal/\n"
    "- [ ] Max Depth → https://leetcode.com/problems/maximum-depth-of-binary-tree/\n"
    "- [ ] Diameter of Tree → https://leetcode.com/problems/diameter-of-binary-tree/\n"
    "- [ ] Invert Tree → https://leetcode.com/problems/invert-binary-tree/\n"
    "- [ ] Same Tree → https://leetcode.com/problems/same-tree/"
)

days[23] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 23/120\n"
    "📚 Sorting: Selection & Insertion Sort\n\n"
    "📹 Video:\n"
    "- [ ] Selection Sort → https://www.coursera.com/lecture/algorithms-part1/selection-sort-UQxHc\n"
    "- [ ] Insertion Sort → https://www.coursera.com/lecture/algorithms-part1/insertion-sort-bkAt3\n\n"
    "💻 Implement:\n"
    "- [ ] Selection Sort\n"
    "- [ ] Insertion Sort\n"
    "- [ ] So sánh O(n²) vs O(n) khi gần sorted"
)

days[24] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 24/120\n"
    "📚 Sorting: Quicksort\n\n"
    "📹 Video:\n"
    "- [ ] Quicksort → https://www.coursera.com/lecture/algorithms-part1/quicksort-vjvxc\n"
    "- [ ] CS61B → https://archive.org/details/ucberkeley_webcast_B6Oe5l2MoGU\n"
    "- [ ] 3-way Quicksort → https://www.coursera.com/lecture/algorithms-part1/3-way-quicksort-8DnyA\n\n"
    "💻 Implement:\n"
    "- [ ] Quicksort Lomuto partition\n"
    "- [ ] Quicksort Hoare partition\n"
    "- [ ] O(n log n) average vs O(n²) worst case"
)

days[25] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 25/120\n"
    "📚 Sorting: Mergesort\n\n"
    "📹 Video:\n"
    "- [ ] Mergesort → https://www.coursera.com/learn/algorithms-part1/home/week/3\n"
    "- [ ] CS61B → https://archive.org/details/ucberkeley_webcast_0f7UXMEaCtY\n"
    "- [ ] Bottom-up → https://www.coursera.com/lecture/algorithms-part1/bottom-up-mergesort-QwO2C\n\n"
    "💻 Implement:\n"
    "- [ ] Mergesort (top-down)\n"
    "- [ ] Mergesort (bottom-up)\n"
    "- [ ] So sánh Quicksort vs Mergesort"
)

days[26] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 26/120\n"
    "📚 Sorting Review\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Sort Colors → https://leetcode.com/problems/sort-colors/\n"
    "- [ ] Merge Sorted Array → https://leetcode.com/problems/merge-sorted-array/\n\n"
    "📖 Ôn: Bảng so sánh Big-O tất cả sorting algorithms"
)

days[27] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 27/120\n"
    "📚 Ôn tập Trees + Sorting\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Binary Tree Max Path Sum → https://leetcode.com/problems/binary-tree-maximum-path-sum/\n\n"
    "📝 Viết lại từ đầu (không nhìn code):\n"
    "- [ ] BST\n"
    "- [ ] Quicksort\n"
    "- [ ] Mergesort"
)

days[28] = (
    "🌳 Phase 2: Trees & Sorting — Ngày 28/120\n"
    "📚 ÔN TẬP CUỐI PHASE 2\n\n"
    "📝 Kiểm tra:\n"
    "- [ ] 4 cách duyệt cây (pre, in, post, level)\n"
    "- [ ] BST vs Array vs Linked List\n"
    "- [ ] Heap O(log n) insert/extractMin\n"
    "- [ ] Sorting stability\n"
    "- [ ] Time complexity mỗi algorithm\n\n"
    "🧪 Làm 2 bài Medium về Trees + Sorting"
)

# Phase 3: Graphs (Days 29-42)
days[29] = (
    "📊 Phase 3: Đồ thị — Ngày 29/120\n"
    "📚 Graphs: Giới thiệu & Biểu diễn\n\n"
    "📹 Video:\n"
    "- [ ] Graphs CS61B → https://archive.org/details/ucberkeley_webcast_gRe2l1zHjM0\n"
    "- [ ] Graph Rep → https://www.coursera.org/lecture/data-structures/graphs-0nXQT\n\n"
    "💻 Implement:\n"
    "- [ ] Adjacency Matrix\n"
    "- [ ] Adjacency List\n"
    "- [ ] So sánh 2 cách biểu diễn"
)

days[30] = (
    "📊 Phase 3: Đồ thị — Ngày 30/120\n"
    "📚 Graphs: BFS\n\n"
    "📹 Video:\n"
    "- [ ] BFS Harvard → https://www.youtube.com/watch?v=oDqjPvD54Ss\n"
    "- [ ] BFS CS61B → https://archive.org/details/ucberkeley_webcast_OQ7QfTlw_4A\n"
    "- [ ] BFS MIT → https://www.youtube.com/watch?v=s-CYnVz-uh4\n\n"
    "💻 Implement:\n"
    "- [ ] BFS dùng queue\n"
    "- [ ] Shortest path (unweighted)\n"
    "- [ ] Connected components"
)

days[31] = (
    "📊 Phase 3: Đồ thị — Ngày 31/120\n"
    "📚 Graphs: DFS\n\n"
    "📹 Video:\n"
    "- [ ] DFS CS61B → https://archive.org/details/ucberkeley_webcast_4vH3l1j8OHw\n"
    "- [ ] DFS MIT → https://www.youtube.com/watch?v=AfSk24UTFS8\n\n"
    "💻 Implement:\n"
    "- [ ] DFS đệ quy\n"
    "- [ ] DFS iterative (dùng stack)\n"
    "- [ ] Cycle detection trong directed graph"
)

days[32] = (
    "📊 Phase 3: Đồ thị — Ngày 32/120\n"
    "📚 BFS & DFS Practice\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Number of Islands → https://leetcode.com/problems/number-of-islands/\n"
    "- [ ] Clone Graph → https://leetcode.com/problems/clone-graph/\n"
    "- [ ] Course Schedule → https://leetcode.com/problems/course-schedule/"
)

days[33] = (
    "📊 Phase 3: Đồ thị — Ngày 33/120\n"
    "📚 Topological Sort\n\n"
    "📹 Video:\n"
    "- [ ] Topo Sort CS61B → https://archive.org/details/ucberkeley_webcast_BV7nA77iyLI\n"
    "- [ ] MIT → https://www.youtube.com/watch?v=AfSk24UTFS8\n\n"
    "💻 Implement:\n"
    "- [ ] Topo Sort dùng DFS\n"
    "- [ ] Kahn's Algorithm (BFS)\n"
    "- [ ] Dependency resolution"
)

days[34] = (
    "📊 Phase 3: Đồ thị — Ngày 34/120\n"
    "📚 Dijkstra\n\n"
    "📹 Video:\n"
    "- [ ] Dijkstra CS61B → https://archive.org/details/ucberkeley_webcast_8m8ncl7pBug\n"
    "- [ ] MIT → https://www.youtube.com/watch?v=NSHizBK9JD8&t=1731s\n\n"
    "💻 Implement:\n"
    "- [ ] Dijkstra dùng priority queue\n"
    "- [ ] Shortest path giữa 2 nodes"
)

days[35] = (
    "📊 Phase 3: Đồ thị — Ngày 35/120\n"
    "📚 Bellman-Ford & Floyd-Warshall\n\n"
    "📹 Video:\n"
    "- [ ] Bellman-Ford → https://www.youtube.com/watch?v=lyw4FaxrwHg\n"
    "- [ ] Floyd-Warshall → https://www.youtube.com/watch?v=4OQeCuLYB-U\n\n"
    "💻 Implement Bellman-Ford\n"
    "📝 So sánh Dijkstra vs Bellman-Ford vs Floyd-Warshall"
)

days[36] = (
    "📊 Phase 3: Đồ thị — Ngày 36/120\n"
    "📚 Minimum Spanning Tree\n\n"
    "📹 Video:\n"
    "- [ ] Kruskal → https://archive.org/details/ucberkeley_webcast_7qwr0KQGBqg\n"
    "- [ ] Prim → https://www.coursera.org/lecture/algorithms-part2/prims-algorithm-e5uCJ\n\n"
    "💻 Implement:\n"
    "- [ ] Kruskal (Union-Find)\n"
    "- [ ] Prim (priority queue)"
)

days[37] = (
    "📊 Phase 3: Đồ thị — Ngày 37/120\n"
    "📚 Union-Find\n\n"
    "📹 Video:\n"
    "- [ ] Union-Find CS61B → https://archive.org/details/ucberkeley_webcast_qb0BeO2C1Lw\n"
    "- [ ] Coursera → https://www.coursera.org/lecture/data-structures/union-find-3qLtn\n\n"
    "💻 Implement: find, union, connected, path compression"
)

days[38] = (
    "📊 Phase 3: Đồ thị — Ngày 38/120\n"
    "📚 Graphs Practice\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Connected Components → https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/\n"
    "- [ ] Pacific Atlantic → https://leetcode.com/problems/pacific-atlantic-water-flow/\n"
    "- [ ] Word Ladder → https://leetcode.com/problems/word-ladder/"
)

days[39] = (
    "📊 Phase 3: Đồ thị — Ngày 39/120\n"
    "📚 Graphs: Advanced\n\n"
    "📹 Video:\n"
    "- [ ] Kosaraju SCC → https://www.youtube.com/watch?v=RpgcYH7U4qA\n"
    "- [ ] A* Search → https://www.youtube.com/watch?v=ySN5Wnu88nE\n\n"
    "💻 Implement Kosaraju (SCC)"
)

days[40] = (
    "📊 Phase 3: Đồ thị — Ngày 40/120\n"
    "📚 Graphs Practice (tiếp)\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Alien Dictionary → https://leetcode.com/problems/alien-dictionary/\n"
    "- [ ] Cheapest Flights → https://leetcode.com/problems/cheapest-flights-within-k-stops/\n"
    "- [ ] Network Delay Time → https://leetcode.com/problems/network-delay-time/"
)

days[41] = (
    "📊 Phase 3: Đồ thị — Ngày 41/120\n"
    "📚 Ôn tập Graphs\n\n"
    "📝 Tổng kết:\n"
    "- [ ] BFS vs DFS: khi nào dùng?\n"
    "- [ ] Dijkstra vs Bellman-Ford\n"
    "- [ ] Topological Sort ứng dụng\n"
    "- [ ] MST (Kruskal vs Prim)\n"
    "- [ ] Union-Find ứng dụng\n\n"
    "💻 Viết lại: BFS, DFS, Dijkstra, Topo Sort, Union-Find"
)

days[42] = (
    "📊 Phase 3: Đồ thị — Ngày 42/120\n"
    "📚 ÔN TẬP CUỐI PHASE 3\n\n"
    "🧪 Làm ít nhất 2 bài Medium về Graph\n"
    "- [ ] 1 bài BFS\n"
    "- [ ] 1 bài DFS/Dijkstra/Topo\n\n"
    "📖 Ôn lại:\n"
    "- [ ] Graph representations\n"
    "- [ ] Time & Space complexity từng thuật toán\n"
    "- [ ] Lưu ý khi implement graph trong interview"
)

# Phase 4: Kỹ thuật nâng cao (Days 43-56)
days[43] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 43/120\n"
    "📚 Recursion (Đệ quy)\n\n"
    "📹 Video:\n"
    "- [ ] Lecture 8 Stanford → https://www.youtube.com/watch?v=gl3emqCuueQ\n"
    "- [ ] Lecture 9 Stanford → https://www.youtube.com/watch?v=uFJhEPrbycQ\n"
    "- [ ] 5 Steps to Recursive Problem → https://youtu.be/ngCos392W4w\n\n"
    "💻 Implement:\n"
    "- [ ] Factorial, Fibonacci (đệ quy)\n"
    "- [ ] Binary Search (đệ quy)\n"
    "- [ ] Tower of Hanoi"
)

days[44] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 44/120\n"
    "📚 Recursion & Backtracking\n\n"
    "📹 Video:\n"
    "- [ ] Lecture 10 Stanford → https://www.youtube.com/watch?v=NdF1QDTRkck\n"
    "- [ ] Lecture 11 Stanford → https://www.youtube.com/watch?v=p-gpaIGRCQI\n\n"
    "📖 Đọc Backtracking Blueprint\n\n"
    "💻 Implement Backtracking:\n"
    "- [ ] N-Queens\n"
    "- [ ] Sudoku Solver\n"
    "- [ ] Permutations"
)

days[45] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 45/120\n"
    "📚 Recursion Practice\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Subsets → https://leetcode.com/problems/subsets/\n"
    "- [ ] Permutations → https://leetcode.com/problems/permutations/\n"
    "- [ ] Combination Sum → https://leetcode.com/problems/combination-sum/\n"
    "- [ ] Letter Combinations → https://leetcode.com/problems/letter-combinations-of-a-phone-number/\n"
    "- [ ] Generate Parentheses → https://leetcode.com/problems/generate-parentheses/"
)

days[46] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 46/120\n"
    "📚 Dynamic Programming - Giới thiệu\n\n"
    "📹 Video:\n"
    "- [ ] Skiena Intro DP → https://www.youtube.com/watch?v=wAA0AMfcJHQ\n"
    "- [ ] Skiena Edit Distance → https://www.youtube.com/watch?v=T3A4jlHlhtA\n"
    "- [ ] Tushar Roy DP → https://www.youtube.com/watch?v=vYquumk4nWw\n\n"
    "💻 Fibonacci: bottom-up vs top-down\n"
    "📝 So sánh recursion vs memoization vs tabulation"
)

days[47] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 47/120\n"
    "📚 DP Classic Problems\n\n"
    "📹 Video:\n"
    "- [ ] 0/1 Knapsack → https://www.youtube.com/watch?v=8LusJS5-AGo\n"
    "- [ ] LCS → https://www.youtube.com/watch?v=NnD96abizww\n"
    "- [ ] LIS → https://www.youtube.com/watch?v=fV-TF4OvZpk\n\n"
    "💻 Implement:\n"
    "- [ ] 0/1 Knapsack\n"
    "- [ ] Longest Common Subsequence\n"
    "- [ ] Longest Increasing Subsequence"
)

days[48] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 48/120\n"
    "📚 DP Practice\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Climbing Stairs → https://leetcode.com/problems/climbing-stairs/\n"
    "- [ ] House Robber → https://leetcode.com/problems/house-robber/\n"
    "- [ ] Coin Change → https://leetcode.com/problems/coin-change/\n"
    "- [ ] Longest Palindromic Substring → https://leetcode.com/problems/longest-palindromic-substring/\n"
    "- [ ] Maximum Product Subarray → https://leetcode.com/problems/maximum-product-subarray/"
)

days[49] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 49/120\n"
    "📚 DP Advanced\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Edit Distance → https://leetcode.com/problems/edit-distance/\n"
    "- [ ] Unique Paths → https://leetcode.com/problems/unique-paths/\n"
    "- [ ] Word Break → https://leetcode.com/problems/word-break/\n"
    "- [ ] LCS → https://leetcode.com/problems/longest-common-subsequence/\n\n"
    "💻 Pattern nhận biết bài toán DP + Tối ưu space complexity"
)

days[50] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 50/120\n"
    "📚 Object-Oriented Programming\n\n"
    "📹 Video:\n"
    "- [ ] OOP in 7min → https://www.youtube.com/watch?v=pTB0EiLXUC8\n"
    "- [ ] SOLID → https://www.youtube.com/watch?v=GtZtQ2vfFcA\n\n"
    "📖 SOLID Principles:\n"
    "- [ ] S: Single Responsibility\n"
    "- [ ] O: Open/Closed\n"
    "- [ ] L: Liskov Substitution\n"
    "- [ ] I: Interface Segregation\n"
    "- [ ] D: Dependency Inversion\n\n"
    "💻 Design class diagram + implement inheritance"
)

days[51] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 51/120\n"
    "📚 Design Patterns\n\n"
    "📹 UML Review → https://www.youtube.com/watch?v=3cmzqZzwNDM\n\n"
    "📖 Học các patterns:\n"
    "- [ ] Strategy\n"
    "- [ ] Singleton\n"
    "- [ ] Adapter\n"
    "- [ ] Decorator\n"
    "- [ ] Factory\n"
    "- [ ] Observer\n\n"
    "💻 Code ít nhất 3 patterns"
)

days[52] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 52/120\n"
    "📚 Combinatorics & Probability\n\n"
    "📖 Permutations vs Combinations\n"
    "📹 Probability Khan Academy\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Permutations → https://leetcode.com/problems/permutations/\n"
    "- [ ] Combinations → https://leetcode.com/problems/combinations/\n"
    "- [ ] Pow(x,n) → https://leetcode.com/problems/powx-n/"
)

days[53] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 53/120\n"
    "📚 NP-Completeness & Caches\n\n"
    "📖 NP-Complete → https://en.wikipedia.org/wiki/NP-completeness\n"
    "📹 Caches MIT → https://www.youtube.com/watch?v=102A6Z8jYEs\n"
    "📹 LRU Cache → https://www.youtube.com/watch?v=8-FZ0Hm5lNM\n\n"
    "💻 Implement LRU Cache\n"
    "🧪 https://leetcode.com/problems/lru-cache/"
)

days[54] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 54/120\n"
    "📚 Processes & Threads\n\n"
    "📹 Video → https://www.youtube.com/watch?v=ICjLyUx2bQs\n\n"
    "📖 Đọc:\n"
    "- [ ] Concurrency vs Parallelism\n"
    "- [ ] Mutexes & Semaphores\n"
    "- [ ] Race Conditions, Deadlocks\n\n"
    "💻 Implement Producer-Consumer"
)

days[55] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 55/120\n"
    "📚 Strings & Tries\n\n"
    "📹 String Searching MIT → https://www.youtube.com/watch?v=GTJr8OvyEVQ\n"
    "📹 Rabin-Karp → https://www.youtube.com/watch?v=H4VrKHVG5qI\n\n"
    "💻 Implement Trie: insert, search, startsWith\n\n"
    "🧪 LeetCode:\n"
    "- [ ] Implement Trie → https://leetcode.com/problems/implement-trie-prefix-tree/\n"
    "- [ ] Longest Common Prefix → https://leetcode.com/problems/longest-common-prefix/"
)

days[56] = (
    "🔬 Phase 4: Kỹ thuật nâng cao — Ngày 56/120\n"
    "📚 ÔN TẬP CUỐI PHASE 4\n\n"
    "📝 Tổng kết:\n"
    "- [ ] Recursion vs DP: khi nào dùng?\n"
    "- [ ] 5 patterns DP thường gặp\n"
    "- [ ] SOLID & Design Patterns\n"
    "- [ ] LRU Cache implementation\n\n"
    "🧪 Làm 1 DP Medium + 1 Strings Medium + 1 Trie"
)

# Phase 5: System Design (Days 57-70)
days[57] = (
    "🏗️ Phase 5: System Design — Ngày 57/120\n"
    "📚 Scalability Fundamentals\n\n"
    "📹 Video:\n"
    "- [ ] Scalability → https://www.youtube.com/watch?v=-W9F__D3oY4\n"
    "- [ ] System Design Intro → https://www.youtube.com/watch?v=Y-Gl4HEsU5E\n\n"
    "📖 System Design Primer → https://github.com/donnemartin/system-design-primer"
)

days[58] = (
    "🏗️ Phase 5: System Design — Ngày 58/120\n"
    "📚 Scalability Concepts\n\n"
    "📖 Đọc:\n"
    "- [ ] Vertical vs Horizontal Scaling\n"
    "- [ ] Load Balancing\n"
    "- [ ] Database Replication\n"
    "- [ ] Caching (CDN, Redis)\n\n"
    "📹 Load Balancing → https://www.youtube.com/watch?v=K0Ta65OqQkY\n\n"
    "💻 Vẽ diagram: Single → Multi-server"
)

days[59] = (
    "🏗️ Phase 5: System Design — Ngày 59/120\n"
    "📚 Databases & Storage\n\n"
    "📹 Database Indexes → https://www.youtube.com/watch?v=fsG1XaZEaps\n"
    "📹 SQL vs NoSQL → https://www.youtube.com/watch?v=QwevGzVu_zk\n"
    "📹 CAP Theorem → https://www.youtube.com/watch?v=BHQCMSV_L7Y\n\n"
    "📖 CAP Theorem (giải thích) → http://ksat.me/a-plain-english-introduction-to-cap-theorem/"
)

days[60] = (
    "🏗️ Phase 5: System Design — Ngày 60/120\n"
    "📚 Distributed Systems\n\n"
    "📹 MIT 6.824 → https://www.youtube.com/watch?v=cQP8WApzIQQ\n\n"
    "📖 Đọc:\n"
    "- [ ] Paxos & Raft\n"
    "- [ ] NoSQL Patterns → http://horicky.blogspot.com/2009/11/nosql-patterns.html\n"
    "- [ ] MapReduce"
)

days[61] = (
    "🏗️ Phase 5: System Design — Ngày 61/120\n"
    "📚 Case Study: URL Shortener\n\n"
    "💻 Thiết kế:\n"
    "- [ ] Requirements\n"
    "- [ ] Tính toán dung lượng\n"
    "- [ ] Database schema\n"
    "- [ ] API design\n"
    "- [ ] High-level diagram\n\n"
    "🎯 Key: hashing, base62 encoding, caching"
)

days[62] = (
    "🏗️ Phase 5: System Design — Ngày 62/120\n"
    "📚 Case Study: Web Crawler\n\n"
    "💻 Thiết kế:\n"
    "- [ ] BFS crawling\n"
    "- [ ] URL dedup (Bloom Filter)\n"
    "- [ ] Distributed crawling\n"
    "- [ ] Rate limiting\n\n"
    "🎯 Key: BFS, Bloom Filter, Distributed Systems"
)

days[63] = (
    "🏗️ Phase 5: System Design — Ngày 63/120\n"
    "📚 Case Study: Chat System\n\n"
    "💻 Thiết kế:\n"
    "- [ ] WebSockets vs Polling\n"
    "- [ ] Message storage\n"
    "- [ ] Online presence\n"
    "- [ ] Group chat\n\n"
    "🎯 Key: WebSocket, message queue, real-time sync"
)

days[64] = (
    "🏗️ Phase 5: System Design — Ngày 64/120\n"
    "📚 Case Study: Social Media Feed\n\n"
    "💻 Thiết kế:\n"
    "- [ ] Fan-out on write vs read\n"
    "- [ ] Timeline generation\n"
    "- [ ] Feed ranking\n"
    "- [ ] Push vs Pull\n\n"
    "🎯 Key: Fan-out, caching, ranking"
)

days[65] = (
    "🏗️ Phase 5: System Design — Ngày 65/120\n"
    "📚 Case Study: Rate Limiter\n\n"
    "💻 Thiết kế:\n"
    "- [ ] Token Bucket vs Leaky Bucket\n"
    "- [ ] Distributed rate limiting\n"
    "- [ ] Redis-based\n\n"
    "🎯 Key: Rate limiting algorithms, sliding window"
)

days[66] = (
    "🏗️ Phase 5: System Design — Ngày 66/120\n"
    "📚 Design Patterns cho System\n\n"
    "📖 Đọc:\n"
    "- [ ] Consistent Hashing\n"
    "- [ ] Bloom Filters → https://en.wikipedia.org/wiki/Bloom_filter\n"
    "- [ ] Merkle Trees\n"
    "- [ ] Quorum & Leader Election\n\n"
    "💻 Implement Bloom Filter + Consistent Hashing"
)

days[67] = (
    "🏗️ Phase 5: System Design — Ngày 67/120\n"
    "📚 Case Study: YouTube\n\n"
    "💻 Thiết kế:\n"
    "- [ ] Video upload pipeline\n"
    "- [ ] Transcoding\n"
    "- [ ] CDN & caching\n"
    "- [ ] Recommendations\n\n"
    "🎯 Key: CDN, transcoding, microservices"
)

days[68] = (
    "🏗️ Phase 5: System Design — Ngày 68/120\n"
    "📚 Case Study: Uber\n\n"
    "💻 Thiết kế:\n"
    "- [ ] Location tracking\n"
    "- [ ] Matching algorithm\n"
    "- [ ] Pricing engine\n"
    "- [ ] Real-time updates\n\n"
    "🎯 Key: Geohashing, quad tree, real-time"
)

days[69] = (
    "🏗️ Phase 5: System Design — Ngày 69/120\n"
    "📚 Practice: Tự design\n\n"
    "💻 Tự thiết kế:\n"
    "- [ ] Design a Parking Lot\n"
    "- [ ] Design a Library System\n\n"
    "📖 Đọc Latency Numbers:\n"
    "→ http://everythingisdata.wordpress.com/2009/10/17/numbers-everyone-should-know/"
)

days[70] = (
    "🏗️ Phase 5: System Design — Ngày 70/120\n"
    "📚 ÔN TẬP CUỐI PHASE 5\n\n"
    "📝 Tổng kết:\n"
    "- [ ] CAP Theorem: CP, AP, CA?\n"
    "- [ ] Consistent Hashing?\n"
    "- [ ] SQL vs NoSQL?\n"
    "- [ ] Các bước design trong interview\n\n"
    "💻 Thuộc lòng latency numbers + Vẽ diagram"
)

# Phase 6: Coding Practice (Days 71-84)
days[71] = (
    "💻 Phase 6: Coding Practice — Ngày 71/120\n"
    "📚 LeetCode: Arrays & Hashing\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Two Sum → https://leetcode.com/problems/two-sum/\n"
    "- [ ] Longest Consecutive Sequence → https://leetcode.com/problems/longest-consecutive-sequence/\n"
    "- [ ] Majority Element → https://leetcode.com/problems/majority-element/\n"
    "- [ ] Move Zeroes → https://leetcode.com/problems/move-zeroes/"
)

days[72] = (
    "💻 Phase 6: Coding Practice — Ngày 72/120\n"
    "📚 LeetCode: Two Pointers & Sliding Window\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] 3Sum → https://leetcode.com/problems/3sum/\n"
    "- [ ] Container With Most Water → https://leetcode.com/problems/container-with-most-water/\n"
    "- [ ] Longest Substring Without Repeating → https://leetcode.com/problems/longest-substring-without-repeating-characters/\n"
    "- [ ] Minimum Window Substring → https://leetcode.com/problems/minimum-window-substring/"
)

days[73] = (
    "💻 Phase 6: Coding Practice — Ngày 73/120\n"
    "📚 LeetCode: Stacks & Queues\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Daily Temperatures → https://leetcode.com/problems/daily-temperatures/\n"
    "- [ ] Largest Rectangle in Histogram → https://leetcode.com/problems/largest-rectangle-in-histogram/\n"
    "- [ ] Car Fleet → https://leetcode.com/problems/car-fleet/"
)

days[74] = (
    "💻 Phase 6: Coding Practice — Ngày 74/120\n"
    "📚 LeetCode: Linked Lists\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Reorder List → https://leetcode.com/problems/reorder-list/\n"
    "- [ ] Copy List with Random Pointer → https://leetcode.com/problems/copy-list-with-random-pointer/\n"
    "- [ ] Find the Duplicate Number → https://leetcode.com/problems/find-the-duplicate-number/"
)

days[75] = (
    "💻 Phase 6: Coding Practice — Ngày 75/120\n"
    "📚 LeetCode: Binary Trees\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Construct Tree from Preorder and Inorder → https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/\n"
    "- [ ] Right Side View → https://leetcode.com/problems/binary-tree-right-side-view/\n"
    "- [ ] Count Good Nodes → https://leetcode.com/problems/count-good-nodes-in-binary-tree/"
)

days[76] = (
    "💻 Phase 6: Coding Practice — Ngày 76/120\n"
    "📚 LeetCode: Heaps\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Task Scheduler → https://leetcode.com/problems/task-scheduler/\n"
    "- [ ] Design Twitter → https://leetcode.com/problems/design-twitter/\n"
    "- [ ] K Closest Points → https://leetcode.com/problems/k-closest-points-to-origin/"
)

days[77] = (
    "💻 Phase 6: Coding Practice — Ngày 77/120\n"
    "📚 LeetCode: Graphs\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Surrounded Regions → https://leetcode.com/problems/surrounded-regions/\n"
    "- [ ] Rotting Oranges → https://leetcode.com/problems/rotting-oranges/\n"
    "- [ ] Course Schedule II → https://leetcode.com/problems/course-schedule-ii/\n"
    "- [ ] Redundant Connection → https://leetcode.com/problems/redundant-connection/"
)

days[78] = (
    "💻 Phase 6: Coding Practice — Ngày 78/120\n"
    "📚 LeetCode: Dynamic Programming\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Palindromic Substrings → https://leetcode.com/problems/palindromic-substrings/\n"
    "- [ ] Decode Ways → https://leetcode.com/problems/decode-ways/\n"
    "- [ ] Coin Change II → https://leetcode.com/problems/coin-change-ii/\n"
    "- [ ] Partition Equal Subset Sum → https://leetcode.com/problems/partition-equal-subset-sum/"
)

days[79] = (
    "💻 Phase 6: Coding Practice — Ngày 79/120\n"
    "📚 LeetCode: Intervals\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Merge Intervals → https://leetcode.com/problems/merge-intervals/\n"
    "- [ ] Non-overlapping Intervals → https://leetcode.com/problems/non-overlapping-intervals/\n"
    "- [ ] Meeting Rooms II → https://leetcode.com/problems/meeting-rooms-ii/"
)

days[80] = (
    "💻 Phase 6: Coding Practice — Ngày 80/120\n"
    "📚 LeetCode: Greedy\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Jump Game → https://leetcode.com/problems/jump-game/\n"
    "- [ ] Jump Game II → https://leetcode.com/problems/jump-game-ii/\n"
    "- [ ] Gas Station → https://leetcode.com/problems/gas-station/"
)

days[81] = (
    "💻 Phase 6: Coding Practice — Ngày 81/120\n"
    "📚 LeetCode: Advanced Graphs\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Min Cost to Connect All Points → https://leetcode.com/problems/min-cost-to-connect-all-points/\n"
    "- [ ] Network Delay Time → https://leetcode.com/problems/network-delay-time/\n"
    "- [ ] Swim in Rising Water → https://leetcode.com/problems/swim-in-rising-water/"
)

days[82] = (
    "💻 Phase 6: Coding Practice — Ngày 82/120\n"
    "📚 LeetCode: Tries & Bit Manipulation\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Design Add and Search Words → https://leetcode.com/problems/design-add-and-search-words-data-structure/\n"
    "- [ ] Word Search II → https://leetcode.com/problems/word-search-ii/\n"
    "- [ ] Sum of Two Integers → https://leetcode.com/problems/sum-of-two-integers/\n"
    "- [ ] Reverse Integer → https://leetcode.com/problems/reverse-integer/"
)

days[83] = (
    "💻 Phase 6: Coding Practice — Ngày 83/120\n"
    "📚 LeetCode: Math & Geometry\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] Rotate Image → https://leetcode.com/problems/rotate-image/\n"
    "- [ ] Spiral Matrix → https://leetcode.com/problems/spiral-matrix/\n"
    "- [ ] Set Matrix Zeroes → https://leetcode.com/problems/set-matrix-zeroes/\n"
    "- [ ] Happy Number → https://leetcode.com/problems/happy-number/"
)

days[84] = (
    "💻 Phase 6: Coding Practice — Ngày 84/120\n"
    "📚 ÔN TẬP CUỐI PHASE 6\n\n"
    "🧪 Mock Test: 3 bài trong 45 phút\n"
    "- [ ] 1 Easy (5 phút)\n"
    "- [ ] 2 Medium (20 phút mỗi bài)\n\n"
    "📝 Review patterns + Time complexity"
)

# Phase 7: Mock Interviews (Days 85-98)
days[85] = (
    "🎯 Phase 7: Mock Interviews — Ngày 85/120\n"
    "📚 Behavioral Questions\n\n"
    "📖 Chuẩn bị câu trả lời:\n"
    "- [ ] Tell me about yourself (30s, 60s, 120s)\n"
    "- [ ] Why do you want to work here?\n"
    "- [ ] A challenge you overcame\n"
    "- [ ] A conflict you resolved\n"
    "- [ ] Strengths/Weaknesses\n\n"
    "💻 Ghi âm và nghe lại"
)

days[86] = (
    "🎯 Phase 7: Mock Interviews — Ngày 86/120\n"
    "📚 Company Research\n\n"
    "Chọn công ty mục tiêu:\n"
    "- [ ] Đọc về culture\n"
    "- [ ] Quy trình phỏng vấn\n"
    "- [ ] Glassdoor reviews\n"
    "- [ ] Tech stack\n"
    "- [ ] Leadership Principles"
)

days[87] = (
    "🎯 Phase 7: Mock Interviews — Ngày 87/120\n"
    "📚 Mock: Arrays & Strings\n\n"
    "🧪 Tự mock (30 phút mỗi câu):\n"
    "- [ ] Longest Substring Without Repeating\n"
    "- [ ] Trapping Rain Water\n"
    "- [ ] Longest Palindromic Substring\n\n"
    "Sau mỗi câu: think aloud → tối ưu → test edge cases"
)

days[88] = (
    "🎯 Phase 7: Mock Interviews — Ngày 88/120\n"
    "📚 Mock: Trees & Graphs\n\n"
    "🧪 Tự mock:\n"
    "- [ ] Binary Tree Max Path Sum\n"
    "- [ ] Word Ladder\n"
    "- [ ] Number of Islands\n\n"
    "Sau mỗi câu: nói to solution → vẽ diagram → optimize"
)

days[89] = (
    "🎯 Phase 7: Mock Interviews — Ngày 89/120\n"
    "📚 Mock: DP & Design\n\n"
    "🧪 Tự mock:\n"
    "- [ ] LIS (DP)\n"
    "- [ ] Design URL Shortener\n"
    "- [ ] Coin Change (DP)\n\n"
    "Thực hành: approach → code → test → analyze"
)

days[90] = (
    "🎯 Phase 7: Mock Interviews — Ngày 90/120\n"
    "📚 Review: Coding Patterns\n\n"
    "📖 Ôn tập:\n"
    "- [ ] Sliding Window, Two Pointers\n"
    "- [ ] Fast & Slow Pointers\n"
    "- [ ] Merge Intervals, Cyclic Sort\n"
    "- [ ] Tree BFS, Tree DFS\n"
    "- [ ] Two Heaps, Subsets\n"
    "- [ ] Modified Binary Search\n"
    "- [ ] Top K Elements, K-way Merge\n"
    "- [ ] Backtracking, DP patterns"
)

days[91] = (
    "🎯 Phase 7: Mock Interviews — Ngày 91/120\n"
    "📚 Full Mock Interview #1 (1 tiếng)\n\n"
    "- [ ] Câu 1 (15 phút): Easy-Medium\n"
    "- [ ] Câu 2 (25 phút): Medium-Hard\n"
    "- [ ] Q&A (10 phút): Behavioral\n"
    "- [ ] Q&A (10 phút): Hỏi interviewer\n\n"
    "📝 Ghi chép điểm mạnh, yếu"
)

days[92] = (
    "🎯 Phase 7: Mock Interviews — Ngày 92/120\n"
    "📚 Full Mock Interview #2\n\n"
    "🧪 1 tiếng:\n"
    "- [ ] 2 coding (40 phút)\n"
    "- [ ] 1 system design (20 phút)\n"
    "- [ ] Behavioral\n\n"
    "📝 Ghi âm, xác định weak spots"
)

days[93] = (
    "🎯 Phase 7: Mock Interviews — Ngày 93/120\n"
    "📚 Weak Areas: Focus Day 1\n\n"
    "Xác định yếu nhất → tập trung:\n"
    "- [ ] Chọn 1 topic yếu (DP? Graphs? Trees?)\n"
    "- [ ] Ôn lại lý thuyết\n"
    "- [ ] Làm 3 bài Medium\n"
    "- [ ] Đọc solutions khác\n"
    "- [ ] Viết lại code 2 lần"
)

days[94] = (
    "🎯 Phase 7: Mock Interviews — Ngày 94/120\n"
    "📚 Weak Areas: Focus Day 2\n\n"
    "- [ ] Chọn topic yếu tiếp theo\n"
    "- [ ] Ôn lý thuyết\n"
    "- [ ] Làm 3 bài Medium\n"
    "- [ ] So sánh solutions\n"
    "- [ ] Tự giải lại từ đầu (không nhìn)"
)

days[95] = (
    "🎯 Phase 7: Mock Interviews — Ngày 95/120\n"
    "📚 Speed Practice\n\n"
    "🧪 Thời gian giới hạn:\n"
    "- [ ] 3 Easy: 5 phút mỗi bài\n"
    "- [ ] 2 Medium: 15 phút mỗi bài\n"
    "- [ ] 1 Hard: 25 phút (optional)\n\n"
    "📝 Ghi lại thời gian hoàn thành"
)

days[96] = (
    "🎯 Phase 7: Mock Interviews — Ngày 96/120\n"
    "📚 System Design & Behavioral Review\n\n"
    "📖 Ôn:\n"
    "- [ ] System Design checklist\n"
    "- [ ] STAR method\n"
    "- [ ] Latency numbers\n"
    "- [ ] CAP Theorem refresher\n\n"
    "💻 Practice: Design Instagram, Design Dropbox"
)

days[97] = (
    "🎯 Phase 7: Mock Interviews — Ngày 97/120\n"
    "📚 Company-Specific Prep\n\n"
    "Giải Top Interview Questions của công ty mục tiêu:\n"
    "→ https://leetcode.com/problem-list/top-google-questions/\n"
    "→ https://leetcode.com/problem-list/top-amazon-questions/\n"
    "→ https://leetcode.com/problem-list/top-facebook-questions/\n\n"
    "💻 Làm ít nhất 5 câu"
)

days[98] = (
    "🎯 Phase 7: Mock Interviews — Ngày 98/120\n"
    "📚 ÔN TẬP CUỐI PHASE 7\n\n"
    "📝 Tổng kết:\n"
    "- [ ] Review mock interview mistakes\n"
    "- [ ] Ôn coding patterns\n"
    "- [ ] Tối ưu think aloud\n"
    "- [ ] Chuẩn bị 3 câu hỏi cho interviewer\n\n"
    "🧪 2 Medium + 1 Easy (30 phút)"
)

# Phase 8: Final Sprint (Days 99-120)
days[99] = (
    "🚀 Phase 8: Final Sprint — Ngày 99/120\n"
    "📚 Tổng ôn: Data Structures\n\n"
    "📝 Ôn nhanh từng cấu trúc:\n"
    "- [ ] Array & Dynamic Array\n"
    "- [ ] Linked List (Singly, Doubly)\n"
    "- [ ] Stack & Queue\n"
    "- [ ] Hash Table\n"
    "- [ ] Heap (Min/Max)\n"
    "- [ ] Tree (BST, Balanced)\n"
    "- [ ] Graph (Adj Matrix/List)\n"
    "- [ ] Trie\n\n"
    "Mỗi cấu trúc: Operations, Time Complexity, Khi nào dùng?"
)

days[100] = (
    "🚀 Phase 8: Final Sprint — Ngày 100/120\n"
    "📚 Tổng ôn: Algorithms\n\n"
    "📝 Ôn nhanh:\n"
    "- [ ] Sorting: Selection, Insertion, Merge, Quick, Heap\n"
    "- [ ] BFS & DFS (Tree & Graph)\n"
    "- [ ] Topological Sort\n"
    "- [ ] Dijkstra, Bellman-Ford, Floyd-Warshall\n"
    "- [ ] MST: Kruskal, Prim\n"
    "- [ ] DP: Knapsack, LCS, LIS, Edit Distance\n"
    "- [ ] Binary Search (4 variants)\n"
    "- [ ] Bit Manipulation\n\n"
    "🧪 Code nhanh: Binary Search, Quicksort, BFS, Dijkstra"
)

days[101] = (
    "🚀 Phase 8: Final Sprint — Ngày 101/120\n"
    "📚 LeetCode Countdown: Ngày 1\n\n"
    "🧪 Giải 4 bài:\n"
    "- [ ] 1 Easy (5 phút)\n"
    "- [ ] 2 Medium (15 phút mỗi bài)\n"
    "- [ ] 1 Hard (25 phút)\n\n"
    "📝 Ghi patterns, lỗi sai, time management"
)

days[102] = (
    "🚀 Phase 8: Final Sprint — Ngày 102/120\n"
    "📚 LeetCode Countdown: Ngày 2\n\n"
    "🧪 4 bài mới:\n"
    "- [ ] Random 1 Easy\n"
    "- [ ] Random 2 Medium\n"
    "- [ ] Random 1 Hard\n\n"
    "📝 Review: Có cách tối ưu hơn không?"
)

days[103] = (
    "🚀 Phase 8: Final Sprint — Ngày 103/120\n"
    "📚 LeetCode Countdown: Ngày 3\n\n"
    "🧪 DP & Graphs:\n"
    "- [ ] 1 DP Medium\n"
    "- [ ] 2 Graph Medium\n"
    "- [ ] 1 DP Hard (optional)\n\n"
    "💻 Luyện think aloud: explain → code → trade-offs"
)

days[104] = (
    "🚀 Phase 8: Final Sprint — Ngày 104/120\n"
    "📚 LeetCode Countdown: Ngày 4\n\n"
    "🧪 Mixed:\n"
    "- [ ] 4 bài (2 Easy + 2 Medium) có giới hạn thời gian\n\n"
    "📝 Focus: code cleanliness, variable naming, edge cases"
)

days[105] = (
    "🚀 Phase 8: Final Sprint — Ngày 105/120\n"
    "📚 System Design Final Review\n\n"
    "📖 30 phút mỗi design:\n"
    "- [ ] URL Shortener\n"
    "- [ ] Web Crawler\n"
    "- [ ] Chat System\n"
    "- [ ] Social Media Feed\n\n"
    "💻 Nhớ: Requirements, capacity, diagram, schema, API, trade-offs"
)

days[106] = (
    "🚀 Phase 8: Final Sprint — Ngày 106/120\n"
    "📚 Full Mock Interview #3 (1 tiếng)\n\n"
    "- [ ] 2 coding questions\n"
    "- [ ] 1 system design\n"
    "- [ ] Behavioral\n\n"
    "📝 Bấm giờ, ghi âm, tự đánh giá"
)

days[107] = (
    "🚀 Phase 8: Final Sprint — Ngày 107/120\n"
    "📚 LeetCode Countdown: Ngày 5\n\n"
    "🧪 Speed round:\n"
    "- [ ] 3 Easy (15 phút tổng)\n"
    "- [ ] 2 Medium (20 phút tổng)\n\n"
    "📝 So sánh solution của mình vs optimal"
)

days[108] = (
    "🚀 Phase 8: Final Sprint — Ngày 108/120\n"
    "📚 LeetCode Countdown: Ngày 6\n\n"
    "🧪 Focus bài hay hỏi trong interview:\n"
    "- [ ] Two Sum (tất cả variants)\n"
    "- [ ] Merge Intervals\n"
    "- [ ] LRU Cache\n"
    "- [ ] Meeting Rooms II\n"
    "- [ ] Number of Islands\n"
    "- [ ] Course Schedule\n\n"
    "💻 Mỗi bài: code sạch, giải thích, test"
)

days[109] = (
    "🚀 Phase 8: Final Sprint — Ngày 109/120\n"
    "📚 Company-Specific Deep Dive\n\n"
    "- [ ] Ôn culture của công ty mục tiêu\n"
    "- [ ] Leadership Principles\n"
    "- [ ] Chuẩn bị 3 câu STAR:\n"
    "  - [ ] Story 1: Challenge/Conflict\n"
    "  - [ ] Story 2: Initiative/Leadership\n"
    "  - [ ] Story 3: Failure/Lesson"
)

days[110] = (
    "🚀 Phase 8: Final Sprint — Ngày 110/120\n"
    "📚 LeetCode Countdown: Ngày 7\n\n"
    "🧪 Comprehensive:\n"
    "- [ ] 2 Medium mới\n"
    "- [ ] 1 Hard\n"
    "- [ ] 1 System Design\n\n"
    "📝 Kiểm tra tốc độ, độ chính xác, communication"
)

days[111] = (
    "🚀 Phase 8: Final Sprint — Ngày 111/120\n"
    "📚 Final Weak Areas\n\n"
    "Xác định 2-3 topics còn yếu nhất:\n"
    "- [ ] Topic 1: Làm 2 bài\n"
    "- [ ] Topic 2: Làm 2 bài\n"
    "- [ ] Topic 3: Làm 1 bài\n\n"
    "💻 Quality > Quantity"
)

days[112] = (
    "🚀 Phase 8: Final Sprint — Ngày 112/120\n"
    "📚 Full Mock Interview #4 (1.5 tiếng)\n\n"
    "- [ ] Behavioral (15 phút)\n"
    "- [ ] Coding #1 (25 phút)\n"
    "- [ ] Coding #2 (25 phút)\n"
    "- [ ] System Design (25 phút)\n\n"
    "📝 Đánh giá tổng thể"
)

days[113] = (
    "🚀 Phase 8: Final Sprint — Ngày 113/120\n"
    "📚 T-7: Tuần cuối!\n\n"
    "📝 Kế hoạch:\n"
    "- Ngày 113-114: Warm-up (Easy + Medium)\n"
    "- Ngày 115-116: Heavy practice\n"
    "- Ngày 117-118: Mock interviews\n"
    "- Ngày 119: Light review\n"
    "- Ngày 120: Nghỉ ngơi!\n\n"
    "🎯 Còn 7 ngày nữa! 💪"
)

days[114] = (
    "🚀 Phase 8: Final Sprint — Ngày 114/120\n"
    "📚 T-6: Warm-up\n\n"
    "🧪 Nhẹ nhàng:\n"
    "- [ ] 2 Easy\n"
    "- [ ] 2 Medium\n\n"
    "📝 Ôn:\n"
    "- [ ] Big O cheat sheet\n"
    "- [ ] Coding patterns checklist\n"
    "- [ ] System Design template"
)

days[115] = (
    "🚀 Phase 8: Final Sprint — Ngày 115/120\n"
    "📚 T-5: Heavy Practice\n\n"
    "🧪 5 bài Medium:\n"
    "- [ ] 1 Array/Hashing\n"
    "- [ ] 1 Tree\n"
    "- [ ] 1 Graph\n"
    "- [ ] 1 DP\n"
    "- [ ] 1 Design/String\n\n"
    "💻 Mỗi bài: explain (2p) → code (10-15p) → test (2p)"
)

days[116] = (
    "🚀 Phase 8: Final Sprint — Ngày 116/120\n"
    "📚 T-4: Heavy Practice Day 2\n\n"
    "🧪 Hôm nay:\n"
    "- [ ] 2 bài Medium (từ company cũ)\n"
    "- [ ] 1 System Design (Payment System)\n"
    "- [ ] 1 Behavioral (ghi âm)\n\n"
    "📝 Review: Xem lại notes 115 ngày qua"
)

days[117] = (
    "🚀 Phase 8: Final Sprint — Ngày 117/120\n"
    "📚 T-3: Mock Interview #5 (cuối)\n\n"
    "🧪 1 tiếng:\n"
    "- [ ] Coding #1 (20 phút)\n"
    "- [ ] Coding #2 (20 phút)\n"
    "- [ ] Q&A (10 phút)\n"
    "- [ ] Behavioral (10 phút)\n\n"
    "📝 Còn gap nào không?"
)

days[118] = (
    "🚀 Phase 8: Final Sprint — Ngày 118/120\n"
    "📚 T-2: Final Polish\n\n"
    "📝 Checklist:\n"
    "- [ ] 3 câu hỏi cho interviewer\n"
    "- [ ] Xem lại resume\n"
    "- [ ] Intro: Tell me about yourself\n"
    "- [ ] Kiểm tra logistics\n\n"
    "🧪 Làm 2 bài LeetCode warm up"
)

days[119] = (
    "🚀 Phase 8: Final Sprint — Ngày 119/120\n"
    "📚 T-1: Rest & Light Review\n\n"
    "⚠️ KHÔNG HỌC NẶNG!\n"
    "- [ ] Đọc notes ngắn (30 phút)\n"
    "- [ ] Xem patterns (15 phút)\n"
    "- [ ] Tập 'Tell me about yourself' (5 phút)\n"
    "- [ ] Chuẩn bị quần áo\n"
    "- [ ] NGỦ SỚM!\n\n"
    "🎯 Bạn đã sẵn sàng! 😎"
)

days[120] = (
    "🏆 Phase 8: Final Sprint — Ngày 120/120\n"
    "🎉 CHÚC MỪNG! HOÀN THÀNH!\n\n"
    "📚 Đã học:\n"
    "✅ Big-O & Algorithm Analysis\n"
    "✅ Data Structures: Arrays, LL, Stack, Queue, Hash Table\n"
    "✅ Trees, BST, Heap, Balanced Trees, Sorting\n"
    "✅ Graphs: BFS, DFS, Dijkstra, Topo Sort, MST\n"
    "✅ Recursion, DP, Backtracking\n"
    "✅ System Design & Scalability\n"
    "✅ 100+ LeetCode problems\n"
    "✅ Mock interviews & Behavioral prep\n\n"
    "💪 Bây giờ hãy tự tin đi phỏng vấn nhé!\n\n"
    "🔥 BEST OF LUCK! 🔥"
)

# Generate JSON
os.makedirs(os.path.dirname(NOTES_FILE), exist_ok=True)

notes = {}
for day_num in range(1, 121):
    date = START_DATE + timedelta(days=day_num - 1)
    date_str = date.strftime("%Y-%m-%d")
    notes[date_str] = days[day_num]

with open(NOTES_FILE, "w", encoding="utf-8") as f:
    json.dump(notes, f, ensure_ascii=False, indent=2)

keys = sorted(notes.keys())
print(f"✅ Đã ghi {len(keys)} ngày roadmap vào {NOTES_FILE}")
print(f"📅 Từ: {keys[0]} đến: {keys[-1]}")
print(f"📝 Dung lượng: {os.path.getsize(NOTES_FILE)} bytes")
