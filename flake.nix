{
  description = "Metadata api";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/24.11-beta";
    treefmt-nix.url = "github:numtide/treefmt-nix";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      treefmt-nix,
      flake-utils,
    }@inputs:
    flake-utils.lib.eachSystem
      [
        "aarch64-linux"
        "x86_64-linux"
      ]
      (
        system:
        let
          pkgs = import nixpkgs {
            inherit system;
          };

          insert_app = import ./packages/insert_app/default.nix { python = pkgs.python3; };
          treefmtEval = treefmt-nix.lib.evalModule pkgs {
            projectRootFile = "flake.nix";
            programs = {
              nixfmt.enable = true;
              ruff-format.enable = true;
              ruff-check.enable = true;
            };
          };

        in
        {

          formatter = treefmtEval.config.build.wrapper;

          packages = {
            # insert_app = import ./packages/insert_app/default.nix { python = pkgs.python3; };
            docker-insert-app = import ./docker/insert_app.nix {
              inherit pkgs;
              insert-app = insert_app;
            };
          };

          devShells.default = pkgs.mkShell {
            packages = with pkgs; [
              docker
              python3Packages.flask
            ];
            shellHook = ''
              source .env
              export PYTHONPATH=$PYTHONPATH:$PWD/packages/insert_app/src
            '';
          };
        }
      );
}
