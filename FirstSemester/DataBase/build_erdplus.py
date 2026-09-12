import json
import uuid
import time

def generate_erdplus():
    doc_id = str(uuid.uuid4())
    timestamp = int(time.time() * 1000)

    entities_data = [
        {
            "name": "Продавець",
            "x": 2200, "y": 150,
            "attrs": [
                ("ID_Продавця", True),
                ("Нікнейм", False),
                ("Рейтинг", False)
            ],
            "attr_offsets": [(-110, -80), (0, -110), (110, -80)]
        },
        {
            "name": "Покупець",
            "x": 200, "y": 150,
            "attrs": [
                ("ID_Покупця", True),
                ("Email", False),
                ("Дата_реєстрації", False)
            ],
            "attr_offsets": [(-110, -80), (0, -110), (110, -80)]
        },
        {
            "name": "Категорія",
            "x": 1600, "y": 150,
            "attrs": [
                ("ID_Категорії", True),
                ("Назва", False)
            ],
            "attr_offsets": [(-80, -90), (80, -90)]
        },
        {
            "name": "3D_Модель",
            "x": 1600, "y": 700,
            "attrs": [
                ("ID_Моделі", True),
                ("ID_Продавця", False),
                ("ID_Категорії", False),
                ("Назва", False),
                ("Опис", False),
                ("Ціна", False),
                ("Кількість_полігонів", False),
                ("Наявність_текстури", False)
            ],
            "attr_offsets": [(130, -90), (140, -40), (140, 10), (140, 60), (130, 110), (230, -40), (230, 20), (230, 80)]
        },
        {
            "name": "Файл_Моделі",
            "x": 1600, "y": 1250,
            "attrs": [
                ("ID_Файлу", True),
                ("ID_Моделі", False),
                ("Формат", False),
                ("Розмір_МБ", False)
            ],
            "attr_offsets": [(-120, 80), (-40, 110), (40, 110), (120, 80)]
        },
        {
            "name": "Кошик",
            "x": 200, "y": 700,
            "attrs": [
                ("ID_Кошика", True),
                ("ID_Покупця", False),
                ("Статус", False),
                ("Дата_створення", False)
            ],
            "attr_offsets": [(-130, -70), (-130, 0), (-130, 70), (-50, 110)]
        },
        {
            "name": "Елемент_Кошика",
            "x": 900, "y": 700,
            "attrs": [
                ("ID_Елемента", True),
                ("ID_Кошика", False),
                ("ID_Моделі", False),
                ("Фіксована_ціна", False)
            ],
            "attr_offsets": [(-100, -90), (100, -90), (-100, 90), (100, 90)]
        },
        {
            "name": "Транзакція",
            "x": 550, "y": 1250,
            "attrs": [
                ("ID_Транзакції", True),
                ("ID_Кошика", False),
                ("ID_Покупця", False),
                ("Сума", False),
                ("Дата", False)
            ],
            "attr_offsets": [(-120, 70), (-50, 110), (50, 110), (120, 70), (0, 140)]
        },
        {
            "name": "Відгук",
            "x": 900, "y": 150,
            "attrs": [
                ("ID_Відгуку", True),
                ("ID_Моделі", False),
                ("ID_Покупця", False),
                ("Оцінка", False),
                ("Текст", False)
            ],
            "attr_offsets": [(-110, -80), (-40, -110), (40, -110), (110, -80), (0, -150)]
        }
    ]

    relationships_data = [
        {
            "label": "Створює",
            "source": "Продавець",
            "target": "3D_Модель",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1900, "y": 425
        },
        {
            "label": "Класифікує",
            "source": "Категорія",
            "target": "3D_Модель",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1600, "y": 425
        },
        {
            "label": "Містить файл",
            "source": "3D_Модель",
            "target": "Файл_Моделі",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1600, "y": 975
        },
        {
            "label": "Отримує відгук",
            "source": "3D_Модель",
            "target": "Відгук",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1250, "y": 425
        },
        {
            "label": "Залишає відгук",
            "source": "Покупець",
            "target": "Відгук",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 550, "y": 150
        },
        {
            "label": "Має кошик",
            "source": "Покупець",
            "target": "Кошик",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 200, "y": 425
        },
        {
            "label": "Включає в кошик",
            "source": "Кошик",
            "target": "Елемент_Кошика",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 550, "y": 700
        },
        {
            "label": "Додається як елемент",
            "source": "3D_Модель",
            "target": "Елемент_Кошика",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 1250, "y": 700
        },
        {
            "label": "Оплачує кошик",
            "source": "Кошик",
            "target": "Транзакція",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 375, "y": 975
        },
        {
            "label": "Здійснює платіж",
            "source": "Покупець",
            "target": "Транзакція",
            "sourceCard": {"min": "Mandatory", "max": "One"},
            "targetCard": {"min": "Mandatory", "max": "Many"},
            "x": 200, "y": 1250
        }
    ]

    nodes = []
    edges = []
    entity_map = {}

    # Build Entity & Attribute nodes
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

        # Attributes
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

    # Build Relationship nodes & edges
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
                "x": 50.0,
                "y": 50.0,
                "zoom": 0.5
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

    print("Successfully generated Завд2_Лаб1.erdplus for the new marketplace domain!")
    print(f"Total nodes: {len(nodes)} (Entities: {len(entities_data)}, Attributes: {sum(len(e['attrs']) for e in entities_data)}, Relationships: {len(relationships_data)})")
    print(f"Total edges: {len(edges)}")

if __name__ == "__main__":
    generate_erdplus()
