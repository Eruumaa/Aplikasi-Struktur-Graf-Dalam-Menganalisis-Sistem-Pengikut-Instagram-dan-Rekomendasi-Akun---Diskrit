import pandas as pd
import networkx as nx
import community as community_louvain

edges_df = pd.read_csv('Network_for_IC_LT.txt', sep='\t', header=None, names=['follower', 'following'])

stats_df = pd.read_csv('Instagram_User_Stats.csv')

G = nx.DiGraph()

G.add_edges_from(zip(edges_df['follower'], edges_df['following']))


G.remove_edges_from(list(nx.selfloops(G)))

print(f"Jumlah Simpul: {G.number_of_nodes()}")
print(f"Jumlah Sisi: {G.number_of_edges()}")

in_degrees = dict(G.in_degree())

df_in_degree = pd.DataFrame(list(in_degrees.items()), columns=['ID_Akun', 'In_Degree'])

df_in_degree = df_in_degree.sort_values(by='In_Degree', ascending=False)

G_undirected = G.to_undirected()


partition = community_louvain.best_partition(G_undirected)

num_communities = len(set(partition.values()))
print(f"Total komunitas yang terdeteksi: {num_communities}")

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