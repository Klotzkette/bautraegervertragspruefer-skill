#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
btv_python="${BTV_PYTHON:-python3}"

"$btv_python" scripts/check_skill_quality.py
"$btv_python" scripts/check_workflow_contract.py
"$btv_python" scripts/package_plugin.py --check
"$btv_python" scripts/test_plugin_tools.py
"$btv_python" scripts/test_contract_artifacts.py
"$btv_python" tests/verify_testakten.py
"$btv_python" scripts/check_legal_anchors.py
"$btv_python" scripts/check_navigation.py

if [[ "${BTV_VERIFY_BUILDS:-0}" == "1" ]]; then
  "$btv_python" scripts/check_contract_builds.py --rebuild
else
  "$btv_python" scripts/check_contract_builds.py
fi

echo "validate_repo: all requested repository checks passed"
