%define oname after_commit

Name:       rubygem-%{oname}
Version:    1.0.8
Release:    2
Summary:    Callback for ActiveRecord
Group:      Development/Ruby
License:    GPLv2+ or Ruby License
URL:        https://github.com/freelancing-god/after_commit
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(activerecord) < 3.0.0
Requires:   rubygem(sqlite3-ruby)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A Ruby on Rails plugin to add an after_commit callback. This can be used
to trigger methods only after the entire transaction is complete.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.textile
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sat Dec 04 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.8-1mdv2011.0
+ Revision: 609438
- import rubygem-after_commit

