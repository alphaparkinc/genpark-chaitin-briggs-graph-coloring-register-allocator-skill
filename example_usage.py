from client import ChaitinBriggsRegisterAllocator

def main():
    print("=== Testing Chaitin-Briggs Register Allocator ===")
    allocator = ChaitinBriggsRegisterAllocator(k_registers=3)
    allocator.add_interference('v1', 'v2')
    allocator.add_interference('v2', 'v3')
    allocator.add_interference('v1', 'v3')
    allocator.add_interference('v3', 'v4')

    res = allocator.allocate()
    print("Allocation result:", res)
    assert res['success'] is True
    assert res['coloring']['v1'] != res['coloring']['v2']
    assert res['coloring']['v2'] != res['coloring']['v3']
    print("Register Allocator verified successfully!")

if __name__ == '__main__':
    main()
