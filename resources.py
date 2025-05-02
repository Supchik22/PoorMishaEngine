import os
import json
import xml.etree.ElementTree as ET

class Res:
    @staticmethod
    def load( path):
        ext = os.path.splitext(path)[1].lower()

        if ext == ".json":
            return Res._load_json(path)
        elif ext in [".scn"]:
            return Res._load_scn(path)
        elif ext == ".txt":
            return Res._load_text(path)
        else:
            raise ValueError(f"Unknown resource type: {ext}")
    @staticmethod
    def _load_json( path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    @staticmethod
    def _load_text( path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    @staticmethod
    def _load_scn(path):
        tree = ET.parse(path)
        root = tree.getroot()
        return Res._parse_node(root)
    @staticmethod
    def _parse_node( xml_node):
        node_dict = {
            "type": xml_node.get("type", "Node"),
            "name": xml_node.get("name", "Unnamed"),
            "children": [Res._parse_node(child) for child in xml_node.findall("node")]
        }
        return node_dict
