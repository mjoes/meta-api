{
  description = "Metadata api";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/24.11-beta";
  };

  outputs = { self, nixpkgs }@inputs:
  let 
    system = "aarch64-linux";
    pkgs = import nixpkgs {
      inherit system;
    };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        python3Packages.requests
        python3Packages.flask
      ];
      shellHook = ''
        source .env
      '';
    };
  };
}
