# src/space.py
import networkx as nx

class ParkGraph:
    def __init__(self, nodes_df, edges_df):
        self.G = nx.Graph()
        self._build_graph(nodes_df, edges_df)
        
    def _build_graph(self, nodes_df, edges_df):
        """Membangun graph NetworkX dari dataframe."""
        
        # 1. Tambahkan Nodes (Titik)
        for _, row in nodes_df.iterrows():
            self.G.add_node(
                row['node_id'],
                pos=(row['x_px'], row['y_px']), # Simpan koordinat pixel
                pos_m=(row['x_m'], row['y_m'])  # Simpan koordinat meter (opsional)
            )
            
        # 2. Tambahkan Edges (Garis Jalan)
        for _, row in edges_df.iterrows():
            if row['from_node'] in self.G.nodes and row['to_node'] in self.G.nodes:
                self.G.add_edge(
                    row['from_node'],
                    row['to_node'],
                    edge_id=row['edge_id'],
                    weight=row['length_m'], # Penting untuk shortest path nanti
                    edge_type=row['edge_type']
                )

    def get_graph(self):
        return self.G