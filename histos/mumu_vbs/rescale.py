from pathlib import Path
import yaml
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', metavar="DIR", help='input directory', default='unscaled/6_TeV/nunuWW/truth')
    parser.add_argument('--output', '-o', metavar="DIR", help='output directory', default='6_TeV/nunuWW/truth')
    parser.add_argument('--energy', '-e', default=6, help='cm energy in TeV')
    args = parser.parse_args()
    root_input_path = Path(args.input)
    root_output_path = Path(args.output)
    xsec_path = root_input_path / 'cross_section.yaml'
    lumi_path = Path('lumi.yaml')
    energy = args.energy
    
    with xsec_path.open('r') as f:
        xsecs = yaml.load(f, Loader=yaml.SafeLoader)
    with lumi_path.open('r') as f:
        lumis = yaml.load(f, Loader=yaml.SafeLoader)
    lumi = lumis[energy]

    for input_path in root_input_path.rglob('*.root'):
        try:
            relative_path = input_path.relative_to(root_input_path)
            process = input_path.stem
            xsec = xsecs[process]
            output_path = root_output_path / relative_path
            output_path.parent.mkdir(exist_ok=True, parents=True)
            arg = f"root -q -b -l 'rescale.C(\"{input_path}\", \"{output_path}\", {xsec}, {lumi})'"
            subprocess.run(arg, shell=True)
        except BaseException as e:
            print(e)

if __name__ == '__main__':
    main()