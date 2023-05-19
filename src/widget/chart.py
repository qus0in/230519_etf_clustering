import streamlit as st
import pandas as pd

import plotly.figure_factory as ff
import plotly.graph_objects as go
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

from src.data.history import *

def dendrogram(etfs):
    data = {k: v.Close for k, v in st.session_state.history.items()}
    df = pd.concat(data, axis=1)
    df_er = get_earning_rate(df, etfs)

    # 상관계수 행렬 계산
    corr_matrix = df_er.corr()

    # 거리 행렬로 변환
    dist_matrix = 1 - corr_matrix.abs()

    # 덴드로그램 그리기
    fig = ff.create_dendrogram(corr_matrix.values, labels=corr_matrix.columns)

    fig.update_layout(
        # title='덴드로그램',  # 그래프 제목
        xaxis={'title': '클러스터'},  # x축 제목
        yaxis={'title': '거리'},  # y축 제목
        height=600,
        margin=dict(l=0, r=0, t=0, b=0)  # 여백을 모두 0으로 설정
    )
    
    st.plotly_chart(fig, use_container_width=True)
    return corr_matrix

def silhouette(corr_matrix):
    # 계층적 클러스터링 수행
    cluster = AgglomerativeClustering()

    # 클러스터 수 범위 설정
    min_clusters = 2
    max_clusters = 10

    # 결과 저장 리스트
    silhouette_scores = []

    # 각 클러스터 수에 대해 클러스터링 수행 및 평가 지표 계산
    for n_clusters in range(min_clusters, max_clusters + 1):
        cluster.set_params(n_clusters=n_clusters)
        labels = cluster.fit_predict(corr_matrix)
        silhouette_scores.append(silhouette_score(corr_matrix, labels))

    # 클러스터 수에 따른 실루엣 스코어 시각화
    fig = go.Figure(data=go.Scatter(x=list(range(min_clusters, max_clusters + 1)),
                                    y=silhouette_scores, mode='lines+markers'))
    fig.update_layout(
        # title='클러스터 수에 따른 실루엣 스코어',
        xaxis_title='클러스터 수',
        yaxis_title='실루엣 스코어',
        height=400,
        margin=dict(l=0, r=0, t=0, b=0)  # 여백을 모두 0으로 설정
    )
    st.plotly_chart(fig, use_container_width=True)

    best_score = max(silhouette_scores)
    best_index = silhouette_scores.index(best_score)
    best_num_clusters = best_index + min_clusters
    return best_num_clusters
