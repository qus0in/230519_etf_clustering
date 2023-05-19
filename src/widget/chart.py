import streamlit as st
import pandas as pd

import plotly.figure_factory as ff
from scipy.spatial.distance import squareform

from src.data.history import *

def dendrogram():
    data = {k: v.Close for k, v in st.session_state.history.items()}
    df = pd.concat(data, axis=1)
    df_er = get_earning_rate(df)

    # 상관계수 행렬 계산
    corr_matrix = df_er.corr()

    # 거리 행렬로 변환
    dist_matrix = 1 - corr_matrix.abs()

    # 덴드로그램 그리기
    fig = ff.create_dendrogram(corr_matrix.values, labels=corr_matrix.columns)

    fig.update_layout(
        title='덴드로그램',  # 그래프 제목
        xaxis={'title': '클러스터'},  # x축 제목
        yaxis={'title': '거리'},  # y축 제목
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)