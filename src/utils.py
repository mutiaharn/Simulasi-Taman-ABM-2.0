# src/utils.py
import pandas as pd
import os

def load_data():
    """
    Memuat semua dataset dengan jalur folder yang otomatis dideteksi.
    """
    # --- LOGIKA PENCARIAN FOLDER ---
    # 1. Ambil lokasi file utils.py ini berada (misal: .../Simulasi_Taman_ABM/src)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Mundur satu langkah ke folder project utama (.../Simulasi_Taman_ABM)
    project_root = os.path.dirname(current_dir)
    
    # 3. Masuk ke folder data (.../Simulasi_Taman_ABM/data)
    data_dir = os.path.join(project_root, 'data')
    
    print(f"[INFO] Mencari dataset di: {data_dir}") # Debugging

    files = {
        "zone_config": "zone_config.csv",
        "path_nodes": "path_nodes.csv",
        "path_edges": "path_edges.csv",
        "park_facilities": "park_facilities.csv",
    }
    
    data = {}
    for key, filename in files.items():
        file_path = os.path.join(data_dir, filename)
        
        if os.path.exists(file_path):
            try:
                data[key] = pd.read_csv(file_path)
                # print(f"[OK] {filename} termuat.")
            except Exception as e:
                print(f"[ERROR] Gagal membaca {filename}: {e}")
        else:
            print(f"[MISSING] File tidak ditemukan: {file_path}")
            
    return data