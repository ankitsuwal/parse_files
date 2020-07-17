from os import listdir
import shutil
import os

import glob

#####################################################################
# Below code for match file name and save into another directory.
#####################################################################
# images_path = ["/home/ankit/bfl/label_image/18-05-2020/18_05_2020_15_34_46/", "/home/ankit/bfl/label_image/18-05-2020/18-05-2020_15_23_10/",
# "/home/ankit/bfl/label_image/18-05-2020/yolo_14_50_44/", "/home/ankit/bfl/label_image/18-05-2020/yolo_15_21_34/"]

# dst = "/home/ankit/bfl/label_image/delete_img/"
# txt_path = "/home/ankit/bfl/label_image/15_07_2020_txt/"
# img_path = "/home/ankit/Downloads/snaps/"
# # for img_path in images_path:
# count1, count2 = 0, 0
# for file in listdir(img_path):
#     img = file.split(".")[1]
#     if img == "jpg":
#         count1 += 1
#     elif img == "txt":
#         count2 += 1
#         img_file = img_path + file
#         shutil.copy(img_file, dst)
#     print(">>>>: ", file)
# print("img total: {}, txt toal: {}".format(count1, count2))
# for file in listdir(img_path):
#     txt_name = file.split(".")[0] + ".txt"
#     for root, dirs, files in os.walk(txt_path):
#         if txt_name in files:
#             image = img_path + file
#             shutil.move(image, dst)
#             print(txt_name)

#####################################################################
# Below code for match file name and save into another directory.
#####################################################################

# dst = "/home/ankit/bfl/label_image/18_ImgAndTxt/"
# txt_path = "/home/ankit/bfl/label_image/txt_files/"
# img_path = "/home/ankit/bfl/label_image/18_ImgAndTxt/"
# for file in listdir(img_path):
#     txt_name = file.split(".")[0] + ".txt"
#     for root, dirs, files in os.walk(txt_path):
#         if txt_name in files:
#             txt_file = txt_path + txt_name
#             shutil.copy(txt_file, dst)
#             print(txt_name)


################################################
 # for save frame in interval
################################################
# import cv2
# count = 0
#
#
# def create_frame(path, to_save_frame):
#     print(">>>>: ", path)
#     global count
#     try:
#         cap = cv2.VideoCapture(path)
#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 print("error while reading video")
#
#             if count % 24 == 0:
#                 cv2.imwrite(to_save_frame + "t_300620_%d.jpg" % count, frame)
#                 print("count: ", count)
#             count += 1
#             if cv2.waitKey(25) & 0xFF == ord('q'):
#                 break
#         cap.release()
#         cv2.destroyAllWindows()
#     except Exception as e:
#         print(e)
#
#
# if __name__ == "__main__":
#
#     # path = "/home/ankit/bfl/label_image/drive/1/15-28-48/secu_22-05-2020 08_09_31.mkv"
#     to_save_frame = "/home/ankit/bfl/label_image/frames/"
#     files_path = "/home/ankit/bfl/label_image/videos/"
#     for path in listdir(files_path):
#         create_frame(files_path + path, to_save_frame)

##################################################################
# for rename the file in same directory
##################################################################
# if __name__ == "__main__":
#     path = "/home/ankit/bfl/label_image/copy/copy_txt/"
#     count = 88
#     for file in listdir(path):
#         os.rename(path + file, path + "gate11_08_15_66_" + str(count) + ".txt")
#         count += 1
################################################################
# Remove last characher from the line
################################################################
files = "/home/ankit/Downloads/txt/"
tosave = "/home/ankit/bfl/label_image/remo/"
for file in listdir(files):
    new_file_content = ""
    ext = file.split(".")[1]
    if ext == "txt":
        with open(files + file, 'r', encoding='utf8') as fp:
            for line in fp.readlines():
                stripped_line = line.strip()
                new_line = stripped_line.replace(line, stripped_line)
                new_file_content += new_line + "\n"

    writing_file = open(tosave + file, "w")
    writing_file.write(new_file_content)
    writing_file.close()

# reading_file.close()
