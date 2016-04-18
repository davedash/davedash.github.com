require 'rake/clean'

task :clean do
    puts 'Cleaning _site...'
    CLEAN.include('_site/**')
    rmtree CLEAN
end

desc 'Everything you need to do before you deploy'
task :pre_deploy do
    Rake::Task["tags"].invoke
    puts 'Building site...'
    sh 'jekyll build'
end

desc 'Quickly sync static assets to build dir'
task :sync_static do
    sh "rsync -a static/ _site/static/"
end

desc 'Generate tags page'
task :tags do
  puts "Generating tags..."
  require 'rubygems'
  require 'jekyll'
  include Jekyll::Filters

  site = Jekyll::Site.new(Jekyll::Configuration::DEFAULTS)
  site.read
  site.tags.sort.each do |category, posts|

    next if category == ".net"
    html = ''
    html << <<-HTML
---
layout: default
title: Entries tagged "#{category}"
tag: #{category}
type: "#{category.gsub(/\b\w/){$&.upcase}}"
---
    <h1 id="#{category}">Entries tagged &ldquo;#{category}&rdquo;</h1>
    <div id="posts" class="container">
      {% for post in site.tags['#{category}'] %}
        {% assign date=post.date | date: '%-d %B %Y' %}
        {% assign tag='' %}
        {% for tag_ in post.tags %}
          {% if tag_ != "#{category}" %}
            {% assign tag=tag_ %}
          {% endif %}
        {% endfor %}
        {% include mason.html tag=tag date=date description=post.excerpt url=post.url title=post.title %}
      {% endfor %}
    </div>

    HTML

    FileUtils.mkdir_p "tag/#{category.downcase}"
    File.open("tag/#{category.downcase}/index.html", 'w+') do |file|
      file.puts html
    end

    # ATOM.xml

    html = ''
    html << <<-HTML
---
layout:
---
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

 <title>Dave Dash</title>
 <link href="http://davedash.com/tag/#{category.downcase}/atom.xml" rel="self"/>
 <link href="http://davedash.com/tag/#{category.downcase}"/>
 <updated>{{ site.time | date_to_xmlschema }}</updated>
 <id>http://davedash.com/</id>
 <author>
   <name>Dave Dash</name>
   <email>dd+atom1@davedash.com</email>
 </author>

 {% for post in site.tags['#{category}'] %}
 <entry>
   <title>{{ post.title }}</title>
   <link href="http://davedash.com{{ post.url }}"/>
   <updated>{{ post.date | date_to_xmlschema }}</updated>
   <id>http://davedash.com{{ post.id }}</id>
   <content type="html">{{ post.content | xml_escape }}</content>
 </entry>
 {% endfor %}

</feed>
    HTML

    File.open("tag/#{category.downcase}/atom.xml", 'w+') do |file|
      file.puts html
    end

  end
  puts 'Done.'
end
