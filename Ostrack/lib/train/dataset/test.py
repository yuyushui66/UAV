#!/root/miniconda3/bin/python
# import torch
# from torch.utils.data.distributed import DistributedSampler
# # datasets related

# from lib.train.data import sampler, opencv_loader, processing, LTRLoader
# import lib.train.data.transforms as tfm
# from lib.utils.misc import is_main_process
import got10kYu
test = Got10k(settings.env.got10k_dir, split='vottrain', image_loader=image_loader)

print(test.sequence_list)