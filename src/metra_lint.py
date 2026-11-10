"""Metra Lint: validation of measurement schema descriptors."""

from dataclasses import dataclass
from pathlib import Path
import yaml


@dataclass
class Finding:
    path: str
    rule: str
    message: str


def load_rules(path):
    with open(path, encoding='utf-8') as handle:
        return yaml.safe_load(handle)['rules']


def check(descriptor, rules):
    findings = []
    for rule in rules:
        field = rule['field']
        if rule.get('required') and field not in descriptor:
            findings.append(Finding(field, rule['id'], 'missing field'))
        if 'max_length' in rule and len(str(descriptor.get(field, ''))) > rule['max_length']:
            findings.append(Finding(field, rule['id'], 'too long'))
    return findings


def main(argv=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema', required=True)
    parser.add_argument('--input', required=True)
    args = parser.parse_args(argv)
    rules = load_rules(args.schema)
    for path in sorted(Path(args.input).glob('*.yaml')):
        descriptor = yaml.safe_load(path.read_text(encoding='utf-8'))
        for finding in check(descriptor, rules):
            print(f'{path}: {finding.rule}: {finding.message}')


if __name__ == '__main__':
    main()
