import os
import os.path
import re


app_config = {
    "base_url": "https://ftp.linuxbase.org/pub/lsb/bundles",
    "base_path": "/srv/ftp/pub/lsb/bundles"
}


arch_mapping = {"ia32": "32-bit Intel/AMD",
                "ia64": "IA-64",
                "x86_64": "64-bit Intel/AMD",
                "ppc32": "POWER32",
                "ppc64": "POWER64",
                "s390": "31-bit System/z",
                "s390x": "64-bit System/z"}


def _get_released_bundle_dir(dirs):
    released_dir_versions = []
    for dir in dirs:
        m = re.match(r'released-(\d+)\.(\d+)\.(\d+)', dir)
        if m is not None:
            released_dir_versions.append(m.groups())

    versions = [(int(x), int(y), int(z))
                for (x, y, z) in released_dir_versions]
    versions.sort()

    return "released-{0}.{1}.{2}".format(*(versions[-1]))


def _arch_name_from_filename(fn):
    m = re.search(r'([^\.]+)\.tar\.gz', fn)
    if m is not None:
        return m.group(1)
    else:
        raise KeyError("could not find an architecture in the file name")


def _get_grouped_paths(paths, identifiers):
    results = {}
    for path in paths:
        fn = os.path.basename(path)
        arch = _arch_name_from_filename(fn)
        if arch not in results:
            results[arch] = {}
        for (regex, key) in identifiers:
            if re.search(regex, fn):
                results[arch][key] = path
                break
    return results


def _get_paths(bundle_type):
    released_path = _get_released_bundle_dir(os.listdir(app_config["base_path"]))
    full_released_path = os.path.join(app_config["base_path"], released_path, bundle_type)
    for path in sorted(os.listdir(full_released_path)):
        if path[0] != ".":
            yield os.path.join(released_path, bundle_type, path)


def get_sdks():
    for path in _get_paths("sdk"):
        fn = os.path.basename(path)
        yield {"name": arch_mapping[_arch_name_from_filename(fn)],
               "fn": fn,
               "url": os.path.join(app_config["base_url"], path)}


def get_appkits():
    identifiers = [('-local', "local"), ('', "pkg")]
    appkit_paths = _get_grouped_paths(_get_paths("app-testkit"),
                                      identifiers)
    for arch in sorted(appkit_paths.keys()):
        pkg_fn = os.path.basename(appkit_paths[arch]["pkg"])
        local_fn = os.path.basename(appkit_paths[arch]["local"])
        yield {"name": arch_mapping[_arch_name_from_filename(pkg_fn)],
               "pkg_fn": pkg_fn,
               "pkg_url": os.path.join(app_config["base_url"],
                                       appkit_paths[arch]["pkg"]),
               "local_fn": local_fn,
               "local_url": os.path.join(app_config["base_url"],
                                         appkit_paths[arch]["local"])}


def get_dtks():
    return [{"name": "IA32 Distribution Test Kit",
             "mgr_fn": "lsb-dist-testkit-manager-5.0.0-2.ia32.tar.gz",
             "mgr_url": "https://ftp.linuxfoundation.org/pub/lsb/bundles/released-5.0.0/dist-testkit/lsb-dist-testkit-manager-5.0.0-2.ia32.tar.gz",
             "full_fn": "lsb-dist-testkit-5.0.0-2.ia32.tar.gz",
             "full_url": "https://ftp.linuxfoundation.org/pub/lsb/bundles/released-5.0.0/dist-testkit/lsb-dist-testkit-5.0.0-2.ia32.tar.gz"}]
