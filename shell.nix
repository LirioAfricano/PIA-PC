with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "pip-env";
  buildInputs = [
    # System requirements.
    readline

    # Python requirements (enough to get a virtualenv going).
    python38Full
    python38Packages.virtualenv
    python38Packages.pip
    python38Packages.setuptools
    python38Packages.setuptools_scm
    python38Packages.pillow
    python38Packages.beautifulsoup4
    python38Packages.requests
    python38Packages.autopep8
  ];
  src = null;
  shellHook = ''
    # Allow the use of wheels.
    SOURCE_DATE_EPOCH=$(date +%s)

    # Augment the dynamic linker path
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${R}/lib/R/lib:${readline}/lib
  '';
}
