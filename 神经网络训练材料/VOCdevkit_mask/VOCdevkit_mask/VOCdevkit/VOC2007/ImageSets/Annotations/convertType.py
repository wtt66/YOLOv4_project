import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random

classes = ["nomask", "mask"]
classesOri = ["no_mask", "have_mask"]


def convert_annotation(image_id):
    in_file = open('VOCdevkit\VOC2007\Annotations\%s.xml' % image_id)
    out_file = open('VOCdevkit\VOC2007\Annotationsed\%s.txt' % image_id, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
