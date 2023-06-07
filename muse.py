import torch
from muse_maskgit_pytorch import VQGanVAE, VQGanVAETrainer

vae = VQGanVAE(
    dim = 256,
    vq_codebook_size = 512
)
trainer = VQGanVAETrainer(
    vae = vae,
    image_size = 16,             # you may want to start with small images, and then curriculum learn to larger ones, but because the vae is all convolution, it should generalize to 512 (as in paper) without training on it
    folder = '壁纸/黑白/',
    batch_size = 4,
    grad_accum_every = 8,
    num_train_steps = 50000
).cuda()
trainer.train()