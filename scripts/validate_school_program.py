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
    from grade_five_core_lessons import SEQUENCES as GRADE_FIVE_CORE_SEQUENCES, build_sequence as build_grade_five_core_sequence
    from grade_five_remaining_lessons import SEQUENCES as GRADE_FIVE_REMAINING_SEQUENCES, build_sequence as build_grade_five_remaining_sequence
    from grade_six_math_lessons import SEQUENCES as GRADE_SIX_MATH_SEQUENCES, build_sequence as build_grade_six_math_sequence
    from grade_six_remaining_lessons import SEQUENCES as GRADE_SIX_REMAINING_SEQUENCES, build_sequence as build_grade_six_remaining_sequence
    from grade_seven_core_lessons import SEQUENCES as GRADE_SEVEN_CORE_SEQUENCES, build_sequence as build_grade_seven_core_sequence
    from grade_seven_next_five_lessons import SEQUENCES as GRADE_SEVEN_NEXT_FIVE_SEQUENCES, build_sequence as build_grade_seven_next_five_sequence
    from grade_seven_remaining_lessons import SEQUENCES as GRADE_SEVEN_REMAINING_SEQUENCES, build_sequence as build_grade_seven_remaining_sequence
    from grade_eight_core_lessons import SEQUENCES as GRADE_EIGHT_CORE_SEQUENCES, build_sequence as build_grade_eight_core_sequence
    from grade_eight_next_four_lessons import SEQUENCES as GRADE_EIGHT_NEXT_FOUR_SEQUENCES, build_sequence as build_grade_eight_next_four_sequence
    from grade_eight_remaining_lessons import SEQUENCES as GRADE_EIGHT_REMAINING_SEQUENCES, build_sequence as build_grade_eight_remaining_sequence
    from grade_one_middle_core_lessons import SEQUENCES as GRADE_ONE_MIDDLE_CORE_SEQUENCES, build_sequence as build_grade_one_middle_core_sequence
    from grade_one_middle_next_four_lessons import SEQUENCES as GRADE_ONE_MIDDLE_NEXT_FOUR_SEQUENCES, build_sequence as build_grade_one_middle_next_four_sequence
    from grade_one_middle_remaining_lessons import SEQUENCES as GRADE_ONE_MIDDLE_REMAINING_SEQUENCES, build_sequence as build_grade_one_middle_remaining_sequence
    from grade_two_middle_core_lessons import SEQUENCES as GRADE_TWO_MIDDLE_CORE_SEQUENCES, build_sequence as build_grade_two_middle_core_sequence
    from grade_two_middle_next_four_lessons import SEQUENCES as GRADE_TWO_MIDDLE_NEXT_FOUR_SEQUENCES, build_sequence as build_grade_two_middle_next_four_sequence
    from grade_two_middle_remaining_lessons import SEQUENCES as GRADE_TWO_MIDDLE_REMAINING_SEQUENCES, build_sequence as build_grade_two_middle_remaining_sequence
    from grade_three_middle_core_lessons import SEQUENCES as GRADE_THREE_MIDDLE_CORE_SEQUENCES, build_sequence as build_grade_three_middle_core_sequence
    from grade_three_middle_remaining_lessons import SEQUENCES as GRADE_THREE_MIDDLE_REMAINING_SEQUENCES, build_sequence as build_grade_three_middle_remaining_sequence
    from grade_four_middle_lessons import SEQUENCES as GRADE_FOUR_MIDDLE_SEQUENCES, build_sequence as build_grade_four_middle_sequence
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
    from scripts.grade_five_core_lessons import SEQUENCES as GRADE_FIVE_CORE_SEQUENCES, build_sequence as build_grade_five_core_sequence
    from scripts.grade_five_remaining_lessons import SEQUENCES as GRADE_FIVE_REMAINING_SEQUENCES, build_sequence as build_grade_five_remaining_sequence
    from scripts.grade_six_math_lessons import SEQUENCES as GRADE_SIX_MATH_SEQUENCES, build_sequence as build_grade_six_math_sequence
    from scripts.grade_six_remaining_lessons import SEQUENCES as GRADE_SIX_REMAINING_SEQUENCES, build_sequence as build_grade_six_remaining_sequence
    from scripts.grade_seven_core_lessons import SEQUENCES as GRADE_SEVEN_CORE_SEQUENCES, build_sequence as build_grade_seven_core_sequence
    from scripts.grade_seven_next_five_lessons import SEQUENCES as GRADE_SEVEN_NEXT_FIVE_SEQUENCES, build_sequence as build_grade_seven_next_five_sequence
    from scripts.grade_seven_remaining_lessons import SEQUENCES as GRADE_SEVEN_REMAINING_SEQUENCES, build_sequence as build_grade_seven_remaining_sequence
    from scripts.grade_eight_core_lessons import SEQUENCES as GRADE_EIGHT_CORE_SEQUENCES, build_sequence as build_grade_eight_core_sequence
    from scripts.grade_eight_next_four_lessons import SEQUENCES as GRADE_EIGHT_NEXT_FOUR_SEQUENCES, build_sequence as build_grade_eight_next_four_sequence
    from scripts.grade_eight_remaining_lessons import SEQUENCES as GRADE_EIGHT_REMAINING_SEQUENCES, build_sequence as build_grade_eight_remaining_sequence
    from scripts.grade_one_middle_core_lessons import SEQUENCES as GRADE_ONE_MIDDLE_CORE_SEQUENCES, build_sequence as build_grade_one_middle_core_sequence
    from scripts.grade_one_middle_next_four_lessons import SEQUENCES as GRADE_ONE_MIDDLE_NEXT_FOUR_SEQUENCES, build_sequence as build_grade_one_middle_next_four_sequence
    from scripts.grade_one_middle_remaining_lessons import SEQUENCES as GRADE_ONE_MIDDLE_REMAINING_SEQUENCES, build_sequence as build_grade_one_middle_remaining_sequence
    from scripts.grade_two_middle_core_lessons import SEQUENCES as GRADE_TWO_MIDDLE_CORE_SEQUENCES, build_sequence as build_grade_two_middle_core_sequence
    from scripts.grade_two_middle_next_four_lessons import SEQUENCES as GRADE_TWO_MIDDLE_NEXT_FOUR_SEQUENCES, build_sequence as build_grade_two_middle_next_four_sequence
    from scripts.grade_two_middle_remaining_lessons import SEQUENCES as GRADE_TWO_MIDDLE_REMAINING_SEQUENCES, build_sequence as build_grade_two_middle_remaining_sequence
    from scripts.grade_three_middle_core_lessons import SEQUENCES as GRADE_THREE_MIDDLE_CORE_SEQUENCES, build_sequence as build_grade_three_middle_core_sequence
    from scripts.grade_three_middle_remaining_lessons import SEQUENCES as GRADE_THREE_MIDDLE_REMAINING_SEQUENCES, build_sequence as build_grade_three_middle_remaining_sequence
    from scripts.grade_four_middle_lessons import SEQUENCES as GRADE_FOUR_MIDDLE_SEQUENCES, build_sequence as build_grade_four_middle_sequence

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
    all_developed.update({code: build_grade_five_core_sequence(code) for code in GRADE_FIVE_CORE_SEQUENCES})
    all_developed.update({code: build_grade_five_remaining_sequence(code) for code in GRADE_FIVE_REMAINING_SEQUENCES})
    all_developed.update({code: build_grade_six_math_sequence(code) for code in GRADE_SIX_MATH_SEQUENCES})
    all_developed.update({code: build_grade_six_remaining_sequence(code) for code in GRADE_SIX_REMAINING_SEQUENCES})
    all_developed.update({code: build_grade_seven_core_sequence(code) for code in GRADE_SEVEN_CORE_SEQUENCES})
    all_developed.update({code: build_grade_seven_next_five_sequence(code) for code in GRADE_SEVEN_NEXT_FIVE_SEQUENCES})
    all_developed.update({code: build_grade_seven_remaining_sequence(code) for code in GRADE_SEVEN_REMAINING_SEQUENCES})
    all_developed.update({code: build_grade_eight_core_sequence(code) for code in GRADE_EIGHT_CORE_SEQUENCES})
    all_developed.update({code: build_grade_eight_next_four_sequence(code) for code in GRADE_EIGHT_NEXT_FOUR_SEQUENCES})
    all_developed.update({code: build_grade_eight_remaining_sequence(code) for code in GRADE_EIGHT_REMAINING_SEQUENCES})
    all_developed.update({code: build_grade_one_middle_core_sequence(code) for code in GRADE_ONE_MIDDLE_CORE_SEQUENCES})
    all_developed.update({code: build_grade_one_middle_next_four_sequence(code) for code in GRADE_ONE_MIDDLE_NEXT_FOUR_SEQUENCES})
    all_developed.update({code: build_grade_one_middle_remaining_sequence(code) for code in GRADE_ONE_MIDDLE_REMAINING_SEQUENCES})
    all_developed.update({code: build_grade_two_middle_core_sequence(code) for code in GRADE_TWO_MIDDLE_CORE_SEQUENCES})
    all_developed.update({code: build_grade_two_middle_next_four_sequence(code) for code in GRADE_TWO_MIDDLE_NEXT_FOUR_SEQUENCES})
    all_developed.update({code: build_grade_two_middle_remaining_sequence(code) for code in GRADE_TWO_MIDDLE_REMAINING_SEQUENCES})
    all_developed.update({code: build_grade_three_middle_core_sequence(code) for code in GRADE_THREE_MIDDLE_CORE_SEQUENCES})
    all_developed.update({code: build_grade_three_middle_remaining_sequence(code) for code in GRADE_THREE_MIDDLE_REMAINING_SEQUENCES})
    all_developed.update({code: build_grade_four_middle_sequence(code) for code in GRADE_FOUR_MIDDLE_SEQUENCES})
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
        is_fifth_remaining = oa_code.startswith(("AR05 OA ", "EF05 OA ", "HI05 OA ", "IN05 OA ", "EN05 OA ", "LC05 OA ", "MU05 OA ", "OR05 OA ", "TE05 OA "))
        is_sixth = oa_code.startswith(("MA06 OA ", "LE06 OA ", "CN06 OA ", "HI06 OA ", "AR06 OA ", "EF06 OA ", "IN06 OA ", "EN06 OA ", "LC06 OA ", "MU06 OA ", "OR06 OA ", "TE06 OA "))
        if is_sixth or is_fifth_remaining or oa_code.startswith(("MA01 OA ", "MA02 OA ", "MA03 OA ", "MA04 OA ", "MA05 OA ", "LE05 OA ", "CN05 OA ", "LE03 OA ", "CN03 OA ", "HI03 OA ", "AR03 OA ", "EF03 OA ", "EN03 OA ", "LC03 OA ", "MU03 OA ", "OR03 OA ", "TE03 OA ", "LE02 OA ", "CN02 OA ", "HI02 OA ", "AR02 OA ", "MU02 OA ", "EF02 OA ", "OR02 OA ", "TE02 OA ", "EN02 OA ", "LC02 OA ", "CN01 OA ", "HI01 OA ", "AR01 OA ", "MU01 OA ", "EF01 OA ", "OR01 OA ", "TE01 OA ", "EN01 OA ", "LC01 OA ")) or oa_code == "LE01 OA 03":
            for field in ("topic", "pedagogical_explanation", "prerequisites", "vocabulary", "official_alignment"):
                if not objective.get(field):
                    errors.append(f"{oa_code}: falta fundamento específico {field}")
            alignment = objective.get("official_alignment", {})
            if len(alignment.get("indicators", [])) < 3 or not alignment.get("source", "").startswith("https://www.curriculumnacional.cl/"):
                errors.append(f"{oa_code}: alineación oficial insuficiente")
            if (is_sixth or is_fifth_remaining or oa_code.startswith(("MA01 OA ", "MA02 OA ", "MA03 OA ", "MA04 OA ", "MA05 OA ", "LE05 OA ", "CN05 OA ", "LE03 OA ", "CN03 OA ", "HI03 OA ", "AR03 OA ", "EF03 OA ", "EN03 OA ", "LC03 OA ", "MU03 OA ", "OR03 OA ", "TE03 OA ", "LE02 OA ", "CN02 OA ", "HI02 OA ", "AR02 OA ", "MU02 OA ", "EF02 OA ", "OR02 OA ", "TE02 OA ", "EN02 OA ", "LC02 OA ", "LE01 OA ", "CN01 OA ", "HI01 OA ", "AR01 OA ", "MU01 OA ", "EF01 OA ", "OR01 OA ", "TE01 OA ", "EN01 OA ", "LC01 OA "))) and alignment.get("source") != official_urls.get(oa_code):
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
            if is_sixth or is_fifth_remaining or oa_code.startswith(("MA01 OA ", "MA02 OA ", "MA03 OA ", "MA04 OA ", "MA05 OA ", "LE05 OA ", "CN05 OA ", "LE03 OA ", "CN03 OA ", "HI03 OA ", "AR03 OA ", "EF03 OA ", "EN03 OA ", "LC03 OA ", "MU03 OA ", "OR03 OA ", "TE03 OA ", "LE02 OA ", "CN02 OA ", "HI02 OA ", "AR02 OA ", "MU02 OA ", "EF02 OA ", "OR02 OA ", "TE02 OA ", "EN02 OA ", "LC02 OA ", "CN01 OA ", "HI01 OA ", "AR01 OA ", "MU01 OA ", "EF01 OA ", "OR01 OA ", "TE01 OA ", "EN01 OA ", "LC01 OA ")) or oa_code == "LE01 OA 03":
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

    seventh_grade = [item for item in classes if item.get("course_order") == 7]
    expected_seventh_core = {
        "matematica": (83, 19, 82, 19),
        "lengua-literatura": (147, 25, 33, 8),
        "ciencias-naturales": (72, 15, 89, 21),
        "historia-geografia-ciencias-sociales": (113, 23, 91, 20),
        "ingles": (80, 16, 21, 5),
        "educacion-fisica-salud": (25, 5, 28, 7),
        "artes-visuales": (29, 6, 33, 8),
        "ingles-propuesta": (65, 13, 85, 21),
        "lengua-indigena": (41, 8, 0, 0),
        "musica": (30, 7, 37, 9),
        "orientacion": (49, 10, 0, 0),
        "tecnologia": (26, 6, 16, 4),
    }
    for slug, expected_counts in expected_seventh_core.items():
        rows = [item for item in seventh_grade if item.get("subject_slug") == slug]
        core = [item for item in rows if item.get("editorial_status") == "desarrollada"]
        integrated = [item for item in rows if item.get("editorial_status") == "integrada"]
        actual = (len(core), len({item.get("oa_code") for item in core}), len(integrated), len({item.get("oa_code") for item in integrated}))
        if actual != expected_counts:
            errors.append(f"Cobertura desarrollada o transversal incompleta en 7° básico: {slug}")
        if any(item.get("editorial_status") in {"secuenciada", "borrador"} for item in rows):
            errors.append(f"7° básico no debe conservar propuestas pendientes en {slug}")
    if any(item.get("editorial_status") in {"secuenciada", "borrador"} for item in seventh_grade):
        errors.append("7° básico no debe conservar propuestas pendientes")

    eighth_grade = [item for item in classes if item.get("course_order") == 8]
    expected_eighth_core = {
        "matematica": (77, 17, 82, 19),
        "lengua-literatura": (155, 26, 33, 8),
        "ciencias-naturales": (74, 15, 89, 21),
        "historia-geografia-ciencias-sociales": (117, 22, 91, 20),
        "artes-visuales": (29, 6, 33, 8),
        "musica": (30, 7, 37, 9),
        "educacion-fisica-salud": (26, 5, 28, 7),
        "orientacion": (49, 10, 0, 0),
        "tecnologia": (26, 6, 16, 4),
        "ingles": (80, 16, 21, 5),
        "ingles-propuesta": (65, 13, 0, 0),
        "lengua-indigena": (43, 9, 0, 0),
    }
    for slug, expected_counts in expected_eighth_core.items():
        rows = [item for item in eighth_grade if item.get("subject_slug") == slug]
        core = [item for item in rows if item.get("editorial_status") == "desarrollada"]
        integrated = [item for item in rows if item.get("editorial_status") == "integrada"]
        actual = (len(core), len({item.get("oa_code") for item in core}), len(integrated), len({item.get("oa_code") for item in integrated}))
        if actual != expected_counts:
            errors.append(f"Cobertura desarrollada o transversal incompleta en 8° básico: {slug}")
        if any(item.get("editorial_status") in {"secuenciada", "borrador"} for item in rows):
            errors.append(f"8° básico no debe conservar propuestas pendientes en {slug}")
    eighth_counts = {
        status: sum(item.get("editorial_status") == status for item in eighth_grade)
        for status in ("desarrollada", "integrada", "secuenciada")
    }
    if eighth_counts != {"desarrollada": 771, "integrada": 430, "secuenciada": 0}:
        errors.append(f"Estado editorial de 8° básico incoherente: {eighth_counts}")

    first_middle = [item for item in classes if item.get("course_order") == 9]
    expected_first_middle_core = {
        "matematica": (66, 15, 89, 21),
        "lengua-literatura": (143, 24, 33, 8),
        "ciencias-naturales": (100, 20, 93, 21),
        "historia-geografia-ciencias-sociales": (132, 25, 103, 23),
        "ingles": (80, 16, 21, 5),
        "ingles-propuesta": (65, 13, 0, 0),
        "artes-visuales": (29, 6, 33, 8),
        "musica": (32, 7, 37, 9),
        "educacion-fisica-salud": (28, 5, 28, 7),
        "orientacion": (52, 10, 0, 0),
        "tecnologia": (26, 6, 19, 4),
    }
    for slug, expected_counts in expected_first_middle_core.items():
        rows = [item for item in first_middle if item.get("subject_slug") == slug]
        core = [item for item in rows if item.get("editorial_status") == "desarrollada"]
        integrated = [item for item in rows if item.get("editorial_status") == "integrada"]
        actual = (len(core), len({item.get("oa_code") for item in core}), len(integrated), len({item.get("oa_code") for item in integrated}))
        if actual != expected_counts:
            errors.append(f"Cobertura desarrollada o transversal incompleta en 1° medio: {slug}")
        if any(item.get("editorial_status") in {"secuenciada", "borrador"} for item in rows):
            errors.append(f"La asignatura desarrollada de 1° medio conserva propuestas pendientes: {slug}")
    first_middle_counts = {
        status: sum(item.get("editorial_status") == status for item in first_middle)
        for status in ("desarrollada", "integrada", "secuenciada")
    }
    if first_middle_counts != {"desarrollada": 753, "integrada": 456, "secuenciada": 0}:
        errors.append(f"Estado editorial de 1° medio incoherente: {first_middle_counts}")

    second_middle = [item for item in classes if item.get("course_order") == 10]
    expected_second_middle_core = {
        "matematica": (55, 12, 89, 21),
        "lengua-literatura": (146, 24, 33, 8),
        "ciencias-naturales": (85, 18, 93, 21),
        "historia-geografia-ciencias-sociales": (142, 25, 103, 23),
        "ingles": (81, 16, 21, 5),
        "ingles-propuesta": (66, 13, 0, 0),
        "artes-visuales": (30, 6, 33, 8),
        "musica": (31, 7, 37, 9),
        "educacion-fisica-salud": (28, 5, 28, 7),
        "orientacion": (52, 10, 0, 0),
        "tecnologia": (28, 6, 19, 4),
    }
    for slug, expected_counts in expected_second_middle_core.items():
        rows = [item for item in second_middle if item.get("subject_slug") == slug]
        core = [item for item in rows if item.get("editorial_status") == "desarrollada"]
        integrated = [item for item in rows if item.get("editorial_status") == "integrada"]
        actual = (len(core), len({item.get("oa_code") for item in core}), len(integrated), len({item.get("oa_code") for item in integrated}))
        if actual != expected_counts:
            errors.append(f"Cobertura desarrollada o transversal incompleta en 2° medio: {slug}")
        if any(item.get("editorial_status") in {"secuenciada", "borrador"} for item in rows):
            errors.append(f"La asignatura desarrollada de 2° medio conserva propuestas pendientes: {slug}")
    second_middle_counts = {
        status: sum(item.get("editorial_status") == status for item in second_middle)
        for status in ("desarrollada", "integrada", "secuenciada")
    }
    if second_middle_counts != {"desarrollada": 744, "integrada": 456, "secuenciada": 0}:
        errors.append(f"Estado editorial de 2° medio incoherente: {second_middle_counts}")

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
            quality_tokens = ["Insumo concreto y consigna", "Recurso listo para usar", "Consigna exacta", "Referencia para modelar y corregir", "Pauta de evaluación de cuatro niveles", "Distribución de 45 minutos"]
            tokens = ["Propósito docente", "Meta para estudiantes", "Materiales y preparación", "Criterios observables", "Decisión posterior", "Tarea breve y flexible", "Actividades complementarias", "Control de dificultades con acciones", "Coordinación profesional", *quality_tokens]
            if item.get("subject_slug") == "matematica" and item.get("course_order") in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
                tokens.append("Habilidad y actitud en esta clase")
            if item.get("subject_slug") == "lenguaje-comunicacion" and item.get("course_order") in {1, 3, 5, 6}:
                tokens.append("Actitud transversal en esta clase")
            if item.get("subject_slug") == "lengua-literatura" and (item.get("course_order") in {7, 9, 10} or (item.get("course_order") == 8 and item.get("oa_code") != "LE08 OA 09")):
                tokens.append("Actitud transversal en esta clase")
            if item.get("subject_slug") in {"ciencias-naturales", "historia-geografia-ciencias-sociales"} and item.get("course_order") in {1, 3, 5, 6, 7, 8, 9, 10}:
                tokens.append("Habilidad y actitud en esta clase")
            if item.get("subject_slug") == "artes-visuales" and item.get("course_order") in {1, 3, 5, 6, 7, 8, 9, 10}:
                tokens.append("Actitud transversal en esta clase")
            if item.get("subject_slug") in {"musica", "educacion-fisica-salud", "tecnologia", "ingles", "ingles-propuesta"} and item.get("course_order") in {1, 3, 5, 6, 7, 8, 9, 10} and not (item.get("subject_slug") == "ingles-propuesta" and item.get("course_order") == 10):
                tokens.append("Actitud transversal en esta clase")
            if item.get("subject_slug") == "lengua-cultura-pueblos-originarios-ancestrales" and item.get("course_order") in {1, 3, 5}:
                tokens.append("Actitud transversal en esta clase")
            for token in tokens:
                if token not in html_cache[web_path]:
                    errors.append(f"{web_path} no materializa el contrato desarrollado: falta {token}")
            if item["lesson"] == 1:
                for token in quality_tokens:
                    if html_cache[web_path].count(token) != item["lesson_count"]:
                        errors.append(f"{web_path} debe incluir {item['lesson_count']} bloques de «{token}»")
                markdown_quality_tokens = ["### Insumo concreto y consigna", "**Recurso listo para usar:**", "**Consigna exacta:**", "**Referencia para modelar y corregir:**", "**Pauta de evaluación de cuatro niveles:**", "| Distribución de 45 minutos |"]
                for token in markdown_quality_tokens:
                    if markdown_cache[markdown_path].count(token) != item["lesson_count"]:
                        errors.append(f"{markdown_path} debe incluir {item['lesson_count']} bloques de «{token}»")
                forbidden_phrases = ["responde al foco específico de la clase", "Recursos reutilizables para", "Modela cómo modelar", "no por imitar el ejemplo", "no se transfiere mecánicamente a otro OA", ",,", "oficial.."]
                for phrase in forbidden_phrases:
                    if phrase in markdown_cache[markdown_path]:
                        errors.append(f"{markdown_path} conserva redacción genérica o defectuosa: {phrase}")

    pages = list((root / "site/classes").rglob("*.html"))
    if len(pages) != objective_count:
        errors.append(f"Páginas de OA: {len(pages)}, esperadas: {objective_count}")
    for required in ("index.html", "documentacion.html", "styles.css", "app.js", "catalog.json", "updates.json", "404.html", "icon.svg", "manifest.webmanifest", "sitemap.xml", "competencias/index.html", "competencias/data/taxonomy.v1.json", "competencias/data/progressions.v1.json", "competencias/data/frameworks.v1.json", "competencias/data/item-bank.v1.json", "levels/1-basico.html", "levels/2-basico.html", "levels/3-basico.html", "levels/4-basico.html", "levels/5-basico.html", "levels/6-basico.html", "levels/7-basico.html", "levels/8-basico.html", "levels/1-medio.html", "levels/2-medio.html", "levels/3-medio.html", "levels/4-medio.html", "reviews/review-record.schema.json", "reviews/pilot-record.schema.json"):
        if not (root / "site" / required).is_file():
            errors.append(f"Falta artefacto de Pages: {required}")
    documentation_pages = list((root / "site/docs").rglob("*.html"))
    if len(documentation_pages) < 41:
        errors.append(f"Documentación HTML incompleta: {len(documentation_pages)} páginas, esperadas al menos 41")
    sitemap_path = root / "site/sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8") if sitemap_path.is_file() else ""
    if sitemap.count("<url>") != objective_count + len(documentation_pages) + 15:
        errors.append("El sitemap no enumera portada, documentación, competencias, los doce niveles, documentos HTML y páginas de OA")
    updates_path = root / "site/updates.json"
    if updates_path.is_file():
        try:
            updates = json.loads(updates_path.read_text(encoding="utf-8"))
            changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
            first_heading = re.search(r"^## (\d{4}-\d{2}-\d{2}) · (.+)$", changelog, re.MULTILINE)
            latest = updates.get("updates", [])[0]
            if not first_heading or latest.get("date") != first_heading.group(1) or latest.get("title") != first_heading.group(2):
                errors.append("Novedades públicas desincronizadas con la primera entrada del CHANGELOG")
            if not latest.get("summary"):
                errors.append("La novedad pública más reciente no tiene resumen visible")
        except (json.JSONDecodeError, IndexError, AttributeError) as exc:
            errors.append(f"site/updates.json inválido: {exc}")
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
    fifth_level_page = root / "site/levels/5-basico.html"
    fifth_level_html = fifth_level_page.read_text(encoding="utf-8") if fifth_level_page.is_file() else ""
    for token in ("1.340", "295", "12", "920 desarrolladas", "420 integradas", "0 propuestas pendientes", "Completo no significa revisado"):
        if token not in fifth_level_html:
            errors.append(f"Vista de 5° básico incompleta: falta {token}")
    sixth_level_page = root / "site/levels/6-basico.html"
    sixth_level_html = sixth_level_page.read_text(encoding="utf-8") if sixth_level_page.is_file() else ""
    for token in ("1.374", "301", "12", "952 desarrolladas", "422 integradas", "0 propuestas pendientes", "Completo no significa revisado"):
        if token not in sixth_level_html:
            errors.append(f"Vista de 6° básico incompleta: falta {token}")
    seventh_level_page = root / "site/levels/7-basico.html"
    seventh_level_html = seventh_level_page.read_text(encoding="utf-8") if seventh_level_page.is_file() else ""
    for token in ("1.275", "275", "12", "760 desarrolladas", "515 integradas", "0 propuestas pendientes", "Completo no significa revisado"):
        if token not in seventh_level_html:
            errors.append(f"Vista de 7° básico incompleta: falta {token}")
    eighth_level_page = root / "site/levels/8-basico.html"
    eighth_level_html = eighth_level_page.read_text(encoding="utf-8") if eighth_level_page.is_file() else ""
    for token in ("1.201", "253", "12", "771 desarrolladas", "430 integradas", "0 pendientes", "Completo no significa revisado"):
        if token not in eighth_level_html:
            errors.append(f"Vista de 8° básico incompleta: falta {token}")
    first_middle_page = root / "site/levels/1-medio.html"
    first_middle_html = first_middle_page.read_text(encoding="utf-8") if first_middle_page.is_file() else ""
    for token in ("1.209", "253", "753 desarrolladas", "456 integradas", "0 pendientes", "11 denominaciones"):
        if token not in first_middle_html:
            errors.append(f"Vista de 1° medio incompleta: falta {token}")
    second_middle_page = root / "site/levels/2-medio.html"
    second_middle_html = second_middle_page.read_text(encoding="utf-8") if second_middle_page.is_file() else ""
    for token in ("1.200", "248", "744 desarrolladas", "456 integradas", "0 pendientes", "Once recorridos"):
        if token not in second_middle_html:
            errors.append(f"Vista de 2° medio incompleta: falta {token}")
    third_middle_page = root / "site/levels/3-medio.html"
    third_middle_html = third_middle_page.read_text(encoding="utf-8") if third_middle_page.is_file() else ""
    for token in ("98", "495", "18", "0 propuestas pendientes", "Matemática", "Lengua y literatura", "Fuentes explícitas", "Completo no significa revisado"):
        if token not in third_middle_html:
            errors.append(f"Vista de 3° medio incompleta: falta {token}")
    fourth_middle_page = root / "site/levels/4-medio.html"
    fourth_middle_html = fourth_middle_page.read_text(encoding="utf-8") if fourth_middle_page.is_file() else ""
    for token in ("91", "466", "17", "0 propuestas pendientes", "Matemática", "Lengua y literatura", "Fuentes explícitas", "Completo no significa revisado"):
        if token not in fourth_middle_html:
            errors.append(f"Vista de 4° medio incompleta: falta {token}")
    documentation_page = root / "site/documentacion.html"
    documentation_html = documentation_page.read_text(encoding="utf-8") if documentation_page.is_file() else ""
    for token in ("Documentación pedagógica", "149 guías de asignatura", "doce niveles completos · 17 guías de 4° medio", "Primer nivel completo", "Segundo nivel completo", "Tercer nivel completo", "Cuarto nivel completo", "Quinto nivel completo", "Sexto nivel completo", "Séptimo nivel completo", "Octavo nivel completo", "Tercer nivel de Enseñanza Media completo", "Cuarto nivel de Enseñanza Media completo", "¿Qué es un OA?", "Roles en el aula", "Cobertura navegable", "Markdown + HTML", "Pilotaje de aula"):
        if token not in documentation_html:
            errors.append(f"Portada documental incompleta: falta {token}")
    if any(documentation_html.count(f"Leer guía de {level} completa") != 11 for level in ("1°", "2°", "3°", "4°")):
        errors.append("La portada documental no presenta las 11 guías de los cuatro niveles con igual visibilidad")
    if documentation_html.count("Leer guía de 5° completa") != 12:
        errors.append("La portada documental no presenta las 12 guías de 5° básico")
    if documentation_html.count("Leer guía de 6° completa") != 12:
        errors.append("La portada documental no presenta las 12 guías de 6° básico")
    if documentation_html.count("Leer guía de 7° completa") != 12:
        errors.append("La portada documental no presenta las 12 guías de 7° básico")
    if documentation_html.count("Leer guía de 8°") != 12:
        errors.append("La portada documental no presenta las 12 guías de 8° básico")
    if documentation_html.count("Leer guía de 1° medio") != 11:
        errors.append("La portada documental no presenta las 11 guías de 1° medio")
    if documentation_html.count("Leer guía de 2° medio") != 11:
        errors.append("La portada documental no presenta las 11 guías de 2° medio")
    if documentation_html.count("Leer guía de 3° medio") != 18:
        errors.append("La portada documental no presenta las dieciocho guías desarrolladas de 3° medio")
    if documentation_html.count("Leer guía de 4° medio") != 17:
        errors.append("La portada documental no presenta las diecisiete guías desarrolladas de 4° medio")
    required_docs = {
        "README.md": ("12.997", "2.823", "8.841", "4.156", "691 clases de 1° básico", "721 de 2°", "757 de 3°", "811 de 4°", "920 de 5°", "952 de 6°", "760 de 7°", "771 de 8°", "753 clases disciplinares", "147 OA de contenido + 106 OA transversales", "744 clases disciplinares", "142 OA de contenido + 106 OA transversales", "495 clases", "466 clases", "0 propuestas pendientes", "6° básico · desarrollo OA por OA", "7° básico · desarrollo OA por OA", "8° básico · desarrollo OA por OA", "1° medio completo · once denominaciones", "2° medio completo · once denominaciones", "3° medio completo", "4° medio completo", "portal público de GitHub Pages", "Cómo se mejora el contenido desarrollado", "De dónde sale el contenido", "Portal, navegación y formatos", "Caja de herramientas pedagógicas", "Rutas según quién usa el repositorio", "Para docentes y equipos pedagógicos", "Calidad y CI", "Qué es y qué no es este programa", "Idea fuerza", "Documentación de principio a fin"),
        "docs/README.md": ("1° básico a 4° medio completos internamente", "1° medio completo", "2° medio completo", "3° medio completo", "4° medio completo", "149 guías disponibles", "Estado verificable", "Cómo leer los estados", "Protocolo de pilotaje"),
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
        "docs/5-basico/README.md": ("12 denominaciones curriculares", "920 clases desarrolladas", "420 experiencias integradas", "0 propuestas pendientes", "Anatomía y diferenciación"),
        "docs/5-basico/matematica.md": ("115 clases desarrolladas", "86 experiencias integradas", "Continuidad con 4° básico", "Recorrido OA por OA"),
        "docs/5-basico/lenguaje-comunicacion.md": ("166 clases desarrolladas", "29 experiencias integradas", "Continuidad con 4° básico", "Recorrido OA por OA"),
        "docs/5-basico/ciencias-naturales.md": ("64 clases desarrolladas", "58 experiencias integradas", "Continuidad con 4° básico", "Recorrido OA por OA"),
        "docs/5-basico/historia-geografia-ciencias-sociales.md": ("106 clases desarrolladas", "91 experiencias integradas", "Continuidad con 4° básico", "Recorrido OA por OA"),
        "docs/5-basico/artes-visuales.md": ("27 clases desarrolladas", "28 experiencias integradas", "Continuidad con 4° básico", "Recorrido OA por OA"),
        "docs/5-basico/ingles.md": ("76 clases desarrolladas", "16 experiencias integradas", "Continuidad con 4° básico", "Recorrido OA por OA"),
        "docs/5-basico/lengua-cultura-pueblos-originarios-ancestrales.md": ("135 clases desarrolladas", "Continuidad con 4° básico", "Resguardos culturales"),
        "docs/QUINTO_BASICO.md": ("920 clases desarrolladas", "420 experiencias transversales integradas", "12 denominaciones curriculares", "Continuidad con 4° básico"),
        "docs/6-basico/README.md": ("12 denominaciones curriculares", "952 clases desarrolladas", "422 experiencias integradas", "0 propuestas pendientes", "Anatomía y diferenciación"),
        "docs/6-basico/matematica.md": ("98 clases desarrolladas", "88 experiencias integradas", "Continuidad con 5° básico", "Recorrido OA por OA"),
        "docs/6-basico/lenguaje-comunicacion.md": ("176 clases desarrolladas", "29 experiencias integradas", "Continuidad con 5° básico", "Recorrido OA por OA"),
        "docs/6-basico/ciencias-naturales.md": ("78 clases desarrolladas", "53 experiencias integradas", "Continuidad con 5° básico", "Recorrido OA por OA"),
        "docs/6-basico/historia-geografia-ciencias-sociales.md": ("116 clases desarrolladas", "96 experiencias integradas", "Continuidad con 5° básico", "Recorrido OA por OA"),
        "docs/6-basico/lengua-cultura-pueblos-originarios-ancestrales.md": ("144 clases desarrolladas", "Continuidad con 5° básico", "Resguardos culturales"),
        "docs/SEXTO_BASICO.md": ("952 clases desarrolladas", "422 experiencias transversales integradas", "12 denominaciones curriculares", "Continuidad con 5° básico"),
        "docs/7-basico/README.md": ("desarrollo interno completo", "760 clases disciplinares", "515 experiencias transversales integradas", "12 denominaciones curriculares"),
        "docs/7-basico/matematica.md": ("83 clases desarrolladas", "82 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/lengua-literatura.md": ("147 clases desarrolladas", "33 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/ciencias-naturales.md": ("72 clases desarrolladas", "89 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/historia-geografia-ciencias-sociales.md": ("113 clases desarrolladas", "91 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/ingles.md": ("80 clases desarrolladas", "21 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/educacion-fisica-salud.md": ("25 clases desarrolladas", "28 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/artes-visuales.md": ("29 clases desarrolladas", "33 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/ingles-propuesta.md": ("65 clases desarrolladas", "85 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/lengua-indigena.md": ("41 clases desarrolladas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/musica.md": ("30 clases desarrolladas", "37 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/orientacion.md": ("49 clases desarrolladas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/7-basico/tecnologia.md": ("26 clases desarrolladas", "16 experiencias integradas", "Continuidad con 6° básico", "Recorrido OA por OA"),
        "docs/SEPTIMO_BASICO.md": ("760 clases desarrolladas", "515 experiencias transversales integradas", "12 denominaciones curriculares", "Continuidad con 6° básico"),
        "docs/8-basico/README.md": ("8° básico con desarrollo interno completo", "771 clases disciplinares", "430 experiencias transversales integradas", "0 pendientes", "12 denominaciones curriculares"),
        "docs/8-basico/matematica.md": ("77 clases desarrolladas", "82 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/lengua-literatura.md": ("155 clases desarrolladas", "33 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/ciencias-naturales.md": ("74 clases desarrolladas", "89 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/historia-geografia-ciencias-sociales.md": ("117 clases desarrolladas", "91 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/artes-visuales.md": ("29 clases desarrolladas", "33 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/musica.md": ("30 clases desarrolladas", "37 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/educacion-fisica-salud.md": ("26 clases desarrolladas", "28 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/orientacion.md": ("49 clases desarrolladas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/tecnologia.md": ("26 clases desarrolladas", "16 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/ingles.md": ("80 clases desarrolladas", "21 experiencias integradas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/ingles-propuesta.md": ("65 clases desarrolladas", "Continuidad con 7° básico", "Recorrido OA por OA"),
        "docs/8-basico/lengua-indigena.md": ("43 clases desarrolladas", "Continuidad con 7° básico", "Resguardos culturales"),
        "docs/OCTAVO_BASICO.md": ("771 clases desarrolladas", "430 experiencias transversales integradas", "0 propuestas pendientes", "12 denominaciones curriculares", "Continuidad con 7° básico"),
        "docs/1-medio/README.md": ("1° medio con desarrollo interno completo", "753 clases disciplinares desarrolladas", "456 experiencias transversales integradas", "0 propuestas pendientes"),
        "docs/1-medio/matematica.md": ("66 clases desarrolladas", "89 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/lengua-literatura.md": ("143 clases desarrolladas", "33 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/ciencias-naturales.md": ("100 clases desarrolladas", "93 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/historia-geografia-ciencias-sociales.md": ("132 clases desarrolladas", "103 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/ingles.md": ("80 clases desarrolladas", "21 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/ingles-propuesta.md": ("65 clases desarrolladas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/artes-visuales.md": ("29 clases desarrolladas", "33 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/musica.md": ("32 clases desarrolladas", "37 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/educacion-fisica-salud.md": ("28 clases desarrolladas", "28 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/orientacion.md": ("52 clases desarrolladas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/1-medio/tecnologia.md": ("26 clases desarrolladas", "19 experiencias integradas", "Continuidad con 8° básico", "Recorrido OA por OA"),
        "docs/PRIMERO_MEDIO.md": ("753 clases desarrolladas", "456 experiencias transversales integradas", "0 propuestas pendientes"),
        "docs/2-medio/README.md": ("2° medio con desarrollo interno completo", "744 clases disciplinares desarrolladas", "456 experiencias transversales integradas", "0 propuestas pendientes", "las once denominaciones"),
        "docs/2-medio/matematica.md": ("12 OA de contenido", "55 clases desarrolladas", "89 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/lengua-literatura.md": ("24 OA de contenido", "146 clases desarrolladas", "33 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/ciencias-naturales.md": ("18 OA de contenido", "85 clases desarrolladas", "93 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/historia-geografia-ciencias-sociales.md": ("25 OA de contenido", "142 clases desarrolladas", "103 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/ingles.md": ("16 OA de contenido", "81 clases desarrolladas", "21 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/ingles-propuesta.md": ("13 OA de contenido", "66 clases desarrolladas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/artes-visuales.md": ("6 OA de contenido", "30 clases desarrolladas", "33 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/musica.md": ("7 OA de contenido", "31 clases desarrolladas", "37 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/educacion-fisica-salud.md": ("5 OA de contenido", "28 clases desarrolladas", "28 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/orientacion.md": ("10 OA de contenido", "52 clases desarrolladas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/2-medio/tecnologia.md": ("6 OA de contenido", "28 clases desarrolladas", "19 experiencias integradas", "Continuidad con 1° medio", "Recorrido OA por OA"),
        "docs/SEGUNDO_MEDIO.md": ("Desarrollo pedagógico interno completo", "744 clases desarrolladas", "456 experiencias transversales integradas", "0 propuestas pendientes", "Continuidad con 1° medio"),
        "docs/3-medio/README.md": ("3° medio · Formación General completo", "495 clases disciplinares desarrolladas", "0 propuestas pendientes", "Ambiente y sostenibilidad", "Matemática", "Lengua y literatura", "Tecnología y sociedad"),
        "docs/3-medio/matematica-3o-medio.md": ("4 OA de contenido", "17 clases desarrolladas", "Continuidad con 2° medio", "Recorrido OA por OA", "Fuente y límites"),
        "docs/3-medio/lengua-literatura-3o-medio.md": ("9 OA de contenido", "59 clases desarrolladas", "Continuidad con 2° medio", "Recorrido OA por OA", "Fuente y límites"),
        "docs/TERCERO_MEDIO.md": ("Desarrollo pedagógico interno completo", "495 clases desarrolladas", "0 propuestas pendientes", "Continuidad con 2° medio"),
        "docs/4-medio/README.md": ("4° medio · Formación General completo", "466 clases disciplinares desarrolladas", "0 propuestas pendientes", "Ambiente y sostenibilidad", "Matemática", "Lengua y literatura", "Tecnología y sociedad"),
        "docs/4-medio/matematica-4o-medio.md": ("4 OA de contenido", "17 clases desarrolladas", "Continuidad con 3° medio", "Recorrido OA por OA", "Fuente y límites"),
        "docs/4-medio/lengua-literatura-4o-medio.md": ("8 OA de contenido", "53 clases desarrolladas", "Continuidad con 3° medio", "Recorrido OA por OA", "Fuente y límites"),
        "docs/CUARTO_MEDIO.md": ("Desarrollo pedagógico interno completo", "466 clases desarrolladas", "0 propuestas pendientes", "Continuidad con 3° medio"),
        "docs/SYLLABUS.md": ("Marco de reconstrucción de 1° básico a 4° medio", "2° medio: 744 + 456", "3° medio: 495 desarrolladas", "4° medio: 466 desarrolladas", "Planificación de principio a fin"),
        "docs/RUBRICA_EVALUACION.md": ("Rúbrica transversal", "Decisiones posteriores"),
        "docs/FAQ.md": ("Preguntas frecuentes", "¿Las 1.034 clases caben en un año?"),
        "docs/GUIA_FAMILIAS.md": ("Guía para familias", "Acompañar sin reemplazar"),
        "docs/REVISION_HUMANA.md": ("Protocolo de revisión humana", "Registro de evidencia"),
        "docs/PILOTAJE_AULA.md": ("Protocolo de pilotaje de aula", "0 pilotajes de aula registrados", "pilot-record.schema.json"),
        "docs/QUE_ES_UN_OA.md": ("OA significa Objetivo de Aprendizaje", "OA, clase, actividad y evidencia"),
        "docs/GLOSARIO.md": ("Glosario educativo", "Códigos rápidos"),
        "docs/ROLES_DOCENTES.md": ("Roles profesionales dentro del aula", "Antes, durante y después"),
        "docs/DIFICULTADES_EN_EL_AULA.md": ("Control de dificultades en el aula con acciones", "observar → actuar → comprobar → decidir"),
        "docs/COBERTURA.md": ("Cobertura completa y navegable", "12.997"),
        "docs/PLAN_DESARROLLO.md": ("Plan maestro de desarrollo y control profesional", "4° medio — desarrollo interno completo", "Ninguna", "Definición y orden editorial de 1° básico a 4° medio", "MA2M OA 12", "LE2M OA 24", "FG-MATE-4M-OAC-04", "FG-LELI-4M-OAC-08", "FG-CIAS-3y4-OAC-01", "Gates del desarrollo interno", "- [x] Todos los OA disciplinares"),
        "docs/FORMATOS.md": ("Registros pedagógicos en Markdown y HTML", "8.841 clases disciplinares", "4.156 experiencias de integración transversal", "12.997 registros pedagógicos"),
        "docs/LICENCIAS.md": ("Guía simple de licencias", "Atribución sugerida"),
        "docs/EVALUACION_FORMATIVA.md": ("Logrado con autonomía", "Sin evidencia suficiente"),
        "TEACHING_GUIDE.md": ("Anatomía de una clase", "Consideraciones para el contenido desarrollado de 1° básico a 4° medio", "doce niveles completos", "calidad de fuentes"),
        "METHODOLOGY.md": ("Flujo de construcción", "Estados editoriales"),
        "LEARNING_PATHS.md": ("Docente de contenido desarrollado · 1° básico a 4° medio", "Coordinación pedagógica o UTP"),
        "ROADMAP.md": ("8.841 clases desarrolladas", "Completo: 952 desarrolladas + 422 integradas", "Completo: 760 desarrolladas + 515 integradas", "Completo: 771 desarrolladas + 430 integradas", "Completo: 753 desarrolladas + 456 integradas", "Completo: 744 desarrolladas + 456 integradas", "495 desarrolladas", "466 desarrolladas", "0 pendientes", "Criterio para declarar un nivel completo"),
        "CONTRIBUTING.md": ("Contrato de una clase desarrollada", "Usa **clase**, no “sesión”"),
        "LICENSING.md": ("Modelo por capas", "Respuesta rápida"),
        "ASSET_LICENSES.md": ("Licencias de activos visuales", "site/icon.svg"),
        "site/index.html": ("Desde 1° básico hasta 4° medio", "Trayectoria completa hasta 4° medio", "8.841 clases", "4.156 experiencias integradas", "levels/7-basico.html", "levels/8-basico.html", "levels/1-medio.html", "levels/2-medio.html", "levels/3-medio.html", "levels/4-medio.html"),
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
    stale_current_claims = {
        "README.md": ("Siete asignaturas de 7°", "Cinco denominaciones pendientes de 7° básico", "7 clases piloto en 8° básico", "Desde 8° básico hasta 4° medio", "Desde 1° hasta 4° medio", "8° básico en desarrollo", "seis asignaturas de 8°", "Seis asignaturas desarrolladas de 8° básico", "Una mejora de 1°, 2°, 3°, 4° o 5° básico", "Docente de 1°, 2° o 3° básico", "6.094 clases desarrolladas", "3.179 experiencias integradas", "6.383 clases desarrolladas", "3.244 experiencias integradas", "3.370 propuestas secuenciadas", "6.592 clases desarrolladas", "3.366 experiencias integradas", "878 propuestas", "6.969 clases desarrolladas", "3.583 experiencias integradas", "284 propuestas", "7.136 clases desarrolladas", "3.700 experiencias integradas", "2.161 propuestas", "8.375 clases desarrolladas", "466 propuestas pendientes"),
        "docs/README.md": ("Siete asignaturas de 7°", "Las 86 guías disponibles", "Las 92 guías disponibles", "Las 94 guías disponibles", "Las 98 guías disponibles", "103 guías disponibles", "132 guías disponibles", "seis asignaturas desarrolladas de 8°", "8° básico en desarrollo", "6.383", "3.244", "6.592", "3.366", "878 propuestas", "6.969", "3.583", "284 propuestas", "7.136", "3.700", "2.161 propuestas", "1° básico a 3° medio completos internamente"),
        "docs/SYLLABUS.md": ("Siete asignaturas de 7°", "núcleo de 8°", "seis asignaturas desarrolladas de 8°", "354 propuestas pendientes"),
        "docs/PLAN_DESARROLLO.md": ("7° básico — siguiente nivel por desarrollar", "Definición y orden editorial de 1° a 6° básico", "control interno completo niveles 1 a 6", "control interno completo niveles 1 a 7 y seis asignaturas 8"),
        "EDITORIAL_STATUS.md": ("Desarrollo parcial de 8° básico", "Otras asignaturas del nivel", "354 propuestas secuenciadas"),
        "ROADMAP.md": ("En desarrollo: 482 desarrolladas + 365 integradas", "354 pendientes en 8° básico", "6.383 clases desarrolladas", "3.244 experiencias integradas", "7.136 clases desarrolladas", "3.700 experiencias integradas", "2.161 propuestas", "8.375 clases desarrolladas", "466 pendientes"),
        "VALIDATION_REPORT.md": ("Seis asignaturas de 8° completas", "6.094 desarrolladas en total", "6.383 desarrolladas en total", "3.244 experiencias", "7.136 desarrolladas", "3.700 experiencias", "2.161 propuestas"),
        "site/index.html": ("1° a 6° básico con desarrollo pedagógico interno completo", "1° a 7° básico con desarrollo pedagógico interno completo", "4.859 clases desarrolladas", "6.094 clases desarrolladas", "6.383 clases desarrolladas", "2.299 experiencias integradas", "3.179 experiencias integradas", "3.244 experiencias integradas", "7.136 clases", "3.700 experiencias", "2.161 propuestas", "Seis niveles completos", "siete niveles completos", "Once niveles completos", "8.375 clases"),
    }
    for relative_path, stale_tokens in stale_current_claims.items():
        document = (root / relative_path).read_text(encoding="utf-8")
        for token in stale_tokens:
            if token in document:
                errors.append(f"{relative_path} conserva una afirmación vigente obsoleta: {token}")
    for relative_path in ("README.md", "CURRICULUM.md", "EDITORIAL_STATUS.md", "VALIDATION_REPORT.md", "docs/COBERTURA.md", "docs/FORMATOS.md", "docs/README.md"):
        document = (root / relative_path).read_text(encoding="utf-8")
        if "12.997 clases" in document:
            errors.append(f"{relative_path} confunde registros pedagógicos con clases independientes")
    for document_path in (root / "docs").rglob("*.md"):
        document = document_path.read_text(encoding="utf-8")
        if any(token in document for token in ("{len(transverse)}", "{integrated_count}", "{class_count}")):
            errors.append(f"{document_path.relative_to(root)} conserva un marcador de plantilla sin resolver")
    main_readme = (root / "README.md").read_text(encoding="utf-8")
    try:
        positive_section = main_readme.split("### ✅ Sí es", 1)[1].split("### ❌ No es", 1)[0]
        negative_section = main_readme.split("### ❌ No es", 1)[1].split("## 💡 Idea fuerza", 1)[0]
    except IndexError:
        errors.append("README.md no conserva la separación explícita entre alcance y límites")
    else:
        for token in ("8.841 clases disciplinares", "4.156 experiencias de integración transversal"):
            if token not in positive_section:
                errors.append(f"README.md omite un hecho actual en la sección Sí es: {token}")
        for token in ("8.841 clases disciplinares", "4.156 experiencias"):
            if token in negative_section:
                errors.append(f"README.md contradice el estado actual dentro de No es: {token}")
    if "sirve hoy para cuatro cosas" in main_readme:
        errors.append("README.md anuncia cuatro recorridos, pero enumera más de cuatro")
    for token in ("Docente de 3° medio", "Docente de 4° medio", "Syllabus general de 1° básico a 4° medio"):
        if token not in main_readme:
            errors.append(f"README.md omite el alcance vigente: {token}")

    syllabus = (root / "docs/SYLLABUS.md").read_text(encoding="utf-8")
    for token in ("2.823 OA", "12.997 registros pedagógicos", "8.841 clases disciplinares", "4.156 experiencias"):
        if token not in syllabus:
            errors.append(f"docs/SYLLABUS.md omite el hecho vigente: {token}")
    level_folders = (
        "1-basico", "2-basico", "3-basico", "4-basico", "5-basico", "6-basico",
        "7-basico", "8-basico", "1-medio", "2-medio", "3-medio", "4-medio",
    )
    for course_order, folder in enumerate(level_folders, start=1):
        if f"{folder}/README.md" not in syllabus:
            errors.append(f"docs/SYLLABUS.md no enlaza el índice del nivel: {folder}")
        subject_slugs = {item["subject_slug"] for item in classes if item.get("course_order") == course_order}
        for subject_slug in subject_slugs:
            if f"{folder}/{subject_slug}.md" not in syllabus:
                errors.append(f"docs/SYLLABUS.md omite la guía vigente: {folder}/{subject_slug}.md")
    for relative_path in (
        "README.md", "docs/README.md", "docs/SYLLABUS.md", "docs/COBERTURA.md",
        "EDITORIAL_STATUS.md", "VALIDATION_REPORT.md",
    ):
        surface = (root / relative_path).read_text(encoding="utf-8")
        for token in ("2.823", "12.997", "8.841", "4.156"):
            if token not in surface:
                errors.append(f"{relative_path} omite la cifra canónica vigente: {token}")
    try:
        complete_readme_sections = {
            "portada": main_readme.split("## 👋 Empieza aquí", 1)[0],
            "Empieza aquí": main_readme.split("## 👋 Empieza aquí", 1)[1].split("## 🧭 OA, en palabras simples", 1)[0],
            "De dónde sale el contenido": main_readme.split("## 📖 De dónde sale el contenido", 1)[1].split("## 📍 Estado actual", 1)[0],
            "Rutas según quién usa el repositorio": main_readme.split("## 🧭 Rutas según quién usa el repositorio", 1)[1].split("## 👩‍🏫 Para docentes y equipos pedagógicos", 1)[0],
            "Para docentes y equipos pedagógicos": main_readme.split("## 👩‍🏫 Para docentes y equipos pedagógicos", 1)[1].split("## 📊 Evaluación que conduce a una decisión", 1)[0],
            "Documentación de principio a fin": main_readme.split("## 📚 Documentación de principio a fin", 1)[1].split("## 🗺️ Cobertura total", 1)[0],
            "pie": main_readme.split('<div align="center">', 2)[-1],
        }
    except IndexError:
        errors.append("README.md no conserva la estructura esperada de secciones completas")
    else:
        for section_name, section in complete_readme_sections.items():
            for folder in level_folders:
                if f"docs/{folder}/README.md" not in section:
                    errors.append(f"README.md omite {folder} en la sección completa: {section_name}")
    for course_order in range(1, 9):
        level_link = f"docs/{course_order}-basico/README.md"
        if level_link not in main_readme:
            errors.append(f"README.md no enlaza el índice completo de {course_order}° básico")
        subject_slugs = {
            item["subject_slug"]
            for item in classes
            if item.get("course_order") == course_order
        }
        for subject_slug in subject_slugs:
            guide_link = f"docs/{course_order}-basico/{subject_slug}.md"
            if guide_link not in main_readme:
                errors.append(f"README.md no informa o enlaza la guía resuelta: {guide_link}")
    if "docs/1-medio/README.md" not in main_readme:
        errors.append("README.md no enlaza el índice de 1° medio")
    for subject_slug in sorted({item["subject_slug"] for item in classes if item.get("course_order") == 9}):
        guide_link = f"docs/1-medio/{subject_slug}.md"
        if guide_link not in main_readme:
            errors.append(f"README.md no informa o enlaza la guía resuelta: {guide_link}")
    if "docs/2-medio/README.md" not in main_readme:
        errors.append("README.md no enlaza el índice de 2° medio")
    for subject_slug in sorted({item["subject_slug"] for item in classes if item.get("course_order") == 10}):
        guide_link = f"docs/2-medio/{subject_slug}.md"
        if guide_link not in main_readme:
            errors.append(f"README.md no informa o enlaza la guía resuelta: {guide_link}")
    if "docs/3-medio/README.md" not in main_readme:
        errors.append("README.md no enlaza el índice completo de 3° medio")
    for subject_slug in sorted({item["subject_slug"] for item in classes if item.get("course_order") == 11}):
        guide_link = f"docs/3-medio/{subject_slug}.md"
        if guide_link not in main_readme:
            errors.append(f"README.md no informa o enlaza la guía resuelta: {guide_link}")
        guide_path = root / guide_link
        if guide_path.is_file():
            guide = guide_path.read_text(encoding="utf-8")
            oa_count = len({item["oa_code"] for item in classes if item.get("course_order") == 11 and item.get("subject_slug") == subject_slug})
            if "Explicación pedagógica OA por OA" not in guide or guide.count("**Qué significa para la enseñanza.**") != oa_count:
                errors.append(f"Guía de 3° medio sin explicación pedagógica completa OA por OA: {subject_slug}")
    if "docs/4-medio/README.md" not in main_readme:
        errors.append("README.md no enlaza el índice completo de 4° medio")
    for subject_slug in sorted({item["subject_slug"] for item in classes if item.get("course_order") == 12}):
        guide_link = f"docs/4-medio/{subject_slug}.md"
        if guide_link not in main_readme:
            errors.append(f"README.md no informa o enlaza la guía resuelta: {guide_link}")
        guide_path = root / guide_link
        if guide_path.is_file():
            guide = guide_path.read_text(encoding="utf-8")
            oa_count = len({item["oa_code"] for item in classes if item.get("course_order") == 12 and item.get("subject_slug") == subject_slug})
            if "Explicación pedagógica OA por OA" not in guide or guide.count("**Qué significa para la enseñanza.**") != oa_count:
                errors.append(f"Guía de 4° medio sin explicación pedagógica completa OA por OA: {subject_slug}")
    for schema_path in ("reviews/review-record.schema.json", "reviews/pilot-record.schema.json"):
        try:
            schema = json.loads((root / schema_path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Esquema de evidencia inválido {schema_path}: {exc}")
            continue
        if schema.get("type") != "object" or not schema.get("required"):
            errors.append(f"Esquema de evidencia incompleto: {schema_path}")
    review_records = [path for path in (root / "reviews").glob("*.json") if not path.name.endswith(".schema.json")]
    if review_records and catalog.get("editorial_counts", {}).get("revisada") == 0:
        errors.append("Existen registros de revisión sin sincronizar el estado editorial")
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
    expected_fifth_guides = {item["subject_slug"] for item in classes if item.get("course_order") == 5}
    fifth_subject_guides = {path.stem for path in (root / "docs/5-basico").glob("*.md") if path.name != "README.md"}
    if fifth_subject_guides != expected_fifth_guides:
        errors.append(f"Guías de asignatura de 5° básico incompletas: actuales={len(fifth_subject_guides)}, esperadas={len(expected_fifth_guides)}")
    fifth_index = (root / "docs/5-basico/README.md").read_text(encoding="utf-8")
    if fifth_index.count("\n## ") < first_index.count("\n## "):
        errors.append("El índice de 5° básico tiene menor profundidad documental que el de 1° básico")
    for subject_slug in sorted(expected_fifth_guides):
        fifth_guide = (root / "docs/5-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        for token in ("Continuidad con 4° básico", "Resultados de aprendizaje", "Prerrequisitos", "Cómo recorrer", "Anatomía estable", "Estructura por ejes", "Recorrido OA por OA", "Qué observar", "Preparación y materiales", "Error frecuente", "Acceso y profundización"):
            if token not in fifth_guide:
                errors.append(f"Guía de 5° {subject_slug} incompleta: falta {token}")
        baseline_slug = "ingles-propuesta" if subject_slug == "ingles" else subject_slug
        first_guide = (root / "docs/1-basico" / f"{baseline_slug}.md").read_text(encoding="utf-8")
        if fifth_guide.count("\n## ") < first_guide.count("\n## "):
            errors.append(f"Guía de 5° {subject_slug} tiene menor profundidad documental que su equivalente de 1°")
    expected_sixth_guides = {item["subject_slug"] for item in classes if item.get("course_order") == 6}
    sixth_subject_guides = {path.stem for path in (root / "docs/6-basico").glob("*.md") if path.name != "README.md"}
    if sixth_subject_guides != expected_sixth_guides:
        errors.append(f"Guías de asignatura de 6° básico incompletas: actuales={len(sixth_subject_guides)}, esperadas={len(expected_sixth_guides)}")
    sixth_index = (root / "docs/6-basico/README.md").read_text(encoding="utf-8")
    if sixth_index.count("\n## ") < first_index.count("\n## "):
        errors.append("El índice de 6° básico tiene menor profundidad documental que el de 1° básico")
    for subject_slug in sorted(expected_sixth_guides):
        sixth_guide = (root / "docs/6-basico" / f"{subject_slug}.md").read_text(encoding="utf-8")
        for token in ("Continuidad con 5° básico", "Resultados de aprendizaje", "Prerrequisitos", "Cómo recorrer", "Anatomía estable", "Estructura por ejes", "Recorrido OA por OA", "Qué observar", "Preparación y materiales", "Error frecuente", "Acceso y profundización"):
            if token not in sixth_guide:
                errors.append(f"Guía de 6° {subject_slug} incompleta: falta {token}")
        baseline_slug = "ingles-propuesta" if subject_slug == "ingles" else subject_slug
        first_guide = (root / "docs/1-basico" / f"{baseline_slug}.md").read_text(encoding="utf-8")
        if sixth_guide.count("\n## ") < first_guide.count("\n## "):
            errors.append(f"Guía de 6° {subject_slug} tiene menor profundidad documental que su equivalente de 1°")
    documentation_files = list(root.glob("*.md")) + list((root / "docs").rglob("*.md"))
    public_portal = "https://vladimiracunadev-create.github.io/chilean-school-learning-path/"
    for document_path in documentation_files:
        document = document_path.read_text(encoding="utf-8")
        for destination in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document):
            if (
                "vladimiracunadev-create.github.io/chilean-school-learning-path" in destination
                and destination.rstrip("/") != public_portal.rstrip("/")
            ) or re.search(r"(?:^|/)site/.*\.html(?:#.*)?$", destination):
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
            if clean.lower().endswith(".md") and not clean.startswith(("http://", "https://")):
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
    print(f"OK: {catalog['class_count']} registros ({catalog['editorial_counts']['desarrollada']} clases + {catalog['editorial_counts']['integrada']} integraciones), {catalog['objective_count']} OA, {catalog['course_count']} niveles y {catalog['reading_link_count']} lecturas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
