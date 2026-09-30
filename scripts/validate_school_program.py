"""Validate the generated Chilean school program and its Pages artifact."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from grade_one_math_lessons import MATH_ATTITUDES, MATH_SKILLS, SEQUENCES as MATH_SEQUENCES, build_math_sequence, transversal_links
    from grade_one_language_lessons import ATTITUDES as LANGUAGE_ATTITUDES, SEQUENCES as LANGUAGE_SEQUENCES, attitude_link, build_language_sequence
    from grade_one_science_history_arts_lessons import ART_ATTITUDES, HISTORY_ATTITUDES, HISTORY_SKILLS, SCIENCE_ATTITUDES, SCIENCE_SKILLS, SEQUENCES as SHA_SEQUENCES, build_sequence as build_sha_sequence
    from grade_one_remaining_lessons import ATTITUDES as REMAINING_ATTITUDES, SEQUENCES as REMAINING_SEQUENCES, build_sequence as build_remaining_sequence
    from grade_two_math_lessons import MATH_ATTITUDES as GRADE_TWO_MATH_ATTITUDES, MATH_SKILLS as GRADE_TWO_MATH_SKILLS, SEQUENCES as GRADE_TWO_MATH_SEQUENCES, build_math_sequence as build_grade_two_math_sequence
    from grade_two_language_science_history_lessons import LANGUAGE_ATTITUDES as GRADE_TWO_LANGUAGE_ATTITUDES, SCIENCE_SKILLS as GRADE_TWO_SCIENCE_SKILLS, SCIENCE_ATTITUDES as GRADE_TWO_SCIENCE_ATTITUDES, HISTORY_SKILLS as GRADE_TWO_HISTORY_SKILLS, HISTORY_ATTITUDES as GRADE_TWO_HISTORY_ATTITUDES, L as GRADE_TWO_LANGUAGE_SEQUENCES, S as GRADE_TWO_SCIENCE_SEQUENCES, H as GRADE_TWO_HISTORY_SEQUENCES, build_sequence as build_grade_two_lsh_sequence
    from grade_two_arts_music_pe_lessons import ART_ATTITUDES as GRADE_TWO_ART_ATTITUDES, MUSIC_ATTITUDES as GRADE_TWO_MUSIC_ATTITUDES, PE_ATTITUDES as GRADE_TWO_PE_ATTITUDES, AR as GRADE_TWO_ART_SEQUENCES, MU as GRADE_TWO_MUSIC_SEQUENCES, EF as GRADE_TWO_PE_SEQUENCES, build_sequence as build_grade_two_amp_sequence
    from grade_two_remaining_lessons import ATTITUDES as GRADE_TWO_REMAINING_ATTITUDES, OR as GRADE_TWO_ORIENTATION_SEQUENCES, TE as GRADE_TWO_TECHNOLOGY_SEQUENCES, EN as GRADE_TWO_ENGLISH_SEQUENCES, LC_META as GRADE_TWO_INDIGENOUS_SEQUENCES, build_sequence as build_grade_two_remaining_sequence
    from grade_three_math_language_lessons import LANGUAGE as GRADE_THREE_LANGUAGE_SEQUENCES, LANGUAGE_ATTITUDES as GRADE_THREE_LANGUAGE_ATTITUDES, MATH as GRADE_THREE_MATH_SEQUENCES, MATH_ATTITUDES as GRADE_THREE_MATH_ATTITUDES, MATH_SKILLS as GRADE_THREE_MATH_SKILLS, build_sequence as build_grade_three_ml_sequence, complete_pilot_sequence
    from grade_three_science_history_lessons import HISTORY as GRADE_THREE_HISTORY_SEQUENCES, HISTORY_ATTITUDES as GRADE_THREE_HISTORY_ATTITUDES, HISTORY_SKILLS as GRADE_THREE_HISTORY_SKILLS, SCIENCE as GRADE_THREE_SCIENCE_SEQUENCES, SCIENCE_ATTITUDES as GRADE_THREE_SCIENCE_ATTITUDES, SCIENCE_SKILLS as GRADE_THREE_SCIENCE_SKILLS, build_sequence as build_grade_three_sh_sequence, complete_history_pilot
    from grade_three_arts_pe_english_indigenous_lessons import AR as GRADE_THREE_ART_SEQUENCES, ATTITUDES as GRADE_THREE_APEI_ATTITUDES, EF as GRADE_THREE_PE_SEQUENCES, EN as GRADE_THREE_ENGLISH_SEQUENCES, LC as GRADE_THREE_INDIGENOUS_SEQUENCES, build_sequence as build_grade_three_apei_sequence
    from grade_three_music_orientation_technology_lessons import ATTITUDES as GRADE_THREE_MOT_ATTITUDES, MU as GRADE_THREE_MUSIC_SEQUENCES, OR as GRADE_THREE_ORIENTATION_SEQUENCES, TE as GRADE_THREE_TECHNOLOGY_SEQUENCES, build_sequence as build_grade_three_mot_sequence
    from grade_four_math_lessons import MATH as GRADE_FOUR_MATH_SEQUENCES, MATH_ATTITUDES as GRADE_FOUR_MATH_ATTITUDES, MATH_SKILLS as GRADE_FOUR_MATH_SKILLS, build_sequence as build_grade_four_math_sequence
    from grade_four_remaining_lessons import SEQUENCES as GRADE_FOUR_REMAINING_SEQUENCES, build_sequence as build_grade_four_remaining_sequence
except ImportError:
    from scripts.grade_one_math_lessons import MATH_ATTITUDES, MATH_SKILLS, SEQUENCES as MATH_SEQUENCES, build_math_sequence, transversal_links
    from scripts.grade_one_language_lessons import ATTITUDES as LANGUAGE_ATTITUDES, SEQUENCES as LANGUAGE_SEQUENCES, attitude_link, build_language_sequence
    from scripts.grade_one_science_history_arts_lessons import ART_ATTITUDES, HISTORY_ATTITUDES, HISTORY_SKILLS, SCIENCE_ATTITUDES, SCIENCE_SKILLS, SEQUENCES as SHA_SEQUENCES, build_sequence as build_sha_sequence
    from scripts.grade_one_remaining_lessons import ATTITUDES as REMAINING_ATTITUDES, SEQUENCES as REMAINING_SEQUENCES, build_sequence as build_remaining_sequence
    from scripts.grade_two_math_lessons import MATH_ATTITUDES as GRADE_TWO_MATH_ATTITUDES, MATH_SKILLS as GRADE_TWO_MATH_SKILLS, SEQUENCES as GRADE_TWO_MATH_SEQUENCES, build_math_sequence as build_grade_two_math_sequence
    from scripts.grade_two_language_science_history_lessons import LANGUAGE_ATTITUDES as GRADE_TWO_LANGUAGE_ATTITUDES, SCIENCE_SKILLS as GRADE_TWO_SCIENCE_SKILLS, SCIENCE_ATTITUDES as GRADE_TWO_SCIENCE_ATTITUDES, HISTORY_SKILLS as GRADE_TWO_HISTORY_SKILLS, HISTORY_ATTITUDES as GRADE_TWO_HISTORY_ATTITUDES, L as GRADE_TWO_LANGUAGE_SEQUENCES, S as GRADE_TWO_SCIENCE_SEQUENCES, H as GRADE_TWO_HISTORY_SEQUENCES, build_sequence as build_grade_two_lsh_sequence
    from scripts.grade_two_arts_music_pe_lessons import ART_ATTITUDES as GRADE_TWO_ART_ATTITUDES, MUSIC_ATTITUDES as GRADE_TWO_MUSIC_ATTITUDES, PE_ATTITUDES as GRADE_TWO_PE_ATTITUDES, AR as GRADE_TWO_ART_SEQUENCES, MU as GRADE_TWO_MUSIC_SEQUENCES, EF as GRADE_TWO_PE_SEQUENCES, build_sequence as build_grade_two_amp_sequence
    from scripts.grade_two_remaining_lessons import ATTITUDES as GRADE_TWO_REMAINING_ATTITUDES, OR as GRADE_TWO_ORIENTATION_SEQUENCES, TE as GRADE_TWO_TECHNOLOGY_SEQUENCES, EN as GRADE_TWO_ENGLISH_SEQUENCES, LC_META as GRADE_TWO_INDIGENOUS_SEQUENCES, build_sequence as build_grade_two_remaining_sequence
    from scripts.grade_three_math_language_lessons import LANGUAGE as GRADE_THREE_LANGUAGE_SEQUENCES, LANGUAGE_ATTITUDES as GRADE_THREE_LANGUAGE_ATTITUDES, MATH as GRADE_THREE_MATH_SEQUENCES, MATH_ATTITUDES as GRADE_THREE_MATH_ATTITUDES, MATH_SKILLS as GRADE_THREE_MATH_SKILLS, build_sequence as build_grade_three_ml_sequence, complete_pilot_sequence
    from scripts.grade_three_science_history_lessons import HISTORY as GRADE_THREE_HISTORY_SEQUENCES, HISTORY_ATTITUDES as GRADE_THREE_HISTORY_ATTITUDES, HISTORY_SKILLS as GRADE_THREE_HISTORY_SKILLS, SCIENCE as GRADE_THREE_SCIENCE_SEQUENCES, SCIENCE_ATTITUDES as GRADE_THREE_SCIENCE_ATTITUDES, SCIENCE_SKILLS as GRADE_THREE_SCIENCE_SKILLS, build_sequence as build_grade_three_sh_sequence, complete_history_pilot
    from scripts.grade_three_arts_pe_english_indigenous_lessons import AR as GRADE_THREE_ART_SEQUENCES, ATTITUDES as GRADE_THREE_APEI_ATTITUDES, EF as GRADE_THREE_PE_SEQUENCES, EN as GRADE_THREE_ENGLISH_SEQUENCES, LC as GRADE_THREE_INDIGENOUS_SEQUENCES, build_sequence as build_grade_three_apei_sequence
    from scripts.grade_three_music_orientation_technology_lessons import ATTITUDES as GRADE_THREE_MOT_ATTITUDES, MU as GRADE_THREE_MUSIC_SEQUENCES, OR as GRADE_THREE_ORIENTATION_SEQUENCES, TE as GRADE_THREE_TECHNOLOGY_SEQUENCES, build_sequence as build_grade_three_mot_sequence
    from scripts.grade_four_math_lessons import MATH as GRADE_FOUR_MATH_SEQUENCES, MATH_ATTITUDES as GRADE_FOUR_MATH_ATTITUDES, MATH_SKILLS as GRADE_FOUR_MATH_SKILLS, build_sequence as build_grade_four_math_sequence
    from scripts.grade_four_remaining_lessons import SEQUENCES as GRADE_FOUR_REMAINING_SEQUENCES, build_sequence as build_grade_four_remaining_sequence

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "curriculum/catalog.json"
REQUIRED_CLASS_FIELDS = {
    "id", "class_code", "lesson", "lesson_count", "phase", "topic", "course",
    "course_slug", "course_order", "subject", "subject_slug", "axis", "oa_code",
    "oa_text", "coverage", "source_url", "editorial_status", "publication_status",
    "path", "web_path",
}
REQUIRED_DEVELOPED_FIELDS = {
    "title", "purpose", "goal", "opening", "model", "guided", "independent",
    "ticket", "materials", "support", "extension", "evidence", "criteria",
    "next_step", "short_version",
}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        catalog = json.loads((root / "curriculum/catalog.json").read_text(encoding="utf-8"))
        snapshot = json.loads((root / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
        developed = json.loads((root / "content/developed-lessons.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"No se pudo cargar la fuente de verdad: {exc}"]

    classes = catalog.get("classes", [])
    official_urls = {objective["code"]: objective["url"] for record in snapshot.get("records", []) for objective in record.get("objectives", [])}
    objective_count = sum(len(record.get("objectives", [])) for record in snapshot.get("records", []))
    expected = {"schema_version": 8, "class_count": len(classes), "objective_count": objective_count, "course_count": 12}
    for key, value in expected.items():
        if catalog.get(key) != value:
            errors.append(f"{key}: catálogo={catalog.get(key)!r}, esperado={value!r}")
    if [item.get("id") for item in classes] != list(range(1, len(classes) + 1)):
        errors.append("Los ids de clase no son consecutivos")
    codes = [item.get("class_code") for item in classes]
    if len(codes) != len(set(codes)):
        errors.append("Hay códigos de clase duplicados")
    all_developed = dict(developed.get("objectives", {}))
    all_developed.update({code: build_math_sequence(code) for code in MATH_SEQUENCES})
    all_developed.update({code: build_language_sequence(code) for code in LANGUAGE_SEQUENCES})
    all_developed.update({code: build_sha_sequence(code) for code in SHA_SEQUENCES})
    all_developed.update({code: build_remaining_sequence(code) for code in REMAINING_SEQUENCES})
    all_developed.update({code: build_grade_two_math_sequence(code) for code in GRADE_TWO_MATH_SEQUENCES})
    all_developed.update({code: build_grade_two_lsh_sequence(code) for code in GRADE_TWO_LANGUAGE_SEQUENCES | GRADE_TWO_SCIENCE_SEQUENCES | GRADE_TWO_HISTORY_SEQUENCES})
    all_developed.update({code: build_grade_two_amp_sequence(code) for code in GRADE_TWO_ART_SEQUENCES | GRADE_TWO_MUSIC_SEQUENCES | GRADE_TWO_PE_SEQUENCES})
    all_developed.update({code: build_grade_two_remaining_sequence(code) for code in GRADE_TWO_ORIENTATION_SEQUENCES | GRADE_TWO_TECHNOLOGY_SEQUENCES | GRADE_TWO_ENGLISH_SEQUENCES | GRADE_TWO_INDIGENOUS_SEQUENCES})
    all_developed.update({code: build_grade_three_ml_sequence(code) for code in GRADE_THREE_MATH_SEQUENCES | GRADE_THREE_LANGUAGE_SEQUENCES})
    complete_pilot_sequence(all_developed["MA03 OA 11"])
    all_developed.update({code: build_grade_three_sh_sequence(code) for code in GRADE_THREE_SCIENCE_SEQUENCES | GRADE_THREE_HISTORY_SEQUENCES})
    complete_history_pilot(all_developed["HI03 OA 05"])
    all_developed.update({code: build_grade_three_apei_sequence(code) for code in GRADE_THREE_ART_SEQUENCES | GRADE_THREE_PE_SEQUENCES | GRADE_THREE_ENGLISH_SEQUENCES | GRADE_THREE_INDIGENOUS_SEQUENCES})
    all_developed.update({code: build_grade_three_mot_sequence(code) for code in GRADE_THREE_MUSIC_SEQUENCES | GRADE_THREE_ORIENTATION_SEQUENCES | GRADE_THREE_TECHNOLOGY_SEQUENCES})
    all_developed.update({code: build_grade_four_math_sequence(code) for code in GRADE_FOUR_MATH_SEQUENCES})
    all_developed.update({code: build_grade_four_remaining_sequence(code) for code in GRADE_FOUR_REMAINING_SEQUENCES})
    for index, lesson in enumerate(all_developed["MA01 OA 01"]["lessons"]):
        lesson["transversal"] = transversal_links(1, index, lesson["goal"].removeprefix("Hoy ").rstrip("."))
    for index, lesson in enumerate(all_developed["LE01 OA 03"]["lessons"]):
        lesson["transversal"] = [attitude_link(3, index, lesson["goal"].removeprefix("Hoy ").rstrip("."))]
    developed_codes = set(all_developed)
    developed_count = sum(item.get("oa_code") in developed_codes for item in classes)
    draft_count = sum(item.get("editorial_status") == "borrador" for item in classes)
    integrated_count = sum(item.get("editorial_status") == "integrada" for item in classes)
    if catalog.get("editorial_counts") != {"inventariada": len(classes), "secuenciada": len(classes), "borrador": draft_count, "desarrollada": developed_count, "integrada": integrated_count, "revisada": 0, "publicada": len(classes)}:
        errors.append("Los estados editoriales no coinciden con la cobertura declarada")
    transversal_codes: set[str] = set()
    grade_two_transversal_codes: set[str] = set()
    grade_two_lsh_transversal_codes: dict[str, set[str]] = {"LE": set(), "CN": set(), "HI": set()}
    grade_two_amp_transversal_codes: dict[str, set[str]] = {"AR": set(), "MU": set(), "EF": set()}
    grade_two_remaining_transversal_codes: dict[str, set[str]] = {"TE": set(), "EN": set(), "LC": set()}
    grade_three_math_transversal_codes: set[str] = set()
    grade_three_language_transversal_codes: set[str] = set()
    grade_three_science_transversal_codes: set[str] = set()
    grade_three_history_transversal_codes: set[str] = set()
    grade_three_apei_transversal_codes: dict[str, set[str]] = {prefix: set() for prefix in GRADE_THREE_APEI_ATTITUDES}
    grade_three_mot_transversal_codes: dict[str, set[str]] = {prefix: set() for prefix in GRADE_THREE_MOT_ATTITUDES}
    grade_four_math_transversal_codes: set[str] = set()
    language_attitude_codes: set[str] = set()
    sha_transversal_codes: dict[str, set[str]] = {"CN": set(), "HI": set(), "AR": set()}
    remaining_transversal_codes: dict[str, set[str]] = {prefix: set() for prefix in REMAINING_ATTITUDES}
    for oa_code, objective in all_developed.items():
        if oa_code.startswith(("MA01 OA ", "MA02 OA ", "MA03 OA ", "MA04 OA ", "LE03 OA ", "CN03 OA ", "HI03 OA ", "AR03 OA ", "EF03 OA ", "EN03 OA ", "LC03 OA ", "MU03 OA ", "OR03 OA ", "TE03 OA ", "LE02 OA ", "CN02 OA ", "HI02 OA ", "AR02 OA ", "MU02 OA ", "EF02 OA ", "OR02 OA ", "TE02 OA ", "EN02 OA ", "LC02 OA ", "CN01 OA ", "HI01 OA ", "AR01 OA ", "MU01 OA ", "EF01 OA ", "OR01 OA ", "TE01 OA ", "EN01 OA ", "LC01 OA ")) or oa_code == "LE01 OA 03":
            for field in ("topic", "pedagogical_explanation", "prerequisites", "vocabulary", "official_alignment"):
                if not objective.get(field):
                    errors.append(f"{oa_code}: falta fundamento específico {field}")
            alignment = objective.get("official_alignment", {})
            if len(alignment.get("indicators", [])) < 3 or not alignment.get("source", "").startswith("https://www.curriculumnacional.cl/"):
                errors.append(f"{oa_code}: alineación oficial insuficiente")
            if oa_code.startswith(("MA01 OA ", "MA02 OA ", "MA03 OA ", "MA04 OA ", "LE03 OA ", "CN03 OA ", "HI03 OA ", "AR03 OA ", "EF03 OA ", "EN03 OA ", "LC03 OA ", "MU03 OA ", "OR03 OA ", "TE03 OA ", "LE02 OA ", "CN02 OA ", "HI02 OA ", "AR02 OA ", "MU02 OA ", "EF02 OA ", "OR02 OA ", "TE02 OA ", "EN02 OA ", "LC02 OA ", "LE01 OA ", "CN01 OA ", "HI01 OA ", "AR01 OA ", "MU01 OA ", "EF01 OA ", "OR01 OA ", "TE01 OA ", "EN01 OA ", "LC01 OA ")) and alignment.get("source") != official_urls.get(oa_code):
                errors.append(f"{oa_code}: la fuente de alineación no coincide con la ficha oficial del snapshot")
        for index, lesson in enumerate(objective.get("lessons", []), 1):
            missing = REQUIRED_DEVELOPED_FIELDS - lesson.keys()
            if missing:
                errors.append(f"{oa_code}, clase {index}: faltan campos editoriales {', '.join(sorted(missing))}")
            if len(lesson.get("criteria", [])) < 3:
                errors.append(f"{oa_code}, clase {index}: requiere al menos tres criterios observables")
            if len(str(lesson.get("title", "")).strip()) < 8:
                errors.append(f"{oa_code}, clase {index}: title no identifica la experiencia")
            for field in REQUIRED_DEVELOPED_FIELDS - {"criteria", "title"}:
                if len(str(lesson.get(field, "")).strip()) < 20:
                    errors.append(f"{oa_code}, clase {index}: {field} no tiene desarrollo suficiente")
            if oa_code.startswith(("MA01 OA ", "MA02 OA ", "MA03 OA ", "MA04 OA ", "LE03 OA ", "CN03 OA ", "HI03 OA ", "AR03 OA ", "EF03 OA ", "EN03 OA ", "LC03 OA ", "MU03 OA ", "OR03 OA ", "TE03 OA ", "LE02 OA ", "CN02 OA ", "HI02 OA ", "AR02 OA ", "MU02 OA ", "EF02 OA ", "OR02 OA ", "TE02 OA ", "EN02 OA ", "LC02 OA ", "CN01 OA ", "HI01 OA ", "AR01 OA ", "MU01 OA ", "EF01 OA ", "OR01 OA ", "TE01 OA ", "EN01 OA ", "LC01 OA ")) or oa_code == "LE01 OA 03":
                for field in ("home_task", "complementary", "difficulty_actions", "specialist_coordination"):
                    if not lesson.get(field):
                        errors.append(f"{oa_code}, clase {index}: falta extensión pedagógica {field}")
                if "…" in lesson.get("goal", ""):
                    errors.append(f"{oa_code}, clase {index}: la meta estudiantil está truncada")
            if oa_code.startswith("MA01 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 2 or {link.get("type") for link in links} != {"Habilidad", "Actitud"}:
                    errors.append(f"{oa_code}, clase {index}: falta integración observable de habilidad y actitud")
                transversal_codes.update(link.get("code", "") for link in links)
            if oa_code.startswith("MA02 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 2 or {link.get("type") for link in links} != {"Habilidad", "Actitud"}:
                    errors.append(f"{oa_code}, clase {index}: falta integración observable de habilidad y actitud")
                grade_two_transversal_codes.update(link.get("code", "") for link in links)
            if oa_code.startswith("MA03 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 2 or {link.get("type") for link in links} != {"Habilidad", "Actitud"}:
                    errors.append(f"{oa_code}, clase {index}: falta integración observable de habilidad y actitud")
                grade_three_math_transversal_codes.update(link.get("code", "") for link in links)
            if oa_code.startswith("MA04 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 2 or {link.get("type") for link in links} != {"Habilidad", "Actitud"}:
                    errors.append(f"{oa_code}, clase {index}: falta integración observable de habilidad y actitud")
                grade_four_math_transversal_codes.update(link.get("code", "") for link in links)
            if oa_code.startswith("LE03 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 1 or links[0].get("type") != "Actitud":
                    errors.append(f"{oa_code}, clase {index}: falta integración observable de actitud")
                grade_three_language_transversal_codes.update(link.get("code", "") for link in links)
            if oa_code.startswith("CN03 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 2 or {link.get("type") for link in links} != {"Habilidad", "Actitud"}:
                    errors.append(f"{oa_code}, clase {index}: integración científica transversal incompleta")
                grade_three_science_transversal_codes.update(link.get("code", "") for link in links)
            if oa_code.startswith("HI03 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 2 or {link.get("type") for link in links} != {"Habilidad", "Actitud"}:
                    errors.append(f"{oa_code}, clase {index}: integración histórica transversal incompleta")
                grade_three_history_transversal_codes.update(link.get("code", "") for link in links)
            if oa_code.startswith(("AR03 OA ", "EF03 OA ", "EN03 OA ", "LC03 OA ")):
                links = lesson.get("transversal", [])
                if len(links) != 1 or links[0].get("type") != "Actitud":
                    errors.append(f"{oa_code}, clase {index}: integración observable de actitud incompleta")
                grade_three_apei_transversal_codes[oa_code[:2]].update(link.get("code", "") for link in links)
            if oa_code.startswith(("MU03 OA ", "TE03 OA ")):
                links = lesson.get("transversal", [])
                if len(links) != 1 or links[0].get("type") != "Actitud":
                    errors.append(f"{oa_code}, clase {index}: integración observable de actitud incompleta")
                grade_three_mot_transversal_codes[oa_code[:2]].update(link.get("code", "") for link in links)
            if oa_code.startswith("OR03 OA ") and lesson.get("transversal"):
                errors.append(f"{oa_code}, clase {index}: Orientación no debe inventar OA actitudinales separados")
            if oa_code.startswith(("LE02 OA ", "CN02 OA ", "HI02 OA ")):
                links = lesson.get("transversal", [])
                expected_types = {"Actitud"} if oa_code.startswith("LE02") else {"Habilidad", "Actitud"}
                if {link.get("type") for link in links} != expected_types:
                    errors.append(f"{oa_code}, clase {index}: integración transversal incompleta")
                grade_two_lsh_transversal_codes[oa_code[:2]].update(link.get("code", "") for link in links)
            if oa_code.startswith(("AR02 OA ", "MU02 OA ", "EF02 OA ")):
                links = lesson.get("transversal", [])
                if len(links) != 1 or links[0].get("type") != "Actitud":
                    errors.append(f"{oa_code}, clase {index}: integración observable de actitud incompleta")
                grade_two_amp_transversal_codes[oa_code[:2]].update(link.get("code", "") for link in links)
            if oa_code.startswith(("TE02 OA ", "EN02 OA ", "LC02 OA ")):
                links = lesson.get("transversal", [])
                if len(links) != 1 or links[0].get("type") != "Actitud":
                    errors.append(f"{oa_code}, clase {index}: integración observable de actitud incompleta")
                grade_two_remaining_transversal_codes[oa_code[:2]].update(link.get("code", "") for link in links)
            if oa_code.startswith("LE01 OA "):
                links = lesson.get("transversal", [])
                if len(links) != 1 or links[0].get("type") != "Actitud":
                    errors.append(f"{oa_code}, clase {index}: falta integración observable de actitud")
                language_attitude_codes.update(link.get("code", "") for link in links)
            if oa_code.startswith(("CN01 OA ", "HI01 OA ", "AR01 OA ")):
                links = lesson.get("transversal", [])
                expected_types = {"Actitud"} if oa_code.startswith("AR") else {"Habilidad", "Actitud"}
                if {link.get("type") for link in links} != expected_types:
                    errors.append(f"{oa_code}, clase {index}: integración transversal incompleta")
                sha_transversal_codes[oa_code[:2]].update(link.get("code", "") for link in links)
            if oa_code.startswith(("MU01 OA ", "EF01 OA ", "OR01 OA ", "TE01 OA ", "EN01 OA ", "LC01 OA ")):
                links = lesson.get("transversal", [])
                prefix = oa_code[:2]
                expected_count = 0 if prefix == "OR" else 1
                if len(links) != expected_count or links and links[0].get("type") != "Actitud":
                    errors.append(f"{oa_code}, clase {index}: integración de actitud incoherente")
                if prefix in remaining_transversal_codes:
                    remaining_transversal_codes[prefix].update(link.get("code", "") for link in links)
    expected_transversal_codes = {code for code, _ in MATH_SKILLS + MATH_ATTITUDES}
    if transversal_codes != expected_transversal_codes:
        errors.append("Las 83 clases de Matemática no cubren los 16 OA transversales de habilidad y actitud")
    expected_grade_two_transversal_codes = {code for code, _ in GRADE_TWO_MATH_SKILLS + GRADE_TWO_MATH_ATTITUDES}
    if grade_two_transversal_codes != expected_grade_two_transversal_codes:
        errors.append("Las 93 clases de Matemática de 2° básico no cubren los 15 OA transversales")
    if grade_three_math_transversal_codes != {code for code, _ in GRADE_THREE_MATH_SKILLS + GRADE_THREE_MATH_ATTITUDES}:
        errors.append("Las 112 clases de Matemática de 3° básico no cubren sus 20 OA transversales")
    if grade_four_math_transversal_codes != {code for code, _ in GRADE_FOUR_MATH_SKILLS + GRADE_FOUR_MATH_ATTITUDES}:
        errors.append("Las 118 clases de Matemática de 4° básico no cubren sus 20 OA transversales")
    if grade_three_language_transversal_codes != {code for code, _ in GRADE_THREE_LANGUAGE_ATTITUDES}:
        errors.append("Las 157 clases de Lenguaje de 3° básico no cubren sus 7 OA de actitud")
    if grade_three_science_transversal_codes != {code for code, _ in GRADE_THREE_SCIENCE_SKILLS + GRADE_THREE_SCIENCE_ATTITUDES}:
        errors.append("Las 55 clases de Ciencias de 3° básico no cubren sus 12 OA transversales")
    if grade_three_history_transversal_codes != {code for code, _ in GRADE_THREE_HISTORY_SKILLS + GRADE_THREE_HISTORY_ATTITUDES}:
        errors.append("Las 72 clases de Historia de 3° básico no cubren sus 18 OA transversales")
    for prefix, pool in GRADE_THREE_APEI_ATTITUDES.items():
        if grade_three_apei_transversal_codes[prefix] != {code for code, _ in pool}:
            errors.append(f"Las clases de {prefix}03 no cubren todas sus actitudes transversales")
    for prefix, pool in GRADE_THREE_MOT_ATTITUDES.items():
        if grade_three_mot_transversal_codes[prefix] != {code for code, _ in pool}:
            errors.append(f"Las clases de {prefix}03 no cubren todas sus actitudes transversales")
    expected_grade_two_lsh = {
        "LE": {code for code, _ in GRADE_TWO_LANGUAGE_ATTITUDES},
        "CN": {code for code, _ in GRADE_TWO_SCIENCE_SKILLS + GRADE_TWO_SCIENCE_ATTITUDES},
        "HI": {code for code, _ in GRADE_TWO_HISTORY_SKILLS + GRADE_TWO_HISTORY_ATTITUDES},
    }
    for prefix, expected_codes in expected_grade_two_lsh.items():
        if grade_two_lsh_transversal_codes[prefix] != expected_codes:
            errors.append(f"Las clases de {prefix}02 no cubren todos sus OA transversales")
    expected_grade_two_amp = {
        "AR": {code for code, _ in GRADE_TWO_ART_ATTITUDES},
        "MU": {code for code, _ in GRADE_TWO_MUSIC_ATTITUDES},
        "EF": {code for code, _ in GRADE_TWO_PE_ATTITUDES},
    }
    for prefix, expected_codes in expected_grade_two_amp.items():
        if grade_two_amp_transversal_codes[prefix] != expected_codes:
            errors.append(f"Las clases de {prefix}02 no cubren todas sus actitudes transversales")
    for prefix, pool in GRADE_TWO_REMAINING_ATTITUDES.items():
        if grade_two_remaining_transversal_codes[prefix] != {code for code, _ in pool}:
            errors.append(f"Las clases de {prefix}02 no cubren todas sus actitudes transversales")
    if language_attitude_codes != {code for code, _ in LANGUAGE_ATTITUDES}:
        errors.append("Las 131 clases de Lenguaje no cubren los 7 OA transversales de actitud")
    expected_sha = {"CN": {code for code, _ in SCIENCE_SKILLS + SCIENCE_ATTITUDES}, "HI": {code for code, _ in HISTORY_SKILLS + HISTORY_ATTITUDES}, "AR": {code for code, _ in ART_ATTITUDES}}
    for prefix, expected_codes in expected_sha.items():
        if sha_transversal_codes[prefix] != expected_codes:
            errors.append(f"Las clases de {prefix} no cubren todos sus OA transversales")
    for prefix, pool in REMAINING_ATTITUDES.items():
        if remaining_transversal_codes[prefix] != {code for code, _ in pool}:
            errors.append(f"Las clases de {prefix} no cubren todas sus actitudes transversales")
    first_grade = [item for item in classes if item.get("course_order") == 1]
    first_grade_developed = sum(item.get("editorial_status") == "desarrollada" for item in first_grade)
    first_grade_integrated = sum(item.get("editorial_status") == "integrada" for item in first_grade)
    first_grade_drafts = sum(item.get("editorial_status") == "borrador" for item in first_grade)
    if len(first_grade) != 1034 or first_grade_developed != 691 or first_grade_integrated != 343 or first_grade_drafts != 0:
        errors.append("Estado de 1° básico incoherente (esperadas: 691 desarrolladas, 343 integradas y 0 borradores)")
    math_core = [item for item in first_grade if item.get("subject_slug") == "matematica" and item.get("editorial_status") == "desarrollada"]
    if len(math_core) != 83 or len({item.get("oa_code") for item in math_core}) != 20:
        errors.append("Matemática de 1° básico debe contener exactamente 83 clases desarrolladas en 20 OA de contenido")
    math_integrated = [item for item in first_grade if item.get("subject_slug") == "matematica" and item.get("editorial_status") == "integrada"]
    if len(math_integrated) != 68 or len({item.get("oa_code") for item in math_integrated}) != 16:
        errors.append("Matemática de 1° básico debe integrar 68 experiencias de 16 OA de habilidad/actitud")
    language_core = [item for item in first_grade if item.get("subject_slug") == "lenguaje-comunicacion" and item.get("editorial_status") == "desarrollada"]
    if len(language_core) != 131 or len({item.get("oa_code") for item in language_core}) != 26:
        errors.append("Lenguaje de 1° básico debe contener exactamente 131 clases desarrolladas en 26 OA de contenido")
    language_integrated = [item for item in first_grade if item.get("subject_slug") == "lenguaje-comunicacion" and item.get("editorial_status") == "integrada"]
    if len(language_integrated) != 29 or len({item.get("oa_code") for item in language_integrated}) != 7:
        errors.append("Lenguaje de 1° básico debe integrar 29 experiencias de 7 OA de actitud")
    expected_subjects = {"ciencias-naturales": (49, 12, 40, 10), "historia-geografia-ciencias-sociales": (68, 15, 64, 16), "artes-visuales": (24, 5, 28, 7), "musica": (29, 7, 28, 7), "educacion-fisica-salud": (48, 11, 32, 8), "orientacion": (35, 8, 0, 0), "tecnologia": (26, 6, 20, 5), "ingles-propuesta": (69, 14, 16, 4), "lengua-cultura-pueblos-originarios-ancestrales": (129, 29, 18, 4)}
    for slug, (core_count, core_oa, integrated_count_expected, integrated_oa) in expected_subjects.items():
        core = [item for item in first_grade if item.get("subject_slug") == slug and item.get("editorial_status") == "desarrollada"]
        integrated = [item for item in first_grade if item.get("subject_slug") == slug and item.get("editorial_status") == "integrada"]
        if (len(core), len({item.get("oa_code") for item in core}), len(integrated), len({item.get("oa_code") for item in integrated})) != (core_count, core_oa, integrated_count_expected, integrated_oa):
            errors.append(f"Cobertura desarrollada o transversal incompleta en {slug}")
    second_grade = [item for item in classes if item.get("course_order") == 2]
    second_developed = sum(item.get("editorial_status") == "desarrollada" for item in second_grade)
    second_integrated = sum(item.get("editorial_status") == "integrada" for item in second_grade)
    second_sequenced = sum(item.get("editorial_status") == "secuenciada" for item in second_grade)
    if len(second_grade) != 1072 or (second_developed, second_integrated, second_sequenced) != (721, 351, 0):
        errors.append("Estado de 2° básico incoherente (esperadas: 721 desarrolladas, 351 integradas y 0 secuenciadas)")
    second_math = [item for item in second_grade if item.get("subject_slug") == "matematica"]
    second_math_core = [item for item in second_math if item.get("editorial_status") == "desarrollada"]
    second_math_integrated = [item for item in second_math if item.get("editorial_status") == "integrada"]
    if (len(second_math_core), len({item.get("oa_code") for item in second_math_core})) != (93, 22):
        errors.append("Matemática de 2° básico debe contener 93 clases desarrolladas en 22 OA de contenido")
    if (len(second_math_integrated), len({item.get("oa_code") for item in second_math_integrated})) != (64, 15):
        errors.append("Matemática de 2° básico debe contener 64 experiencias integradas en 15 OA transversales")
    expected_second_subjects = {
        "lenguaje-comunicacion": (149, 30, 29, 7),
        "ciencias-naturales": (57, 14, 44, 11),
        "historia-geografia-ciencias-sociales": (72, 16, 72, 18),
        "artes-visuales": (24, 5, 28, 7),
        "musica": (29, 7, 28, 7),
        "educacion-fisica-salud": (47, 11, 32, 8),
        "orientacion": (35, 8, 0, 0),
        "tecnologia": (31, 7, 20, 5),
        "ingles-propuesta": (68, 14, 16, 4),
        "lengua-cultura-pueblos-originarios-ancestrales": (116, 27, 18, 4),
    }
    for slug, expected_counts in expected_second_subjects.items():
        subject_rows = [item for item in second_grade if item.get("subject_slug") == slug]
        core = [item for item in subject_rows if item.get("editorial_status") == "desarrollada"]
        integrated = [item for item in subject_rows if item.get("editorial_status") == "integrada"]
        actual = (len(core), len({item.get("oa_code") for item in core}), len(integrated), len({item.get("oa_code") for item in integrated}))
        if actual != expected_counts:
            errors.append(f"Cobertura desarrollada o transversal incompleta en 2° básico: {slug}")
    if any(item.get("editorial_status") == "secuenciada" for item in second_grade):
        errors.append("2° básico no debe conservar propuestas sólo secuenciadas")

    third_grade = [item for item in classes if item.get("course_order") == 3]
    third_developed = sum(item.get("editorial_status") == "desarrollada" for item in third_grade)
    third_integrated = sum(item.get("editorial_status") == "integrada" for item in third_grade)
    third_sequenced = sum(item.get("editorial_status") == "secuenciada" for item in third_grade)
    if len(third_grade) != 1136 or (third_developed, third_integrated, third_sequenced) != (757, 379, 0):
        errors.append("Estado de 3° básico incoherente (esperadas: 757 desarrolladas, 379 integradas y 0 secuenciadas)")
    expected_third_subjects = {
        "artes-visuales": (25, 5, 28, 7),
        "ciencias-naturales": (55, 13, 49, 12),
        "educacion-fisica-salud": (48, 11, 32, 8),
        "historia-geografia-ciencias-sociales": (72, 16, 72, 18),
        "ingles-propuesta": (69, 14, 16, 4),
        "lengua-cultura-pueblos-originarios-ancestrales": (116, 26, 18, 4),
        "lenguaje-comunicacion": (157, 31, 29, 7),
        "matematica": (112, 26, 87, 20),
        "musica": (35, 8, 28, 7),
        "orientacion": (35, 8, 0, 0),
        "tecnologia": (33, 7, 20, 5),
    }
    for slug, expected_counts in expected_third_subjects.items():
        subject_rows = [item for item in third_grade if item.get("subject_slug") == slug]
        core = [item for item in subject_rows if item.get("editorial_status") == "desarrollada"]
        integrated = [item for item in subject_rows if item.get("editorial_status") == "integrada"]
        actual = (len(core), len({item.get("oa_code") for item in core}), len(integrated), len({item.get("oa_code") for item in integrated}))
        if actual != expected_counts:
            errors.append(f"Cobertura desarrollada o transversal incompleta en 3° básico: {slug}")

    fourth_math = [item for item in classes if item.get("course_order") == 4 and item.get("subject_slug") == "matematica"]
    fourth_math_core = [item for item in fourth_math if item.get("editorial_status") == "desarrollada"]
    fourth_math_integrated = [item for item in fourth_math if item.get("editorial_status") == "integrada"]
    if (len(fourth_math_core), len({item.get("oa_code") for item in fourth_math_core})) != (118, 27):
        errors.append("Matemática de 4° básico debe contener 118 clases desarrolladas en 27 OA de contenido")
    if (len(fourth_math_integrated), len({item.get("oa_code") for item in fourth_math_integrated})) != (87, 20):
        errors.append("Matemática de 4° básico debe integrar 87 experiencias de 20 OA transversales")
    if any(item.get("editorial_status") == "secuenciada" for item in fourth_math):
        errors.append("Matemática de 4° básico no debe conservar propuestas sólo secuenciadas")
    fourth_grade = [item for item in classes if item.get("course_order") == 4]
    expected_fourth_subjects = {
        "artes-visuales": (25, 5, 28, 7), "ciencias-naturales": (71, 17, 49, 12),
        "educacion-fisica-salud": (49, 11, 32, 8), "historia-geografia-ciencias-sociales": (82, 18, 77, 19),
        "ingles-propuesta": (69, 14, 16, 4), "lengua-cultura-pueblos-originarios-ancestrales": (126, 29, 18, 4),
        "lenguaje-comunicacion": (161, 30, 29, 7), "matematica": (118, 27, 87, 20),
        "musica": (35, 8, 28, 7), "orientacion": (40, 9, 0, 0), "tecnologia": (35, 7, 20, 5),
    }
    for slug, expected_counts in expected_fourth_subjects.items():
        rows = [item for item in fourth_grade if item.get("subject_slug") == slug]
        core = [item for item in rows if item.get("editorial_status") == "desarrollada"]
        integrated = [item for item in rows if item.get("editorial_status") == "integrada"]
        actual = (len(core), len({item.get("oa_code") for item in core}), len(integrated), len({item.get("oa_code") for item in integrated}))
        if actual != expected_counts:
            errors.append(f"Cobertura desarrollada o transversal incompleta en 4° básico: {slug}")
    if any(item.get("editorial_status") in {"secuenciada", "borrador"} for item in fourth_grade):
        errors.append("4° básico no debe conservar propuestas pendientes")

    markdown_cache: dict[str, str] = {}
    html_cache: dict[str, str] = {}
    for item in classes:
        missing = REQUIRED_CLASS_FIELDS - item.keys()
        if missing:
            errors.append(f"Clase {item.get('id', '?')} sin campos: {', '.join(sorted(missing))}")
            continue
        if not 4 <= item["lesson_count"] <= 7 or not 1 <= item["lesson"] <= item["lesson_count"]:
            errors.append(f"Dosificación inválida en {item['class_code']}")
        markdown_path, markdown_anchor = item["path"].split("#", 1)
        if markdown_path not in markdown_cache:
            path = root / markdown_path
            markdown_cache[markdown_path] = path.read_text(encoding="utf-8") if path.is_file() else ""
            if not markdown_cache[markdown_path]:
                errors.append(f"Falta Markdown {markdown_path}")
        if markdown_anchor not in markdown_cache[markdown_path]:
            errors.append(f"Falta ancla {markdown_anchor} en {markdown_path}")
        web_path, web_anchor = item["web_path"].split("#", 1)
        if web_path not in html_cache:
            path = root / "site" / web_path
            html_cache[web_path] = path.read_text(encoding="utf-8") if path.is_file() else ""
            if not html_cache[web_path]:
                errors.append(f"Falta página HTML {web_path}")
            for token in ('<html lang="es">', "<title>", "<h1>", "canonical", "breadcrumbs"):
                if html_cache[web_path] and token not in html_cache[web_path]:
                    errors.append(f"{web_path} no contiene {token}")
        if f'id="{web_anchor}"' not in html_cache[web_path]:
            errors.append(f"Falta ancla web {web_anchor} en {web_path}")
        if item["editorial_status"] == "desarrollada":
            tokens = ["Propósito docente", "Meta para estudiantes", "Materiales y preparación", "Criterios observables", "Decisión posterior", "Tarea breve y flexible", "Actividades complementarias", "Control de dificultades con acciones", "Coordinación profesional"]
            if item.get("subject_slug") == "matematica" and item.get("course_order") in {1, 2, 3, 4}:
                tokens.append("Habilidad y actitud en esta clase")
            if item.get("subject_slug") == "lenguaje-comunicacion" and item.get("course_order") in {1, 3}:
                tokens.append("Actitud transversal en esta clase")
            if item.get("subject_slug") in {"ciencias-naturales", "historia-geografia-ciencias-sociales"} and item.get("course_order") in {1, 3}:
                tokens.append("Habilidad y actitud en esta clase")
            if item.get("subject_slug") == "artes-visuales" and item.get("course_order") in {1, 3}:
                tokens.append("Actitud transversal en esta clase")
            if item.get("subject_slug") in {"musica", "educacion-fisica-salud", "tecnologia", "ingles-propuesta", "lengua-cultura-pueblos-originarios-ancestrales"} and item.get("course_order") in {1, 3}:
                tokens.append("Actitud transversal en esta clase")
            for token in tokens:
                if token not in html_cache[web_path]:
                    errors.append(f"{web_path} no materializa el contrato desarrollado: falta {token}")

    pages = list((root / "site/classes").rglob("*.html"))
    if len(pages) != objective_count:
        errors.append(f"Páginas de OA: {len(pages)}, esperadas: {objective_count}")
    for required in ("index.html", "documentacion.html", "styles.css", "app.js", "catalog.json", "404.html", "icon.svg", "manifest.webmanifest", "sitemap.xml", "levels/1-basico.html", "levels/2-basico.html", "levels/3-basico.html", "levels/4-basico.html"):
        if not (root / "site" / required).is_file():
            errors.append(f"Falta artefacto de Pages: {required}")
    documentation_pages = list((root / "site/docs").rglob("*.html"))
    if len(documentation_pages) < 38:
        errors.append(f"Documentación HTML incompleta: {len(documentation_pages)} páginas, esperadas al menos 38")
    sitemap_path = root / "site/sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8") if sitemap_path.is_file() else ""
    if sitemap.count("<url>") != objective_count + len(documentation_pages) + 6:
        errors.append("El sitemap no enumera portada, documentación, vistas de 1° a 4° básico, documentos HTML y páginas de OA")
    level_page = root / "site/levels/1-basico.html"
    level_html = level_page.read_text(encoding="utf-8") if level_page.is_file() else ""
    for token in ("1.034", "237", "11", "691", "343", "Contrato pedagógico"):
        if token not in level_html:
            errors.append(f"Vista de 1° básico incompleta: falta {token}")
    second_level_page = root / "site/levels/2-basico.html"
    second_level_html = second_level_page.read_text(encoding="utf-8") if second_level_page.is_file() else ""
    for token in ("1.072", "247", "11", "721", "351", "0 propuestas pendientes", "Completo no significa revisado"):
        if token not in second_level_html:
            errors.append(f"Vista de 2° básico incompleta: falta {token}")
    third_level_page = root / "site/levels/3-basico.html"
    third_level_html = third_level_page.read_text(encoding="utf-8") if third_level_page.is_file() else ""
    for token in ("1.136", "257", "11", "757", "379", "0 propuestas pendientes", "Completo no significa revisado"):
        if token not in third_level_html:
            errors.append(f"Vista de 3° básico incompleta: falta {token}")
    fourth_level_page = root / "site/levels/4-basico.html"
    fourth_level_html = fourth_level_page.read_text(encoding="utf-8") if fourth_level_page.is_file() else ""
    for token in ("1.195", "268", "11", "811", "384", "0 propuestas pendientes", "Completo no significa revisado"):
        if token not in fourth_level_html:
            errors.append(f"Vista de 4° básico incompleta: falta {token}")
    documentation_page = root / "site/documentacion.html"
    documentation_html = documentation_page.read_text(encoding="utf-8") if documentation_page.is_file() else ""
    for token in ("Documentación pedagógica", "44 guías de asignatura", "11 guías por cada uno de los cuatro niveles completos", "Primer nivel completo", "Segundo nivel completo", "Tercer nivel completo", "Cuarto nivel completo", "¿Qué es un OA?", "Roles en el aula", "Cobertura navegable", "Markdown + HTML"):
        if token not in documentation_html:
            errors.append(f"Portada documental incompleta: falta {token}")
    if any(documentation_html.count(f"Leer guía de {level} completa") != 11 for level in ("1°", "2°", "3°", "4°")):
        errors.append("La portada documental no presenta las 11 guías de los cuatro niveles con igual visibilidad")
    required_docs = {
        "README.md": ("12.997", "2.823", "691 clases disciplinares", "721 clases disciplinares", "757 clases disciplinares", "811 clases disciplinares", "Cómo se mejora el contenido desarrollado", "De dónde sale el contenido", "Portal, navegación y formatos", "Caja de herramientas pedagógicas", "Rutas según quién usa el repositorio", "Para docentes y equipos pedagógicos", "Calidad y CI", "Qué es y qué no es este programa", "Idea fuerza", "Documentación de principio a fin"),
        "docs/README.md": ("Estado verificable", "Cómo leer los estados"),
        "docs/PRIMERO_BASICO.md": ("1.034", "Decisiones con evidencia"),
        "docs/SEGUNDO_BASICO.md": ("1.072", "Decisiones con evidencia", "Continuidad"),
        "docs/TERCERO_BASICO.md": ("1.136", "Decisiones con evidencia", "Continuidad"),
        "docs/CUARTO_BASICO.md": ("1.195", "Contrato de calidad", "Continuidad"),
        "docs/1-basico/README.md": ("Las 11 asignaturas", "Progresión pedagógica común"),
        "docs/2-basico/README.md": ("Las 11 asignaturas", "721 clases desarrolladas", "351 experiencias integradas", "Progresión pedagógica común", "Anatomía de una clase"),
        "docs/2-basico/matematica.md": ("93 clases desarrolladas", "64 experiencias integradas", "Continuidad con 1° básico"),
        "docs/3-basico/README.md": ("Las 11 asignaturas", "757 clases desarrolladas", "379 experiencias integradas", "Progresión pedagógica común", "Anatomía de una clase"),
        "docs/3-basico/matematica.md": ("112 clases desarrolladas", "87 experiencias integradas", "Continuidad con 2° básico"),
        "docs/4-basico/README.md": ("Las 11 asignaturas", "811 clases desarrolladas", "384 experiencias integradas", "Progresión pedagógica común", "Anatomía y diferenciación"),
        "docs/4-basico/matematica.md": ("118 clases desarrolladas", "87 experiencias integradas", "Continuidad con 3° básico", "Recorrido OA por OA"),
        "docs/SYLLABUS.md": ("Marco de reconstrucción de 1°, 2°, 3° y 4° básico", "Planificación de principio a fin"),
        "docs/RUBRICA_EVALUACION.md": ("Rúbrica transversal", "Decisiones posteriores"),
        "docs/FAQ.md": ("Preguntas frecuentes", "¿Las 1.034 clases caben en un año?"),
        "docs/GUIA_FAMILIAS.md": ("Guía para familias", "Acompañar sin reemplazar"),
        "docs/REVISION_HUMANA.md": ("Protocolo de revisión humana", "Registro de evidencia"),
        "docs/QUE_ES_UN_OA.md": ("OA significa Objetivo de Aprendizaje", "OA, clase, actividad y evidencia"),
        "docs/GLOSARIO.md": ("Glosario educativo", "Códigos rápidos"),
        "docs/ROLES_DOCENTES.md": ("Roles profesionales dentro del aula", "Antes, durante y después"),
        "docs/DIFICULTADES_EN_EL_AULA.md": ("Control de dificultades en el aula con acciones", "observar → actuar → comprobar → decidir"),
        "docs/COBERTURA.md": ("Cobertura completa y navegable", "12.997"),
        "docs/PLAN_DESARROLLO.md": ("Plan maestro de desarrollo y control profesional", "Plan por asignatura e ítem", "Controles profesionales", "MA01 OA 20", "Gates para cerrar una asignatura"),
        "docs/FORMATOS.md": ("Clases en Markdown y HTML", "12.997 clases en ambos formatos"),
        "docs/LICENCIAS.md": ("Guía simple de licencias", "Atribución sugerida"),
        "docs/EVALUACION_FORMATIVA.md": ("Logrado con autonomía", "Sin evidencia suficiente"),
        "TEACHING_GUIDE.md": ("Anatomía de una clase", "Consideraciones para 1°, 2°, 3° y 4° básico"),
        "METHODOLOGY.md": ("Flujo de construcción", "Estados editoriales"),
        "LEARNING_PATHS.md": ("Docente de 1°, 2°, 3° o 4° básico", "Coordinación pedagógica o UTP"),
        "ROADMAP.md": ("2.987 clases desarrolladas", "4° básico", "Criterio para declarar un nivel completo"),
        "CONTRIBUTING.md": ("Contrato de una clase desarrollada", "Usa **clase**, no “sesión”"),
        "LICENSING.md": ("Modelo por capas", "Respuesta rápida"),
        "ASSET_LICENSES.md": ("Licencias de activos visuales", "site/icon.svg"),
    }
    for relative_path, tokens in required_docs.items():
        document_path = root / relative_path
        document = document_path.read_text(encoding="utf-8") if document_path.is_file() else ""
        if not document:
            errors.append(f"Falta documentación: {relative_path}")
            continue
        for token in tokens:
            if token not in document:
                errors.append(f"{relative_path} incompleto: falta {token}")
    learning_paths = (root / "LEARNING_PATHS.md").read_text(encoding="utf-8")
    for legacy_term in ("Licencias de software", "SPDX/SBOM/REUSE", "data scientists"):
        if legacy_term in learning_paths:
            errors.append(f"LEARNING_PATHS.md conserva contenido heredado: {legacy_term}")
    expected_subject_guides = {item["subject_slug"] for item in classes if item.get("course_order") == 1}
    subject_guides = {path.stem for path in (root / "docs/1-basico").glob("*.md") if path.name != "README.md"}
    if subject_guides != expected_subject_guides:
        errors.append(f"Guías de asignatura de 1° básico incompletas: actuales={len(subject_guides)}, esperadas={len(expected_subject_guides)}")
    for subject_slug in sorted(expected_subject_guides):
        guide = (root / "docs/1-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        for token in ("Resultados de aprendizaje", "Prerrequisitos", "Cómo recorrer", "Estructura por ejes", "Recorrido OA por OA", "Error frecuente", "Acceso y profundización"):
            if token not in guide:
                errors.append(f"Guía {subject_slug} incompleta: falta {token}")
    second_subject_guides = {path.stem for path in (root / "docs/2-basico").glob("*.md") if path.name != "README.md"}
    if second_subject_guides != expected_subject_guides:
        errors.append(f"Guías de asignatura de 2° básico incompletas: actuales={len(second_subject_guides)}, esperadas={len(expected_subject_guides)}")
    first_index = (root / "docs/1-basico/README.md").read_text(encoding="utf-8")
    second_index = (root / "docs/2-basico/README.md").read_text(encoding="utf-8")
    if second_index.count("\n## ") < first_index.count("\n## "):
        errors.append("El índice de 2° básico tiene menor profundidad documental que el de 1° básico")
    for subject_slug in sorted(expected_subject_guides):
        first_guide = (root / "docs/1-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        second_guide = (root / "docs/2-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        for token in ("Continuidad con 1° básico", "Resultados de aprendizaje", "Prerrequisitos", "Cómo recorrer", "Anatomía estable", "Estructura por ejes", "Recorrido OA por OA", "Qué observar", "Preparación y materiales", "Error frecuente", "Acceso y profundización"):
            if token not in second_guide:
                errors.append(f"Guía de 2° {subject_slug} incompleta: falta {token}")
        if second_guide.count("\n## ") < first_guide.count("\n## "):
            errors.append(f"Guía de 2° {subject_slug} tiene menor profundidad documental que su equivalente de 1°")
    third_subject_guides = {path.stem for path in (root / "docs/3-basico").glob("*.md") if path.name != "README.md"}
    if third_subject_guides != expected_subject_guides:
        errors.append(f"Guías de asignatura de 3° básico incompletas: actuales={len(third_subject_guides)}, esperadas={len(expected_subject_guides)}")
    third_index = (root / "docs/3-basico/README.md").read_text(encoding="utf-8")
    if third_index.count("\n## ") < first_index.count("\n## "):
        errors.append("El índice de 3° básico tiene menor profundidad documental que el de 1° básico")
    for subject_slug in sorted(expected_subject_guides):
        first_guide = (root / "docs/1-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        third_guide = (root / "docs/3-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        for token in ("Continuidad con 2° básico", "Resultados de aprendizaje", "Prerrequisitos", "Cómo recorrer", "Anatomía estable", "Estructura por ejes", "Recorrido OA por OA", "Qué observar", "Preparación y materiales", "Error frecuente", "Acceso y profundización"):
            if token not in third_guide:
                errors.append(f"Guía de 3° {subject_slug} incompleta: falta {token}")
        if third_guide.count("\n## ") < first_guide.count("\n## "):
            errors.append(f"Guía de 3° {subject_slug} tiene menor profundidad documental que su equivalente de 1°")
    fourth_subject_guides = {path.stem for path in (root / "docs/4-basico").glob("*.md") if path.name != "README.md"}
    if fourth_subject_guides != expected_subject_guides:
        errors.append(f"Guías de asignatura de 4° básico incompletas: actuales={len(fourth_subject_guides)}, esperadas={len(expected_subject_guides)}")
    fourth_index = (root / "docs/4-basico/README.md").read_text(encoding="utf-8")
    if fourth_index.count("\n## ") < first_index.count("\n## "):
        errors.append("El índice de 4° básico tiene menor profundidad documental que el de 1° básico")
    for subject_slug in sorted(expected_subject_guides):
        first_guide = (root / "docs/1-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        fourth_guide = (root / "docs/4-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        for token in ("Continuidad con 3° básico", "Resultados de aprendizaje", "Prerrequisitos", "Cómo recorrer", "Anatomía estable", "Estructura por ejes", "Recorrido OA por OA", "Qué observar", "Preparación y materiales", "Error frecuente", "Acceso y profundización"):
            if token not in fourth_guide:
                errors.append(f"Guía de 4° {subject_slug} incompleta: falta {token}")
        if fourth_guide.count("\n## ") < first_guide.count("\n## "):
            errors.append(f"Guía de 4° {subject_slug} tiene menor profundidad documental que su equivalente de 1°")
    documentation_files = list(root.glob("*.md")) + list((root / "docs").rglob("*.md"))
    for document_path in documentation_files:
        document = document_path.read_text(encoding="utf-8")
        for destination in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document):
            if "vladimiracunadev-create.github.io/chilean-school-learning-path" in destination or re.search(r"(?:^|/)site/.*\.html(?:#.*)?$", destination):
                errors.append(f"Cruce Markdown→HTML en {document_path.relative_to(root)}: {destination}")
            if destination.startswith(("http://", "https://", "#", "mailto:")):
                continue
            relative_target = destination.split("#", 1)[0]
            if relative_target.endswith(".html"):
                errors.append(f"Cruce Markdown→HTML en {document_path.relative_to(root)}: {destination}")
            if relative_target and relative_target.endswith(".md") and not (document_path.parent / relative_target).is_file():
                errors.append(f"Enlace Markdown roto en {document_path.relative_to(root)}: {destination}")
    for html_path in (root / "site").rglob("*.html"):
        document = html_path.read_text(encoding="utf-8")
        for destination in re.findall(r'href="([^"]+)"', document):
            clean = destination.split("#", 1)[0].split("?", 1)[0]
            if clean.lower().endswith(".md"):
                errors.append(f"Cruce HTML→Markdown en {html_path.relative_to(root)}: {destination}")
            if not clean or clean.startswith(("http://", "https://", "mailto:", "tel:", "/")):
                continue
            if clean.lower().endswith(".html") and not (html_path.parent / clean).resolve().is_file():
                errors.append(f"Enlace HTML roto en {html_path.relative_to(root)}: {destination}")
    index_path = root / "site/index.html"
    index = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
    for token in ('lang="es"', '<main>', 'id="explorar"', 'id="q"', 'id="level"', 'id="subject"', 'id="coverage"'):
        if token not in index:
            errors.append(f"Portada incompleta: falta {token}")
    if re.search(r"\bsesiones?\b", index, flags=re.IGNORECASE):
        errors.append("La portada llama sesiones a las clases")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("VALIDACIÓN FALLIDA")
        for error in errors[:100]:
            print(" -", error)
        if len(errors) > 100:
            print(f" - … y {len(errors) - 100} errores más")
        return 1
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    print(f"OK: {catalog['class_count']} clases, {catalog['objective_count']} OA, {catalog['course_count']} niveles y {catalog['reading_link_count']} lecturas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
