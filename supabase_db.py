import streamlit as st
import pandas as pd
from supabase import create_client
#SUPABASE CONFIGURATION
SUPABASE_URL="https://sicntekffkeqdvupjden.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNpY250ZWtmZmtlcWR2dXBqZGVuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDE0NjgsImV4cCI6MjA4MTYxNzQ2OH0.O4lv7nTvTDIiAJpZE3JPf77_pRSav1Kzfpl3g3lgS0Y"
supabase=create_client(SUPABASE_URL,SUPABASE_KEY)
#STREAMLIT UI
st.title("HDFC BANK (Supabase)")
menu=["REGISTER","VIEW"]
choice=st.sidebar.selectbox("Menu",menu)
#REGISTER
if choice=="REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("AGE",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    balance=st.number_input("BALANCE",min_value=500)
    if st.button("Save"):
        supabase.table("users").insert({
            "name":name,
            "age":age,
            "account":account,
            "balance":balance}).execute()
        st.success("User added successfully")
#View Students
if choice=="VIEW":
    st.subheader("View users")
    data=supabase.table("users").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)
    
