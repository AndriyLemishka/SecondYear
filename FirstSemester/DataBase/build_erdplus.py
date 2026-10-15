import json
import uuid
import time
import os

def generate_erdplus():
    doc_id = str(uuid.uuid4())
    timestamp = int(time.time() * 1000)

    # Organic, hand-crafted layout matching Task 1 natural placement
    entities_data = [
        {
            "name": "Покупець",
            "x": 265.4, "y": 184.2,
            "attrs": [
                ("ID_Покупця", True),
                ("Email", False),
                ("Дата_реєстрації", False)
            ],
            "attr_offsets": [(-118.4, -96.2), (12.3, -112.5), (-142.1, 18.6)]
        },
        {
            "name": "Кошик",
            "x": 294.8, "y": 692.6,
            "attrs": [
                ("ID_Кошика", True),
                ("ID_Покупця", False),
                ("Статус", False),
                ("Сума_до_оплати", False),
                ("Дата_створення", False)
            ],
            "attr_offsets": [(-128.5, -74.3), (-145.2, 5.8), (-132.7, 86.4), (-54.1, 124.9), (58.6, 118.2)]
        },
        {
            "name": "Елемент_Кошика",
            "x": 884.2, "y": 741.5,
            "attrs": [
                ("ID_Елемента", True),
                ("ID_Кошика", False),
                ("ID_Моделі", False),
                ("Фіксована_ціна", False)
            ],
            "attr_offsets": [(-84.3, -108.6), (76.2, -112.4), (-88.5, 104.7), (82.1, 109.3)]
        },
        {
            "name": "Відгук",
            "x": 896.7, "y": 142.8,
            "attrs": [
                ("ID_Відгуку", True),
                ("ID_Моделі", False),
                ("ID_Покупця", False),
                ("Оцінка", False),
                ("Текст", False)
            ],
            "attr_offsets": [(-136.2, -62.4), (-68.4, -106.8), (14.2, -121.5), (98.6, -94.7), (152.1, -32.8)]
        },
        {
            "name": "3D_Модель",
            "x": 1548.3, "y": 654.9,
            "attrs": [
                ("ID_Моделі", True),
                ("ID_Продавця", False),
                ("ID_Категорії", False),
                ("ID_Ліцензії", False),
                ("Назва", False),
                ("Опис", False),
                ("Ціна", False),
                ("Кількість_полігонів", False),
                ("Наявність_текстури", False)
            ],
            "attr_offsets": [
                (-65.0, -115.0),
                (75.0, -115.0),
                (135.0, -25.0),
                (125.0, 80.0),
                (65.0, 125.0),
                (-65.0, 125.0),
                (-120.0, 90.0),
                (-145.0, 40.0),
                (-145.0, -30.0)
            ]
        },
        {
            "name": "Категорія",
            "x": 1482.6, "y": 126.3,
            "attrs": [
                ("ID_Категорії", True),
                ("Назва", False)
            ],
            "attr_offsets": [(-94.2, -88.5), (86.4, -92.1)]
        },
        {
            "name": "Продавець",
            "x": 2168.4, "y": 196.7,
            "attrs": [
                ("ID_Продавця", True),
                ("Нікнейм", False),
                ("Рейтинг", False)
            ],
            "attr_offsets": [(-76.8, -96.4), (38.2, -112.6), (132.5, -64.8)]
        },
        {
            "name": "Ліцензія",
            "x": 2124.8, "y": 782.3,
            "attrs": [
                ("ID_Ліцензії", True),
                ("ID_Зміни", False),
                ("Назва_ліцензії", False),
                ("Тип_використання", False),
                ("Дозвіл_на_модифікацію", False),
                ("Дата_створення", False),
                ("Час_створення", False)
            ],
            "attr_offsets": [
                (-50.0, -135.0),
                (95.0, -140.0),
                (185.0, -80.0),
                (200.0, 0.0),
                (185.0, 85.0),
                (95.0, 145.0),
                (-50.0, 135.0)
            ]
        },
        {
            "name": "Файл_Моделі",
            "x": 1592.5, "y": 1234.8,
            "attrs": [
                ("ID_Файлу", True),
                ("ID_Моделі", False),
                ("Формат", False),
                ("Розмір_МБ", False)
            ],
            "attr_offsets": [(-128.4, 76.2), (-46.2, 118.5), (52.8, 116.4), (134.2, 74.8)]
        }
    ]

    relationships_data = [
        {
            "label": "Формує кошик",
            "source": "Покупець",
            "target": "Кошик",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 274.6, "y": 436.8
        },
        {
            "label": "Включає в кошик",
            "source": "Кошик",
            "target": "Елемент_Кошика",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 586.3, "y": 712.4
        },
        {
            "label": "Додається як елемент",
            "source": "3D_Модель",
            "target": "Елемент_Кошика",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1212.8, "y": 694.2
        },
        {
            "label": "Залишає відгук",
            "source": "Покупець",
            "target": "Відгук",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 578.4, "y": 158.6
        },
        {
            "label": "Отримує відгук",
            "source": "3D_Модель",
            "target": "Відгук",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1218.6, "y": 396.4
        },
        {
            "label": "Класифікує",
            "source": "Категорія",
            "target": "3D_Модель",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1512.4, "y": 388.2
        },
        {
            "label": "Створює",
            "source": "Продавець",
            "target": "3D_Модель",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1854.2, "y": 422.8
        },
        {
            "label": "Регулює",
            "source": "Ліцензія",
            "target": "3D_Модель",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1832.6, "y": 716.5
        },
        {
            "label": "Містить файл",
            "source": "3D_Модель",
            "target": "Файл_Моделі",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1568.4, "y": 942.1
        }
    ]

    nodes = []
    edges = []
    entity_map = {}

    for edef in entities_data:
        ent_id = str(uuid.uuid4())
        entity_map[edef["name"]] = ent_id

        ent_node = {
            "id": ent_id,
            "type": "Entity",
            "position": {
                "x": float(edef["x"]),
                "y": float(edef["y"])
            },
            "data": {
                "label": edef["name"],
                "type": "Regular",
                "isConnectable": False,
                "isSelected": False
            },
            "measured": {
                "width": 100,
                "height": 50
            },
            "selected": False,
            "dragging": False
        }
        nodes.append(ent_node)

        for i, (attr_name, is_pk) in enumerate(edef["attrs"]):
            attr_id = str(uuid.uuid4())
            dx, dy = edef["attr_offsets"][i]

            attr_node = {
                "id": attr_id,
                "parentId": ent_id,
                "type": "Attribute",
                "position": {
                    "x": float(dx),
                    "y": float(dy)
                },
                "data": {
                    "label": attr_name,
                    "types": {"Unique": True} if is_pk else [],
                    "isSelected": False,
                    "isConnectable": False
                },
                "measured": {
                    "width": 100,
                    "height": 50
                },
                "selected": False
            }
            nodes.append(attr_node)

            edge_id = str(uuid.uuid4())
            attr_edge = {
                "id": edge_id,
                "type": "Attribute",
                "source": ent_id,
                "target": attr_id
            }
            edges.append(attr_edge)

    for rdef in relationships_data:
        rel_id = str(uuid.uuid4())
        src_id = entity_map[rdef["source"]]
        tgt_id = entity_map[rdef["target"]]

        rel_node = {
            "id": rel_id,
            "type": "Relationship",
            "position": {
                "x": float(rdef["x"]),
                "y": float(rdef["y"])
            },
            "data": {
                "label": rdef["label"],
                "sourceEntityDetails": {
                    "id": src_id,
                    "minCardinality": rdef["sourceCard"]["min"],
                    "maxCardinality": rdef["sourceCard"]["max"]
                },
                "targetEntityDetails": {
                    "id": tgt_id,
                    "minCardinality": rdef["targetCard"]["min"],
                    "maxCardinality": rdef["targetCard"]["max"]
                },
                "isSelected": False,
                "isConnectable": True
            },
            "measured": {
                "width": 100,
                "height": 50
            },
            "selected": False
        }
        nodes.append(rel_node)

        edge1 = {
            "id": f"{rel_id}->{src_id};{src_id}->{tgt_id}",
            "type": "Relationship",
            "source": rel_id,
            "target": src_id,
            "data": {
                "id": f"{rel_id}->{src_id}",
                "minCardinality": rdef["sourceCard"]["min"],
                "maxCardinality": rdef["sourceCard"]["max"]
            }
        }
        edges.append(edge1)

        edge2 = {
            "id": f"{rel_id}->{tgt_id};{src_id}->{tgt_id}",
            "type": "Relationship",
            "source": rel_id,
            "target": tgt_id,
            "data": {
                "id": f"{rel_id}->{tgt_id}",
                "minCardinality": rdef["targetCard"]["min"],
                "maxCardinality": rdef["targetCard"]["max"]
            }
        }
        edges.append(edge2)

    erdplus_doc = {
        "diagramType": 1,
        "data": {
            "nodes": nodes,
            "edges": edges,
            "viewport": {
                "x": 60.0,
                "y": 60.0,
                "zoom": 0.52
            }
        },
        "name": "Завд2_Лаб1",
        "folder": {
            "name": "Diagrams",
            "folderType": 1,
            "depth": 0,
            "id": 413914
        },
        "id": doc_id,
        "updatedAtTimestamp": timestamp
    }

    with open("Завд2_Лаб1.erdplus", "w", encoding="utf-8") as f:
        json.dump(erdplus_doc, f, ensure_ascii=False, indent=2)

    lab1_dir = "Лаб 1"
    if os.path.exists(lab1_dir):
        with open(os.path.join(lab1_dir, "Завд2_Лаб1.erdplus"), "w", encoding="utf-8") as f:
            json.dump(erdplus_doc, f, ensure_ascii=False, indent=2)

    print("Successfully generated organic/natural Завд2_Лаб1.erdplus in root and Лаб 1!")

if __name__ == "__main__":
    generate_erdplus()
