import tensorflow as tf

# Check if TensorFlow can access the GPUs
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices("GPU")))

# # List all physical GPUs
# physical_gpus = tf.config.experimental.list_physical_devices("GPU")
# for gpu in physical_gpus:
#     print(gpu)

# # Set memory growth for GPUs
# if physical_gpus:
#     try:
#         for gpu in physical_gpus:
#             tf.config.experimental.set_memory_growth(gpu, True)
#         logical_gpus = tf.config.experimental.list_logical_devices("GPU")
#         print(len(physical_gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
#     except RuntimeError as e:
#         print(e)

# # Create a simple computation to verify GPU usage
# # Ensure to use GPU:1 (NVIDIA RTX 2050)
# with tf.device("/GPU:1"):
#     a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
#     b = tf.constant([[1.0, 1.0], [0.0, 1.0]])
#     c = tf.matmul(a, b)

# print(c)
