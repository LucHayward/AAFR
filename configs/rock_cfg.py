# parameters for the pipeline
pipeline_parameters = {
    'processing_module': "standard",
    'registration_module': "teaser",
    'evaluation_metrics': ["rms"]
}

# data_list
# num_of_points = 30_000  # resampling to n points
num_of_points = 30_000  # resampling to n points
# see paper for details (graph creation)
to = 100
tb = 0.1
dil = 0.01 # Controls dilation, increasing this could help _closing_ lines
thre = 0.90 # Controls the "on the dge" threshold, decreasing this results in more points classified as border.
N = 15
variables_as_list = [num_of_points, num_of_points, N, to, to, to, tb, tb, tb, dil, thre]

# Output folder
import os, pdb, json

name = f'A13-A5-{num_of_points}'
output_dir = os.path.join('rock_results', name)
os.makedirs(output_dir, exist_ok=True)

# list of broken objects (for now pairs)
data_folder = 'data'
data_list = []

cat_ff = os.path.join(data_folder, "rocks")
for fracture_folder in os.listdir(cat_ff):
    objects_folder = os.path.join(cat_ff, fracture_folder, 'objects')
    p_o1 = os.path.join(objects_folder, 'A5.ply')
    p_o2 = os.path.join(objects_folder, 'A13.ply')
    solution_folder = os.path.join(cat_ff, fracture_folder, 'solution')
    broken_obj_dict = {
        "path_obj1": p_o1,
        "path_obj2": p_o2,
        "category": "rocks",
        "fracture": fracture_folder
    }
    if os.path.exists(solution_folder):
        with open(os.path.join(solution_folder, 'solution.json'), 'r') as sj:
            solution = json.load(sj)
        broken_obj_dict['solution'] = solution

    data_list.append(broken_obj_dict)
