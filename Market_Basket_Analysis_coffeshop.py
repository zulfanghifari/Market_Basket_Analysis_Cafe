import streamlit as st
import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import association_rules, apriori

# Set page configuration
st.set_page_config(page_title="Market Basket Analysis", layout="wide")

# Title
st.title("Market Basket Analysis Menggunakan Algoritma Apriori")

# Load and prepare data
@st.cache_data
def load_data():
    # Ganti dengan path file Anda
    df = pd.read_csv("bread basket.csv")
    
    # Data preparation
    df["Item"] = df["Item"].apply(lambda item: item.lower())
    df["Item"] = df["Item"].apply(lambda item: item.strip())
    df = df[["Transaction", "Item"]].copy()
    
    return df

@st.cache_data
def prepare_basket_data(df):
    # Create item count
    item_count = df.groupby(["Transaction", "Item"])["Item"].count().reset_index(name="Count")
    
    # Pivot table
    item_count_pivot = item_count.pivot_table(
        index='Transaction',
        columns="Item",
        values='Count',
        aggfunc="sum"
    ).fillna(0)
    
    # Convert to int and encode
    item_count_pivot = item_count_pivot.astype("int32")
    
    def encode(x):
        if x <= 0:
            return 0
        elif x >= 1:
            return 1
    
    item_count_pivot = item_count_pivot.map(encode)
    
    return item_count_pivot

# Load data
try:
    df = load_data()
    item_count_pivot = prepare_basket_data(df)
    
    # Get unique items and periods
    unique_items = sorted(df["Item"].unique())
    
    # Sidebar filters
    st.subheader("Item")
    selected_item = st.selectbox("", unique_items, index=unique_items.index("bread") if "bread" in unique_items else 0)
    
    st.subheader("Period Day")
    period_options = ["Morning", "Afternoon", "Evening", "Night"]
    selected_period = st.selectbox("", period_options, index=1)
    
    st.subheader("Weekday / Weekend")
    day_type_options = ["Weekday", "Weekend"]
    selected_day_type = st.selectbox("", day_type_options, index=0)
    
    st.subheader("Month")
    month_range = st.slider("", min_value=1, max_value=12, value=11, format="")
    month_names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("Jan")
    with col3:
        st.write("Dec")
    st.write(f"**{month_names[month_range]}**")
    
    st.subheader("Day")
    day_range = st.slider(" ", min_value=0, max_value=6, value=0, format="")
    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.write("Mon")
    with col3:
        st.write("Sun")
    st.write(f"**{day_names[day_range]}**")
    
    # Generate association rules
    @st.cache_data
    def generate_rules(basket_data, min_support=0.01, min_threshold=1):
        frequent_items = apriori(basket_data, min_support=min_support, use_colnames=True)
        rules = association_rules(frequent_items, metric="lift", min_threshold=min_threshold)
        return rules
    
    rules = generate_rules(item_count_pivot)
    
    # Filter rules based on selected item
    filtered_rules = rules[rules['antecedents'].apply(lambda x: selected_item in x)]
    
    # Display result
    st.subheader("Hasil Rekomendasi :")
    
    if not filtered_rules.empty:
        # Get the top recommendation
        top_rule = filtered_rules.sort_values('confidence', ascending=False).iloc[0]
        consequent = list(top_rule['consequents'])[0]
        
        result_text = f"Jika Konsumen Membeli **{selected_item.capitalize()}**, maka konsumen akan membeli **{consequent.capitalize()}** secara bersamaan"
        
        st.success(result_text)
        
        # Show additional statistics
        with st.expander("Lihat Detail Metrik"):
            st.write(f"**Support:** {top_rule['support']:.4f}")
            st.write(f"**Confidence:** {top_rule['confidence']:.4f}")
            st.write(f"**Lift:** {top_rule['lift']:.4f}")
            
            # Show top 5 rules
            st.write("\n**Top 5 Rekomendasi:**")
            display_df = filtered_rules.head(5).copy()
            display_df['antecedents'] = display_df['antecedents'].apply(lambda x: ', '.join(list(x)))
            display_df['consequents'] = display_df['consequents'].apply(lambda x: ', '.join(list(x)))
            st.dataframe(display_df[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
        
        # Add explanation section
        st.markdown("---")
        st.subheader("📊 Penjelasan Metrik")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### Support")
            st.write(f"**Nilai:** {top_rule['support']:.4f} ({top_rule['support']*100:.2f}%)")
            st.info("""
            **Support** menunjukkan seberapa sering kombinasi item muncul dalam seluruh transaksi.
            
            Semakin tinggi nilai support, semakin sering kombinasi item tersebut dibeli bersama-sama.
            """)
            st.write(f"Kombinasi **{selected_item}** dan **{consequent}** muncul dalam **{top_rule['support']*100:.2f}%** dari total transaksi.")
        
        with col2:
            st.markdown("### Confidence")
            st.write(f"**Nilai:** {top_rule['confidence']:.4f} ({top_rule['confidence']*100:.2f}%)")
            st.info("""
            **Confidence** menunjukkan probabilitas pelanggan membeli item B ketika mereka membeli item A.
            
            Nilai confidence yang tinggi menunjukkan hubungan yang kuat antara kedua item.
            """)
            st.write(f"Ketika pelanggan membeli **{selected_item}**, ada **{top_rule['confidence']*100:.2f}%** kemungkinan mereka juga membeli **{consequent}**.")
        
        with col3:
            st.markdown("### Lift")
            st.write(f"**Nilai:** {top_rule['lift']:.4f}")
            lift_interpretation = ""
            if top_rule['lift'] > 1:
                lift_interpretation = "Pembelian item-item ini **saling berkaitan positif** (sering dibeli bersama)."
            elif top_rule['lift'] == 1:
                lift_interpretation = "Pembelian item-item ini **independen** (tidak ada hubungan khusus)."
            else:
                lift_interpretation = "Pembelian item-item ini **berkaitan negatif** (jarang dibeli bersama)."
            
            st.info(f"""
            **Lift** mengukur seberapa kuat hubungan antara dua item dibandingkan jika mereka dibeli secara acak.
            
            - Lift > 1: Item dibeli bersama lebih sering dari yang diharapkan
            - Lift = 1: Tidak ada hubungan khusus
            - Lift < 1: Item jarang dibeli bersama
            """)
            st.write(lift_interpretation)
        
        # Business recommendation
        st.markdown("---")
        st.subheader("💡 Rekomendasi Bisnis")
        
        recommendations = f"""
        Berdasarkan analisis Market Basket untuk item **{selected_item.capitalize()}**:
        
        1. **Strategi Cross-Selling:** Tempatkan **{consequent}** di dekat **{selected_item}** untuk meningkatkan penjualan.
        
        2. **Bundle Promotion:** Buat paket promosi yang menggabungkan **{selected_item}** dan **{consequent}** dengan harga spesial.
        
        3. **Rekomendasi Produk:** Sistem dapat merekomendasikan **{consequent}** kepada pelanggan yang membeli **{selected_item}**.
        
        4. **Inventory Management:** Pastikan stok **{consequent}** tersedia ketika **{selected_item}** sedang laris.
        """
        
        st.success(recommendations)
    else:
        st.warning(f"Tidak ada rekomendasi yang ditemukan untuk item **{selected_item.capitalize()}**")
        st.info("Coba pilih item lain yang memiliki hubungan asosiasi lebih kuat dengan item lainnya.")

except FileNotFoundError:
    st.error("File 'bread basket.csv' tidak ditemukan. Pastikan file berada di direktori yang sama dengan script ini.")
    st.info("Silakan upload file CSV Anda atau sesuaikan path file di kode.")
except Exception as e:
    st.error(f"Terjadi kesalahan: {str(e)}")
    st.info("Pastikan file CSV Anda memiliki kolom: Transaction, Item, date_time, period_day, weekday_weekend")