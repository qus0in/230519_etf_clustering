import plotly.figure_factory as ff
from scipy.spatial.distance import squareform

def dendrogram():
    data = st.session_state.history
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
        width=800,
        height=600
    )
    
    st.plotly_chart(fig)