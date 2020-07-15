from PIL import Image
import pkgutil
import io 
import seaborn as sns
import matplotlib.pyplot as plt

def plot_static(X, Y):
    cmap=plt.cm.YlOrRd_r 

    joint_shot_chart = sns.jointplot(X*10, Y*10, stat_func=None,
                                 kind='kde', space=0, color=cmap(0.1),
                                 cmap=cmap, n_levels=50, alpha=1.0)
    ax = joint_shot_chart.ax_joint
    ax.set_xlim(0,470)
    ax.set_ylim(0,500)

    img_data = pkgutil.get_data(__name__, "fullcourt.png")
    img = Image.open(io.BytesIO(img_data))
    img = img.resize((940, 500), Image.ANTIALIAS)
    plt.axis('off')
    ax.imshow(img, zorder=100)
    return joint_shot_chart 
