{
  description = "Metadata api";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/24.11-beta";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs =
    {
      self,
      nixpkgs,
      treefmt-nix,
    }@inputs:
    let
      system = "aarch64-linux";
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

      formatter.${system} = treefmtEval.config.build.wrapper;

      packages.${system} = {
        # insert_app = import ./packages/insert_app/default.nix { python = pkgs.python3; };
        docker-insert-app = import ./docker/insert_app.nix {
          inherit pkgs;
          insert-app = insert_app;
        };
      };

      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          docker
          python3Packages.flask
        ];
        shellHook = ''
          source .env
          export PYTHONPATH=$PYTHONPATH:$PWD/packages/insert_app/src
        '';
      };
    };
}
