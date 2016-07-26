%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name is-buffer

Summary:       Determine if an object is Buffer
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.0.2
Release:       2%{?dist}
License:       MIT
URL:           https://github.com/feross/is-buffer
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
This module lets you check if an object is a Buffer without 
using Buffer.isBuffer (which includes the whole buffer module 
in browserify).

It's future-proof and works in node too!

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json test %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc LICENSE README.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-2
- Enable scl macros

* Thu Sep 10 2015 Troy Dawson <tdawson@redhat.com> - 1.0.2-1
- Initial package
