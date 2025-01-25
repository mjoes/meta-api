{ pkgs, insert-app }:

pkgs.dockerTools.buildLayeredImage {
  name = "docker-insert-app";
  tag = "latest";
  config.Entrypoint = [ "${insert-app}/bin/insert-app" ];
}
