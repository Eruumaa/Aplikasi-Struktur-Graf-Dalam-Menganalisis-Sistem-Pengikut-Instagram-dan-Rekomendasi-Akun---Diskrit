import pandas as pd
import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. PRA-PEMROSESAN & KONSTRUKSI GRAF
# ==========================================
print("[-] Membaca dataset...")
edges_df = pd.read_csv(r'data/Network for IC LT.txt', sep=r'\s+', header=None, usecols=[0, 1], names=['follower', 'following'])

stats_df = pd.read_csv(r'data/Instagram User Stats.csv')

if 'id' in stats_df.columns:
    stats_df = stats_df.rename(columns={'id': 'ID_Akun'})
elif 'user_id' in stats_df.columns:
    stats_df = stats_df.rename(columns={'user_id': 'ID_Akun'})

print("[-] Membangun graf...")
G = nx.DiGraph()
G.add_edges_from(zip(edges_df['follower'], edges_df['following']))

G.remove_edges_from(list(nx.selfloop_edges(G)))

print(f"\n[HASIL] Jumlah Simpul : {G.number_of_nodes()}")
print(f"[HASIL] Jumlah Sisi   : {G.number_of_edges()}")

# ==========================================
# 2. ANALISIS SENTRALITAS (CENTRALITY)
# ==========================================
print("\n[-] Menghitung In-Degree Centrality...")
in_degrees = dict(G.in_degree())
df_in_degree = pd.DataFrame(list(in_degrees.items()), columns=['ID_Akun', 'In_Degree'])
df_in_degree = df_in_degree.sort_values(by='In_Degree', ascending=False)

print("[-] Menghitung Betweenness Centrality (Aproksimasi k=100)...")
betweenness_centrality = nx.betweenness_centrality(G, k=100, normalized=True, seed=42)
df_between = pd.DataFrame(list(betweenness_centrality.items()), columns=['ID_Akun', 'Betweenness'])
df_between = df_between.sort_values(by='Betweenness', ascending=False)

print("[-] Menghitung Closeness Centrality (Top 50 Akun)...")
top_50_nodes = df_in_degree['ID_Akun'].head(50).tolist()
closeness_centrality = {}
for node in top_50_nodes:
    closeness_centrality[node] = nx.closeness_centrality(G, u=node)
df_close = pd.DataFrame(list(closeness_centrality.items()), columns=['ID_Akun', 'Closeness'])
df_close = df_close.sort_values(by='Closeness', ascending=False)

# ==========================================
# 3. DETEKSI KOMUNITAS (LOUVAIN)
# ==========================================
print("\n[-] Menjalankan Algoritma Louvain...")
G_undirected = G.to_undirected()
partition = community_louvain.best_partition(G_undirected, random_state=42)
num_communities = len(set(partition.values()))
print(f"[HASIL] Total komunitas yang terdeteksi: {num_communities}")

# ==========================================
# 4. SISTEM REKOMENDASI AKUN (JACCARD)
# ==========================================
def jaccard_recommendation(G, target_node, top_n=5):
    recommendations = []
    target_following = set(G.successors(target_node))
    
    for neighbor in target_following:
        for candidate in G.successors(neighbor):
            if candidate != target_node and candidate not in target_following:
                candidate_following = set(G.successors(candidate))
                intersection = len(target_following.intersection(candidate_following))
                union = len(target_following.union(candidate_following))
                
                if union > 0:
                    jaccard_score = intersection / union
                    recommendations.append((candidate, jaccard_score))
                    
    recommendations = list(set(recommendations))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]

# ==========================================
# 5. CETAK HASIL KE TERMINAL UNTUK MAKALAH
# ==========================================
print("\n" + "="*50)
print("--- TABEL 5.1: Top 5 Akun In-Degree ---")
print(df_in_degree.head(5).to_string(index=False))

target_akun = df_in_degree.iloc[0]['ID_Akun']
hasil_rekomendasi = jaccard_recommendation(G, target_akun, top_n=5)

print(f"\n--- TABEL 5.2: Rekomendasi Akun untuk Target {target_akun} ---")
for kandidat, skor in hasil_rekomendasi:
    print(f"Kandidat: {kandidat} | Skor Jaccard: {skor:.4f}")
print("="*50)

# ==========================================
# 6. VISUALISASI SUB-GRAF KOMUNITAS
# ==========================================
print("\n[-] Men-generate Visualisasi Sub-Graf (Top 200 Akun)...")
top_200_nodes = df_in_degree['ID_Akun'].head(200).tolist()
G_sub = G.subgraph(top_200_nodes)

pos = nx.spring_layout(G_sub, k=0.15, iterations=20, seed=42)

sub_partition = {node: partition[node] for node in G_sub.nodes()}
unique_communities = list(set(sub_partition.values()))
num_sub_communities = len(unique_communities)
cmap = sns.color_palette("hsv", num_sub_communities)

community_color_map = {comm: cmap[i] for i, comm in enumerate(unique_communities)}
node_colors = [community_color_map[sub_partition[node]] for node in G_sub.nodes()]

plt.figure(figsize=(12, 12))
nx.draw_networkx_nodes(G_sub, pos, node_size=60, node_color=node_colors, alpha=0.9, edgecolors='black')
nx.draw_networkx_edges(G_sub, pos, alpha=0.15, edge_color='gray')
plt.title("Visualisasi Sub-Graf Komunitas Instagram\n(200 Akun Paling Berpengaruh)", fontsize=16, fontweight='bold')
plt.axis("off")
plt.show()

# ==========================================
# TAMBAHAN KODE UNTUK HASIL BAB 5
# ==========================================
print("\n" + "="*50)
print("--- Figure 5.1: Top 5 Nodes by Degree Centrality ---")
print(df_in_degree.head(5).to_string(index=False))

print("\n--- Figure 5.2: Top 5 Nodes by Betweenness Centrality ---")
print(df_between.head(5).to_string(index=False))

print("\n--- Figure 5.3: Top 5 Nodes by Closeness Centrality ---")
print(df_close.head(5).to_string(index=False))

print("\n--- Figure 5.4: Detected Communities ---")
print(f"Total komunitas (sirkel) yang berhasil dideteksi: {num_communities}")

print("\n--- Figure 5.6: Network Density Result ---")
density = nx.density(G)
print(f"Kepadatan Jaringan (Network Density): {density:.6f}")

print("\n--- Figure 5.7: Average Path Length Result ---")
G_sub_undirected = G_sub.to_undirected()
largest_cc = max(nx.connected_components(G_sub_undirected), key=len)
G_largest_cc = G_sub_undirected.subgraph(largest_cc)
apl = nx.average_shortest_path_length(G_largest_cc)
print(f"Rata-rata Panjang Lintasan (Average Path Length) pada Sub-Graf: {apl:.4f}")

print(f"\n--- Figure 5.8: Top 5 Recommendation Result untuk Akun {target_akun} ---")
for kandidat, skor in hasil_rekomendasi:
    print(f"Kandidat: {kandidat} | Skor Jaccard: {skor:.4f}")

print("\n--- Figure 5.9: Top 10 Users by Degree ---")
print(df_in_degree.head(10).to_string(index=False))
print("="*50)