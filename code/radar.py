def get_radar_figure(results):
    import numpy as np
    import matplotlib.pyplot as plt
    import io
    from django.http import HttpResponse

    data_length = len(results[0])
    angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    result_data = [[v for v in result.values()] for result in results]
    data_now = np.concatenate((result_data[0], [result_data[0][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    fig = plt.figure(figsize=(10, 6), dpi=100)
    fig.suptitle("健康雷达图")
    ax1 = plt.subplot(121, polar=True)
    ax, data, name = [ax1], [data_now], ["Username"]
    for i in range(len(results):
        for j in np.arange(0, 100+20, 20):
            ax[i].plot(angles, (data_length + 1)*[j], '-.', lw=0.5, color='black')
        for j in range(data_length):
            ax[i].plot([angles[j], angles[j]], [0, 1000], '-.', lw=0.5, color='black')
        ax[i].plot(angles, data[i], color='b')
        ax[i].spines['polar'].set_visible(False)
        ax[i].grid(False)
        for a, b in zip(angles, data[i]):
            ax[i].text(a, b+5, '%.00f' % b, ha='center', va='center', fontsize=12, color='b')
        ax[i].set_thetagrids(angles*180/np.pi, labels)
        ax[i].set_theta_zero_location('N')
        ax[i].set_rlim(0, 1000)
        ax[i].set_rlabel_position(0)
        ax[i].set_title(name[i])

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    fig_data=buf.getvalue()
    response = HttpResponse(fig_data, content_type='image/png')
    return response
