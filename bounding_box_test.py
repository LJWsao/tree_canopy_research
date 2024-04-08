from deepforest import main
from deepforest import get_data
import matplotlib.pyplot as plt

model = main.deepforest()
model.use_release()





#predict_image returns plot in BlueGreenRed (opencv style), but matplotlib likes RedGreenBlue, switch the channel order. Many functions in deepforest will automatically perform this flip for you and give a warning.
for x in range(4):
    image_base_path = r'C:\Users\lamines24\Documents\tree_canopy_research\street_trees_level_'
    sample_image_path = get_data(image_base_path + str(x+1) + r'.tif')
    # img = model.predict_image(path=sample_image_path, return_plot=True)
    predicted_raster = model.predict_tile(sample_image_path, return_plot = True, patch_size=300,patch_overlap=0.25)
    plt.imsave(r'C:\Users\lamines24\Documents\tree_canopy_research\trees_test_result_raster_' + str(x+1) + r'.jpg', predicted_raster)