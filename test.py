import networkx as nx

def count_cut_vertices(N, M, u, v, edges):
    # Tạo đồ thị có hướng
    G = nx.DiGraph()
    G.add_edges_from(edges)
    
    # Tìm các thành phần liên thông mạnh (strongly connected components)
    scc = list(nx.strongly_connected_components(G))
    
    # Đỉnh thắt là đỉnh nằm trong tất cả các thành phần liên thông mạnh
    cut_vertices = 0
    
    # Duyệt qua tất cả các đỉnh trong đồ thị
    for node in range(1, N+1):
        # Tạo một bản sao của đồ thị và loại bỏ node
        G_copy = G.copy()
        G_copy.remove_node(node)
        
        # Kiểm tra xem có tồn tại đường đi từ u đến v trong đồ thị đã loại bỏ node hay không
        if nx.has_path(G_copy, u, v):
            continue
        else:
            cut_vertices += 1

    return cut_vertices


# Đọc số lượng bộ test
t = int(input())

for _ in range(t):
    # Đọc thông tin cho từng bộ test
    N, M, u, v = map(int, input().split())
    
    # Đọc các cạnh của đồ thị
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))
    
    # Gọi hàm để đếm các đỉnh thắt
    result = count_cut_vertices(N, M, u, v, edges)
    print(result)
